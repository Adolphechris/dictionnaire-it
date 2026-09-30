## `AES` — Advanced Encryption Standard [Sécurité]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** Rijndael
**Contextes :** chiffrer des données au repos ou en transit (chiffrement de disque LUKS/BitLocker, paquets HTTPS, VPN, stockage de secrets)
**Rôle :** Algorithme de chiffrement symétrique par bloc de référence mondiale (clés de 128, 192 ou 256 bits), adopté par le NIST et la NSA pour la protection des données sensibles.
**Syntaxe :** `openssl enc -aes-256-cbc -in fichier.txt -out fichier.enc`
**Cas réguliers :**
- `AES-256-GCM` — Mode de chiffrement symétrique combinant confidentialité et authentification d'intégrité (AEAD)
- `AES-256-CBC` — Mode par blocs chaînés nécessitant un vecteur d'initialisation (IV) aléatoire
**Origine :** Joan Daemen et Vincent Rijmen (1998 / standardisé par le NIST en 2001).
**Subtilités/confusions :**
- Étant symétrique, la MÊME clé secrète est utilisée pour chiffrer et déchiffrer.
- Bénéficie d'instructions matérielles dédiées (`AES-NI`) sur les processeurs modernes pour des débits de plusieurs Go/s.
**Urgences/dangers :** ⚠️ Ne jamais réutiliser le même vecteur d'initialisation (IV) ou nonce avec une même clé en mode AES-GCM.
**Précautions :** Privilégier systématiquement le mode `AES-256-GCM` aux modes plus anciens comme CBC ou ECB.
**Équivalents :** ChaCha20, Twofish, 3DES (obsolète)
**Voir aussi :** RSA, ECC, HMAC, openssl

## `RSA` — Rivest-Shamir-Adleman [Sécurité]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** —
**Contextes :** échanger des clés secrètes, signer numériquement des documents ou des commits Git, s'authentifier par clé SSH et certificats TLS
**Rôle :** Premier algorithme de chiffrement asymétrique (à clé publique et clé privée) historiquement robuste, basé sur la difficulté mathématique de la factorisation des grands nombres premiers.
**Syntaxe :** `ssh-keygen -t rsa -b 4096 -C "email@exemple.com"`
**Cas réguliers :**
- `RSA-4096` — Paire de clés RSA avec une longueur de clé de 4096 bits (standard recommandé)
- `RSA-2048` — Longueur minimale tolérée en production (1024 bits est désormais totalement proscrit)
**Origine :** Ron Rivest, Adi Shamir et Leonard Adleman (MIT, 1977).
**Subtilités/confusions :**
- La clé publique chiffre ou vérifie la signature ; la clé privée déchiffre ou signe.
- Plus lent et génère des clés beaucoup plus longues que la cryptographie sur courbes elliptiques (ECC / Ed25519).
**Urgences/dangers :** ⚠️ Les clés RSA de 1024 bits ou moins ne sont plus sûres et peuvent être cassées.
**Précautions :** Migrer les nouvelles clés d'authentification vers Ed25519 ou utiliser au minimum du RSA 3072/4096 bits.
**Équivalents :** ECC, Ed25519, DSA (obsolète)
**Voir aussi :** ECC, ssh-keygen, openssl, PKI

## `ECC` — Elliptic Curve Cryptography [Sécurité]
**Niveau :** avance | **Popularité :** 96 | **Aliases :** ECDSA, Ed25519
**Contextes :** s'authentifier de manière ultra-sécurisée et rapide sur des serveurs SSH, établir des sessions TLS 1.3, signer des transactions blockchain ou des paquets d'applications
**Rôle :** Algorithme de cryptographie à clé publique basé sur la structure algébrique des courbes elliptiques sur les corps finis, offrant une sécurité équivalente à RSA avec des clés beaucoup plus courtes.
**Syntaxe :** `ssh-keygen -t ed25519 -C "email@exemple.com"`
**Cas réguliers :**
- `Ed25519` — Courbe elliptique ultra-rapide et sécurisée (courbe Curve25519 par Daniel J. Bernstein)
- `ECDSA` — Algorithme de signature sur courbe elliptique standardisé par le NIST (ex: secp256r1)
**Origine :** Neal Koblitz et Victor S. Miller (1985).
**Subtilités/confusions :**
- Une clé Ed25519 de 256 bits offre un niveau de sécurité équivalent ou supérieur à une clé RSA de 3072 bits, tout en s'exécutant 10× plus vite !
**Urgences/dangers :** —
**Précautions :** Privilégier la courbe Curve25519 (Ed25519) aux courbes du NIST pour éviter les soupçons de portes dérobées historiques.
**Équivalents :** RSA, DSA
**Voir aussi :** RSA, ssh-keygen, TLS, PKI

## `TLS` — Transport Layer Security [Réseau/Sécurité]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** SSL (abus de langage)
**Contextes :** sécuriser les communications réseau sur Internet (HTTPS, SMTPS, IMAPS, WSS, VPN TLS) en garantissant la confidentialité, l'authenticité et l'intégrité des données
**Rôle :** Protocole cryptographique de la couche transport (modèle OSI) qui chiffre les échanges entre un client et un serveur au-dessus de TCP.
**Syntaxe :** `curl --tlsv1.3 https://exemple.com`
**Cas réguliers :**
- `TLS 1.3` — Version moderne et ultra-sécurisée du protocole (2018) réduisant la poignée de main (*handshake*) à 1 RTT et supprimant les suites de chiffrement obsolètes
- `TLS 1.2` — Version précédente encore largement déployée en rétro-compatibilité
**Origine :** IETF (1999) — conçu pour remplacer le protocole SSL (Secure Sockets Layer) d'Netscape.
**Subtilités/confusions :**
- Ne pas appeler SSL un protocole moderne : SSL 2.0 et SSL 3.0 sont officiellement devenus obsolètes et vulnérables (POODLE, BEAST).
**Urgences/dangers :** ⚠️ Désactiver TLS 1.0 et TLS 1.1 sur tous les serveurs web en production.
**Précautions :** Utiliser des outils d'audit comme SSL Labs pour vérifier la note de configuration TLS de vos serveurs (viser A+).
**Équivalents :** QUIC / HTTP/3, SSH, IPsec
**Voir aussi :** CA, PKI, HTTPS, certbot

## `SSL` — Secure Sockets Layer [Réseau/Sécurité]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** —
**Contextes :** ancêtre historique des protocoles de chiffrement web ; terme encore largement utilisé par abus de langage pour désigner les certificats HTTPS ou TLS
**Rôle :** Protocole cryptographique original développé par Netscape dans les années 1990 pour sécuriser les transactions sur le World Wide Web.
**Syntaxe :** `openssl s_client -connect exemple.com:443`
**Cas réguliers :**
- `Certificat SSL` — Appellation commerciale courante désignant en réalité un certificat numérique X.509/TLS
- `SSL 3.0` — Dernière version de SSL (1996), désormais bannie pour failles de sécurité majeures
**Origine :** Taher Elgamal / Netscape (1994).
**Subtilités/confusions :**
- SSL est le PREDECESSEUR de TLS. Tous les protocoles SSL (1.0, 2.0, 3.0) sont aujourd'hui obsolètes et désactivés.
**Urgences/dangers :** ⚠️ Ne jamais autoriser le fallback vers SSL 3.0 sous peine de subir des attaques par dégradation (*downgrade attacks*).
**Précautions :** Remplacer le terme SSL par TLS dans la documentation technique et les configurations.
**Équivalents :** TLS
**Voir aussi :** TLS, openssl, HTTPS, CA

## `PKI` — Public Key Infrastructure [Sécurité]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** IGP (Infrastructure à Clés Publiques)
**Contextes :** gérer le cycle de vie complet des certificats numériques (émission, renouvellement, révocation) dans une entreprise ou sur le Web global
**Rôle :** Ensemble de rôles, de politiques, d'équipements et de procédures nécessaires pour créer, gérer, distribuer, utiliser et révoquer des certificats numériques basés sur la cryptographie asymétrique.
**Syntaxe :** `openssl req -new -x509 -key server.key -out server.crt -days 365`
**Cas réguliers :**
- `Autorité de Certification (CA)` — Élément central de la PKI qui signe les certificats d'identité
- `Liste de Révocation de Certificats (CRL)` — Liste des certificats révoqués avant leur date d'expiration
**Origine :** Travaux UIT-T X.509 / IETF PKIX (1988).
**Subtilités/confusions :**
- Repose sur la confiance transitive : si le client fait confiance à la CA racine, il fait confiance à tous les certificats signés par cette CA.
**Urgences/dangers :** ⚠️ La compromission de la clé privée de la CA racine d'une PKI invalide la sécurité de tout le système.
**Précautions :** Conserver la clé privée de la CA racine hors-ligne (*Offline Root CA*) et utiliser des CA intermédiaires pour l'émission quotidienne.
**Équivalents :** Web of Trust (PGP)
**Voir aussi :** CA, CSR, X509, certbot

## `CA` — Certificate Authority [Sécurité]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** AC (Autorité de Certification)
**Contextes :** délivrer des certificats X.509 vérifiés pour des noms de domaine, des serveurs, des signatures de code ou des identités d'employés
**Rôle :** Tiers de confiance (entité certifiée) habilité à signer cryptographiquement des certificats numériques pour attester du lien entre une clé publique et l'identité de son propriétaire.
**Syntaxe :** `certbot --nginx -d exemple.com`
**Cas réguliers :**
- `Let's Encrypt` — CA publique, gratuite et automatisée (via protocole ACME) ayant démocratisé le HTTPS mondial
- `CA racine (Root CA)` — Certificat auto-signé pré-installé dans les magasins de confiance des navigateurs et OS
- `CA intermédiaire` — CA déléguée par la CA racine pour signer les certificats finaux
**Origine :** Spécification X.509 / IETF (1988).
**Subtilités/confusions :**
- Un navigateur web intègre une liste de ~150 CA racines de confiance par défaut.
**Urgences/dangers :** —
**Précautions :** Automatiser le renouvellement des certificats délivrés par les CA (durée de validité désormais réduite à 90 jours ou moins).
**Équivalents :** Let's Encrypt, DigiCert, Sectigo, HashiCorp Vault CA
**Voir aussi :** PKI, CSR, X509, certbot

## `CSR` — Certificate Signing Request [Sécurité]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** faire une demande officielle de certificat HTTPS auprès d'une Autorité de Certification (CA) en fournissant sa clé publique et son identité sans exposer sa clé privée
**Rôle :** Fichier de demande encodé (format PEM/PKCS#10) contenant la clé publique d'un serveur et des informations d'identité (nom de domaine, organisation, pays), envoyé à une CA pour signature.
**Syntaxe :** `openssl req -new -key server.key -out server.csr`
**Cas réguliers :**
- `openssl req -newkey rsa:4096 -nodes -keyout server.key -out server.csr` — Générer simultanément la clé privée et le CSR
- `openssl req -in server.csr -noout -text` — Inspecter et vérifier le contenu texte d'un fichier CSR
**Origine :** Norme PKCS#10 (RSA Laboratories, 1993).
**Subtilités/confusions :**
- Le fichier CSR ne contient JAMAIS la clé privée (celle-ci reste strictement sur le serveur hôte).
**Urgences/dangers :** —
**Précautions :** S'assurer de remplir correctement le champ `Subject Alternative Name` (SAN) dans le CSR car les navigateurs modernes ignorent le champ `Common Name` (CN).
**Équivalents :** SPKAC
**Voir aussi :** CA, PKI, X509, openssl

## `X.509` — Format standard de certificat numérique [Sécurité]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** X509, PKIX
**Contextes :** structurer les certificats de sécurité pour le HTTPS, le VPN, la signature de code, le protocole S/MIME et les identités d'infrastructure
**Rôle :** Standard international de l'UIT-T définissant le format de représentation de certificats à clé publique, codés en ASN.1 (formats PEM ou DER).
**Syntaxe :** `openssl x509 -in cert.crt -text -noout`
**Cas réguliers :**
- `Format PEM` — Encodage Base64 lisible encadré par `-----BEGIN CERTIFICATE-----` (extension `.crt`, `.pem`)
- `Format DER` — Encodage binaire brut du certificat (extension `.der`, `.cer`)
- `Format PKCS#12 (.pfx/.p12)` — Archive protégée par mot de passe contenant le certificat ET la clé privée
**Origine :** Union Internationale des Télécommunications (UIT-T, 1988).
**Subtilités/confusions :**
- Un certificat X.509 contient : la version, le numéro de série, l'algorithme de signature, l'émetteur (CA), la période de validité, le sujet (domaine), la clé publique et les extensions (SAN).
**Urgences/dangers :** —
**Précautions :** Convertir entre PEM et DER via `openssl x509 -inform DER -in cert.der -outform PEM -out cert.pem`.
**Équivalents :** Cose, PGP Key
**Voir aussi :** CA, PKI, CSR, openssl

## `HMAC` — Hash-based Message Authentication Code [Sécurité]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** vérifier l'intégrité et l'authenticité d'un message échangé entre deux parties partageant un secret (signatures d'API HTTP, tokens JWT, vérification de webhooks)
**Rôle :** Construction cryptographique combinant une fonction de hachage (SHA-256, SHA-512) avec une clé secrète partagée pour produire un empreinte d'authentification inaltérable.
**Syntaxe :** `echo -n "message" | openssl dgst -sha256 -hmac "cle_secrete"`
**Cas réguliers :**
- `HMAC-SHA256` — Algorithme de signature d'API et de webhooks le plus utilisé (GitHub, Stripe, AWS)
- `HMAC-SHA512` — Variante à haute sécurité pour les environnements sensibles
**Origine :** Mihir Bellare, Ran Canetti et Hugo Krawczyk (1996 / RFC 2104).
**Subtilités/confusions :**
- Diffère d'un simple hachage (`sha256(message)`) car il exige la connaissance d'une **clé secrète** pour générer ou valider le hachage.
**Urgences/dangers :** ⚠️ Toujours utiliser une comparaison à temps constant (*timing-safe comparison*) lors de la vérification d'un HMAC pour éviter les attaques par canal auxiliaire (*timing attacks*).
**Précautions :** Choisir une clé secrète HMAC d'une longueur au moins égale à la taille de la sortie du hachage (ex: 256 bits / 32 octets aléatoires pour SHA-256).
**Équivalents :** CMAC, Poly1305, KMAC
**Voir aussi :** JWT, SHA256, openssl

## `JWT` — JSON Web Token [Web/Sécurité]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** RFC 7519
**Contextes :** transmettre des informations d'authentification et de session de manière compacte et sécurisée entre un client (SPA React/Flutter) et un serveur d'API REST
**Rôle :** Standard ouvert (RFC 7519) définissant un format compact et auto-contenu pour échanger des affirmations (*claims*) sous forme d'objet JSON signé (HMAC ou RSA/ECC).
**Syntaxe :** `Header.Payload.Signature` (3 parties séparées par des points et encodées en Base64URL)
**Cas réguliers :**
- `Bearer Token` — Transmission du JWT dans l'en-tête HTTP : `Authorization: Bearer eyJhbGci...`
- `Access Token` — JWT à courte durée de vie (ex: 15 min) contenant l'ID et les rôles de l'utilisateur
- `Refresh Token` — Jeton permettant d'obtenir un nouvel Access Token sans ressaisir ses identifiants
**Origine :** Michael B. Jones, John Bradley, Nat Sakimura / IETF (2015).
**Subtilités/confusions :**
- Un JWT standard est **SIGNE mais pas CHIFFRE** par défaut : n'importe qui peut décoder le payload Base64 pour en lire le contenu ! Ne jamais y mettre de mot de passe ou donnée confidentielle.
**Urgences/dangers :** ⚠️ Rejeter impérativement les tokens spécifiant l'algorithme `alg: "none"` (faille classique d'implémentation).
**Précautions :** Conserver les JWT sensibles dans des cookies `HttpOnly; Secure; SameSite=Strict` plutôt que dans le `localStorage` du navigateur pour contrer les attaques XSS.
**Équivalents :** PASETO, Macaroon, SAML
**Voir aussi :** HMAC, OAuth2, SSO, CORS

## `OWASP` — Open Worldwide Application Security Project [Sécurité]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** auditer la sécurité des applications web, former les équipes de développement aux bonnes pratiques de codage sécurisé, appliquer le OWASP Top 10
**Rôle :** Fondation à but non lucratif dédiée à l'amélioration de la sécurité des logiciels, célèbre pour ses guides, standards et sa liste des 10 risques de sécurité applicative les plus critiques (*OWASP Top 10*).
**Syntaxe :** (Organisation / Référentiel de sécurité)
**Cas réguliers :**
- `OWASP Top 10` — Classement de référence des 10 failles web les plus courantes (Injection, Authentification brisée, XSS, Misconfiguration…)
- `OWASP ASVS` — Application Security Verification Standard (référentiel de critères de sécurité pour les audits)
- `OWASP ZAP` — Zed Attack Proxy (outil open source de scan de vulnérabilités web)
**Origine :** Mark Curphey (2001).
**Subtilités/confusions :**
- OWASP n'est pas un outil en soi, mais une communauté et un ensemble de standards de sécurité universellement reconnus.
**Urgences/dangers :** —
**Précautions :** Intégrer la checklist du OWASP Top 10 dès la phase de conception d'une architecture logicielle (*Security by Design*).
**Équivalents :** SANS Top 25, NIST SP 800-53, CIS Controls
**Voir aussi :** XSS, CSRF, SQLi, semgrep

## `XSS` — Cross-Site Scripting [Web/Sécurité]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** comprendre, détecter et corriger l'injection de scripts JavaScript malveillants exécutés dans le navigateur d'un utilisateur légitime
**Rôle :** Faille de sécurité web majeure permettant à un attaquant d'injecter du code exécutable côté client (JavaScript) dans des pages web vues par d'autres utilisateurs.
**Syntaxe :** (Vulnérabilité applicative web)
**Cas réguliers :**
- `Stored XSS (Persistant)` — Le script malveillant est stocké en base de données et ré-exécuté chez tous les visiteurs affichant la page
- `Reflected XSS (Refléte)` — Le script malveillant est injecté via un lien contenant un paramètre d'URL non nettoyé
- `DOM-based XSS` — La vulnérabilité réside exclusivement dans le code JavaScript côté client qui manipule le DOM de manière non sécurisée
**Origine :** Découverte dans les premiers navigateurs Netscape/Internet Explorer (1999).
**Subtilités/confusions :**
- Permet à l'attaquant de voler des cookies de session, de détourner le compte de la victime ou de rediriger l'utilisateur vers un site de phishing.
**Urgences/dangers :** ⚠️ Ne JAMAIS insérer des données utilisateur brutes dans le DOM via `innerHTML` ou `dangerouslySetInnerHTML`.
**Précautions :** Échapper systématiquement toutes les données utilisateur affichées dans l'HTML et appliquer des en-têtes `Content-Security-Policy` (CSP) stricts.
**Équivalents :** CSRF, SQLi
**Voir aussi :** OWASP, CSRF, CORS, JWT

## `CSRF` — Cross-Site Request Forgery [Web/Sécurité]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** XSRF, Sea-Surf
**Contextes :** protéger une application web contre la soumission non sollicitée d'actions malveillantes exécutées à l'insu d'un utilisateur authentifié
**Rôle :** Attaque web qui piège le navigateur d'une victime authentifiée pour lui faire exécuter une action non désirée sur une application web dans laquelle elle est actuellement connectée.
**Syntaxe :** (Vulnérabilité applicative web)
**Cas réguliers :**
- `CSRF Token` — Jeton secret, unique et imprévisible généré par le serveur et inclus dans chaque formulaire pour valider la provenance de la requête
- `Cookie SameSite` — Attribut de cookie (`SameSite=Lax` ou `Strict`) empêchant le navigateur d'envoyer le cookie d'authentification lors de requêtes cross-site
**Origine :** Découverte au début des années 2000 / vulgarisée par Peter Watkins (2001).
**Subtilités/confusions :**
- Diffère de XSS : l'attaque XSS exécute du code malveillant chez la victime, alors que CSRF exploite la **confiance** que le serveur accorde au navigateur de la victime.
**Urgences/dangers :** ⚠️ Les requêtes modifiant l'état du serveur (POST, PUT, DELETE) doivent impérativement être protégées par un jeton anti-CSRF.
**Précautions :** Utiliser des cookies de session configurés avec `SameSite=Lax` ou `SameSite=Strict` et vérifier les en-têtes `Origin` et `Referer`.
**Équivalents :** XSS, SSRF
**Voir aussi :** OWASP, XSS, CORS, JWT

## `SQLi` — SQL Injection [Bases de données/Sécurité]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Injection SQL
**Contextes :** comprendre, auditer et prévenir l'une des failles de sécurité les plus destructrices, permettant d'exécuter des commandes SQL non autorisées sur une base de données
**Rôle :** Technique d'attaque par laquelle un utilisateur malveillant injecte des fragments de code SQL dans des champs de saisie ou des paramètres d'URL pour altérer la requête exécutée par le serveur.
**Syntaxe :** `SELECT * FROM users WHERE username = 'admin' OR '1'='1' --'`
**Cas réguliers :**
- `In-band SQLi (Error/Union)` — L'attaquant extrait directement les données de la base affichées dans la réponse HTTP ou les messages d'erreur
- `Blind SQLi (Boolean/Time-based)` — L'attaquant déduit les données caractère par caractère en mesurant le temps de réponse du serveur (`WAITFOR DELAY` / `SLEEP()`)
**Origine :** Jeff Forristal « rain forest puppy » (1998 / Phrack magazine).
**Subtilités/confusions :**
- Peut permettre non seulement le vol de toute la base de données, mais aussi l'effacement complet des tables (`DROP TABLE`) ou l'exécution de commandes système (`xp_cmdshell`).
**Urgences/dangers :** ⚠️ Ne JAMAIS concaténer des chaînes de caractères saisies par l'utilisateur directement dans une requête SQL !
**Précautions :** Utiliser EXCLUSIVEMENT des requêtes préparées avec des requêtes paramétrées (*Prepared Statements*) ou un ORM sécurisé.
**Équivalents :** NoSQLi, Command Injection
**Voir aussi :** OWASP, SQL, ORM, PostgreSQL

## `CORS` — Cross-Origin Resource Sharing [Web/Sécurité]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** autoriser ou restreindre les requêtes HTTP AJAX (`fetch`, `axios`) effectuées par un navigateur depuis un domaine (ex: `app.com`) vers un serveur d'API situé sur un autre domaine (ex: `api.com`)
**Rôle :** Mécanisme de sécurité basé sur des en-têtes HTTP HTTP qui permet à un serveur d'indiquer les origines (domaines, protocoles, ports) autres que la sienne autorisées à charger ses ressources.
**Syntaxe :** En-tête HTTP serveur : `Access-Control-Allow-Origin: https://mon-app.com`
**Cas réguliers :**
- `Access-Control-Allow-Origin` — Spécifier les origines autorisées (`*` pour public, ou une URL exacte)
- `Access-Control-Allow-Methods` — Lister les méthodes HTTP autorisées (ex: `GET, POST, OPTIONS`)
- `Preflight Request (OPTIONS)` — Requête préliminaire automatique envoyée par le navigateur pour vérifier les autorisations avant une requête complexe (ex: avec `POST` JSON ou en-têtes personnalisés)
**Origine :** Spécification W3C / WHATWG (2009).
**Subtilités/confusions :**
- CORS est une restriction appliquée par le **navigateur web** pour protéger l'utilisateur, et non un mécanisme de sécurité du serveur ! Un outil comme `curl` ignore totalement les règles CORS.
**Urgences/dangers :** ⚠️ Ne jamais renvoyer `Access-Control-Allow-Origin: *` conjointement avec `Access-Control-Allow-Credentials: true`.
**Précautions :** Configurer une liste blanche dynamique des domaines autorisés au niveau du middleware de votre framework backend.
**Équivalents :** Same-Origin Policy (SOP)
**Voir aussi :** JWT, XSS, CSRF, HTTP

## `CSP` — Content Security Policy [Web/Sécurité]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** —
**Contextes :** se protéger contre les attaques par injection de code (XSS, détournement de clics / clickjacking) en restreignant les sources de scripts, styles et médias autorisés à s'exécuter
**Rôle :** En-tête de sécurité HTTP (`Content-Security-Policy`) qui permet aux administrateurs de déclarer une liste blanche de sources approuvées pour les contenus exécutables du site web.
**Syntaxe :** En-tête HTTP : `Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com`
**Cas réguliers :**
- `script-src 'self'` — N'autoriser l'exécution que des scripts JavaScript provenant du même domaine
- `frame-ancestors 'none'` — Interdire totalement l'intégration du site web dans une `<iframe>` (protection anti-clickjacking)
- `Report-Only Mode` — Tester la politique CSP sans bloquer les ressources grâce à `Content-Security-Policy-Report-Only`
**Origine :** Brandon Sterne / Mozilla (2004) / Standardisé par le W3C (2012).
**Subtilités/confusions :**
- Bloque l'exécution du JavaScript inline (`<script>alert(1)</script>`) par défaut sauf si le mot-clé `'unsafe-inline'` ou un `nonce` cryptographique est fourni.
**Urgences/dangers :** —
**Précautions :** Utiliser des jetons à usage unique (`nonce-XXXXX`) pour autoriser les scripts légitimes sans assouplir la politique globale.
**Équivalents :** X-Frame-Options, X-Content-Type-Options
**Voir aussi :** XSS, CORS, OWASP, HTTPS

## `HSTS` — HTTP Strict Transport Security [Web/Sécurité]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** RFC 6797
**Contextes :** forcer les navigateurs web à ne communiquer avec votre site qu'en HTTPS sécurisé et empêcher toute tentative de dégradation vers le protocole HTTP non chiffré
**Rôle :** En-tête de réponse HTTP qui ordonne au navigateur d'interdire toute connexion non chiffrée (HTTP) vers le domaine pendant une période donnée et de rediriger automatiquement les requêtes en interne vers HTTPS.
**Syntaxe :** `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`
**Cas réguliers :**
- `max-age=31536000` — Conserver la consigne de connexion HTTPS stricte pendant 1 an (en secondes)
- `includeSubDomains` — Appliquer la règle HTTPS obligatoire à TOUS les sous-domaines
- `preload` — Soumettre le domaine à la liste d'inclusion universelle d'HSTS (*HSTS Preload List*) intégrée directement dans les navigateurs Chrome/Firefox/Safari
**Origine :** Jeff Hodges, Collin Jackson, Adam Barth / IETF (2012 / RFC 6797).
**Subtilités/confusions :**
- Protège contre les attaques de type Man-in-the-Middle (Mitm) et le stripping SSL (ex: outil SSLstrip) lors de la toute première connexion d'un utilisateur.
**Urgences/dangers :** ⚠️ Une fois `includeSubDomains` activé et pré-chargé, si l'un de vos sous-domaines n'a pas de certificat TLS valide, il deviendra totalement inaccessible !
**Précautions :** Tester HSTS avec un `max-age` court (ex: 300 secondes) avant d'activer une durée de 1 an avec `preload`.
**Équivalents :** HTTPS Redirection
**Voir aussi :** TLS, SSL, HTTPS, CA

## `WAF` — Web Application Firewall [Sécurité]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Pareto WAF
**Contextes :** filtrer, surveiller et bloquer le trafic HTTP/HTTPS malveillant ciblant une application web (injections SQL, XSS, bots, attaques DDoS de couche 7)
**Rôle :** Pare-feu applicatif qui s'interpose en reverse-proxy devant les serveurs web pour analyser les requêtes applicatives au niveau de la couche 7 du modèle OSI.
**Syntaxe :** (Équipement réseau ou service cloud : Cloudflare WAF, AWS WAF, ModSecurity)
**Cas réguliers :**
- `ModSecurity` — Moteur WAF open source classique souvent intégré comme module Nginx ou Apache
- `Cloudflare / AWS WAF` — WAF cloud managé qui bloque automatiquement les signatures d'attaques connues sans surcoût d'infrastructure
**Origine :** Eran Reshef / Imperva & Sanctum (fin des années 1990).
**Subtilités/confusions :**
- Un pare-feu réseau classique (iptables, UFW) filtre les IPs et ports (couches 3/4) ; un WAF analyse le contenu des requêtes HTTP (payloads JSON, formulaires, cookies).
**Urgences/dangers :** —
**Précautions :** Un WAF est une couche de défense en profondeur (*Defense in Depth*) et ne doit JAMAIS remplacer la correction des failles dans le code source de l'application !
**Équivalents :** RASP (Runtime Application Self-Protection), IDS/IPS
**Voir aussi :** OWASP, SQLi, XSS, Cloudflare

## `IDS` — Intrusion Detection System [Sécurité]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** NIDS, HIDS
**Contextes :** surveiller le réseau ou les hôtes pour détecter les activités suspectes, les scannings de ports, les signatures de malwares ou les tentatives de brèche de sécurité
**Rôle :** Système passif d'analyse de sécurité qui écoute le trafic réseau ou les journaux système et génère une alerte lorsqu'une menace ou une anomalie est identifiée.
**Syntaxe :** `snort -A console -q -c /etc/snort/snort.conf`
**Cas réguliers :**
- `NIDS (Network IDS)` — Analyse le trafic réseau en mode miroir (*port SPAN/TAP*) (ex: Snort, Suricata, Zeek)
- `HIDS (Host IDS)` — Analyse l'activité interne d'une machine hôte (fichiers de log, intégrité système, appels système) (ex: OSSEC, Wazuh)
**Origine :** James Anderson (1980) / Dorothy Denning (1986).
**Subtilités/confusions :**
- Un IDS est **PASSIF** : il détecte et alerte les équipes de sécurité, mais n'interrompt pas le trafic suspect de lui-même (contrairement à un IPS).
**Urgences/dangers :** —
**Précautions :** Calibrer soigneusement les règles de détection pour éviter l'épuisement des équipes dû aux faux positifs.
**Équivalents :** IPS, SIEM
**Voir aussi :** IPS, SIEM, Suricata, tcpdump

## `IPS` — Intrusion Prevention System [Sécurité]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** NIPS, HIPS
**Contextes :** bloquer automatiquement et en temps réel le trafic réseau malveillant ou les tentatives d'exploit dès qu'ils sont identifiés
**Rôle :** Système d'analyse de sécurité actif placé en ligne (*inline*) sur le flux réseau, capable de rejeter des paquets, de fermer des connexions TCP ou de bannir des IPs attaquantes.
**Syntaxe :** `suricata -c /etc/suricata/suricata.yaml -i eth0`
**Cas réguliers :**
- `Suricata / Snort 3` — Moteurs IDS/IPS open source haute performance capables d'inspecter les paquets en temps réel à plusieurs dizaines de Gbit/s
- `Fail2ban` — IPS hôte léger bannières d'IPs basées sur l'analyse de logs
**Origine :** Évolution des systèmes IDS à la fin des années 1990 (NSS Group).
**Subtilités/confusions :**
- Étant placé en ligne (*inline*), une panne ou une lenteur de l'IPS peut couper le trafic réseau légitime de toute l'entreprise.
**Urgences/dangers :** ⚠️ Un faux positif agressif sur un IPS peut bloquer les communications légitimes d'un client ou d'un partenaire commercial.
**Précautions :** Déployer d'abord les nouvelles règles en mode IDS (détection seule) pendant quelques semaines avant d'activer le mode IPS (blocage).
**Équivalents :** IDS, WAF, Firewall
**Voir aussi :** IDS, WAF, fail2ban-client, Suricata

## `SIEM` — Security Information and Event Management [Sécurité]
**Niveau :** avance | **Popularité :** 94 | **Aliases :** —
**Contextes :** centraliser, corréler et analyser les journaux de sécurité (*logs*) de l'ensemble des équipements informatiques (serveurs, pare-feux, routeurs, postes de travail) pour détecter des attaques complexes
**Rôle :** Plateforme de sécurité d'entreprise qui agrège des volumes massifs de logs en temps réel, applique des règles de corrélation et génère des alertes pour le centre d'opérations de sécurité (SOC).
**Syntaxe :** (Plateformes : Splunk, Elastic SIEM / ELK, Microsoft Sentinel, IBM QRadar)
**Cas réguliers :**
- `Agrégation de logs` — Collecte centralisée via Syslog, Beats, Fluentbit
- `Corrélation d'événements` — Détecter par exemple qu'un compte a échoué 50 connexions SSH (log serveur), puis a ouvert une session VPN depuis un pays étranger (log VPN)
**Origine :** Mark Nicolett et Amrit Williams (Gartner, 2005) — fusion des concepts SIM (Security Information Management) et SEM (Security Event Management).
**Subtilités/confusions :**
- Le SIEM collecte et analyse les événements ; le **SOAR** automatise les actions de réponse à ces événements.
**Urgences/dangers :** —
**Précautions :** Définir des politiques de rétention et d'indexation claires pour maîtriser les coûts de stockage des logs.
**Équivalents :** SOAR, XDR, ELK Stack
**Voir aussi :** SOAR, EDR, Elasticsearch, auditd

## `SOAR` — Security Orchestration, Automation, and Response [Sécurité]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** automatiser les flux de réponse aux incidents de sécurité (remplacement des tâches manuelles des analystes SOC par des workflows programmés)
**Rôle :** Plateforme logicielle qui permet aux organisations de définir des procédures de réponse automatisées (*playbooks*) interconnectant leurs outils de sécurité (SIEM, EDR, Firewall, Email).
**Syntaxe :** (Plateformes : Splunk SOAR / Phantom, Palo Alto Cortex XSOAR, Shuffle open source)
**Cas réguliers :**
- `Playbook automatisé` — Réception d'une alerte de phishing -> extraction de l'IP malveillante -> ajout de l'IP dans le WAF/Firewall -> isolation du poste infecté via l'EDR -> fermeture du ticket SOC
**Origine :** Terme forgé par Gartner (2017).
**Subtilités/confusions :**
- Compléte le SIEM en transformant les **alertes** textuelles en **actions concrètes automatisées** sans intervention humaine systématique.
**Urgences/dangers :** —
**Précautions :** Prévoir des étapes de validation humaine (*Human-in-the-Loop*) pour les actions destructrices ou à fort impact (ex: isoler un serveur de base de données de production).
**Équivalents :** SIEM, XDR
**Voir aussi :** SIEM, EDR, WAF

## `EDR` — Endpoint Detection and Response [Sécurité]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** —
**Contextes :** surveiller en continu l'activité des postes de travail et serveurs (processus, modifications de registre, connexions réseau) pour bloquer les ransomwares et attaques avancées
**Rôle :** Outil de sécurité installé directement sur les terminaux (endpoints) combinant la détection comportementale en temps réel, l'enregistrement d'activité et la capacité de réponse à distance (isolation réseau, suppression de processus).
**Syntaxe :** (Solutions : CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, Wazuh)
**Cas réguliers :**
- `Détection comportementale` — Détecter qu'un document Word a lancé PowerShell qui télécharge un script exécutable (comportement d'attaque classique)
- `Isolation du terminal` — Déconnecter virtuellement la machine du réseau pour stopper la propagation d'un ransomware tout en maintenant l'accès pour les analystes SOC
**Origine :** Anton Chuvakin (Gartner, 2013).
**Subtilités/confusions :**
- Évolution moderne de l'antivirus traditionnel : l'EDR ne se fie pas aux simples signatures de fichiers, mais analyse le **comportement dynamique** du système.
**Urgences/dangers :** —
**Précautions :** S'assurer de la compatibilité des agents EDR lors des mises à jour du noyau OS sous Linux (modules noyaux ou eBPF).
**Équivalents :** Antivirus Next-Gen (NGAV), XDR
**Voir aussi :** XDR, SIEM, auditd, lynis

## `XDR` — Extended Detection and Response [Sécurité]
**Niveau :** avance | **Popularité :** 92 | **Aliases :** —
**Contextes :** Unifier la détection et la réponse aux menaces de sécurité en unifiant les données des postes (EDR), du réseau (NDR), du cloud et des identités (IAM)
**Rôle :** Évolution convergente de l'EDR et du SIEM qui unifie la visibilité et la corrélation des données de sécurité sur plusieurs couches de l'infrastructure pour une réponse automatisée globale.
**Syntaxe :** (Solutions : Palo Alto Cortex XDR, Trend Micro Vision One, CrowdStrike XDR)
**Cas réguliers :**
- `Corrélation multi-couches` — Lier une anomalie d'authentification cloud (IAM), avec une connexion réseau suspecte (NDR) et la création d'un fichier suspect sur un poste (EDR)
**Origine :** Nir Zuk / Palo Alto Networks (2018).
**Subtilités/confusions :**
- L'EDR se limite aux terminaux ; le XDR s'étend au réseau, au cloud, aux e-mails et aux bases de données.
**Urgences/dangers :** —
**Précautions :** Exige une intégration étroite entre les différents composants logiciels de l'infrastructure de l'entreprise.
**Équivalents :** EDR + SIEM + SOAR
**Voir aussi :** EDR, SIEM, SOAR, IAM

## `CVE` — Common Vulnerabilities and Exposures [Sécurité]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Identifiant CVE
**Contextes :** faire référence à une vulnérabilité de sécurité connue publiquement de manière unique et universelle (ex: `CVE-2021-44228` pour Log4Shell)
**Rôle :** Dictionnaire public de n° d'identification uniques attribués à des vulnérabilités de sécurité informatiques connues, géré par le MITRE et le NVD.
**Syntaxe :** Format : `CVE-AAAA-NNNNN` (ex: `CVE-2024-3094` pour la porte dérobée XZ Utils)
**Cas réguliers :**
- `CVE ID` — Identifiant unique permettant de rechercher des détails factuels et des correctifs sur n'importe quelle base de sécurité
- `Base NVD` — National Vulnerability Database (base américaine qui enrichit les CVEs avec des scores de gravité CVSS)
**Origine :** MITRE Corporation (1999).
**Subtilités/confusions :**
- Un identifiant CVE ne décrit que le problème ; la gravité du problème est mesurée par le score **CVSS**.
**Urgences/dangers :** —
**Précautions :** Configurer vos scanners de vulnérabilités (Trivy, Grype) pour suivre quotidiennement les nouvelles CVEs publiées sur vos dépendances.
**Équivalents :** GHSA (GitHub Security Advisory)
**Voir aussi :** CVSS, CWE, trivy, grype

## `CVSS` — Common Vulnerability Scoring System [Sécurité]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Score CVSS
**Contextes :** évaluer et prioriser la gravité technique d'une vulnérabilité informatique sur une échelle de 0.0 à 10.0
**Rôle :** Standard ouvert d'évaluation de la gravité des vulnérabilités logicielles, calculé en fonction de critères de complexité, d'accès (réseau/local), de privilèges requis et d'impact (CIA).
**Syntaxe :** Score numérique de `0.0` (insignifiant) à `10.0` (critique maximale)
**Cas réguliers :**
- `CVSS v3.1 / v4.0` — Versions actuelles du système de calcul du score
- `Score de 9.0 à 10.0` — Gravité CRITIQUE (nécessite une mise à jour d'urgence immédiate)
- `Score de 7.0 à 8.9` — Gravité ÉLEVÉE (HIGH)
**Origine :** FIRST (Forum of Incident Response and Security Teams, 2005).
**Subtilités/confusions :**
- Le score de base CVSS mesure la gravité technique intrinsèque ; la priorité de correction dépend aussi du contexte réel (ex: si le composant vulnérable est exposé sur Internet ou non).
**Urgences/dangers :** ⚠️ Une vulnérabilité avec un score CVSS ≥ 9.8 exploitable à distance sans authentification doit être corrigée sous 24h.
**Précautions :** Prendre en compte le score environnemental CVSS adapté à votre propre architecture.
**Équivalents :** EPSS (Exploit Prediction Scoring System)
**Voir aussi :** CVE, CWE, trivy

## `CWE` — Common Weakness Enumeration [Sécurité]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** classifier les types de failles de sécurité et erreurs de conception logicielle par catégories (ex: `CWE-79` pour XSS, `CWE-89` pour Injection SQL)
**Rôle :** Dictionnaire communautaire répertoriant les types et catégories de faiblesses et d'erreurs d'architecture ou de programmation logicielle à l'origine des failles de sécurité.
**Syntaxe :** Format : `CWE-NNN` (ex: `CWE-400` pour l'épuisement de ressources)
**Cas réguliers :**
- `CWE-79` — Neutralisation incorrecte d'entrées lors de la génération de pages Web (XSS)
- `CWE-89` — Neutralisation incorrecte d'éléments utilisés dans une commande SQL (SQL Injection)
- `CWE-119` — Restriction incorrecte des opérations dans les limites d'un mémoire tampon (Buffer Overflow)
**Origine :** MITRE Corporation (2006).
**Subtilités/confusions :**
- La **CVE** est une instance spécifique de vulnérabilité dans un produit donné (ex: Log4Shell) ; la **CWE** est la catégorie générale d'erreur (ex: désérialisation non sécurisée).
**Urgences/dangers :** —
**Précautions :** Utiliser les identifiants CWE dans les rapports de static analysis (Semgrep, SonarQube) pour former les développeurs à éviter des catégories complètes de bugs.
**Équivalents :** OWASP Categories
**Voir aussi :** CVE, CVSS, OWASP, semgrep

## `SBOM` — Software Bill of Materials [DevOps/Sécurité]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** Inventaire logiciel
**Contextes :** répertorier l'intégralité des composants open source, bibliothèques, versions et licences intégrés dans un binaire ou une image conteneur
**Rôle :** Fichier d'inventaire formel structuré (formats SPDX ou CycloneDX) listant tous les composants et dépendances de la chaîne d'approvisionnement logicielle d'une application.
**Syntaxe :** `syft mon-image:v1 -o spdx-json > sbom.json`
**Cas réguliers :**
- `SPDX` — Standard ISO/IEC 5962 pour le partage d'inventaires logiciels et de licences
- `CycloneDX` — Standard OWASP léger dédié à la sécurité de la chaîne d'approvisionnement
**Origine :** Décret exécutif américain EO 14028 (2021) / NTIA.
**Subtilités/confusions :**
- Le SBOM est l'équivalent de la liste des ingrédients sur un emballage alimentaire : il permet de savoir instantanément si votre application contient une bibliothèque vulnérable sans avoir à ré-analyser tout le code source.
**Urgences/dangers :** —
**Précautions :** Générer un SBOM automatiquement à chaque étape de build CI/CD et le signer avec Cosign.
**Équivalents :** SPDX, CycloneDX
**Voir aussi :** syft, grype, trivy, cosign

## `Zero Trust` — Architecture de sécurité sans confiance implicite [Sécurité]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** ZTA (Zero Trust Architecture)
**Contextes :** concevoir la sécurité des réseaux modernes en partant du principe qu'aucun réseau (même le réseau local d'entreprise / LAN) n'est sûr et que toute requête doit être authentifiée
**Rôle :** Modèle stratégique de cybersécurité résumé par la maxime « *Never Trust, Always Verify* » (Ne jamais faire confiance, toujours vérifier), exigeant l'authentification et l'autorisation continues de chaque utilisateur et appareil.
**Syntaxe :** (Paradigme d'architecture réseau et sécurité)
**Cas réguliers :**
- `Vérification continue` — Exiger l'authentification MFA, vérifier la santé du poste (EDR) et restreindre les accès au strict nécessaire (principe du moindre privilège)
- `Micro-segmentation` — Découper les réseaux en zones isolées pour empêcher les déplacements latéraux d'un attaquant en cas d'intrusion
**Origine :** John Kindervag / Forrester Research (2010) / Standardisé par le NIST SP 800-207 (2020).
**Subtilités/confusions :**
- Remplace le modèle de sécurité périmétrique traditionnel (« château fort avec douves » / VPN d'entreprise) qui considérait le réseau interne comme sûr par défaut.
**Urgences/dangers :** —
**Précautions :** Implémenter Zero Trust progressivement en commençant par la gestion centralisée des identités (IAM/SSO) et le MFA obligatoire.
**Équivalents :** ZTNA (Zero Trust Network Access), BeyondCorp (Google)
**Voir aussi :** IAM, SSO, EDR, VPN

## `HTTP` — Hypertext Transfer Protocol [Web]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** RFC 9110
**Contextes :** échanger des ressources (documents HTML, réponses JSON, images) entre un client (navigateur, mobile) et un serveur web
**Rôle :** Protocole applicatif de niveau 7 (modèle OSI) fonctionnant selon le schéma requête-réponse sur le protocole de transport TCP.
**Syntaxe :** `curl -v http://exemple.com`
**Cas réguliers :**
- `HTTP/1.1` — Version textuelle classique avec connexions persistantes (`Keep-Alive`)
- `HTTP/2` — Version binaire multiplexée permettant d'envoyer plusieurs requêtes en parallèle sur un unique tuyau TCP
- `HTTP/3` — Version binaire moderne basée sur le protocole de transport UDP QUIC (supprime le blocage de tête de ligne)
**Origine :** Tim Berners-Lee (CERN, 1989 / RFC 1945).
**Subtilités/confusions :**
- Protocole sans état (*stateless*) : chaque requête est indépendante, d'où la nécessité des cookies et des tokens pour gérer les sessions.
**Urgences/dangers :** ⚠️ Le protocole HTTP transmet toutes les données en texte clair (risques de lecture/interception des mots de passe sur le réseau).
**Précautions :** Utiliser systématiquement la version chiffrée HTTPS en production.
**Équivalents :** HTTPS, WebSocket, gRPC
**Voir aussi :** HTTPS, REST, TLS, curl

## `HTTPS` — Hypertext Transfer Protocol Secure [Web/Sécurité]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** HTTP over TLS
**Contextes :** sécuriser les échanges d'un site web ou d'une API REST pour garantir la confidentialité et l'intégrité des données contre les attaques réseau
**Rôle :** Variante sécurisée du protocole HTTP où les paquets applicatifs sont entièrement chiffrés par une couche TLS/SSL.
**Syntaxe :** `curl -v https://exemple.com`
**Cas réguliers :**
- `Port 443` — Port réseau standard utilisé par défaut pour HTTPS (contre le port 80 pour HTTP)
- `Certificat TLS X.509` — Certificat authentifiant le nom de domaine du serveur auprès du client
**Origine :** Netscape Communications (1994).
**Subtilités/confusions :**
- Le chiffrement HTTPS protège le chemin complet du nœud (URL, en-têtes, corps de requête JSON, cookies), mais ne masque pas l'adresse IP et le nom de domaine cible (visible via SNI).
**Urgences/dangers :** —
**Précautions :** Activer l'en-tête HSTS pour empêcher les navigateurs de tenter une connexion en HTTP simple.
**Équivalents :** HTTP/3 (QUIC)
**Voir aussi :** HTTP, TLS, CA, HSTS

## `DNS` — Domain Name System [Réseau/Web]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** RFC 1034/1035
**Contextes :** traduire des noms de domaine compréhensibles par les humains (ex: `google.com`) en adresses IP compréhensibles par les machines (ex: `142.250.180.206`)
**Rôle :** Annuaire distribué et hiérarchique mondial fondamental d'Internet.
**Syntaxe :** `dig +trace exemple.com`
**Cas réguliers :**
- `Enregistrement A / AAAA` — Associer un nom de domaine à une adresse IPv4 (A) ou IPv6 (AAAA)
- `Enregistrement CNAME` — Créer un alias pointeur d'un nom vers un autre nom
- `Enregistrement MX` — Indiquer les serveurs de messagerie responsables de recevoir les emails du domaine
**Origine :** Paul Mockapetris (1983 / IETF).
**Subtilités/confusions :**
- Les modifications de zones DNS prennent du temps à se propager sur la planète en fonction de la durée de vie du cache (**TTL**).
**Urgences/dangers :** ⚠️ Une mauvaise configuration du TTL avant une migration de serveur peut rendre votre service inaccessible pendant des heures.
**Précautions :** Réduire la valeur du TTL à 300 secondes quelques jours avant toute migration d'adresse IP.
**Équivalents :** DoH (DNS over HTTPS), DoT (DNS over TLS), mDNS
**Voir aussi :** dig, nslookup, resolvectl

## `URI` — Uniform Resource Identifier [Web]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** RFC 3986
**Contextes :** identifier de manière unique une ressource physique ou abstraite sur le Web (page HTML, document, image, point d'accès d'API)
**Rôle :** Chaîne de caractères standardisée définissant l'identifiant universel d'une ressource web, qui se décline en **URL** (localisation) et **URN** (nommage).
**Syntaxe :** `schéma://hôte:port/chemin?requête#fragment`
**Cas réguliers :**
- `URL (Uniform Resource Locator)` — URI qui indique à la fois l'identité et le moyen d'y accéder (ex: `https://site.com/doc.pdf`)
- `URN (Uniform Resource Name)` — URI qui identifie une ressource par son nom dans un espace donné sans indiquer où la trouver (ex: `urn:isbn:0451450523`)
**Origine :** Tim Berners-Lee, Roy Fielding, Larry Masinter / IETF (1994 / RFC 3986).
**Subtilités/confusions :**
- Toute URL est une URI, mais toute URI n'est pas forcément une URL !
**Urgences/dangers :** —
**Précautions :** Encoder les caractères spéciaux présents dans les paramètres d'URL (URL Encoding / Percent-encoding, ex: l'espace devient `%20` ou `+`).
**Équivalents :** URL, URN, IRI
**Voir aussi :** HTTP, REST, DOM

## `REST` — Representational State Transfer [Web]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** API RESTful
**Contextes :** concevoir des API web légères, découpées et scalables fondées sur les principes et méthodes natifs du protocole HTTP (GET, POST, PUT, DELETE)
**Rôle :** Style d'architecture logicielle défini par Roy Fielding pour les systèmes hypermédia distribués, reposant sur l'utilisation d'URIs pour les ressources et de verbes HTTP standards.
**Syntaxe :** `GET /api/v1/users/42`
**Cas réguliers :**
- `GET` — Récupérer une ressource sans effet de bord (méthode sûre et idempotente)
- `POST` — Créer une nouvelle ressource
- `PUT / PATCH` — Remplacer complètement (`PUT`) ou modifier partiellement (`PATCH`) une ressource
- `DELETE` — Supprimer une ressource
**Origine :** Roy Fielding (thèse de doctorat, 2000).
**Subtilités/confusions :**
- Une vraie API RESTful respecte la contrainte HATEOAS (intégration de liens hypermédias dans les réponses JSON).
**Urgences/dangers :** —
**Précautions :** Renvoyer les codes de statut HTTP appropriés (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Server Error`).
**Équivalents :** GraphQL, gRPC, SOAP
**Voir aussi :** HTTP, GraphQL, gRPC, JSON

## `SOAP` — Simple Object Access Protocol [Web]
**Niveau :** intermediaire | **Popularité :** 83 | **Aliases :** XML-WS
**Contextes :** échanger des données structurées et fortement typées entre applications d'entreprise historiques (banque, assurance, télécoms)
**Rôle :** Protocole d'échange de messages basé sur le format XML, caractérisé par un contrat d'interface formel strict défini par un fichier **WSDL**.
**Syntaxe :** Message XML enveloppé dans une balise `<soapenv:Envelope>`
**Cas réguliers :**
- `Enveloppe SOAP` — Structure obligatoire contenant un `<Header>` optionnel et un `<Body>` contenant l'appel de méthode
- `WSDL` — Web Services Description Language (fichier XML décrivant exactement les types et méthodes du service)
**Origine :** Dave Winer, Don Box / Microsoft (1998 / Standard W3C 2003).
**Subtilités/confusions :**
- SOAP est un **protocole** strict et verbeux, alors que REST est un **style d'architecture** souple.
**Urgences/dangers :** —
**Précautions :** Valider les schémas XML pour contrer les failles d'injection d'entités externes (XXE).
**Équivalents :** REST, gRPC, GraphQL
**Voir aussi :** REST, gRPC, XML

## `RPC` — Remote Procedure Call [Développement/Réseau]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** exécuter une fonction ou une procédure sur un serveur distant comme s'il s'agissait d'un appel de fonction local dans le code source
**Rôle :** Paradigme de communication réseau dans lequel un programme client invoque une sous-routine sur un autre espace d'adressage sans que le développeur n'ait à coder explicitement les détails réseau.
**Syntaxe :** `client.getUser({ id: 42 })`
**Cas réguliers :**
- `gRPC` — Implémentation moderne haute performance de Google basée sur Protobuf et HTTP/2
- `JSON-RPC / XML-RPC` — Formats RPC légers basés sur du texte JSON ou XML
**Origine :** Bruce Jay Nelson (Xerox PARC, 1981) / Sun RPC (1984).
**Subtilités/confusions :**
- Contrairement à REST (orienté ressources et verbes), le RPC est **orienté actions et fonctions** (`calculator.add(a, b)`).
**Urgences/dangers :** —
**Précautions :** Gérer explicitement les pannes réseau et timeouts car un appel distant peut échouer là où un appel local est garanti.
**Équivalents :** REST, GraphQL
**Voir aussi :** gRPC, REST, SOAP

## `WebSocket` — Communication bidirectionnelle temps réel [Web/Réseau]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** RFC 6455
**Contextes :** établir un canal de communication full-duplex temps réel et persistant entre le navigateur web et le serveur (tchat, jeux en ligne, dashboards financiers, notifications)
**Rôle :** Protocole réseau (RFC 6455) initié via une poignée de main HTTP (*Upgrade header*) puis maintenant un canal TCP persistant à très faible surcoût.
**Syntaxe :** Schéma d'URL : `ws://` ou `wss://` (sécurisé)
**Cas réguliers :**
- `wss://` — WebSocket sécurisé au-dessus de TLS (obligatoire en HTTPS)
- `Handshake HTTP` — Requête HTTP initiale avec en-tête `Upgrade: websocket` pour commuter vers le protocole WS
**Origine :** Ian Hickson / WHATWG & IETF (2011 / RFC 6455).
**Subtilités/confusions :**
- Diffère du simple polling ou des Server-Sent Events (SSE) car le serveur ET le client peuvent émettre des messages à tout moment de façon bidirectionnelle.
**Urgences/dangers :** —
**Précautions :** Configurer des mécanismes de maintien de connexion (*ping/pong heartbeats*) pour éviter la fermeture du socket par les Load Balancers.
**Équivalents :** SSE (Server-Sent Events), Long Polling, WebTransport
**Voir aussi :** HTTP, HTTPS, SSE, TLS

## `SSE` — Server-Sent Events [Web]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** EventSource API
**Contextes :** transmettre un flux continu de données ou de notifications du serveur vers le client en temps réel via une connexion HTTP standard (ex: fil d'actualité, streaming de réponses d'IA/LLM)
**Rôle :** Standard W3C et API navigateur (`EventSource`) permettant au serveur de pousser des données texte au format `text/event-stream` vers le client de manière unidirectionnelle.
**Syntaxe :** En-tête HTTP : `Content-Type: text/event-stream`
**Cas réguliers :**
- `EventSource API` — Instanciation en JavaScript : `const evtSource = new EventSource("/stream");`
- `Streaming LLM` — Format de référence utilisé par OpenAI et les APIs d'IA pour afficher la génération de mot par mot en temps réel
**Origine :** Ian Hickson / WHATWG (2004).
**Subtilités/confusions :**
- Diffère de WebSocket car SSE est **UNIDIRECTIONNEL** (du serveur vers le client uniquement) et tourne sur du pur HTTP standard (reconnexion automatique intégrée !).
**Urgences/dangers :** —
**Précautions :** Désactiver la mise en mémoire tampon des proxies/WAF (ex: en-tête `X-Accel-Buffering: no` sous Nginx) pour garantir la réception immédiate des événements.
**Équivalents :** WebSocket, Long Polling
**Voir aussi :** WebSocket, HTTP, REST

## `DOM` — Document Object Model [Web/Développement]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Arbre DOM
**Contextes :** manipuler la structure, le style et le contenu d'un document HTML ou XML via du code JavaScript dans le navigateur
**Rôle :** Interface de programmation orientée objet (API) représentée sous forme d'arbre hiérarchique de nœuds (`Element`, `Text`, `Comment`) générée par le moteur de rendu du navigateur.
**Syntaxe :** `document.querySelector(".bouton").addEventListener("click", ...)`
**Cas réguliers :**
- `Virtual DOM` — Représentation en mémoire du DOM réel utilisée par React/Vue pour calculer des diffs performants avant de mettre à jour le navigateur
- `Shadow DOM` — Encapsulation isolée de sous-arbres DOM utilisée par les Web Components pour éviter les fuites de styles CSS
**Origine :** W3C (DOM Level 1, 1998).
**Subtilités/confusions :**
- Les modifications directes et répétées du DOM réel déclenchent des étapes coûteuses de calcul de mise en page (*Reflow / Repaint*).
**Urgences/dangers :** —
**Précautions :** Passer par un Virtual DOM ou regrouper les modifications du DOM (*batching*) pour maintenir des performances fluides à 60 FPS.
**Équivalents :** Shadow DOM, Virtual DOM
**Voir aussi :** SPA, XSS, pup, JavaScript

## `SPA` — Single Page Application [Web/Développement]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Application Monopage
**Contextes :** créer des applications web fluides et réactives (React, Vue, Angular, Svelte) qui chargent une unique page HTML et mettent à jour le contenu dynamiquement via AJAX
**Rôle :** Architecture d'application web où le routage et le rendu des vues sont gérés côté client en JavaScript sans rechargement complet de la page par le serveur.
**Syntaxe :** (Architecture frontend : React Router, Vue Router)
**Cas réguliers :**
- `Client-Side Routing` — Interception des changements d'URL via l'API `history.pushState()` du navigateur
- `API-driven` — Récupération de données brutes JSON depuis des endpoints REST ou GraphQL
**Origine :** Stuart Morris (2002) / Popularisé par AngularJS (2010).
**Subtilités/confusions :**
- Les SPA pures ont historiquement des difficultés d'indexation pour le référencement naturel (SEO) car le serveur ne renvoie qu'une coquille HTML vide (`<div id="root"></div>`).
**Urgences/dangers :** —
**Précautions :** Utiliser du rendu côté serveur (**SSR**) ou de la génération statique (**SSG**) lorsque le SEO et le temps de premier affichage sont critiques.
**Équivalents :** MPA (Multi-Page Application), SSR, PWA
**Voir aussi :** SSR, SSG, DOM, REST

## `SSR` — Server-Side Rendering [Web/Développement]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Rendu Côté Serveur
**Contextes :** exécuter le code de composant (React, Vue, Svelte) sur le serveur Node.js à chaque requête pour générer du HTML complet prêt à l'affichage (SEO parfait et First Contentful Paint ultra-rapide)
**Rôle :** Technique de rendu web où le HTML final d'une page est généré à la volée sur le serveur avant d'être transmis au navigateur du client.
**Syntaxe :** (Frameworks SSR : Next.js, Nuxt.js, SvelteKit, Remix)
**Cas réguliers :**
- `Hydratation` — Étape où le JavaScript client « réhydrate » le HTML statique envoyé par le serveur pour réattacher les écouteurs d'événements interactifs
- `SEO Optimization` — Permet aux robots d'indexation (Googlebot) de lire directement le contenu textuel sans exécuter de JS
**Origine :** Architecture web d'origine (PHP/JSP) réinventée pour les frameworks JS modernes (Next.js 2016).
**Subtilités/confusions :**
- Exige un serveur Node.js en exécution continue (contrairement aux sites statiques hébergeables sur un simple bucket S3/Firebase Hosting).
**Urgences/dangers :** —
**Précautions :** Faire attention au surcoût de charge processeur du serveur Node.js lors de très forts pics de trafic.
**Équivalents :** SSG, ISR, SPA
**Voir aussi :** SPA, SSG, ISR, Next.js

## `SSG` — Static Site Generation [Web/Développement]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** Génération de Site Statique
**Contextes :** pré-compiler toutes les pages HTML d'un site web au moment du build (*build time*) pour offrir des performances maximales et une sécurité totale sans serveur applicatif
**Rôle :** Méthode de création de sites web où l'intégralité du HTML, CSS et JS est compilée une fois pour toutes lors du déploiement.
**Syntaxe :** (Générateurs SSG : Astro, Hugo, Gatsby, Jekyll, MkDocs)
**Cas réguliers :**
- `Build Time Rendering` — Génération de 1000 pages HTML à partir de fichiers Markdown ou d'un CMS Headless en une seule passe de compilation
- `Hébergement CDN` — Déploiement instantané des fichiers statiques sur Cloudflare Pages, Vercel ou Netlify
**Origine :** Tom Preston-Werner (Jekyll, 2008).
**Subtilités/confusions :**
- Idéal pour les blogs, documentations et sites vitrines où le contenu ne change pas à chaque seconde.
**Urgences/dangers :** —
**Précautions :** Si le site comporte des dizaines de milliers de pages, le temps de build peut devenir très long (solution : passer à l'ISR).
**Équivalents :** SSR, ISR, SPA
**Voir aussi :** SSR, ISR, SPA, mkdocs

## `ISR` — Incremental Static Regeneration [Web/Développement]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** Régénération Statique Incrémentale
**Contextes :** régénérer des pages statiques individuelles en arrière-plan au fur et à mesure des demandes utilisateurs sans avoir à re-compiler l'intégralité du site web
**Rôle :** Hybride révolutionnaire entre SSG et SSR inventé par Vercel (Next.js) qui permet de conserver les avantages du cache statique tout en rafraîchissant les pages périmées à la demande.
**Syntaxe :** `export const revalidate = 60;` (Next.js : réactiver la page toutes les 60s)
**Cas réguliers :**
- `Stale-While-Revalidate` — Le premier utilisateur reçoit la version en cache statique (instantanée) tandis que le serveur reconstruit la page en arrière-plan pour le visiteur suivant
- `On-demand Revalidation` — Invalider le cache d'une page spécifique via un Webhook dès qu'un contenu est modifié dans le CMS
**Origine :** Guillermo Rauch / Vercel (Next.js 9.5, 2020).
**Subtilités/confusions :**
- Permet de gérer des catalogues e-commerce de millions de produits avec des temps de réponse d'un site statique.
**Urgences/dangers :** —
**Précautions :** Configurer des Webhooks de ré-invalidation ciblés (*On-demand ISR*) pour éviter le gaspillage de générations inutiles.
**Équivalents :** SSG, SSR, Cache-Control
**Voir aussi :** SSR, SSG, SPA, Next.js

## `PWA` — Progressive Web App [Web/Mobile]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Application Web Progressive
**Contextes :** offrir une expérience proche d'une application mobile native (installation sur l'écran d'accueil, fonctionnement hors-ligne, notifications push) à partir d'un simple site web
**Rôle :** Ensemble de technologies web (Service Workers, Web App Manifest, HTTPS) permettant à un site web de s'installer et de fonctionner de façon autonome sur mobile et desktop.
**Syntaxe :** `manifest.json` + enregistrement de `service-worker.js`
**Cas réguliers :**
- `Service Worker` — Script d'arrière-plan interceptant les requêtes réseau pour offrir un mode hors-ligne via un cache agressif
- `Web App Manifest` — Fichier JSON décrivant les icônes, la couleur de thème et le mode d'affichage (`display: standalone`)
**Origine :** Alex Russell et Frances Berriman (Google, 2015).
**Subtilités/confusions :**
- Ne nécessite pas de passer par les magasins d'applications (App Store / Play Store) pour être installée par l'utilisateur.
**Urgences/dangers :** —
**Précautions :** Gérer prudemment la stratégie de mise à jour du cache des Service Workers pour éviter que les utilisateurs ne restent bloqués sur une ancienne version de l'application.
**Équivalents :** Application native (Swift/Kotlin), Flutter, React Native
**Voir aussi :** SPA, HTTPS, DOM

## `SEO` — Search Engine Optimization [Web/Marketing]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Référencement Naturel
**Contextes :** optimiser la structure technique, la vitesse et le contenu d'un site web pour maximiser son positionnement dans les moteurs de recherche (Google, Bing)
**Rôle :** Ensemble de techniques visant à améliorer la visibilité et le classement d'un site web dans les résultats de recherche non payants (organiques).
**Syntaxe :** (Pratiques web : en-têtes HTML `<title>`, `<meta>`, données structurées JSON-LD, sitemap.xml)
**Cas réguliers :**
- `Technical SEO` — Optimisation de la vitesse de chargement (Core Web Vitals), du rendu HTML (SSR/SSG) et de la structure du sitemap
- `On-Page SEO` — Balisage sémantique (`<h1>`, `<h2>`), attributs `alt` sur les images et qualité rédactionnelle
**Origine :** Danny Sullivan / débuts du web (1997).
**Subtilités/confusions :**
- Se distingue du **SEA** (Search Engine Advertising / publicité payante Google Ads).
**Urgences/dangers :** —
**Précautions :** Éviter les techniques de balisage trompeuses (*Black Hat SEO*) sous peine de pénalités et d'éviction manuelle par Google.
**Équivalents :** SEA, SEM, SMO
**Voir aussi :** SSR, SSG, JSON-LD, HTML

## `A11Y` — Accessibility (Accessibilité Numérique) [Web/UI]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** a11y (11 lettres entre A et Y)
**Contextes :** concevoir des sites web et applications utilisables par tous, y compris les personnes en situation de handicap (déficients visuels, moteurs, auditifs)
**Rôle :** Ensemble de normes (WCAG / RGAA) et de règles de conception garantissant que les contenus numériques sont perceptibles, utilisables et compréhensibles par tous.
**Syntaxe :** Attributs ARIA : `<button aria-label="Fermer le menu">X</button>`
**Cas réguliers :**
- `WCAG 2.1` — Web Content Accessibility Guidelines (niveaux de conformité A, AA, AAA)
- `ARIA (Accessible Rich Internet Applications)` — Attributs HTML (`aria-expanded`, `role="dialog"`) aidant les lecteurs d'écran à interpréter les composants complexes
**Origine :** W3C Web Accessibility Initiative (WAI, 1997).
**Subtilités/confusions :**
- L'accessibilité bénéficie à tous (ex: contraste de couleurs élevé sur écran en plein soleil, navigation au clavier).
**Urgences/dangers :** —
**Précautions :** Utiliser des éléments HTML sémantiques natifs (`<button>`, `<nav>`, `<article>`) avant d'ajouter des attributs ARIA personnalisés.
**Équivalents :** RGAA, Section 508
**Voir aussi :** HTML, DOM, UI, UX

## `I18N` — Internationalization [Web/Développement]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** i18n (18 lettres entre I et N)
**Contextes :** concevoir une application logicielle pour qu'elle puisse s'adapter à plusieurs langues, cultures et formats régionaux sans refonte du code source
**Rôle :** Processus de conception d'une application isolant les textes, formats de dates, monnaies et nombres dans des fichiers de ressources localisables.
**Syntaxe :** `t("welcome.message", { name: "Adolphe" })` (ex: avec i18next, react-intl)
**Cas réguliers :**
- `Fichiers de traduction` — Dictionnaires JSON, gettext `.po`/`.mo` ou XLIFF par langue (`fr.json`, `en.json`)
- `Formatage régional` — API JavaScript internationale `Intl.DateTimeFormat` et `Intl.NumberFormat`
**Origine :** DEC (Digital Equipment Corporation, 1970s).
**Subtilités/confusions :**
- **I18N** (Internationalisation) est la **conception technique** permettant la prise en charge de plusieurs langues ; **L10N** (Localisation) est l'**adaptation effective** (traduction) pour une région précise.
**Urgences/dangers :** —
**Précautions :** Ne jamais concaténer des phrases en dur dans le code car l'ordre des mots varie selon la grammaire de chaque langue.
**Équivalents :** L10N, gettext
**Voir aussi :** L10N, JSON, gettext

## `L10N` — Localization [Web/Développement]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** l10n (10 lettres entre L et N)
**Contextes :** adapter les contenus, images, devises, formats de date et règles juridiques d'une application pour un marché ou un pays spécifique (ex: `fr_FR` vs `fr_CA`)
**Rôle :** Processus d'adaptation effective (traduction et contextualisation culturelle) d'un produit logiciel internationalisé pour une région cible.
**Syntaxe :** Code de locale : `fr-FR`, `en-US`, `ja-JP`
**Cas réguliers :**
- `Adaptation culturelle` — Gestion des sens de lecture de droite à gauche (RTL : arabe, hébreu), devises localisées, unités de mesure
- `Locale Identifier` — Combinaison code langue ISO 639-1 + code pays ISO 3166-1
**Origine :** DEC / Industrie logicielle.
**Subtilités/confusions :**
- La localisation implique souvent des adaptations graphiques (ex: prévoir de la place pour l'allemand dont les mots sont 30% plus longs qu'en anglais).
**Urgences/dangers :** —
**Précautions :** Utiliser des attributs `dir="rtl"` sur les éléments HTML parents pour gérer automatiquement les mises en page inversées.
**Équivalents :** I18N, Translation
**Voir aussi :** I18N, HTML, CSS

## `UI` — User Interface [UI/UX]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Interface Utilisateur
**Contextes :** concevoir les éléments visuels et interactifs d'un logiciel, d'un site web ou d'une application mobile (boutons, typographie, couleurs, modales)
**Rôle :** Point d'interaction graphique et visuel entre l'être humain et la machine.
**Syntaxe :** (Design visuel : Figma, CSS, Design Systems, composants UI)
**Cas réguliers :**
- `Design System` — Ensemble de règles, de composants UI réutilisables (Boutons, Inputs, Cards) et de jetons de style (*Design Tokens*)
- `GUI (Graphical User Interface)` — Interface graphique par opposition à la CLI (ligne de commande)
**Origine :** Xerox PARC (1970s) / Apple Macintosh (1984).
**Subtilités/confusions :**
- L'**UI** concerne le **visuel** et l'esthétique ; l'**UX** concerne l'**expérience globale** et la facilité d'utilisation.
**Urgences/dangers :** —
**Précautions :** Respecter une hiérarchie visuelle claire et des contrastes suffisants pour maintenir une bonne accessibilité (A11Y).
**Équivalents :** GUI, Frontend
**Voir aussi :** UX, A11Y, CSS, HTML

## `UX` — User Experience [UI/UX]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Expérience Utilisateur
**Contextes :** étudier, concevoir et optimiser le ressenti global, l'ergonomie et la facilité avec laquelle un utilisateur accomplit son objectif dans une application
**Rôle :** Discipline centrée sur l'utilisateur mesurant l'efficacité, l'intuitivité, l'accessibilité et la satisfaction ressentie lors de l'utilisation d'un produit.
**Syntaxe :** (Méthodologie : Recherche utilisateur, Wireframes, Tests utilisateurs, Parcours client)
**Cas réguliers :**
- `User Journey` — Cartographie du parcours de l'utilisateur étape par étape pour accomplir une action
- `Usability Testing` — Observation d'utilisateurs réels confrontés au prototype de l'application pour identifier les points de friction
**Origine :** Don Norman (Apple, 1993).
**Subtilités/confusions :**
- Une belle UI (superbes couleurs et animations) avec une mauvaise UX (navigation confuse et 15 clics pour payer) donne un produit raté.
**Urgences/dangers :** —
**Précautions :** Valider les hypothèses d'ergonomie auprès d'utilisateurs réels plutôt que de se fier uniquement aux impressions de l'équipe de dev.
**Équivalents :** Ergonomie, Usabilité
**Voir aussi :** UI, A11Y, SPA

## `CSS` — Cascading Style Sheets [Web]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** Feuilles de Style en Cascade
**Contextes :** décrire la présentation visuelle, la mise en page, les couleurs, les polices et les animations des documents HTML
**Rôle :** Langage de style informatique standardisé par le W3C permettant de séparer le contenu (HTML) de sa mise en forme visuelle.
**Syntaxe :** `sélecteur { propriété: valeur; }`
**Cas réguliers :**
- `Flexbox / Grid` — Moteurs de mise en page modernes 1D et 2D
- `Media Queries` — Adaptabilité aux différentes tailles d'écrans (*Responsive Web Design*)
- `CSS Variables (Custom Properties)` — Variables de style dynamique (`var(--primary-color)`)
**Origine :** Håkon Wium Lie / W3C (1996).
**Subtilités/confusions :**
- Le terme « en cascade » signifie que les règles de style s'appliquent avec un ordre de priorité défini par la spécificité des sélecteurs.
**Urgences/dangers :** —
**Précautions :** Privilégier des méthodologies d'organisation CSS (BEM, Tailwind CSS, CSS Modules) pour éviter la surcharge de règles globales incohérentes.
**Équivalents :** Sass/SCSS, Less, Tailwind CSS
**Voir aussi :** HTML, DOM, UI

## `HTML` — HyperText Markup Language [Web]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** HTML5
**Contextes :** structurer le contenu fondamental des pages web (titres, paragraphes, liens, formulaires, images, vidéos)
**Rôle :** Langage de balisage universel du World Wide Web qui décrit la structure sémantique d'un document interprété par les navigateurs.
**Syntaxe :** `<balise attribut="valeur">Contenu</balise>`
**Cas réguliers :**
- `HTML5` — Norme actuelle (2014) introduisant les balises sémantiques (`<header>`, `<nav>`, `<main>`, `<article>`, `<video>`, `<canvas>`)
- `Balisage Sémantique` — Utiliser la bonne balise pour le bon usage (ex: `<button>` pour une action, `<a>` pour une navigation)
**Origine :** Tim Berners-Lee (CERN, 1991 / W3C & WHATWG).
**Subtilités/confusions :**
- HTML n'est pas un langage de programmation : c'est un langage de balisage et de structuration de données.
**Urgences/dangers :** —
**Précautions :** Toujours valider la syntaxe de vos documents avec le W3C Validator et garantir un balisage sémantique propre pour l'A11Y et le SEO.
**Équivalents :** XHTML (obsolète), XML
**Voir aussi :** DOM, CSS, SEO, A11Y

## `SVG` — Scalable Vector Graphics [Web/Multimédia]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Graphiques Vectoriels Scalables
**Contextes :** afficher des icônes, logos, illustrations et graphiques interactifs qui restent parfaitement nettes quelle que soit la résolution d'écran (Retina, 4K)
**Rôle :** Format d'image vectorielle basé sur le langage XML, manipulable directement dans le DOM avec CSS et JavaScript.
**Syntaxe :** `<svg width="100" height="100"><circle cx="50" cy="50" r="40" fill="red" /></svg>`
**Cas réguliers :**
- `Vectoriel` — Défini par des équations géométriques (lignes, courbes de Bézier) plutôt que par une grille de pixels (contrairement à PNG/JPEG)
- `Stylisable` — Peut être animé et coloré dynamiquement via du CSS (`fill: blue;`)
**Origine :** W3C (1999).
**Subtilités/confusions :**
- Étant un fichier XML texte, un fichier SVG peut être inspecté et nettoyé pour réduire sa taille (outil `svgo`).
**Urgences/dangers :** ⚠️ Un fichier SVG téléchargé depuis une source non fiable peut contenir des balises `<script>` exécutables (risque XSS).
**Précautions :** Nettoyer les SVG issus d'utilisateurs externes avec un assainisseur (*DOMPurify*) avant de les afficher.
**Équivalents :** Canvas, WebGL, PNG (matriciel)
**Voir aussi :** Canvas, HTML, CSS, XSS

## `Canvas` — API de rendu 2D en grille de pixels HTML5 [Web/Multimédia]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** HTML5 Canvas
**Contextes :** dessiner des graphiques dynamiques, des jeux vidéo 2D, des éditeurs d'images ou des visualisations de données complexes en temps réel dans le navigateur
**Rôle :** Balise HTML (`<canvas>`) et API JavaScript de dessin bitmap procédural permettant de manipuler directement une grille de pixels à haute vitesse.
**Syntaxe :** `const ctx = canvas.getContext("2d"); ctx.fillRect(10, 10, 50, 50);`
**Cas réguliers :**
- `2D Context` — Moteur de dessin vectoriel et bitmap 2D (lignes, formes, images, texte)
- `Animation Loop` — Boucle de rendu cadencée à 60 FPS via `requestAnimationFrame()`
**Origine :** Apple (pour Safari Dashboard, 2004) / Standardisé dans HTML5 par le W3C.
**Subtilités/confusions :**
- Les éléments dessinés dans un Canvas ne sont **PAS des nœuds du DOM** : il n'y a pas de sous-éléments visibles dans l'inspecteur HTML et l'accessibilité doit être gérée manuellement.
**Urgences/dangers :** —
**Précautions :** Libérer les ressources et éviter les allocations d'objets inutiles dans la boucle `requestAnimationFrame` pour éviter les ralentissements du Garbage Collector.
**Équivalents :** SVG, WebGL
**Voir aussi :** WebGL, SVG, HTML, JavaScript

## `WebGL` — Web Graphics Library [Web/Multimédia]
**Niveau :** avance | **Popularité :** 93 | **Aliases :** WebGL 2.0
**Contextes :** afficher des scènes 3D interactives complexes, des simulateurs, des jeux vidéo 3D et des expériences immersives directement dans le navigateur sans plugin
**Rôle :** API JavaScript basée sur OpenGL ES permettant de rendre des graphiques 2D et 3D matériels accélérés par le GPU dans une balise `<canvas>`.
**Syntaxe :** `const gl = canvas.getContext("webgl2");`
**Cas réguliers :**
- `Three.js / Babylon.js` — Bibliothèques JavaScript de haut niveau masquant la complexité bas niveau des shaders WebGL
- `Shaders GLSL` — Petits programmes d'ombrage exécutés directement sur le processeur graphique (Vertex Shader & Fragment Shader)
**Origine :** Vladimir Vukićević / Khronos Group (2011).
**Subtilités/confusions :**
- WebGL 1.0 est basé sur OpenGL ES 2.0 ; WebGL 2.0 est basé sur OpenGL ES 3.0.
**Urgences/dangers :** —
**Précautions :** Utiliser une bibliothèque de haut niveau comme Three.js sauf besoin spécifique d'écrire des shaders de rendu custom.
**Équivalents :** WebGPU, Canvas 2D, OpenGL
**Voir aussi :** WebGPU, Canvas, Three.js (si présent)

## `WebGPU` — API graphique et de calcul GPU moderne [Web/Multimédia]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** exécuter du rendu 3D haute performance et des calculs parallèles (Machine Learning / IA locale, simulations physiques) sur GPU dans le navigateur
**Rôle :** API web de nouvelle génération succédant à WebGL, offrant un accès à faible surcoût aux fonctionnalités modernes des cartes graphiques (Direct3D 12, Vulkan, Metal).
**Syntaxe :** `const adapter = await navigator.gpu.requestAdapter();`
**Cas réguliers :**
- `Compute Shaders` — Exécution de calculs scientifiques ou de réseaux de neurones (ex: modèles LLM dans le navigateur via WebLLM/Transformers.js)
- `WGSL` — WebGPU Shading Language (langage d'ombrage standard de WebGPU)
**Origine :** W3C GPU for the Web Community Group (Apple, Google, Mozilla, Microsoft, 2023).
**Subtilités/confusions :**
- Offre des performances 3 à 10 fois supérieures à WebGL grâce à un surcoût CPU drastiquement réduit et un support natif des Compute Shaders.
**Urgences/dangers :** —
**Précautions :** Prévoir un repli vers WebGL 2 pour les anciens navigateurs ou systèmes ne supportant pas encore WebGPU.
**Équivalents :** WebGL, Vulkan, Metal, Direct3D 12
**Voir aussi :** WebGL, WASM, Canvas

## `WASM` — WebAssembly [Web/Développement]
**Niveau :** avance | **Popularité :** 95 | **Aliases :** WebAssembly
**Contextes :** exécuter du code compilé à haute performance (C, C++, Rust, Go, Zig) dans le navigateur web à une vitesse quasi-native
**Rôle :** Format d'instructions binaire portable et bac à sable de sécurité conçu pour être exécuté à grande vitesse aux côtés de JavaScript dans les moteurs web.
**Syntaxe :** `WebAssembly.instantiateStreaming(fetch("module.wasm"))`
**Cas réguliers :**
- `Compilations lourdes` — Portages web d'outils complexes (Photoshop web, AutoCAD, moteurs de jeux Unity/Unreal Engine, SQLite, FFmpeg)
- `Rust + WASM` — Écriture de modules de calcul intensif en Rust intégrés dans des applications web via `wasm-pack`
**Origine :** Alon Zakai / W3C Community Group (Google, Mozilla, Apple, Microsoft, 2017).
**Subtilités/confusions :**
- WASM ne remplace pas JavaScript : il collabore avec lui en prenant en charge les tâches de calcul intensif.
**Urgences/dangers :** —
**Précautions :** Utiliser `wasm-bindgen` en Rust ou Emscripten en C++ pour gérer automatiquement les conversions de types entre JS et WASM.
**Équivalents :** ASM.js (obsolète)
**Voir aussi :** rustc, clang, WebGPU, JavaScript

## `JSON` — JavaScript Object Notation [Data/Web]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** RFC 8259
**Contextes :** échanger des données structurées entre serveurs et clients (APIs REST, fichiers de configuration, bases de données NoSQL)
**Rôle :** Format de d'échange de données textuel léger, facile à lire pour les humains et à analyser pour les machines, basé sur une sous-partie de la syntaxe JavaScript.
**Syntaxe :** `{"cle": "valeur", "nombre": 42, "tableau": [1, 2, 3]}`
**Cas réguliers :**
- `JSON.parse()` — Convertir une chaîne JSON en objet JavaScript
- `JSON.stringify()` — Sérialiser un objet JavaScript en chaîne JSON
**Origine :** Douglas Crockford (2001 / RFC 8259).
**Subtilités/confusions :**
- La norme JSON stricte impose d'entourer le nom de toutes les clés par des guillemets doubles `" "` et interdit les virgules traînantes (*trailing commas*).
**Urgences/dangers :** —
**Précautions :** Ne jamais utiliser `eval()` pour parser une chaîne JSON (utiliser exclusivement `JSON.parse()`).
**Équivalents :** YAML, XML, TOML, MessagePack
**Voir aussi :** jq, yq, REST, JWT

## `JSON-LD` — JSON for Linking Data [Web/SEO]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** Données Structurées Schema.org
**Contextes :** enrichir les pages web avec des métadonnées structurées lues par Google pour générer des résultats enrichis (*Rich Snippets*) dans le moteur de recherche
**Rôle :** Standard W3C permettant d'encoder des données liées (Linked Data) en utilisant le format JSON standard via le contexte `@context: "https://schema.org"`.
**Syntaxe :** `<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Product", "name": "..."}</script>`
**Cas réguliers :**
- `Schema.org Product / Article` — Déclarer un produit avec son prix, sa disponibilité et ses avis pour l'affichage dans Google Shopping
- `Schema.org FAQPage` — Déclarer une foire aux questions directement compréhensible par les moteurs de recherche
**Origine :** Manu Sporny / W3C JSON-LD Working Group (2014).
**Subtilités/confusions :**
- Format officiellement recommandé par Google par rapport aux anciens formats de microdonnées (Microdata ou Microformats).
**Urgences/dangers :** —
**Précautions :** Valider vos blocs JSON-LD avec l'outil officiel *Google Rich Results Test*.
**Équivalents :** Microdata, RDFa
**Voir aussi :** SEO, JSON, HTML

## `MP4` — Conteneur multimédia standard MPEG-4 [Multimédia]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** MPEG-4 Part 14
**Contextes :** stocker et diffuser de la vidéo et de l'audio haute définition sur le Web, les smartphones, les téléviseurs et les plateformes de streaming
**Rôle :** Format de conteneur numérique standardisé (ISO/IEC 14496-14) encapsulant des flux vidéo (H.264, H.265, AV1) et audio (AAC, MP3) ainsi que des sous-titres et métadonnées.
**Syntaxe :** `ffmpeg -i entree.avi -c:v libx264 -c:a aaa sortie.mp4`
**Cas réguliers :**
- `Fast Start (moov atom)` — Déplacement de l'en-tête de métadonnées au début du fichier pour permettre la lecture en streaming vidéo avant téléchargement complet
- `Encapsulation H.264 + AAC` — Combinaison vidéo/audio universelle lisible sur 100% des navigateurs et équipements du marché
**Origine :** ISO/IEC Moving Picture Experts Group (MPEG, 2001).
**Subtilités/confusions :**
- MP4 est un **conteneur** (la boîte) et non un codec (la méthode de compression de l'image) : deux fichiers `.mp4` peuvent utiliser des codecs vidéo très différents.
**Urgences/dangers :** —
**Précautions :** Toujours passer l'option `-movflags +faststart` dans FFmpeg lors de l'encodage de fichiers MP4 destinés au web.
**Équivalents :** MKV, WebM, MOV
**Voir aussi :** H264, AAC, WEBM, ffmpeg

## `MKV` — Conteneur multimédia ouvert Matroska [Multimédia]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Matroska
**Contextes :** stocker des films et vidéos haute fidélité contenant plusieurs pistes audio multi-langues, des sous-titres multiples (SRT, ASS) et des chapitres
**Rôle :** Format de conteneur multimédia ouvert et libre de droits capable de contenir un nombre illimité de pistes vidéo, audio, d'images ou de sous-titres au sein d'un fichier unique.
**Syntaxe :** `mkvmerge -o film.mkv video.mp4 audio_fr.aac sous_titres.ass`
**Cas réguliers :**
- `MKVToolNix` — Suite d'outils graphique et CLI de référence pour démuxer et ré-encapsuler des fichiers Matroska sans ré-encodage
- `Format d'archivage` — Format privilégié pour la sauvegarde de vidéos physiques (Blu-Ray/DVD) sans perte de pistes
**Origine :** Steve Lhomme et l'équipe Matroska (2002 / inspiré du format MCF).
**Subtilités/confusions :**
- Contrairement au MP4, le format MKV n'est pas toujours pris en charge nativement par le lecteur HTML5 des navigateurs web sans conversion.
**Urgences/dangers :** —
**Précautions :** Ré-encapsuler un MKV en MP4 sans ré-encoder la vidéo grâce à `ffmpeg -i file.mkv -c copy file.mp4`.
**Équivalents :** MP4, WebM, AVI
**Voir aussi :** MP4, WEBM, ffmpeg

## `WEBM` — Conteneur multimédia web ouvert [Multimédia/Web]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** WebM Project
**Contextes :** intégrer des vidéos légères et libres de droits directement dans des balises HTML5 `<video>` sans payer de redevances de brevets
**Rôle :** Format de conteneur vidéo ouvert conçu spécifiquement pour le Web par Google, basé sur une version simplifiée de Matroska (MKV) et utilisant les codecs libres VP8/VP9/AV1 et Vorbis/Opus.
**Syntaxe :** `<video src="video.webm" controls></video>`
**Cas réguliers :**
- `VP9 / Opus` — Combinaison codec vidéo VP9 et audio Opus offrant une excellente compression visuelle à faible débit
- `Transparence Vidéo` — Support du canal alpha (transparence) dans la vidéo web (idéal pour les animations web)
**Origine :** Google / On2 Technologies (2010).
**Subtilités/confusions :**
- Entièrement libre et gratuit, sans aucuns frais de licence ou de brevet applicables aux développeurs ou diffuseurs.
**Urgences/dangers :** —
**Précautions :** Fournir à la fois un fichier `.webm` (VP9) et un fichier `.mp4` (H.264) dans la balise `<video>` pour une compatibilité navigateur absolue.
**Équivalents :** MP4, MKV
**Voir aussi :** AV1, MP4, HTML, ffmpeg

## `H.264` — Codec vidéo AVC (Advanced Video Coding) [Multimédia]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** H264, MPEG-4 AVC
**Contextes :** compresser des vidéos pour la télévision, le streaming (YouTube, Twitch, Netflix) et les visioconférences avec une compatibilité matérielle absolue
**Rôle :** Standard de compression vidéo (codec) le plus largement déployé au monde, offrant un excellent compromis entre qualité d'image, taux de compression et décodeur matériel GPU.
**Syntaxe :** `ffmpeg -i entree.mov -c:v libx264 -crf 23 sortie.mp4`
**Cas réguliers :**
- `CRF (Constant Rate Factor)` — Contrôle de qualité visuelle sous FFmpeg (valeur recommandée entre 18 et 28)
- `Décodage matériel GPU` — Pris en charge par 99.9% des cartes graphiques, téléphones et télévisions du marché
**Origine :** ITU-T VCEG & ISO/IEC MPEG (2003 / H.264 / MPEG-4 AVC).
**Subtilités/confusions :**
- H.264 est soumis à des brevets gérés par le consortium MPEG LA (bien que le décodeur soit universel et gratuit pour l'utilisateur final).
**Urgences/dangers :** —
**Précautions :** Utiliser le profil `high` et le niveau `4.1` pour un encodage 1080p universel.
**Équivalents :** H.265 (HEVC), VP9, AV1
**Voir aussi :** H265, AV1, MP4, ffmpeg

## `H.265` — Codec vidéo HEVC (High Efficiency Video Coding) [Multimédia]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** H265, HEVC
**Contextes :** diffuser de la vidéo 4K UHD et 8K avec technologie HDR (High Dynamic Range) en réduisant la taille du fichier de 50% par rapport à H.264
**Rôle :** Successeur du codec H.264 offrant une efficacité de compression de données vidéo doublée à qualité visuelle équivalente.
**Syntaxe :** `ffmpeg -i entree.mov -c:v libx265 -crf 28 sortie.mp4`
**Cas réguliers :**
- `Vidéo 4K / HDR10` — Codec standard pour les flux vidéo 4K sur les téléviseurs connectés et iPhone
- `Gain de bande passante` — Permet de streamer de la vidéo HD sur des connexions mobiles limitées
**Origine :** ITU-T VCEG & ISO/IEC MPEG (2013 / H.265 / HEVC).
**Subtilités/confusions :**
- La complexité des licences et brevets de H.265 a freiné son adoption sur le web par rapport à H.264 et au codec ouvert AV1.
**Urgences/dangers :** —
**Précautions :** Vérifier que les navigateurs cibles prennent en charge le décodage matériel HEVC avant de l'imposer en web.
**Équivalents :** AV1, VP9, H.264
**Voir aussi :** H264, AV1, MP4, ffmpeg

## `AV1` — Codec vidéo open source de nouvelle génération [Multimédia/Web]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** AOMedia Video 1
**Contextes :** compresser de la vidéo ultra haute définition (4K/8K) avec une efficacité 30% supérieure à H.265/VP9 sans aucune redevance de brevet
**Rôle :** Codec vidéo ouvert et libre de droits développé par l'Alliance for Open Media (Google, Mozilla, Amazon, Netflix, Apple, Microsoft, NVIDIA).
**Syntaxe :** `ffmpeg -i entree.mp4 -c:v libsvtav1 -crf 30 sortie.mp4`
**Cas réguliers :**
- `SVT-AV1` — Encodeur AV1 open source développé par Intel et la communauté, offrant une vitesse d'encodage praticable en production
- `Adoption Web` — Déployé massivement sur YouTube et Netflix pour réduire les coûts de bande passante mondiale
**Origine :** Alliance for Open Media (AOMedia, 2018).
**Subtilités/confusions :**
- L'encodage logiciel de l'AV1 a longtemps été très lent, mais l'arrivée d'encodeurs matériels sur les GPU récents (RTX 4000, RX 7000, Apple M3) généralise son usage.
**Urgences/dangers :** —
**Précautions :** Utiliser l'encodeur `libsvtav1` avec FFmpeg pour des temps d'encodage optimisés.
**Équivalents :** H.265, VP9, H.264
**Voir aussi :** H264, H265, WEBM, ffmpeg

## `AAC` — Advanced Audio Coding [Multimédia]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** M4A, AAC-LC
**Contextes :** compresser des flux audio numériques de haute qualité pour la musique, le streaming (Apple Music, YouTube) et les fichiers MP4
**Rôle :** Standard de compression audio avec perte (*lossy*) conçu pour succéder au format MP3 en offrant une meilleure qualité sonore à des débits binaire inférieurs.
**Syntaxe :** `ffmpeg -i entree.wav -c:a aac -b:a 192k sortie.m4a`
**Cas réguliers :**
- `AAC-LC (Low Complexity)` — Variante la plus compatible, standard de fait pour la piste audio des fichiers MP4
- `Débit 128 kbps` — Offre une qualité audio imperceptiblement proche du CD audio d'origine
**Origine :** AT&T, Dolby, Sony, Fraunhofer IIS (1997 / MPEG-2 & MPEG-4).
**Subtilités/confusions :**
- Les fichiers ne contenant que de l'audio AAC portent généralement l'extension `.m4a` ou `.aac`.
**Urgences/dangers :** —
**Précautions :** Privilégier un débit d'au moins 128 kbps pour de la musique et 96 kbps pour de la voix.
**Équivalents :** MP3, Opus, FLAC
**Voir aussi :** MP3, FLAC, MP4, ffmpeg

## `FLAC` — Free Lossless Audio Codec [Multimédia]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** archiver et écouter de la musique en qualité studio intégrale sans aucune perte de données sonores
**Rôle :** Format d'encodage et codec audio sans perte (*lossless*) open source et libre de droits qui réduit la taille des fichiers audio de 50% à 60% sans altérer le moindre bit du signal.
**Syntaxe :** `flac chanson.wav -o chanson.flac`
**Cas réguliers :**
- `Archivage CD / Master` — Format de référence des audiophiles et des archivistes de musique (qualité 16/24 bits, 44.1 à 192 kHz)
- `Balises Metadata (Vorbis Comment)` — Intégration complète des pochettes d'albums et des métadonnées (titre, artiste, album)
**Origine :** Josh Coalson / Xiph.Org Foundation (2001).
**Subtilités/confusions :**
- Contrairement au MP3 ou AAC qui coupent des fréquences inaudibles, décompresser un fichier FLAC recrée **à l'octet près** le fichier WAV original.
**Urgences/dangers :** —
**Précautions :** Pris en charge nativement par tous les navigateurs web modernes et systèmes d'exploitation mobile/desktop.
**Équivalents :** ALAC (Apple Lossless), WAV, AIFF
**Voir aussi :** AAC, MP3, ffmpeg

## `MP3` — MPEG-1/2 Audio Layer III [Multimédia]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** MPEG-3 (erreur courante)
**Contextes :** écouter des fichiers audio légers sur n'importe quel équipement électronique ou autoradio ancien
**Rôle :** Format de compression audio historique à perte (*lossy*) ayant révolutionné la distribution de musique numérique sur Internet dans les années 1990.
**Syntaxe :** `ffmpeg -i entree.wav -c:a libmp3lame -b:a 320k sortie.mp3`
**Cas réguliers :**
- `320 kbps (CBR)` — Qualité maximale du format MP3
- `VBR (Variable Bitrate)` — Encodage à débit variable (ex: preset `V0`) adaptant la compression selon la complexité du passage musical
**Origine :** Karlheinz Brandenburg / Institut Fraunhofer IIS (1993).
**Subtilités/confusions :**
- Tous les brevets protégeant le format MP3 ont expiré en 2017 : le format est désormais entièrement tombé dans le domaine public.
**Urgences/dangers :** —
**Précautions :** Pour les nouveaux projets web, préférer AAC ou Opus qui offrent un meilleur son à débit égal.
**Équivalents :** AAC, Opus, Ogg Vorbis
**Voir aussi :** AAC, FLAC, ffmpeg

## `HLS` — HTTP Live Streaming [Multimédia/Web]
**Niveau :** intermediaire | **Popularité :** 96 | **Aliases :** Apple HLS, RFC 8216
**Contextes :** diffuser des flux vidéo en direct (Live) ou à la demande (VOD) vers des millions de spectateurs en s'adaptant dynamiquement à leur débit Internet (Adaptive Bitrate)
**Rôle :** Protocole de streaming adaptatif basé sur HTTP développé par Apple qui découpe les flux vidéo en petits segments (.ts ou .m4s) décrits par un fichier de playlist (`.m3u8`).
**Syntaxe :** `ffmpeg -i camera.mov -c:v h264 -hls_time 6 -hls_playlist_type vod stream.m3u8`
**Cas réguliers :**
- `Fichier Index .m3u8` — Fichier texte de playlist listant les segments vidéo disponibles et les différentes résolutions (1080p, 720p, 480p)
- `Adaptive Bitrate (ABR)` — Le lecteur vidéo bascule automatiquement de résolution en fonction des fluctuations de bande passante du client
**Origine :** Roger Pantos / Apple (2009 / RFC 8216).
**Subtilités/confusions :**
- Le protocole HLS s'appuie sur de simples serveurs HTTP et CDN standards, ce qui le rend infiniment plus scalable que les anciens serveurs de streaming dédiés (RTMP).
**Urgences/dangers :** —
**Précautions :** Utiliser la bibliothèque `hls.js` pour lire les flux HLS sur les navigateurs autres que Safari.
**Équivalents :** DASH (MPEG-DASH), Smooth Streaming
**Voir aussi :** DASH, RTMP, H264, ffmpeg

## `DASH` — Dynamic Adaptive Streaming over HTTP [Multimédia/Web]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** MPEG-DASH, ISO/IEC 23009-1
**Contextes :** diffuser des flux vidéo de haute qualité en streaming adaptatif agnostique des codecs (utilisé par YouTube et Netflix)
**Rôle :** Standard international de streaming vidéo adaptatif sur HTTP défini par le consortium MPEG, structuré autour d'un fichier manifeste XML (`.mpd`).
**Syntaxe :** `ffmpeg -i source.mov -c:v h264 -use_timeline 1 -use_template 1 -f dash manifest.mpd`
**Cas réguliers :**
- `Manifeste MPD (Media Presentation Description)` — Fichier XML répertoriant les représentations vidéo, audio et sous-titres
- `Indépendance du codec` — Supporte nativement H.264, H.265, VP9, AV1, AAC, Opus
**Origine :** Consortium ISO/IEC MPEG (2012).
**Subtilités/confusions :**
- Contrairement à HLS (promu par Apple), MPEG-DASH est un standard ouvert non propriétaire géré par l'ISO.
**Urgences/dangers :** —
**Précautions :** Intégrer le lecteur open source `dash.js` ou `shaka-player` (Google) dans vos projets web.
**Équivalents :** HLS, Smooth Streaming
**Voir aussi :** HLS, AV1, H264, ffmpeg

## `RTMP` — Real-Time Messaging Protocol [Multimédia/Réseau]
**Niveau :** intermediaire | **Popularité :** 88 | **Aliases :** —
**Contextes :** envoyer le flux vidéo produit par un logiciel de régie (OBS Studio, vMix) vers un serveur d'ingestion de streaming (Twitch, YouTube Live, Restream)
**Rôle :** Protocole réseau basé sur TCP développé à l'origine par Macromedia (Adobe) pour la transmission à faible latence de flux vidéo et audio.
**Syntaxe :** URL d'ingestion : `rtmp://live.twitch.tv/app/live_stream_key`
**Cas réguliers :**
- `Ingestion de Live` — Protocole standard d'envoi du signal depuis l'encodeur du streamer (OBS) vers les serveurs cloud
- `RTMPS` — Variante sécurisée du protocole encapsulée dans TLS (port 443)
**Origine :** Macromedia / Adobe Systems (2002).
**Subtilités/confusions :**
- RTMP n'est plus utilisé pour diffuser la vidéo aux spectateurs dans les navigateurs (remplacé par HLS/DASH) ; il reste cantonné à la contribution (ingestion).
**Urgences/dangers :** —
**Précautions :** Migrer à terme les flux d'ingestion vers des alternatives plus modernes à faible latence comme **SRT** ou **RIST**.
**Équivalents :** SRT (Secure Reliable Transport), RIST, WebRTC
**Voir aussi :** HLS, DASH, WebRTC

## `WebRTC` — Web Real-Time Communication [Web/Réseau]
**Niveau :** avance | **Popularité :** 97 | **Aliases :** W3C WebRTC
**Contextes :** établir des visioconférences, appels vocaux ou partages d'écran peer-to-peer (P2P) à très faible latence (< 500 ms) directement entre navigateurs web (Google Meet, Discord, Zoom web)
**Rôle :** Standard W3C/IETF et ensemble d'APIs JavaScript permettant la communication audio, vidéo et de données arbitraires en temps réel sans plugin.
**Syntaxe :** `const pc = new RTCPeerConnection(configuration);`
**Cas réguliers :**
- `RTCPeerConnection` — Gestion du canal audio/vidéo chiffré P2P (SRTP/DTLS)
- `RTCDataChannel` — Échange de données binaires ou texte ultra-rapides en P2P (via SCTP)
- `STUN / TURN` — Serveurs d'infrastructure nécessaires pour traverser les pare-feux et NAT (ICE Candidate)
**Origine :** Google (2011 / Standard W3C 2021).
**Subtilités/confusions :**
- Nécessite un serveur de signalement (*Signaling Server* via WebSocket) pour permettre aux deux clients de s'échanger leurs adresses réseau avant d'établir le lien P2P.
**Urgences/dangers :** —
**Précautions :** Prévoir des serveurs relais TURN pour garantir la connexion lorsque les utilisateurs sont derrière des pare-feux d'entreprise stricts (Symmetric NAT).
**Équivalents :** WebTransport, RTMP
**Voir aussi :** WebSocket, UDP, TLS

## `DNSSEC` — Domain Name System Security Extensions [Réseau/Sécurité]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** RFC 4033/4034/4035
**Contextes :** signer numériquement les enregistrements DNS pour empêcher l'empoisonnement du cache DNS (*DNS Cache Poisoning*) et les redirections malveillantes
**Rôle :** Suite d'extensions de sécurité du protocole DNS ajoutant une authentification cryptographique aux réponses DNS via des signatures électroniques.
**Syntaxe :** `dig +dnssec exemple.com`
**Cas réguliers :**
- `Clé RRSIG` — Signature cryptographique associée à un jeu d'enregistrements DNS
- `Clé DS (Delegation Signer)` — Empreinte de la clé transmise au registre du domaine parent (.fr, .com) pour établir la chaîne de confiance
**Origine :** IETF (1997 / RFC 4033-4035 en 2005).
**Subtilités/confusions :**
- DNSSEC garantit l'**authenticité** et l'**intégrité** de la réponse DNS, mais ne **chiffre pas** les requêtes (pour le chiffrement, utiliser DoH ou DoT).
**Urgences/dangers :** ⚠️ Une erreur de clé ou d'expiration de signature DNSSEC rend l'intégralité de votre nom de domaine totalement invisible sur Internet !
**Précautions :** Utiliser la gestion DNSSEC automatisée proposée par votre registrar ou votre DNS managé (Cloudflare, AWS Route53).
**Équivalents :** DoH, DoT
**Voir aussi :** DNS, DoH, dig, PKI

## `DoH` — DNS over HTTPS [Réseau/Sécurité]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** RFC 8484
**Contextes :** chiffrer les requêtes DNS dans un tunnel HTTPS pour empêcher la surveillance, le filtrage et l'interception des noms de domaine visités par votre FAI ou un réseau Wi-Fi public
**Rôle :** Protocole réseau qui effectue la résolution de noms de domaine DNS chiffrée via le protocole HTTPS (port 443).
**Syntaxe :** `curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=exemple.com'`
**Cas réguliers :**
- `Protection de la vie privée` — Masque les requêtes DNS aux yeux des opérateurs réseau et des hotspots Wi-Fi publics
- `Contournement de censure` — Rend inefficaces les blocages DNS appliqués par les FAI
**Origine :** Paul Hoffman, Patrick McManus / IETF (2018 / RFC 8484).
**Subtilités/confusions :**
- `DoH` utilise HTTPS sur le port 443 (indissociable du trafic web standard) ; `DoT` (DNS over TLS) utilise un port dédié (port 853).
**Urgences/dangers :** —
**Précautions :** Configurer un résolveur DoH de confiance (Cloudflare 1.1.1.1, Quad9 9.9.9.9 ou NextDNS) dans votre navigateur ou OS.
**Équivalents :** DoT (DNS over TLS), DNSCrypt
**Voir aussi :** DNS, DNSSEC, HTTPS, TLS

## `VPN` — Virtual Private Network [Réseau/Sécurité]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** RPV (Réseau Privé Virtuel)
**Contextes :** connecter de manière sécurisée un équipement distant ou un ordinateur portable au réseau interne d'une entreprise via un tunnel chiffré sur Internet
**Rôle :** Technologie réseau créant un canal de communication virtuel chiffré de bout en bout au-dessus d'un réseau non sécurisé comme Internet.
**Syntaxe :** `wg-quick up wg0` (WireGuard) ou `openvpn --config client.ovpn`
**Cas réguliers :**
- `VPN d'Accès Distant (Remote Access)` — Connexion d'un utilisateur nomade au réseau de son entreprise
- `VPN Site-à-Site (Site-to-Site)` — Interconnexion permanente de deux réseaux de réseaux locaux distants (ex: deux bureaux régionaux)
**Origine :** Gurdeep Singh Pall / Microsoft (PPTP, 1996).
**Subtilités/confusions :**
- Un VPN chiffre le trafic entre le client et le serveur VPN, mais n'assure pas l'anonymat absolu si le fournisseur de VPN conserve des journaux d'activité.
**Urgences/dangers :** —
**Précautions :** Migrer les infrastructures VPN historiques vers des protocoles modernes et légers comme WireGuard.
**Équivalents :** WireGuard, OpenVPN, IPsec, Tailscale
**Voir aussi :** WireGuard, OpenVPN, IPsec, TLS

## `IPsec` — Internet Protocol Security [Réseau/Sécurité]
**Niveau :** avance | **Popularité :** 93 | **Aliases :** RFC 4301
**Contextes :** établir des tunnels VPN d'entreprise extrêmement robustes et chiffrés directement au niveau de la couche réseau (IP / couche 3 OSI)
**Rôle :** Suite de protocoles de sécurité de la couche réseau permettant l'authentification, l'intégrité et le chiffrement des paquets IP (AH et ESP).
**Syntaxe :** (Implémentations : StrongSwan, Libreswan, IPsec sous Linux)
**Cas réguliers :**
- `ESP (Encapsulating Security Payload)` — Fournit le chiffrement et l'authentification des données du paquet
- `IKEv2 (Internet Key Exchange v2)` — Protocole de négociation des clés et d'établissement des associations de sécurité
- `Mode Tunnel` — Chiffre l'intégralité du paquet IP d'origine (utilisé pour les VPNs)
**Origine :** John Ioannidis et Dan McDonald / IETF (1995 / RFC 4301).
**Subtilités/confusions :**
- Agit de manière totalement transparente pour les applications situées au-dessus car il opère au niveau du noyau (couche 3) et non dans l'espace utilisateur.
**Urgences/dangers :** —
**Précautions :** Utiliser IKEv2 avec des algorithmes de chiffrement modernes (AES-GCM) et éviter IKEv1 désormais vulnérable.
**Équivalents :** WireGuard, OpenVPN
**Voir aussi :** VPN, WireGuard, OpenVPN, TLS

## `SSL-VPN` — Réseau privé virtuel basé sur SSL/TLS [Réseau/Sécurité]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** TLS-VPN
**Contextes :** fournir un accès distant sécurisé au réseau d'entreprise depuis n'importe quel navigateur web sans avoir à installer un client VPN lourd sur le poste utilisateur
**Rôle :** Type de VPN qui utilise les protocoles TLS/SSL pour sécuriser les connexions distantes, fonctionnant généralement sur le port HTTPS 443 standard.
**Syntaxe :** Accès via portail web HTTPS ou client léger (OpenVPN, FortiClient, Cisco AnyConnect)
**Cas réguliers :**
- `Portail Web SSL-VPN` — Accès aux applications internes (intranet, webmail) via un simple navigateur web
- `Tunnel SSL-VPN` — Redirection complète du trafic réseau via un adaptateur virtuel TUN/TAP
**Origine :** Aventail / NetScreen (début des années 2000).
**Subtilités/confusions :**
- Avantage majeur par rapport à IPsec : traverse facilement les pare-feux et proxys d'entreprise car le trafic emprunte le port HTTPS standard (443).
**Urgences/dangers :** —
**Précautions :** Exiger impérativement l'authentification multi-facteurs (MFA) sur les portails d'accès SSL-VPN.
**Équivalents :** IPsec, WireGuard, OpenVPN
**Voir aussi :** OpenVPN, TLS, VPN, MFA

## `MFA` — Multi-Factor Authentication [Sécurité]
**Niveau :** debutant | **Popularité :** 99 | **Aliases :** 2FA (Two-Factor Authentication), A2F
**Contextes :** renforcer la sécurité des connexions utilisateurs (comptes cloud, VPN, webmail, SSH) en exigeant au moins deux preuves d'identité distinctes
**Rôle :** Système de contrôle d'accès qui requiert la présentation combinée de deux ou plusieurs facteurs indépendants parmi : ce que l'on sait (mot de passe), ce que l'on possède (smartphone, clé YubiKey), ou ce que l'on est (empreinte digitale, visage).
**Syntaxe :** (Mécanisme d'authentification renforcée)
**Cas réguliers :**
- `Facteur 1` — Quelque chose que je sais (mot de passe, code PIN)
- `Facteur 2` — Quelque chose que je possède (application TOTP Authenticator, clé de sécurité FIDO2)
- `Facteur 3` — Quelque chose que je suis (biométrie : TouchID, FaceID)
**Origine :** Brevets d'authentification réseau (années 1990) / Standardisé par le NVD et le NIST.
**Subtilités/confusions :**
- La réception de codes par SMS est considérée comme la forme de 2FA la plus faible en raison des risques de SIM-swapping ; privilégier les clés TOTP ou FIDO2/Passkeys.
**Urgences/dangers :** ⚠️ Le MFA bloque plus de 99% des attaques d'automates et d'usurpation de mots de passe.
**Précautions :** Imposer l'activation du MFA pour tous les accès d'administration infrastructure (AWS, GCP, GitHub, VPN).
**Équivalents :** 2FA, TOTP, FIDO2, Passkey
**Voir aussi :** TOTP, FIDO2, Passkey, SSO

## `TOTP` — Time-based One-Time Password [Sécurité]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** RFC 6238
**Contextes :** générer des codes à usage unique de 6 chiffres se renouvelant toutes les 30 secondes dans une application mobile (Google Authenticator, Authy, 1Password) pour le MFA
**Rôle :** Algorithme standardisé (RFC 6238) calculant un mot de passe temporaire à partir d'un secret partagé et de l'heure courante synchronisée du système.
**Syntaxe :** `oathtool --totp -b "CLE_SECRETE_BASE32"`
**Cas réguliers :**
- `QR Code d'enregistrement` — Encodage de l'URL `otpauth://totp/Service:user@mail.com?secret=JBSWY3DPEHPK3PXP` lue par l'application
- `Fenetre de tolérance` — Le serveur accepte généralement les codes valides à `T - 30s` et `T + 30s` pour compenser de décalages d'horloge légers
**Origine :** IETF (2011 / RFC 6238 / basé sur HOTP).
**Subtilités/confusions :**
- Fonctionne **entièrement hors-ligne** sur le smartphone de l'utilisateur (aucun besoin de réseau mobile ou Internet pour générer le code de 6 chiffres !).
**Urgences/dangers :** —
**Précautions :** Proposer des codes de secours à imprimer lors de l'activation initiale pour éviter qu'un utilisateur ne perde l'accès à son compte en cas de perte de téléphone.
**Équivalents :** HOTP, Push notification, FIDO2
**Voir aussi :** MFA, HOTP, FIDO2

## `HOTP` — HMAC-based One-Time Password [Sécurité]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** RFC 4226
**Contextes :** générer des mots de passe à usage unique basés sur un compteur d'événements (bouton physique sur une carte ou un jeton matériel)
**Rôle :** Algorithme standardisé (RFC 4226) de génération de codes à usage unique utilisant une fonction HMAC-SHA1 et un compteur incrémenté à chaque appui sur le bouton.
**Syntaxe :** `oathtool --hotp -b "CLE_SECRETE_BASE32" --counter=1`
**Cas réguliers :**
- `Jeton matériel (Hardware Token)` — Boîtier physique avec écran LCD qui génère un nouveau code de 6 chiffres à chaque pression du bouton
**Origine :** NINIT / IETF (2005 / RFC 4226).
**Subtilités/confusions :**
- Contrairement à TOTP (basé sur le **temps**), HOTP est basé sur un **compteur d'utilisations** qui s'incrémente à chaque demande.
**Urgences/dangers :** —
**Précautions :** Configurer une fenêtre de resynchronisation du compteur côté serveur en cas d'appuis répétés hors ligne.
**Équivalents :** TOTP, FIDO2
**Voir aussi :** TOTP, MFA, HMAC

## `FIDO2` — Fast Identity Online 2 [Sécurité]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** WebAuthn + CTAP2
**Contextes :** s'authentifier sur le Web de manière totalement immunisée contre le phishing sans saisir de mot de passe, en utilisant des clés physiques (YubiKey) ou des capteurs biométriques
**Rôle :** Ensemble de standards ouverts (Alliance FIDO et W3C) définissant une authentification forte par clé publique nativement prise en charge par les navigateurs web et systèmes d'exploitation.
**Syntaxe :** API JavaScript : `navigator.credentials.create()` et `navigator.credentials.get()`
**Cas réguliers :**
- `WebAuthn` — API JavaScript standard du W3C permettant aux applications web d'interagir avec les clés FIDO2
- `CTAP2 (Client-to-Authenticator Protocol)` — Protocole permettant à une clé USB/NFC (YubiKey) de communiquer avec un système hôte
**Origine :** FIDO Alliance / W3C (2018).
**Subtilités/confusions :**
- FIDO2 lie l'authentification au nom de domaine exact (origine HTTP) : une fausse page de phishing sur un faux domaine ne pourra JAMAIS intercepter la signature FIDO2 !
**Urgences/dangers :** —
**Précautions :** Enregistrer au moins deux clés de sécurité physiques FIDO2 sur les comptes critiques d'administration.
**Équivalents :** Passkey, TOTP
**Voir aussi :** Passkey, MFA, TOTP, RSA

## `Passkey` — Authentification sans mot de passe [Sécurité]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** Clé de Pass (Apple, Google, Microsoft)
**Contextes :** remplacer définitivement les mots de passe traditionnels par des paires de clés cryptographiques FIDO2 synchronisées de manière transparente entre vos appareils (iCloud Keychain, Google Password Manager, 1Password)
**Rôle :** Implémentation grand public et synchronisée du standard FIDO2/WebAuthn permettant de se connecter à des sites web avec TouchID, FaceID ou le schéma du téléphone.
**Syntaxe :** (Standard d'authentification biométrique / cryptographique)
**Cas réguliers :**
- `Passkey Synchronisée` — Clé FIDO2 répliquée de manière chiffrée de bout en bout sur tous vos appareils Apple ou Android
- `Connexion QR Code` — Utiliser son smartphone pour se connecter sur un ordinateur tiers en scannant un QR code
**Origine :** Apple, Google, Microsoft et la FIDO Alliance (2022).
**Subtilités/confusions :**
- Contrairement aux clés FIDO2 matérielles classiques (YubiKey) scellées dans le matériel, les Passkeys modernes se synchronisent entre vos appareils enregistrés.
**Urgences/dangers :** ⚠️ Élimine totalement le risque de fuite de mots de passe par piratage des bases de données de serveurs web.
**Précautions :** Proposer les Passkeys comme méthode de connexion par défaut dans toutes les nouvelles applications web.
**Équivalents :** FIDO2, WebAuthn
**Voir aussi :** FIDO2, MFA, TOTP

## `KDF` — Key Derivation Function [Sécurité]
**Niveau :** avance | **Popularité :** 90 | **Aliases :** Dérivation de clé
**Contextes :** dériver des clés cryptographiques robustes à partir d'un mot de passe saisi par un utilisateur, ou hacher des mots de passe en base de données de manière résistante aux GPU
**Rôle :** Algorithme cryptographique qui prend une valeur d'entrée (mot de passe + sel) et applique des itérations intensives pour générer une ou plusieurs clés cryptographiques sécurisées.
**Syntaxe :** (Algorithmes : Argon2id, bcrypt, PBKDF2, scrypt)
**Cas réguliers :**
- `Argon2id` — Vainqueur du Password Hashing Competition (2015), standard actuel le plus recommandé (résistant aux GPU et ASIC)
- `PBKDF2` — Standard PKCS#5 historique utilisant de nombreuses itérations de HMAC-SHA256
- `bcrypt` — Algorithme de hachage de mot de passe basé sur Blowfish, largement déployé
**Origine :** RSA Laboratories / Standards PKCS (1990s) / PHC (2015).
**Subtilités/confusions :**
- Un KDF est **FAIT POUR ÊTRE LENT** (paramétré par un facteur de coût) afin de rendre les attaques par force brute ou dictionnaire impraticables même sur GPU.
**Urgences/dangers :** ⚠️ Ne jamais hacher des mots de passe avec de simples fonctions de hachage rapides comme MD5, SHA-1 ou SHA-256 bruts !
**Précautions :** Utiliser Argon2id avec un sel aléatoire de 16 octets généré pour chaque mot de passe.
**Équivalents :** Argon2, bcrypt, PBKDF2, scrypt
**Voir aussi :** HMAC, hashcat, openssl

## `RBAC` — Role-Based Access Control [Sécurité/Développement]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** Contrôle d'accès basé sur des rôles
**Contextes :** restreindre les fonctionnalités et données d'une application ou d'une infrastructure en attribuant des rôles aux utilisateurs (ex: Admin, Editeur, Visiteur)
**Rôle :** Modèle de gestion des autorisations où les permissions sont associées à des rôles virtuels, et les utilisateurs sont rattachés à un ou plusieurs de ces rôles.
**Syntaxe :** Ex: `@PreAuthorize("hasRole('ADMIN')")`
**Cas réguliers :**
- `Matrice de rôles` — Rôle `ADMIN` (rwx sur tout), Rôle `USER` (read/write sur ses propres objets), Rôle `GUEST` (read-only)
- `Kubernetes RBAC` — Attribution de `Role` et `ClusterRole` via des `RoleBinding` aux comptes de service
**Origine :** David Ferraiolo et Rick Kuhn / NIST (1992 / Standard ANSI/INCITS 359-2004).
**Subtilités/confusions :**
- Simple à mettre en œuvre, mais peut devenir rigide si le nombre de cas particuliers augmente (problème d'explosion de rôles / *role explosion*).
**Urgences/dangers :** —
**Précautions :** Combiner ou faire évoluer vers le modèle ABAC lorsque des règles contextuelles dynamiques (heure, adresse IP, propriété) sont nécessaires.
**Équivalents :** ABAC, ACL, PBAC
**Voir aussi :** ABAC, IAM, Kubernetes

## `ABAC` — Attribute-Based Access Control [Sécurité/Développement]
**Niveau :** avance | **Popularité :** 88 | **Aliases :** Contrôle d'accès basé sur des attributs
**Contextes :** exprimer des règles d'autorisation ultra-fines et dynamiques dans des applications d'entreprise complexes ou des environnements de défense
**Rôle :** Modèle d'autorisation évalué dynamiquement qui accorde ou refuse l'accès en fonction des attributs du sujet (utilisateur), de la ressource, de l'action et de l'environnement.
**Syntaxe :** Règle : *SI sujet.service == "Finance" ET ressource.statut == "Confidentiel" ET environnement.heure < 18h ALORS Autoriser*
**Cas réguliers :**
- `Attributs du Sujet` — Rôle, département, niveau d'habilitation, âge
- `Attributs de la Ressource` — Propriétaire, niveau de sensibilité, date de création
- `Attributs de l'Environnement` — Adresse IP, géolocalisation, heure de la journée, type d'appareil
**Origine :** NIST SP 800-162 (2014) / Standard XACML.
**Subtilités/confusions :**
- Beaucoup plus flexible et granulaire que RBAC car il ne nécessite pas de créer un nouveau rôle pour chaque combinaison de conditions.
**Urgences/dangers :** —
**Précautions :** Utiliser des moteurs de politique comme Open Policy Agent (**OPA**) ou AWS Verified Permissions pour évaluer les règles ABAC.
**Équivalents :** RBAC, ReBAC (Relationship-Based Access Control)
**Voir aussi :** RBAC, IAM, OPA

## `SAST` — Static Application Security Testing [Développement/Sécurité]
**Niveau :** intermediaire | **Popularité :** 93 | **Aliases :** Analyse statique de sécurité
**Contextes :** scanner le code source non exécuté d'une application dans le pipeline CI/CD pour détecter automatiquement des vulnérabilités de sécurité et mauvaises pratiques
**Rôle :** Technologie d'audit de code source (*White-Box Testing*) qui analyse les fichiers de code, l'AST et les flux de données sans exécuter l'application.
**Syntaxe :** `semgrep scan --config p/security-audit .`
**Cas réguliers :**
- `Analyse de Taint (Taint Analysis)` — Tracer les entrées utilisateur non assainies depuis la source (HTTP) jusqu'à une variable d'exécution sensible (SQL, Shell)
- `Intégration CI` — Bloquer la Pull Request si une vulnérabilité critique est introduite dans le commit
**Origine :** Outils d'analyse statique des années 2000 (Fortify, Coverity, SonarQube, Semgrep).
**Subtilités/confusions :**
- **SAST** analyse le **code source** (boîte blanche sans exécution) ; **DAST** teste l'**application en cours d'exécution** (boîte noire par requêtes HTTP).
**Urgences/dangers :** —
**Précautions :** Configurer les règles pour minimiser le taux de faux positifs afin que les développeurs ne prennent pas l'habitude de masquer les alertes.
**Équivalents :** DAST, IAST, Linting de sécurité
**Voir aussi :** semgrep, OWASP, DAST, CWE

## `SAML` — Security Assertion Markup Language [Sécurité]
**Niveau :** avance | **Popularité :** 91 | **Aliases :** SAML 2.0
**Contextes :** implémenter l'authentification unique (SSO) d'entreprise entre un fournisseur d'identité (Okta, Azure AD, Ping) et des applications SaaS (Salesforce, Slack, AWS)
**Rôle :** Standard ouvert basé sur XML (SAML 2.0) pour l'échange de données d'authentification et d'autorisation entre un Fournisseur d'Identité (IdP) et un Fournisseur de Service (SP).
**Syntaxe :** Assertion XML signée transmise via POST HTTP
**Cas réguliers :**
- `IdP (Identity Provider)` — Le serveur d'authentification central de l'entreprise (ex: Microsoft Entra ID / Azure AD)
- `SP (Service Provider)` — L'application cible qui fait confiance aux assertions XML signées par l'IdP
- `SAML Response` — Document XML signé contenant l'identité de l'utilisateur et ses attributs
**Origine :** Consortium OASIS (SAML 2.0 en 2005).
**Subtilités/confusions :**
- Standard d'entreprise historique basé sur XML, progressivement concurrencé dans les applications modernes par le protocole OIDC (OpenID Connect basé sur JSON/JWT).
**Urgences/dangers :** ⚠️ Toujours vérifier la signature cryptographique XML de l'assertion SAML pour contrer les attaques par injection de commentaires XML (*XML Signature Wrapping*).
**Précautions :** Conserver la clé privée de signature SAML à jour et surveiller son expiration.
**Équivalents :** OIDC (OpenID Connect), WS-Federation
**Voir aussi :** OIDC, OAuth2, SSO, XML

## `OAuth2` — Open Authorization 2.0 [Web/Sécurité]
**Niveau :** intermediaire | **Popularité :** 99 | **Aliases :** RFC 6749
**Contextes :** autoriser une application tierce à accéder à des ressources d'un utilisateur (ex: lire ses contacts Google) sans que l'utilisateur ne lui donne son mot de passe
**Rôle :** Framework d'autorisation standard ouvert (RFC 6749) permettant d'accorder à une application un accès limité à des ressources protégées au nom d'un utilisateur.
**Syntaxe :** `GET /authorize?response_type=code&client_id=XYZ&scope=read`
**Cas réguliers :**
- `Authorization Code Grant + PKCE` — Flux d'autorisation recommandé pour les SPA et applications mobiles
- `Access Token` — Jeton (souvent JWT) présenté par le client pour accéder aux API autorisées
- `Scope` — Définition granulaire des permissions demandées (ex: `read:messages`, `write:profile`)
**Origine :** Eran Hammer, Blaine Cook / IETF (2012 / RFC 6749).
**Subtilités/confusions :**
- **OAuth 2.0 est un protocole d'AUTORISATION**, et non d'authentification ! Pour gérer l'authentification (l'identité de l'utilisateur), il faut utiliser la couche **OIDC** construite au-dessus d'OAuth2.
**Urgences/dangers :** ⚠️ Utiliser impérativement le paramètre `state` ou `PKCE` (`code_challenge`) pour éviter les attaques par interception de code d'autorisation.
**Précautions :** Valider rigoureusement le champ `redirect_uri` côté serveur d'autorisation.
**Équivalents :** OIDC, SAML
**Voir aussi :** OIDC, JWT, HMAC, SSO

## `OIDC` — OpenID Connect [Web/Sécurité]
**Niveau :** intermediaire | **Popularité :** 98 | **Aliases :** OpenID Connect 1.0
**Contextes :** implémenter des boutons de connexion sociale ("Se connecter avec Google / GitHub / Apple") ou l'authentification SSO sur des applications web et mobiles modernes
**Rôle :** Couche d'authentification simple construite au-dessus du framework d'autorisation OAuth 2.0, permettant au client de vérifier l'identité de l'utilisateur final.
**Syntaxe :** `GET /authorize?response_type=code&scope=openid%20profile%20email`
**Cas réguliers :**
- `ID Token` — Jeton au format **JWT** retourné par le serveur contenant les affirmations (*claims*) d'identité de l'utilisateur (`sub`, `email`, `name`, `iss`, `exp`)
- `UserInfo Endpoint` — Endpoint d'API protégé permettant de récupérer des détails supplémentaires sur l'utilisateur
- `Scope openid` — Déclencheur obligatoire dans la requête OAuth2 pour activer le protocole OIDC
**Origine :** OpenID Foundation (2014 / Nat Sakimura, John Bradley, Michael B. Jones).
**Subtilités/confusions :**
- OIDC = OAuth 2.0 (Autorisation) + ID Token JWT (Identité).
**Urgences/dangers :** ⚠️ Toujours vérifier la signature, l'émetteur (`iss`) et le destinataire (`aud`) de l'ID Token JWT reçu.
**Précautions :** Utiliser la découverte automatique via l'endpoint `/.well-known/openid-configuration` pour configurer le client OIDC.
**Équivalents :** SAML 2.0, OAuth2
**Voir aussi :** OAuth2, JWT, SSO, SAML
