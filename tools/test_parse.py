#!/usr/bin/env python3
"""test_parse.py - tests de non-regression du parseur (fixtures locales).

Lancement : python3 tools/test_parse.py
"""
import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parse_rich as pr

FIX = Path(__file__).resolve().parent / "fixtures"
ROOT = Path(__file__).resolve().parent.parent


class TestFixtures(unittest.TestCase):
    """Verifie la lecture d'une fiche : rubriques, puces, titres composes, Face B."""

    @classmethod
    def setUpClass(cls):
        cls.warn = []
        cls.fiches = (pr.parse_fiches(FIX / "faceA_99_fixture.md", cls.warn)
                      + pr.parse_fiches(FIX / "faceB_99_fixture.md", cls.warn))
        cls.by = {f["nom"]: f for f in cls.fiches}

    def test_fixtures_detectees(self):
        self.assertEqual(sorted(self.by), ["TESTB", "alpha", "testfmt", "testnl"])
        self.assertEqual([w for w in self.warn if not w.startswith("W-SIG")], [], self.warn)

    def test_rubrique_non_avalee(self):
        f = self.by["testfmt"]
        self.assertEqual(len(f["cas_reguliers"]), 3)
        for c in f["cas_reguliers"]:
            self.assertNotIn("**", c["cmd"], c)
        self.assertTrue(f["origine"].startswith("fixture locale"), f["origine"])
        self.assertEqual(len(f["subtilites"]), 1)
        self.assertTrue(f["subtilites"][0].startswith("La rubrique suivante"), f["subtilites"])
        self.assertTrue(f["role_fr"].startswith("Commande de test"), f["role_fr"])
        self.assertEqual(f["niveau"], "debutant")
        self.assertEqual(f["popularite"], 42)
        self.assertEqual(f["os"], ["linux", "macos"])
        self.assertEqual(f["aliases"], ["tf"])
        self.assertEqual(f["categories"], ["Fixture"])

    def test_liste_arret_ligne_vide(self):
        f = self.by["testnl"]
        self.assertEqual(len(f["cas_reguliers"]), 2)
        self.assertEqual(f["origine"], "fixture locale (2026)")
        self.assertTrue(f["subtilites"][0].startswith("Une ligne vide"), f["subtilites"])
        self.assertEqual(f["voir_aussi"], ["testfmt"])

    def test_titre_compose(self):
        f = self.by["alpha"]
        self.assertEqual(f["nom"], "alpha")
        self.assertEqual(f["aliases"], ["beta"])
        self.assertEqual(len(f["cas_reguliers"]), 2)

    def test_face_b_champs_conserves(self):
        f = self.by["TESTB"]
        self.assertEqual(f["syntaxe"], "api --foo bar")
        self.assertTrue(f["precautions"])
        self.assertTrue(f["urgences_dangers"])
        self.assertEqual(f["equivalents"], [{"note": "testb-cli"}])
        self.assertEqual(f["exemples"], [{"cmd": "api --demo", "explication": ""}])
        self.assertEqual(len(f["subtilites"]), 2)

    def test_face_b_categorie_et_signification(self):
        f = self.by["TESTB"]
        self.assertEqual(f["signification"], "Test de crochet et categorie")
        self.assertEqual(f["categories"], ["Cloud", "Réseau"])
        self.assertEqual(f["aliases"], ["Test de crochet et categorie", "tb"])

    def test_cas_avec_explication(self):
        f = self.by["testfmt"]
        self.assertEqual(f["cas_reguliers"][1]["cmd"], "testfmt -b")
        self.assertEqual(f["cas_reguliers"][1]["explication"], "deuxieme cas")

    def test_rubriques_sans_accent(self):
        """Les libelles non accentues doivent etre reconnus (robustesse corpus)."""
        f = self.by["testfmt"]
        self.assertEqual(f["pop"], 42) if "pop" in f else None
        self.assertEqual(f["popularite"], 42)
        self.assertEqual(f["role_fr"][:9], "Commande ")


class TestCorpus(unittest.TestCase):
    """Garde-fous sur le corpus complet (aucune ecriture disque)."""

    @classmethod
    def setUpClass(cls):
        cls.entries, cls.errors, cls.warnings, cls.unresolved = pr.build()

    def test_volume(self):
        self.assertGreaterEqual(len(self.entries), 1000)

    def test_aucune_puce_de_rubrique(self):
        """Un item de liste ne doit jamais etre une rubrique avalee ('**Role :** ...')."""
        for e in self.entries:
            for c in e["cas_reguliers"]:
                self.assertFalse(c["cmd"].startswith("**"), "%s : %s" % (e["nom"], c))
                self.assertNotIn(" :**", c["cmd"], "%s : %s" % (e["nom"], c))
            for s in e["subtilites"]:
                self.assertFalse(s.strip().startswith("**"), "%s : %s" % (e["nom"], s))

    def test_face_b_signification_complete(self):
        manquants = [e["nom"] for e in self.entries if e["face"] == "B" and not e["signification"]]
        self.assertEqual(manquants, [], "%d sigles sans signification" % len(manquants))

    def test_rubriques_declarees_conservees(self):
        """Garde-fou de regression : toute rubrique ecrite dans les .md doit arriver dans le JSON.

        C'est le test qui protege contre le bug historique d'avalement des rubriques par la
        lecture des puces (905 fiches touchees, ~940 rubriques Face B perdues a l'import).
        """
        import glob
        paires = (("**Syntaxe :**", "syntaxe"), ("**Précautions :**", "precautions"),
                  ("**Équivalents :**", "equivalents"), ("**Urgences/dangers :**", "urgences_dangers"),
                  ("**Signification :**", "signification"))
        declares = {}
        for f in glob.glob(str(ROOT / "face*.md")):
            txt = Path(f).read_text(encoding="utf-8")
            for lab, cle in paires:
                declares[cle] = declares.get(cle, 0) + txt.count(lab)
        for lab, cle in paires:
            n = sum(1 for e in self.entries if e.get(cle))
            self.assertGreaterEqual(n, declares[cle], "%s : %d importes < %d declares" % (cle, n, declares[cle]))

    def test_categories_toujours_presentes(self):
        for e in self.entries:
            self.assertTrue(e["categories"], "%s sans categorie" % e["nom"])

    def test_identifiants_uniques(self):
        ids = [e["id"] for e in self.entries]
        self.assertEqual(len(ids), len(set(ids)))

    def test_liens_normalises(self):
        """Les cibles de 'voir aussi' ne doivent pas garder d'indication d'OS entre parentheses."""
        for e in self.entries:
            for v in e["voir_aussi"]:
                self.assertEqual(v, v.strip(), "%s : '%s' non trimme" % (e["nom"], v))
                self.assertFalse(v.endswith(")"), "%s : '%s' garde une parenthese" % (e["nom"], v))


if __name__ == "__main__":
    unittest.main(verbosity=2)
