# Face A — Commandes : DOCKER, KUBERNETES ET CONTENEURISATION (fiches riches v3)

> Lot MVP #026 — cible 50 fiches. Avancement : 15/50 (bloc 1 Docker Engine : run, exec, ps, build, images, stop, start, restart, rm, rmi, logs, inspect, pull, push, system prune). Format : `## \`commande\` — titre [OS]` + 10 rubriques obligatoires validées par `tools/parse_rich.py`.

## `docker run` — Créer et démarrer un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** instancier une application conteneurisée, tester un service web en 2 secondes, exécuter un environnement isolé
**Rôle :** Télécharger l'image (si absente), créer une instance de conteneur isolée et démarrer son processus principal.
**Syntaxe :** `docker run [options] <image> [commande] [args]`
**Cas réguliers :**
- `docker run -d -p 8080:80 --name mon-web nginx:alpine` — Lancer un serveur Nginx en arrière-plan avec redirection de port (le plus courant)
- `docker run -it --rm ubuntu:22.04 bash` — Ouvrir un terminal interactif éphémère détruit à la sortie
- `docker run -v $(pwd):/app -w /app node:18 npm test` — Monter le dossier local dans le conteneur pour exécuter des tests
- `docker run --env-file .env postgres:15-alpine` — Injecter des variables d'environnement depuis un fichier
**Origine :** Docker Inc. (2013) — brique fondamentale qui a popularisé la conteneurisation légère au-dessus des cgroups et namespaces Linux.
**Subtilités/confusions :**
- `docker run` combine DEUX actions : `docker create` (instancier) + `docker start` (lancer). Pour relancer un conteneur existant, utiliser `docker start`.
- Sans `-d` (*detached*), le conteneur bloque le terminal. Sans `--rm`, le conteneur arrêté reste sur le disque et occupe de l'espace.
- `-p 8080:80` se lit `<port-hote>:<port-conteneur>` : inverse de la syntaxe de copie.
**Urgences/dangers :** ⚠️ `docker run --privileged` désactive toutes les protections d'isolation et donne au conteneur l'accès root complet à l'hôte.
**Précautions :** Toujours spécifier un tag d'image précis (`postgres:15.3-alpine`) au lieu de `:latest` pour garantir la reproductibilité.
**Équivalents :** podman run, nerdctl run, chroot / systemd-nspawn
**Voir aussi :** docker exec, docker stop, docker ps, docker start

## `docker exec` — Exécuter une commande dans un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** ouvrir un shell dans un conteneur actif, exécuter des requêtes de diagnostic, inspecter un état en direct
**Rôle :** Entrer dans l'espace de noms d'un conteneur EN COURS D'EXÉCUTION pour y lancer un nouveau processus.
**Syntaxe :** `docker exec [options] <conteneur> <commande> [args]`
**Cas réguliers :**
- `docker exec -it mon-app sh` — Ouvrir un shell interactif dans le conteneur (le réflexe de débogage)
- `docker exec -it ma-bdd psql -U postgres` — Ouvrir la console PostgreSQL directement dans le conteneur
- `docker exec mon-app cat /etc/hosts` — Exécuter une commande ponctuelle et afficher sa sortie sans ouvrir de shell
- `docker exec -u root mon-app apt-get update` — Exécuter une commande sous l'identité de l'utilisateur root
**Origine :** Docker 1.3 (2014) — introduit pour remplacer l'usage lourd de démons SSH à l'intérieur des conteneurs.
**Subtilités/confusions :**
- Ne fonctionne QUE sur un conteneur actif (état `running`). Sur un conteneur arrêté, utiliser `docker run` ou `docker start`.
- `-i` garde STDIN ouvert, `-t` alloue un pseudo-terminal (TTY) : la combinaison `-it` est indispensable pour un shell interactif.
- Le processus lancé par `exec` est un processus frère du processus principal (PID 1) du conteneur.
**Urgences/dangers :** — (les modifications apportées au conteneur éphémère seront perdues lors de son redémarrage sauf si sur un volume)
**Précautions :** Ne pas installer d'outils de dev définitifs dans un conteneur de prod via `exec` : modifier plutôt le Dockerfile.
**Équivalents :** kubectl exec, podman exec, nerdctl exec
**Voir aussi :** docker run, docker logs, docker ps

## `docker ps` — Lister les conteneurs [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** docker container ls
**Contextes :** vérifier les conteneurs actifs, trouver l'ID ou le nom d'un conteneur, vérifier la redirection des ports
**Rôle :** Afficher la liste des conteneurs actifs ou arrêtés avec leurs identifiants, images, statut, ports et noms.
**Syntaxe :** `docker ps [options]`
**Cas réguliers :**
- `docker ps` — Lister uniquement les conteneurs en cours d'exécution (le plus courant)
- `docker ps -a` — Lister TOUS les conteneurs (actifs et arrêtés)
- `docker ps -q` — Afficher uniquement les IDs courts (idéal en script: `docker stop $(docker ps -q)`)
- `docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"` — Formatage personnalisé et propre de l'affichage
**Origine :** Docker 0.1 (2013) — s'inspire directement de la commande Unix traditionnelle `ps` (*Process Status*).
**Subtilités/confusions :**
- `docker ps` sans argument masque les conteneurs qui ont planté ou qui se sont arrêtés : utiliser `-a` pour les repérer.
- Les noms de conteneurs non spécifiés sont générés aléatoirement (`funny_hopper`, `loving_darwin`).
- La colonne `PORTS` montre la cartographie `<ip-hôte>:<port-hôte>-><port-conteneur>/<proto>`.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser `-a` systématiquement quand un conteneur semble "disparaître" après un `docker run`.
**Équivalents :** podman ps, kubectl get pods, crictl ps
**Voir aussi :** docker inspect, docker logs, docker stop

## `docker build` — Construire une image Docker [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** docker image build
**Contextes :** empaqueter une application, créer une image sur mesure, automatiser un build dans une chaîne CI/CD
**Rôle :** Lire les instructions d'un fichier `Dockerfile` et construire une image conteneurisée empilant des couches de système de fichiers.
**Syntaxe :** `docker build [options] <contexte-de-build>`
**Cas réguliers :**
- `docker build -t mon-application:1.0 .` — Construire l'image à partir du Dockerfile du dossier courant (le plus courant)
- `docker build -f Dockerfile.prod -t app:prod .` — Utiliser un fichier Dockerfile spécifique
- `docker build --no-cache -t app:clean .` — Forcer la reconstruction complète sans réutiliser le cache de couches
- `docker build --build-arg NODE_ENV=production .` — Passer des variables au moment de la construction
**Origine :** Docker 0.1 (2013) — concept clé ayant démocratisé l'infrastructure as code (IaC) pour les développeurs.
**Subtilités/confusions :**
- Le point final `.` désigne le CONTEXTE de build (l'ensemble des fichiers envoyés au démon Docker) : attention si le dossier contient des gigaoctets !
- Chaque instruction (`RUN`, `COPY`, `ADD`) crée une nouvelle couche d'image mise en cache.
- Utiliser un fichier `.dockerignore` pour exclure `node_modules`, `.git` et les fichiers temporaires du contexte de build.
**Urgences/dangers :** ⚠️ Copier des secrets (`.env`, clés SSH) avec `COPY` dans le Dockerfile les intègre à jamais dans les couches de l'image.
**Précautions :** Optimiser l'ordre des instructions dans le Dockerfile (mettre les dépendances avant le code source) pour maximiser le cache.
**Équivalents :** podman build, buildah bud, kaniko
**Voir aussi :** docker images, docker run, .dockerignore

## `docker images` — Lister les images locales [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 90 | **Aliases :** docker image ls
**Contextes :** vérifier la liste des images disponibles localement, vérifier la taille des images, repérer les images orphelines
**Rôle :** Afficher toutes les images conteneurisées stockées dans le registre local du moteur Docker.
**Syntaxe :** `docker images [options] [dépôt[:tag]]`
**Cas réguliers :**
- `docker images` — Afficher toutes les images stockées avec dépôt, tag, ID et taille (le plus courant)
- `docker images -a` — Lister toutes les images, y compris les couches intermédiaires
- `docker images -f "dangling=true"` — Lister les images orphelines (*dangling images*) sans nom ni tag (`<none>`)
- `docker images --format "{{.Repository}}:{{.Tag}} ({{.Size}})"` — Formatage personnalisé
**Origine :** Docker 0.1 (2013) — outil de consultation du cache d'images local de l'hôte.
**Subtilités/confusions :**
- Les images marquant `<none>:<none>` sont des images orphelines créées lors de la reconstruction d'une image avec un tag existant.
- La taille affichée est la taille décompressée sur le disque hôte, pas la taille transférée sur le réseau lors du `pull`.
- Deux tags peuvent pointer vers le MÊME Image ID (partage de stockage).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Nettoyer régulièrement les images orphelines avec `docker image prune` pour libérer l'espace disque.
**Équivalents :** podman images, nerdctl images, crictl rmi -l
**Voir aussi :** docker rmi, docker build, docker system prune

## `docker stop` — Arrêter un conteneur proprement [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** docker container stop
**Contextes :** stopper un service web, couper une base de données en sauvegardant les transactions, libérer les ports système
**Rôle :** Envoyer le signal `SIGTERM` au processus principal du conteneur, puis `SIGKILL` après un délai de grâce s'il ne s'est pas arrêté.
**Syntaxe :** `docker stop [options] <conteneur>...`
**Cas réguliers :**
- `docker stop mon-app` — Arrêter proprement le conteneur spécifié (le plus courant)
- `docker stop -t 30 ma-bdd` — Accorder un délai de grâce de 30 secondes avant l'arrêt forcé
- `docker stop $(docker ps -q)` — Arrêter TOUS les conteneurs actuellement en cours d'exécution
**Origine :** Docker 0.1 (2013) — arrêt contrôlé respectueux du cycle de vie des applications Unix.
**Subtilités/confusions :**
- `docker stop` envoie d'abord `SIGTERM` (arrêt propre) ; `docker kill` envoie immédiatement `SIGKILL` (arrêt brutal).
- Si l'application dans le conteneur ne gère pas `SIGTERM` ou n'est pas le PID 1, `docker stop` attendra 10 secondes par défaut avant de la tuer.
- L'arrêt d'un conteneur ne le SUPPRIME PAS : son état et son système de fichiers sont conservés.
**Urgences/dangers :** ⚠️ Stopper brutalement une base de données sans délai de grâce suffisant peut provoquer la corruption de tables non flushées.
**Précautions :** S'assurer que le script d'entrée du conteneur (ENTRYPOINT) transmet correctement les signaux Unix au processus fils.
**Équivalents :** podman stop, kubectl delete pod (grace-period), nerdctl stop
**Voir aussi :** docker start, docker kill, docker restart, docker rm

## `docker start` — Relancer un conteneur arrêté [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** docker container start
**Contextes :** redémarrer un conteneur arrêté, reprendre une session de travail arrêtée la veille sans recréer le conteneur
**Rôle :** Démarrer un ou plusieurs conteneurs préalablement créés et actuellement à l'arrêt.
**Syntaxe :** `docker start [options] <conteneur>...`
**Cas réguliers :**
- `docker start mon-app` — Démarrer le conteneur en arrière-plan (le plus courant)
- `docker start -i mon-app` — Démarrer le conteneur et attacher son entrée standard (mode interactif)
- `docker start -a mon-app` — Démarrer et afficher la sortie standard dans le terminal courant
**Origine :** Docker 0.1 (2013) — relance d'un conteneur existant conservant ses fichiers et sa configuration d'origine.
**Subtilités/confusions :**
- Ne crée PAS de nouveau conteneur : réutilise les paramètres de réseau, volumes et variables définis lors du `docker run` d'origine.
- Pour modifier les ports ou les volumes d'un conteneur, il faut le supprimer (`rm`) et réexécuter `docker run`.
**Urgences/dangers :** — (redémarre le conteneur dans son dernier état conservé)
**Précautions :** Vérifier les logs avec `docker logs` juste après le `start` si le conteneur s'arrête immédiatement.
**Équivalents :** podman start, nerdctl start
**Voir aussi :** docker stop, docker run, docker restart, docker ps

## `docker restart` — Redémarrer un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** docker container restart
**Contextes :** appliquer une modification de fichier de conf monté en volume, libérer la mémoire d'une application, relancer après un plantage
**Rôle :** Arrêter (`stop`) puis redémarrer (`start`) un ou plusieurs conteneurs en une seule commande atomique.
**Syntaxe :** `docker restart [options] <conteneur>...`
**Cas réguliers :**
- `docker restart mon-web` — Redémarrer le conteneur immédiatement (le plus courant)
- `docker restart -t 5 ma-bdd` — Redémarrer avec un délai de grâce de 5 secondes pour l'arrêt
**Origine :** Docker 0.1 (2013) — raccourci combinant `stop` et `start`.
**Subtilités/confusions :**
- Exécute un arrêt propre (`SIGTERM`) suivi du délai de grâce avant de relancer le processus principal.
- Le conteneur conserve exactement le même Container ID et la même adresse IP interne.
**Urgences/dangers :** — (identique aux précautions de `docker stop`)
**Précautions :** Vérifier que l'application supporte le redémarrage sans fuite d'état ou verrou d'instance résiduel.
**Équivalents :** podman restart, nerdctl restart
**Voir aussi :** docker stop, docker start, docker ps

## `docker rm` — Supprimer un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** docker container rm
**Contextes :** faire du propre sur la machine hôte, supprimer les conteneurs de test arrêtés, libérer le nom d'un conteneur
**Rôle :** Supprimer un ou plusieurs conteneurs du système de fichiers de l'hôte Docker.
**Syntaxe :** `docker rm [options] <conteneur>...`
**Cas réguliers :**
- `docker rm mon-app` — Supprimer un conteneur arrêté (le plus courant)
- `docker rm -f mon-app` — Forcer la suppression d'un conteneur EN COURS D'EXÉCUTION (envoie `SIGKILL`)
- `docker rm -v mon-app` — Supprimer le conteneur ET ses volumes anonymes associés
- `docker rm $(docker ps -a -q)` — Supprimer TOUS les conteneurs arrêtés de la machine
**Origine :** Docker 0.1 (2013) — libération des ressources disque associées à la couche d'écriture du conteneur.
**Subtilités/confusions :**
- Par défaut, `docker rm` refuse de supprimer un conteneur actif : utiliser `-f` pour forcer ou le stopper d'abord.
- Ne supprime PAS les images sources ni les volumes nommés par défaut.
- `docker container prune` est l'alternative moderne recommandée pour purger tous les conteneurs arrêtés.
**Urgences/dangers :** ⚠️ `docker rm -fv` supprime le conteneur ET ses volumes anonymes : toutes les données non persistées sur un volume nommé sont perdues définitivement.
**Précautions :** S'assurer que les données critiques sont stockées sur des volumes nommés ou des bind mounts avant la suppression.
**Équivalents :** podman rm, kubectl delete pod, nerdctl rm
**Voir aussi :** docker rmi, docker stop, docker system prune

## `docker rmi` — Supprimer une image Docker [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** docker image rm
**Contextes :** libérer plusieurs gigaoctets d'espace disque, supprimer d'anciennes versions d'images de dev
**Rôle :** Supprimer une ou plusieurs images du stockage local de l'hôte Docker.
**Syntaxe :** `docker rmi [options] <image>...`
**Cas réguliers :**
- `docker rmi node:18-alpine` — Supprimer une image par son nom et son tag (le plus courant)
- `docker rmi 8a3f12b` — Supprimer une image par son ID court
- `docker rmi -f mon-app:old` — Forcer la suppression d'une image même si plusieurs tags y font référence
- `docker rmi $(docker images -f "dangling=true" -q)` — Purger toutes les images orphelines sans nom
**Origine :** Docker 0.1 (2013) — libération d'espace disque sur les couches d'images.
**Subtilités/confusions :**
- Impossible de supprimer une image si un conteneur (même arrêté !) s'appuie encore dessus : supprimer le conteneur (`docker rm`) en premier.
- Si une image possède plusieurs tags, `docker rmi` retire simplement le tag spécifié sans supprimer les données tant qu'il reste d'autres tags.
**Urgences/dangers :** — (les images supprimées peuvent toujours être re-téléchargées si elles existent sur un registre distant)
**Précautions :** Purger d'abord les conteneurs inutilisés (`docker container prune`) avant d'exécuter `docker rmi`.
**Équivalents :** podman rmi, nerdctl rmi, crictl rmi
**Voir aussi :** docker images, docker rm, docker system prune

## `docker logs` — Consulter les journaux d'un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** docker container logs
**Contextes :** comprendre pourquoi un conteneur a planté, suivre les requêtes web en direct, déboguer un démarrage de service
**Rôle :** Extraire et afficher les journaux d'événements enregistrés par la sortie standard (STDOUT) et d'erreur (STDERR) d'un conteneur.
**Syntaxe :** `docker logs [options] <conteneur>`
**Cas réguliers :**
- `docker logs mon-app` — Afficher l'intégralité de l'historique des logs (le plus courant)
- `docker logs -f mon-web` — Suivre les logs en temps réel (mode *follow*, équivalent de `tail -f`)
- `docker logs --tail 100 mon-app` — Afficher uniquement les 100 dernières lignes de logs
- `docker logs -t --since 10m mon-app` — Afficher l'horodatage (`-t`) des logs émis ces 10 dernières minutes
**Origine :** Docker 0.1 (2013) — centralisation de la collecte de logs basée sur la capture des flux standards du processus PID 1.
**Subtilités/confusions :**
- N'affiche QUE ce que le processus principal écrit sur STDOUT et STDERR : les logs écrits dans des fichiers internes du conteneur ne sont pas vus ici.
- Par défaut, les logs Docker sont stockés indéfiniment dans des fichiers JSON sur l'hôte : configurer la rotation de logs (`log-driver`) pour éviter la saturation du disque.
**Urgences/dangers :** ⚠️ Lancer `docker logs mon-app` sans `--tail` sur un conteneur actif depuis des mois peut faire défiler des millions de lignes et figer le terminal.
**Précautions :** Utiliser `--tail 100 -f` par réflexe pour consulter les logs récents en direct.
**Équivalents :** kubectl logs, podman logs, nerdctl logs
**Voir aussi :** docker exec, docker inspect, docker ps

## `docker inspect` — Consulter les détails d'un objet [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 86 | **Aliases :** —
**Contextes :** trouver l'adresse IP interne d'un conteneur, vérifier les variables d'environnement injectées, consulter les points de montage
**Rôle :** Afficher sous forme d'un document JSON structuré la totalité de la configuration et de l'état interne d'un objet Docker (conteneur, image, volume, réseau).
**Syntaxe :** `docker inspect [options] <nom-ou-id>...`
**Cas réguliers :**
- `docker inspect mon-app` — Afficher toute la fiche JSON détaillée (le plus courant)
- `docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mon-app` — Extraire uniquement l'adresse IP interne
- `docker inspect --format='{{json .State}}' mon-app` — Extraire uniquement la sous-section de l'état d'exécution
- `docker inspect mon-volume` — Inspecter le chemin physique réel d'un volume sur l'hôte
**Origine :** Docker 0.1 (2013) — outil de diagnostic universel au format JSON.
**Subtilités/confusions :**
- Fonctionne sur TOUS les objets Docker : conteneurs, images, volumes, réseaux, nœuds swarm.
- L'option `--format` ou `-f` utilise la syntaxe des modèles Go (*Go templates*) pour parser directement le JSON.
**Urgences/dangers :** ⚠️ `docker inspect` affiche toutes les variables d'environnement du conteneur EN CLAIR (y compris les mots de passe et clés d'API).
**Précautions :** Filtrer la sortie avec `grep` ou de préférence `jq` / `--format` pour extraire rapidement la donnée recherchée.
**Équivalents :** kubectl get -o json / kubectl describe, podman inspect
**Voir aussi :** docker ps, docker logs, jq

## `docker pull` — Télécharger une image [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 95 | **Aliases :** docker image pull
**Contextes :** pré-télécharger une image avant un déploiement, mettre à jour une image de base vers la dernière révision
**Rôle :** Télécharger une image conteneurisée et ses couches associées depuis un registre distant (Docker Hub ou privé) vers l'hôte local.
**Syntaxe :** `docker pull [options] <nom-image>[:tag]`
**Cas réguliers :**
- `docker pull nginx:alpine` — Télécharger l'image Nginx sous sa variante Alpine (le plus courant)
- `docker pull ubuntu:22.04` — Télécharger la version précise Ubuntu 22.04
- `docker pull ghcr.io/org/app:v1.2` — Télécharger depuis un registre tiers (GitHub Container Registry)
- `docker pull --all-tags redis` — Télécharger TOUS les tags existants d'une image (très lourd !)
**Origine :** Docker 0.1 (2013) — analogue à un `git pull` pour les couches d'images de conteneurs.
**Subtilités/confusions :**
- Si aucun tag n'est spécifié, Docker ajoute automatiquement `:latest` par défaut.
- Ne re-télécharge QUE les couches modifiées ou absentes de votre cache local (gain de bande passante massif).
- `docker run` exécute un `docker pull` automatique si l'image n'existe pas localement.
**Urgences/dangers :** ⚠️ Télécharger des images non officielles ou non vérifiées depuis Docker Hub peut introduire des cryptomineurs ou des portes dérobées.
**Précautions :** Privilégier les images certifiées "Docker Official Image" ou signées ("Docker Content Trust").
**Équivalents :** podman pull, nerdctl pull, crictl pull
**Voir aussi :** docker push, docker images, docker run

## `docker push` — Pousser une image vers un registre [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** docker image push
**Contextes :** publier une application conteneurisée, partager une image avec l'équipe de dev, déployer en production via un registre
**Rôle :** Téléverser une image locale et ses nouvelles couches vers un registre distant (Docker Hub, AWS ECR, GCP GAR, GHCR).
**Syntaxe :** `docker push [options] <nom-image>[:tag]`
**Cas réguliers :**
- `docker push mon-compte/mon-app:1.0` — Pousser l'image sur Docker Hub (le plus courant)
- `docker push ghcr.io/org/app:v1.0.0` — Pousser vers GitHub Container Registry
- `docker push --all-tags mon-compte/mon-app` — Pousser tous les tags locaux d'un même dépôt
**Origine :** Docker 0.1 (2013) — publication distribuée d'artefacts d'applications.
**Subtilités/confusions :**
- Nécessite d'être identifié au préalable avec `docker login` sous peine d'erreur `Permission Denied`.
- L'image DOIT comporter le nom du registre/organisation dans son tag (ex: `registry.domaine.fr/projet/app:v1`).
- Seules les couches inexistantes sur le registre distant sont envoyées sur le réseau.
**Urgences/dangers :** ⚠️ Pousser une image contenant des secrets ou des clés d'API vers un registre public les rend accessibles au monde entier instantanément.
**Précautions :** Scanner l'image avec un outil de vulnérabilités (Trivy, Grype, Docker Scout) avant le push.
**Équivalents :** podman push, nerdctl push
**Voir aussi :** docker pull, docker tag, docker login

## `docker system prune` — Purger l'espace disque Docker [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 92 | **Aliases :** —
**Contextes :** libérer d'urgence des dizaines de gigaoctets d'espace disque, nettoyer les résidus de conteneurs et d'images de dev
**Rôle :** Nettoyer et supprimer en une seule opération tous les éléments Docker inutilisés (conteneurs arrêtés, réseaux orphelins, images non taguées et cache de build).
**Syntaxe :** `docker system prune [options]`
**Cas réguliers :**
- `docker system prune` — Purger les conteneurs arrêtés, les réseaux inutilisés et les images orphelines (le réflexe ménage)
- `docker system prune -a` — Purger TOUTES les images non utilisées par au moins un conteneur (très efficace !)
- `docker system prune --volumes` — Inclure aussi la suppression de TOUS les volumes non utilisés (⚠️ attention données !)
- `docker system prune -f` — Forcer le nettoyage sans demander de confirmation interactive
**Origine :** Docker 1.13 (2017) — commande de maintenance globale introduite pour simplifier les opérations de ménage.
**Subtilités/confusions :**
- Sans `--volumes`, `docker system prune` préserve vos volumes de données persistantes (Postgres, MySQL, etc.).
- L'option `-a` (*all*) supprime aussi les images saines téléchargées si aucun conteneur (même arrêté) n'y est actuellement rattaché.
**Urgences/dangers :** ⚠️ `docker system prune -a --volumes` détruit TOUTES les images et TOUS les volumes de données non rattachés à un conteneur actif sans retour possible.
**Précautions :** Toujours relire attentivement la liste des éléments qui vont être supprimés avant de confirmer par `y`.
**Équivalents :** podman system prune, nerdctl system prune
**Voir aussi :** docker volume, docker rmi, docker volume prune

## `docker compose` — Définir et gérer des applications multi-conteneurs [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 97 | **Aliases :** docker-compose (V1 historique)
**Contextes :** lancer une stack complète (App + BDD + Redis + Nginx) en une commande, orchestrer l'environnement de dev local
**Rôle :** Définir et exécuter des applications multi-conteneurs Docker à partir d'un fichier de configuration déclaratif `compose.yaml`.
**Syntaxe :** `docker compose [options] <up|down|ps|logs|exec|build> [services]`
**Cas réguliers :**
- `docker compose up -d` — Démarrer tous les services en arrière-plan (le plus courant)
- `docker compose down -v` — Stopper et supprimer la stack ET ses volumes associés
- `docker compose logs -f app` — Suivre les logs d'un service spécifique de la stack
- `docker compose exec db psql -U user` — Entrer dans le conteneur du service `db`
**Origine :** Fig (acheté par Docker en 2014) — devenu `docker-compose` (Python V1) puis réécrit nativement en Go dans Docker CLI (Compose V2).
**Subtilités/confusions :**
- Utiliser la commande moderne espace `docker compose` (V2) au lieu du vieux script à tiret `docker-compose` (V1 déprécié).
- Le fichier se nomme `compose.yaml` (ou `docker-compose.yml`) et utilise l'indentation YAML stricte.
- Les services d'une même stack Compose partagent automatiquement un réseau virtuel commun où ils se contactent par leur nom de service (ex: `http://db:5432`).
**Urgences/dangers :** ⚠️ `docker compose down -v` supprime les volumes nommés déclarés dans le compose file : données de bases de données locales perdues si non sauvegardées.
**Précautions :** Séparer la configuration de dev (`compose.override.yaml`) de celle de prod et ne jamais commiter de mots de passe en clair dans le file (utiliser `.env`).
**Équivalents :** podman-compose, kompose (convertit vers Kubernetes)
**Voir aussi :** docker run, docker network, docker volume

## `docker volume` — Gérer le stockage persistant [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** conserver les données d'une base PostgreSQL/MySQL après suppression du conteneur, partager des données entre conteneurs
**Rôle :** Administrer les volumes de données gérés directement par le moteur Docker indépendamment du cycle de vie des conteneurs.
**Syntaxe :** `docker volume <create | ls | inspect | rm | prune>`
**Cas réguliers :**
- `docker volume create pg_data` — Créer un volume nommé persistant (le plus courant)
- `docker volume ls` — Lister tous les volumes enregistrés sur l'hôte
- `docker volume inspect pg_data` — Voir le chemin physique réel sur le disque hôte (`Mountpoint`)
- `docker volume prune` — Nettoyer tous les volumes anonymes ou nommés non utilisés par au moins un conteneur
**Origine :** Docker 1.9 (2015) — mécanisme officiel de découplage du stockage et de l'exécution éphémère des conteneurs.
**Subtilités/confusions :**
- Deux types de montages : *Bind Mounts* (dossier hôte précis `/var/data`) vs *Named Volumes* (gérés par Docker dans `/var/lib/docker/volumes/`).
- Les volumes nommés conservent leurs données même si le conteneur qui les a créés est supprimé via `docker rm`.
- Un volume peut être monté simultanément par plusieurs conteneurs en lecture/écriture.
**Urgences/dangers :** ⚠️ `docker volume rm` ou `docker volume prune` supprime physiquement les fichiers du disque de l'hôte sans possibilité de restauration.
**Précautions :** Sauvegarder régulièrement le contenu des volumes critiques en créant des archives tar via un conteneur temporaire.
**Équivalents :** podman volume, Kubernetes PersistentVolume (PV/PVC)
**Voir aussi :** docker run, docker inspect, docker system prune

## `docker network` — Administrer les réseaux virtuels [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 89 | **Aliases :** —
**Contextes :** isoler les conteneurs de base de données du réseau externe, permettre la communication par nom d'hôte entre services
**Rôle :** Créer, connecter et gérer les réseaux virtuels isolés au-dessus desquels les conteneurs Docker communiquent.
**Syntaxe :** `docker network <create | ls | connect | disconnect | inspect | rm | prune>`
**Cas réguliers :**
- `docker network create mon-reseau` — Créer un réseau de type `bridge` isolé personnalisé (le plus courant)
- `docker network connect mon-reseau mon-app` — Connecter un conteneur existant à un réseau
- `docker network ls` — Lister les réseaux (bridge, host, none, macvlan, overlay)
- `docker network inspect mon-reseau` — Voir les conteneurs connectés et leurs adresses IP attribuées
**Origine :** Docker 1.9 (2015) — architecture réseau modulaire (CNM - Container Network Model).
**Subtilités/confusions :**
- Les conteneurs connectés à un réseau personnalisé bénéficient de la résolution DNS interne intégrée à Docker (`ping db` fonctionne par nom de conteneur).
- Le réseau par défaut `bridge` n'offre PAS la résolution DNS par nom de conteneur (nécessite `--link` obsolète ou un réseau custom).
- Le mode `--net=host` partage le réseau de l'hôte directement (performances maximales mais pas d'isolation de port).
**Urgences/dangers :** ⚠️ Relier un conteneur sensible au réseau `--net=host` expose tous ses ports directement sur les interfaces réseau publiques de la machine hôte.
**Précautions :** Créer un réseau bridge dédié par application pour isoler la base de données du reste de la machine.
**Équivalents :** podman network, Kubernetes CNI (Calico, Cilium, Flannel)
**Voir aussi :** docker run --net, docker inspect, docker compose

## `docker cp` — Copier des fichiers avec un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 87 | **Aliases :** docker container cp
**Contextes :** extraire un fichier de log d'un conteneur qui a planté, injecter un fichier de configuration de test sans reconstruire l'image
**Rôle :** Copier des fichiers ou des dossiers entre le système de fichiers de la machine hôte et un conteneur (actif ou arrêté).
**Syntaxe :** `docker cp <source> <destination>`
**Cas réguliers :**
- `docker cp mon-app:/etc/nginx/nginx.conf ./nginx.conf` — Extraire un fichier du conteneur vers l'hôte (le plus courant)
- `docker cp ./config.json mon-app:/app/config.json` — Copier un fichier local à l'intérieur du conteneur
- `docker cp mon-app:/var/log/app.log -` — Streamer un fichier du conteneur directement sur la sortie standard
**Origine :** Docker 0.8 (2014) — utilitaire de transfert direct basé sur un flux d'archive tar interne.
**Subtilités/confusions :**
- Fonctionne que le conteneur soit en cours d'exécution ou à l'arrêt.
- La syntaxe `<conteneur>:<chemin>` s'inspire directement de la commande `scp`.
- Les modifications apportées par `cp` à un conteneur sont éphémères : elles disparaissent si le conteneur est supprimé et recréé.
**Urgences/dangers :** — (remplace le fichier cible sans confirmation)
**Précautions :** Pour les modifications permanentes, privilégier un volume monté (`bind mount`) ou mettre à jour le Dockerfile.
**Équivalents :** kubectl cp, podman cp, nerdctl cp
**Voir aussi :** docker exec, docker run

## `docker commit` — Créer une image depuis un conteneur [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 78 | **Aliases :** docker container commit
**Contextes :** sauvegarder l'état d'un conteneur modifié manuellement pour investigation, geler un état de débogage rapide
**Rôle :** Enregistrer l'état du système de fichiers d'un conteneur et ses modifications sous la forme d'une nouvelle image Docker.
**Syntaxe :** `docker commit [options] <conteneur> [<dépôt>[:tag]]`
**Cas réguliers :**
- `docker commit mon-conteneur mon-image:debug` — Créer une image à partir du conteneur actuel (le plus courant)
- `docker commit -m "Install curl" -a "Adolphe" mon-app app:v2` — Ajouter un message et un auteur au commit
- `docker commit -c "CMD ['node', 'app.js']" mon-app app:v3` — Modifier la commande de démarrage par défaut de l'image
**Origine :** Docker 0.1 (2013) — s'inspire du concept de `git commit` appliqué à l'état d'un système de fichiers de conteneur.
**Subtilités/confusions :**
- Mettre en pause le conteneur (`-p`, par défaut) pendant le commit évite de corrompre des fichiers en cours d'écriture.
- `docker commit` est une MAUVAISE PRATIQUE pour créer des images de production : il est impossible d'auditer comment l'image a été construite.
- Préférer systématiquement la rédaction d'un `Dockerfile` versionné et reproductible.
**Urgences/dangers :** ⚠️ Générer des images de prod avec `commit` produit des "boîtes noires" impossibles à maintenir et à mettre à jour.
**Précautions :** Réserver l'usage de `docker commit` exclusivement aux sessions d'urgence ou de débogage post-mortem.
**Équivalents :** podman commit, nerdctl commit
**Voir aussi :** docker build, docker export, docker diff

## `docker tag` — Taguer une image [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** docker image tag
**Contextes :** préparer une image pour le push sur un registre (GHCR, ECR), numéroter une version de release (`v1.0.0`), créer un alias `latest`
**Rôle :** Attribuer un nouveau nom de dépôt et un tag de version à une image existante sans dupliquer ses données physiques.
**Syntaxe :** `docker tag <image-source>[:tag-source] <image-cible>[:tag-cible]`
**Cas réguliers :**
- `docker tag mon-app:latest ghcr.io/org/mon-app:v1.0.0` — Taguer une image locale pour un registre distant (le plus courant)
- `docker tag mon-app:1.0.2 mon-app:latest` — Faire pointer le tag `latest` vers la version 1.0.2
- `docker tag 8a3f12b mon-reg.domaine.fr/app:latest` — Taguer une image à partir de son ID court
**Origine :** Docker 0.1 (2013) — système de nommage et d'étiquetage par pointeurs symboliques.
**Subtilités/confusions :**
- `docker tag` ne copie PAS les fichiers de l'image : il crée simplement un nouvel alias (pointeur) vers le même Image ID.
- Supprimer un tag avec `docker rmi mon-app:old` ne détruit l'image que s'il s'agissait du dernier tag pointant dessus.
- Le format cible standard pour un push distant est `<registre>/<organisation>/<nom-image>:<tag>`.
**Urgences/dangers :** — (opération de nommage instantanée et sans risque)
**Précautions :** Toujours taguer les images de release avec des numéros de version précis (SemVer) en plus du tag `latest`.
**Équivalents :** podman tag, nerdctl tag
**Voir aussi :** docker push, docker images, docker build

## `docker login` — S'authentifier auprès d'un registre [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 91 | **Aliases :** docker registry login
**Contextes :** se connecter à Docker Hub, s'authentifier sur un registre privé (AWS ECR, GHCR, GitLab Registry) avant de pull/push
**Rôle :** Enregistrer les jetons ou identifiants d'authentification pour un registre d'images conteneurisées dans le fichier de config local.
**Syntaxe :** `docker login [options] [serveur-registre]`
**Cas réguliers :**
- `docker login` — S'authentifier sur Docker Hub de manière interactive (le plus courant)
- `docker login ghcr.io -u nom-user --password-stdin` — S'authentifier de manière sécurisée sur GitHub Container Registry via un jeton
- `aws ecr get-login-password | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com` — Connexion AWS ECR
**Origine :** Docker 0.1 (2013) — gestion des accès sécurisés aux registres distants.
**Subtilités/confusions :**
- Sans argument de serveur, `docker login` cible Docker Hub par défaut (`index.docker.io/v1/`).
- Les identifiants sont stockés par défaut dans `~/.docker/config.json` (préférer un helper de stockage sécurisé comme `secretservice`, `pass` ou `wincred`).
- Passer le mot de passe via l'argument `-p` en ligne de commande est une mauvaise pratique car il apparaît dans l'historique shell.
**Urgences/dangers :** ⚠️ Exécuter `docker login -p "mon_mot_de_passe"` laisse le secret lisible en clair dans l'historique Bash/Zsh (`history`).
**Précautions :** Toujours passer le mot de passe ou jeton via l'entrée standard avec `--password-stdin`.
**Équivalents :** podman login, nerdctl login, crictl login
**Voir aussi :** docker logout, docker push, docker pull

## `docker logout` — Se déconnecter d'un registre [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 75 | **Aliases :** docker registry logout
**Contextes :** fermer sa session sur une machine partagée, supprimer les jetons d'accès enregistrés sur un agent CI/CD
**Rôle :** Supprimer les identifiants d'authentification enregistrés pour un registre Docker spécifique dans le fichier de configuration local.
**Syntaxe :** `docker logout [serveur-registre]`
**Cas réguliers :**
- `docker logout` — Se déconnecter de Docker Hub (le plus courant)
- `docker logout ghcr.io` — Se déconnecter de GitHub Container Registry
**Origine :** Docker 0.1 (2013) — nettoyage des jetons d'accès locaux.
**Subtilités/confusions :**
- Retire la section d'authentification correspondante du fichier `~/.docker/config.json`.
- N'affecte pas les conteneurs en cours d'exécution ni les images déjà téléchargées localement.
**Urgences/dangers :** — (sécurise la machine en retirant les identifiants)
**Précautions :** Exécuter `docker logout` en fin de script de pipeline CI/CD sur les runners partagés.
**Équivalents :** podman logout, nerdctl logout
**Voir aussi :** docker login, docker config

## `docker stats` — Afficher la consommation des ressources [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** docker container stats
**Contextes :** diagnostiquer un conteneur qui consomme 100% de CPU, vérifier la RAM consommée par une base de données, surveiller l'I/O réseau
**Rôle :** Afficher un tableau de bord en direct de la consommation de ressources (CPU, mémoire, limites, E/S disque et réseau) des conteneurs.
**Syntaxe :** `docker stats [options] [conteneur...]`
**Cas réguliers :**
- `docker stats` — Afficher le tableau de bord en temps réel de TOUS les conteneurs actifs (le réflexe diagnostic)
- `docker stats mon-app ma-bdd` — Surveiller uniquement des conteneurs spécifiques
- `docker stats --no-stream` — Afficher un instantané unique des métriques et quitter immédiatement (idéal pour les scripts)
- `docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"` — Formatage personnalisé
**Origine :** Docker 1.5 (2015) — capture des métriques des cgroups Linux en temps réel.
**Subtilités/confusions :**
- La colonne `MEM USAGE / LIMIT` montre la RAM utilisée par rapport au plafond configuré ou à la RAM totale de la machine hôte.
- `CPU %` peut dépasser 100% sur une machine multi-cœurs (200% = 2 cœurs à 100%).
**Urgences/dangers :** — (commande de consultation en lecture seule)
**Précautions :** Utiliser `--no-stream` pour intégrer des vérifications de consommation dans des scripts de monitoring automatisés.
**Équivalents :** kubectl top pods, podman stats, nerdctl stats
**Voir aussi :** docker top, docker ps, docker inspect

## `docker top` — Lister les processus d'un conteneur [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 82 | **Aliases :** docker container top
**Contextes :** vérifier quels processus Unix s'exécutent à l'intérieur d'un conteneur, vérifier le PID hôte d'un service conteneurisé
**Rôle :** Afficher la liste des processus s'exécutant actuellement à l'intérieur du conteneur avec leurs PIDs hôte et utilisateurs.
**Syntaxe :** `docker top <conteneur> [options-ps]`
**Cas réguliers :**
- `docker top mon-app` — Afficher les processus du conteneur (le plus courant)
- `docker top mon-app -aux` — Transmettre des options personnalisées à la commande `ps` sous-jacente
**Origine :** Docker 0.1 (2013) — fait le lien entre les processus isolés du conteneur et le système de processus global de l'hôte.
**Subtilités/confusions :**
- Révèle le fonctionnement des conteneurs Linux : les processus du conteneur sont de vrais processus visibles sur la machine hôte.
- Le PID affiché dans la colonne `PID` est le PID réel de la machine hôte, pas le PID interne au conteneur (PID 1).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Pratique pour identifier le PID hôte d'un conteneur rétif à tuer directement avec `kill -9 <pid-hote>`.
**Équivalents :** podman top, nerdctl top
**Voir aussi :** docker stats, docker exec, ps

## `docker save` — Exporter une image en archive tar [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 80 | **Aliases :** docker image save
**Contextes :** transférer une image Docker sur un serveur isolé du réseau (air-gapped), sauvegarder une image sur clé USB
**Rôle :** Exporter une ou plusieurs images Docker et l'intégralité de leurs couches dans un fichier d'archive au format tar.
**Syntaxe :** `docker save [options] <image>...`
**Cas réguliers :**
- `docker save -o mon-app.tar mon-app:v1.0` — Exporter l'image sous forme de fichier tar (le plus courant)
- `docker save mon-app:v1.0 | gzip > mon-app.tar.gz` — Exporter et compacter directement avec gzip
- `docker save -o images-all.tar app:v1 db:v1` — Exporter plusieurs images dans un seul fichier tar
**Origine :** Docker 0.7 (2013) — outil de portabilité physique d'images hors-réseau.
**Subtilités/confusions :**
- `docker save` conserve les COUCHES et le TAG de l'image (à recharger avec `docker load`).
- Ne pas confondre `docker save` (exporte une IMAGE) et `docker export` (exporte le système de fichiers d'un CONTENEUR).
**Urgences/dangers :** — (lecture seule de l'image source)
**Précautions :** Toujours compacter l'archive avec `gzip` ou `zstd` car le fichier tar brut peut être extrêmement volumineux.
**Équivalents :** podman save, nerdctl save
**Voir aussi :** docker load, docker export, docker import

## `docker load` — Charger une image depuis un fichier tar [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 80 | **Aliases :** docker image load
**Contextes :** importer une image transférée sur clé USB ou serveur privé isolé, restaurer une archive d'image créée par `docker save`
**Rôle :** Charger une image Docker et ses couches de système de fichiers à partir d'un fichier archive tar ou de l'entrée standard.
**Syntaxe :** `docker load [options]`
**Cas réguliers :**
- `docker load -i mon-app.tar` — Importer l'image depuis le fichier archive tar (le plus courant)
- `docker load < mon-app.tar` — Importer via la redirection d'entrée standard
- `gunzip -c mon-app.tar.gz | docker load` — Décompresser et importer une archive gzip directement
**Origine :** Docker 0.7 (2013) — réciproque de `docker save`.
**Subtilités/confusions :**
- Restaure automatiquement le nom de dépôt, le tag et l'ID d'origine de l'image.
- Ne pas confondre `docker load` (restaure une image issue de `docker save`) et `docker import` (crée une image depuis un tar de `docker export`).
**Urgences/dangers :** — (charge les couches dans le cache d'images local)
**Précautions :** Vérifier que l'espace disque de l'hôte est suffisant avant d'importer une lourde archive d'image.
**Équivalents :** podman load, nerdctl load
**Voir aussi :** docker save, docker import, docker images

## `docker export` — Exporter le système de fichiers d'un conteneur [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** docker container export
**Contextes :** exporter la structure d'un conteneur pour analyse forensique, créer une image racine minimale à partir d'un conteneur
**Rôle :** Exporter le contenu complet du système de fichiers d'un conteneur sous la forme d'un fichier d'archive flat tar.
**Syntaxe :** `docker export [options] <conteneur>`
**Cas réguliers :**
- `docker export -o conteneur-flat.tar mon-app` — Exporter le système de fichiers du conteneur dans une archive (le plus courant)
- `docker export mon-app | gzip > conteneur-flat.tar.gz` — Exporter et compacter en gzip
**Origine :** Docker 0.1 (2013) — aplatissement du système de fichiers d'un conteneur.
**Subtilités/confusions :**
- APLATIT (*flatten*) toutes les couches de l'image en un seul système de fichiers uniforme et PERD l'historique des couches Docker ainsi que le Dockerfile d'origine.
- Ne conserve PAS les volumes de données persistantes rattachés au conteneur.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser `docker save` si l'on souhaite préserver l'historique et les couches de l'image d'origine.
**Équivalents :** podman export, nerdctl export
**Voir aussi :** docker import, docker save, docker load

## `docker import` — Importer un système de fichiers sous forme d'image [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 74 | **Aliases :** docker image import
**Contextes :** créer une image d'origine (*base image*) à partir d'un fichier tarball Linux (ex: Alpine, Ubuntu minifié)
**Rôle :** Créer une nouvelle image Docker à une seule couche à partir d'un fichier tarball ou d'un lien de système de fichiers.
**Syntaxe :** `docker import [options] <fichier|URL> [<dépôt>[:tag]]`
**Cas réguliers :**
- `docker import conteneur-flat.tar ma-base:v1` — Créer une image à partir d'une archive tar d'un système de fichiers (le plus courant)
- `cat rootfs.tar.gz | docker import - mon-linux:custom` — Importer directement depuis un flux compressé
- `docker import -c "CMD /bin/sh" rootfs.tar mon-linux:custom` — Définir la commande d'entrée par défaut lors de l'import
**Origine :** Docker 0.1 (2013) — réciproque de `docker export`.
**Subtilités/confusions :**
- Crée une image minimale à UNE SEULE COUCHE.
- Ne restaure pas la configuration d'origine (ENTRYPOINT, ENV, EXPOSE) : il faut les redéfinir avec les options `-c`.
**Urgences/dangers :** — (crée une nouvelle image locale)
**Précautions :** Spécifier les paramètres de démarrage avec `-c` (`ENV`, `CMD`, `EXPOSE`) lors de l'import.
**Équivalents :** podman import, nerdctl import
**Voir aussi :** docker export, docker load, docker save

## `docker buildx` — Construire des images multi-architectures [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 89 | **Aliases :** —
**Contextes :** construire une image compatible à la fois pour PC x86_64 (Intel/AMD) et Mac Apple Silicon / Raspberry Pi (ARM64)
**Rôle :** Exécuter la construction d'images multi-architectures avancées en s'appuyant sur le moteur de build moderne BuildKit.
**Syntaxe :** `docker buildx <build | create | ls | use | inspect| bake>`
**Cas réguliers :**
- `docker buildx build --platform linux/amd64,linux/arm64 -t app:v1 --push .` — Construire et pusher une image universelle pour x86 et ARM64 (le plus courant)
- `docker buildx create --use` — Créer et sélectionner une instance de builder BuildKit personnalisée
- `docker buildx ls` — Lister les instances de builders et les architectures cibles supportées
- `docker buildx bake` — Exécuter des builds complexes définis dans un fichier HCL/JSON/Compose
**Origine :** Docker 19.03 (2019) — extension officielle intégrant le projet BuildKit de nouvelle génération.
**Subtilités/confusions :**
- Nécessite l'option `--push` ou l'utilisation d'un builder conteneurisé pour exporter directement l'index d'images multi-plateformes vers un registre.
- Utilise QEMU sous le capot pour émuler d'autres architectures processeur lors des étapes `RUN` du build.
- Considérablement plus rapide que le `docker build` classique grâce au parallélisme avancé de BuildKit.
**Urgences/dangers :** — (accélère et sécurise les builds)
**Précautions :** Tester les images générées par émulation QEMU sur de vrais processeurs cibles pour vérifier l'absence d'incompatibilités binaires.
**Équivalents :** buildah, img
**Voir aussi :** docker build, docker push, buildkit

## `kubectl get` — Lister les ressources Kubernetes [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** vérifier les pods qui tournent sur le cluster, lister les services exposés, consulter l'état des nœuds
**Rôle :** Afficher sous forme de tableau synoptique la liste d'une ou plusieurs ressources d'un cluster Kubernetes.
**Syntaxe :** `kubectl get <type-ressource> [<nom>] [options]`
**Cas réguliers :**
- `kubectl get pods` — Lister les pods du namespace courant (le plus courant)
- `kubectl get pods -A` — Lister TOUS les pods de TOUS les namespaces du cluster
- `kubectl get deploy,svc,ing` — Lister simultanément les Deployments, Services et Ingress
- `kubectl get pod mon-pod -o yaml` — Extraire la spécification YAML complète de la ressource en direct
**Origine :** Google / Cloud Native Computing Foundation (2014) — l'inspecteur principal du plan de contrôle Kubernetes.
**Subtilités/confusions :**
- Cible le namespace `default` si aucun namespace n'est spécifié : utiliser `-n <namespace>` pour cibler un autre espace.
- L'option `-o wide` ajoute des colonnes essentielles comme l'IP du pod et le nom du nœud hôte.
- Accepte des sélecteurs de labels (`-l app=frontend`) pour filtrer précisément les résultats.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser `-o custom-columns` ou `jsonpath` dans les scripts d'automatisation au lieu de parser le tableau textuel.
**Équivalents :** crictl pods, docker ps, oc get (OpenShift)
**Voir aussi :** kubectl describe, kubectl apply, kubectl logs

## `kubectl apply` — Appliquer une configuration déclarative [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 98 | **Aliases :** —
**Contextes :** déployer une application sur Kubernetes, mettre à jour la configuration d'un service, appliquer des manifests CI/CD
**Rôle :** Créer ou mettre à jour des ressources Kubernetes à partir d'un fichier de manifest déclaratif (YAML ou JSON) ou d'un dossier.
**Syntaxe :** `kubectl apply -f <fichier|dossier>`
**Cas réguliers :**
- `kubectl apply -f deployment.yaml` — Appliquer la configuration d'un fichier YAML (le plus courant)
- `kubectl apply -f k8s/` — Appliquer récursivement tous les manifests YAML d'un répertoire
- `kubectl apply -k ./overlays/production` — Appliquer un dossier Kustomize avec surcouche de production
- `kubectl apply -f https://example.com/app.yaml` — Appliquer directement un manifest distant depuis une URL
**Origine :** Kubernetes 1.2 (2016) — implémente le principe déclaratif Infrastructure as Code (GitOps).
**Subtilités/confusions :**
- `apply` compare la configuration souhaitée (YAML), la dernière appliquée et l'état réel sur le cluster (3-way merge).
- Préférer `apply` (déclaratif) à `create` (impératif) pour la gestion durable de vos environnements.
- Conserve l'annotation `kubectl.kubernetes.io/last-applied-configuration` sur la ressource.
**Urgences/dangers :** ⚠️ Appliquer un manifest YAML comportant une faute de frappe sur la cible d'un namespace peut impacter la production.
**Précautions :** Exécuter `kubectl apply -f manifest.yaml --dry-run=server` pour valider la configuration avant application.
**Équivalents :** helm install/upgrade, oc apply
**Voir aussi :** kubectl delete, kubectl describe, kubectl diff

## `kubectl describe` — Inspecter une ressource en détail [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 96 | **Aliases :** —
**Contextes :** comprendre pourquoi un pod est bloqué en `CrashLoopBackOff` ou `Pending`, consulter les événements récents d'un pod
**Rôle :** Afficher un rapport détaillé et lisible contenant la configuration, les métriques et les ÉVÉNEMENTS récents d'une ressource Kubernetes.
**Syntaxe :** `kubectl describe <type-ressource> [<nom>]`
**Cas réguliers :**
- `kubectl describe pod mon-pod` — Diagnostiquer le statut et les événements d'un pod (le réflexe d'urgence)
- `kubectl describe node worker-1` — Inspecter la capacité, les allocations et l'état de santé d'un nœud
- `kubectl describe ingress web-ingress` — Vérifier les règles de routage HTTP et le statut des backends
**Origine :** Kubernetes 1.0 (2015) — outil d'investigation de premier niveau pour les administrateurs et développeurs.
**Subtilités/confusions :**
- La section finale **Events** contient la clé du problème dans 90% des cas (image introuvable, quota dépassé, manque de RAM/CPU).
- Ne retourne pas du YAML mais un format textuel enrichi conçu pour la lecture humaine.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Si le pod a été supprimé, ses événements disparaissent du describe : consulter alors les logs du plan de contrôle.
**Équivalents :** docker inspect, oc describe
**Voir aussi :** kubectl logs, kubectl get, kubectl events

## `kubectl logs` — Afficher les journaux d'un Pod [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 97 | **Aliases :** —
**Contextes :** consulter les logs de votre application web sur le cluster, déboguer une exception lancée par un pod
**Rôle :** Extraire et afficher les journaux de la sortie standard (STDOUT) et d'erreur (STDERR) des conteneurs d'un pod.
**Syntaxe :** `kubectl logs [options] <pod> [-c <conteneur>]`
**Cas réguliers :**
- `kubectl logs mon-pod` — Afficher l'historique des logs du pod (le plus courant)
- `kubectl logs -f mon-pod` — Suivre les logs du pod en temps réel (mode *follow*)
- `kubectl logs mon-pod -c conteneur-app` — Cibler un conteneur précis dans un pod multi-conteneurs (*sidecar*)
- `kubectl logs mon-pod --previous` — Afficher les logs de l'INSTANCE PRÉCÉDENTE du conteneur avant son dernier plantage
**Origine :** Kubernetes 1.0 (2015) — capture centralisée des flux d'écriture des conteneurs du cluster.
**Subtilités/confusions :**
- Si le pod contient plusieurs conteneurs, `kubectl logs` exige l'option `-c` pour préciser quel conteneur est visé.
- L'option `--previous` est cruciale pour comprendre la cause d'un plantage (`CrashLoopBackOff`) qui a déjà relancé le conteneur.
- On peut filtrer sur tout un Deployment avec `kubectl logs deployment/mon-app --all-containers`.
**Urgences/dangers :** — (lecture seule)
**Précautions :** Utiliser `--tail=100` pour éviter d'inonder le terminal si l'application génère un volume massif de logs.
**Équivalents :** docker logs, stern (outil CLI de tailing multi-pods), oc logs
**Voir aussi :** kubectl describe, kubectl exec, stern

## `kubectl exec` — Exécuter un shell dans un Pod [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 94 | **Aliases :** —
**Contextes :** se connecter directement dans le conteneur d'un pod en production, vérifier la connectivité réseau interne
**Rôle :** Exécuter une commande ou ouvrir un terminal interactif dans un conteneur s'exécutant sur un pod du cluster.
**Syntaxe :** `kubectl exec [options] <pod> [-c <conteneur>] -- <commande> [args]`
**Cas réguliers :**
- `kubectl exec -it mon-pod -- sh` — Ouvrir un shell interactif dans le pod (le réflexe de débogage)
- `kubectl exec mon-pod -- nslookup db-service` — Tester la résolution DNS interne du cluster
- `kubectl exec -it mon-pod -c app-sidecar -- bash` — Cibler un conteneur sidecar précis dans le pod
**Origine :** Kubernetes 1.0 (2015) — accès direct aux espaces de noms du conteneur distant via WebSockets/SPDY.
**Subtilités/confusions :**
- Les tirets `--` sont obligatoires avant la commande pour séparer les arguments de `kubectl` de ceux de la commande distante.
- Requiert les options `-it` pour démarrer une session de terminal interactive.
- Le pod doit être dans l'état `Running` pour accepter un `exec`.
**Urgences/dangers :** ⚠️ Modifier des fichiers à la main dans un pod via `exec` casse l'immutabilité : la modification sera perdue au prochain redémarrage du pod.
**Précautions :** Privilégier des commandes de lecture seule et diagnostiques lors d'un `exec` sur un pod de production.
**Équivalents :** docker exec, podman exec, oc exec
**Voir aussi :** kubectl logs, kubectl port-forward, kubectl run

## `kubectl delete` — Supprimer des ressources Kubernetes [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 93 | **Aliases :** —
**Contextes :** détruire un environnement de recette, forcer le redémarrage d'un pod bloqué, nettoyer des ressources hors service
**Rôle :** Supprimer des ressources du cluster Kubernetes à partir de leur nom, de leur type, de leurs étiquettes ou d'un manifest YAML.
**Syntaxe :** `kubectl delete <type-ressource> [<nom>|--all] | -f <fichier>`
**Cas réguliers :**
- `kubectl delete pod mon-pod` — Supprimer un pod (s'il est géré par un Deployment, Kubernetes en recréera un neuf)
- `kubectl delete -f deployment.yaml` — Supprimer toutes les ressources définies dans un fichier YAML
- `kubectl delete pod -l app=demo` — Supprimer tous les pods portant le label `app=demo`
- `kubectl delete pod mon-pod --grace-period=0 --force` — Forcer la suppression immédiate d'un pod bloqué (à n'utiliser qu'en crise)
**Origine :** Kubernetes 1.0 (2015) — suppression d'objets sur l'API Server.
**Subtilités/confusions :**
- Supprimer un Pod géré par un ReplicaSet/Deployment ne l'efface pas définitivement : le contrôleur en lancera un nouveau pour maintenir la réplique.
- Pour détruire une application complète, supprimer son Deployment (`kubectl delete deployment <nom>`).
**Urgences/dangers :** ⚠️ `kubectl delete ns <namespace>` supprime le namespace ET TOUTES LES RESSOURCES qu'il contient (pods, services, secrets, volumes persistent).
**Précautions :** Vérifier systématiquement le namespace courant (`kubectl config view`) avant d'exécuter un `delete --all`.
**Équivalents :** docker rm, helm uninstall, oc delete
**Voir aussi :** kubectl apply, kubectl get, kubectl scale

## `kubectl port-forward` — Rediriger un port local vers un Pod [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 91 | **Aliases :** —
**Contextes :** accéder à une base de données ou un tableau de bord interne (Grafana/Redis) non exposé sur Internet depuis son PC
**Rôle :** Créer un tunnel de redirection de port sécurisé entre une adresse locale de votre machine et un pod ou service du cluster.
**Syntaxe :** `kubectl port-forward <ressource/nom> <port-local>:<port-distant>`
**Cas réguliers :**
- `kubectl port-forward pod/mon-pod 8080:80` — Transférer le port local 8080 vers le port 80 du pod (le plus courant)
- `kubectl port-forward svc/ma-bdd 5432:5432` — Transférer le port 5432 vers un Service PostgreSQL interne du cluster
- `kubectl port-forward deployment/grafana 3000:3000 -n monitoring` — Cibler un Deployment dans un namespace précis
**Origine :** Kubernetes 1.0 (2015) — tunnel direct pour le développement et le débogage d'infrastructure privée.
**Subtilités/confusions :**
- Le tunnel reste ouvert tant que la commande `kubectl port-forward` s'exécute dans votre terminal.
- Fonctionne au travers d'un canal sécurisé géré par l'API Server sans exiger de modifier les Ingress ou les pare-feu distants.
**Urgences/dangers :** — (le tunnel se ferme dès que la commande est interrompue avec `Ctrl+C`)
**Précautions :** Ne pas utiliser `port-forward` comme solution de routage de trafic de production (réservé au dev et au debug).
**Équivalents :** ssh -L (tunnel SSH), docker run -p
**Voir aussi :** kubectl proxy, kubectl exec, kubectl expose

## `kubectl create` — Créer une ressource de façon impérative [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 89 | **Aliases :** —
**Contextes :** générer un Secret ou un ConfigMap rapidement à la volée, créer un namespace de test
**Rôle :** Créer une ressource Kubernetes de manière impérative depuis la ligne de commande ou générer une ébauche de YAML.
**Syntaxe :** `kubectl create <type-ressource> <nom> [options]`
**Cas réguliers :**
- `kubectl create namespace dev-test` — Créer un nouveau namespace (le plus courant)
- `kubectl create secret generic mes-cles --from-literal=api_key=12345` — Créer un secret à partir d'une valeur littérale
- `kubectl create configmap ma-conf --from-file=config.json` — Créer un ConfigMap depuis un fichier local
- `kubectl create deployment web --image=nginx --dry-run=client -o yaml > deploy.yaml` — Générer un gabarit YAML propre sans l'appliquer
**Origine :** Kubernetes 1.0 (2015) — création impérative directe d'objets sur l'API Server.
**Subtilités/confusions :**
- `create` échoue si la ressource existe déjà (contrairement à `apply` qui la met à jour).
- L'astuce `--dry-run=client -o yaml` est le secret des administrateurs Kubernetes pour générer des fichiers YAML parfaits sans les écrire de zéro.
**Urgences/dangers :** — (crée la ressource spécifiée)
**Précautions :** Pour les environnements suivis en GitOps, utiliser `create --dry-run=client -o yaml` puis commiter le fichier obtenu avant de l'appliquer.
**Équivalents :** docker run, oc create
**Voir aussi :** kubectl apply, kubectl delete, kubectl get

## `kubectl edit` — Éditer une ressource en ligne [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 85 | **Aliases :** —
**Contextes :** corriger rapidement une variable d'environnement sur un pod de dev, tester une modification d'image à chaud
**Rôle :** Télécharger la spécification YAML d'une ressource du cluster, l'ouvrir dans votre éditeur texte local (Vim/Nano), et appliquer les modifications à la sauvegarde.
**Syntaxe :** `kubectl edit <type-ressource> <nom>`
**Cas réguliers :**
- `kubectl edit deployment mon-app` — Éditer le Deployment de l'application en direct (le plus courant)
- `kubectl edit svc mon-service` — Éditer la configuration d'un service (changement de port ou de type)
- `KUBE_EDITOR="code --wait" kubectl edit deployment mon-app` — Ouvrir l'édition dans VS Code
**Origine :** Kubernetes 1.0 (2015) — modification interactive directe des objets de l'API Server.
**Subtilités/confusions :**
- Si le fichier YAML contient des fautes de syntaxe à la sauvegarde, `kubectl edit` rouvre le fichier en signalant l'erreur sans appliquer la casse.
- Toute modification faite avec `edit` est appliquée immédiatement sur le cluster mais N'EST PAS enregistrée dans vos fichiers YAML locaux ni dans Git.
**Urgences/dangers :** ⚠️ Éditer en direct des ressources de production avec `kubectl edit` crée des divergences (*drift*) incontrôlables par rapport à vos dépôts Git (GitOps).
**Précautions :** Réserver `kubectl edit` aux tests d'urgence et reporter immédiatement la modification dans vos fichiers manifests versionnés.
**Équivalents :** oc edit
**Voir aussi :** kubectl apply, kubectl get, KUBE_EDITOR

## `kubectl scale` — Ajuster la capacité d'un Workload [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** absorber un pic de trafic impromptu, passer une application à zéro réplique pour maintenance, tester la montée en charge
**Rôle :** Modifier instantanément le nombre de répliques (instances de pods) d'un Deployment, ReplicaSet ou StatefulSet.
**Syntaxe :** `kubectl scale --replicas=<nombre> <type-ressource>/<nom>`
**Cas réguliers :**
- `kubectl scale --replicas=5 deployment/mon-app` — Augmenter à 5 le nombre d'instances de l'application (le plus courant)
- `kubectl scale --replicas=0 deployment/mon-app` — Couper temporairement tous les pods de l'application (mise à zéro)
- `kubectl scale --current-replicas=2 --replicas=10 deployment/mon-app` — Ajuster à 10 répliques uniquement si l'actuel est de 2
**Origine :** Kubernetes 1.0 (2015) — redimensionnement horizontal manuel (*Horizontal Scaling*).
**Subtilités/confusions :**
- L'ajustement est quasi instantané : le contrôleur crée ou détruit les pods nécessaires pour atteindre la cible souhaitée.
- Si un autoscaler horizontal (HPA - `HorizontalPodAutoscaler`) est actif sur le Deployment, il écrasera la valeur définie par `kubectl scale` lors de sa prochaine boucle.
**Urgences/dangers :** ⚠️ Augmenter massivement le nombre de répliques sans quotas peut épuiser les ressources CPU/RAM des nœuds du cluster.
**Précautions :** Vérifier que les nœuds disposent de la capacité nécessaire (`kubectl top nodes`) avant d'augmenter fortement le nombre de répliques.
**Équivalents :** docker service scale (Swarm), oc scale
**Voir aussi :** kubectl autoscale, kubectl get pods, kubectl top

## `kubectl config` — Administrer la configuration kubeconfig [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 94 | **Aliases :** —
**Contextes :** basculer entre le cluster de dev, de recette et de production, changer de namespace par défaut, vérifier les identifiants
**Rôle :** Consulter, modifier et basculer entre les différents contextes et clusters enregistrés dans le fichier de configuration `~/.kube/config`.
**Syntaxe :** `kubectl config <use-context | get-contexts | current-context | set-context | view>`
**Cas réguliers :**
- `kubectl config get-contexts` — Lister tous les clusters et contextes configurés (le plus courant)
- `kubectl config use-context prod-cluster` — Basculer instantanément sur le cluster de production
- `kubectl config current-context` — Afficher le nom du contexte actuellement actif
- `kubectl config set-context --current --namespace=monitoring` — Définir le namespace par défaut du contexte actif
**Origine :** Kubernetes 1.0 (2015) — gestion multi-clusters et multi-tenants en ligne de commande.
**Subtilités/confusions :**
- Un "contexte" associe 3 éléments : un Cluster (URL), un User (jeton/certificat) et un Namespace par défaut.
- `kubectl config view` masque les secrets et mots de passe par défaut (sauf si `--raw` est spécifié).
- Des extensions CLI comme `kubectx` et `kubens` simplifient considérablement le basculement rapide de contexte et de namespace.
**Urgences/dangers :** ⚠️ Exécuter une commande destrutrice (`kubectl delete`) en croyant être en Dev alors qu'on est sur le contexte de Prod est l'erreur humaine #1 des sysadmins.
**Précautions :** Configurer une invite de commande (prompt shell) affichant toujours le contexte et le namespace actifs (ex: Starship, kube-ps1).
**Équivalents :** oc project / oc config (OpenShift)
**Voir aussi :** kubectl get, kubectx, kubens

## `kubectl rollout` — Gérer les déploiements progressifs [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** suivre la mise à jour d'une application en temps réel, annuler un déploiement défectueux (*rollback*), redémarrer les pods sans coupure
**Rôle :** Contrôler le déroulement des mises à jour progressives (*rolling updates*) des Deployments, StatefulSets et DaemonSets.
**Syntaxe :** `kubectl rollout <status | history | undo | restart | pause | resume>`
**Cas réguliers :**
- `kubectl rollout status deployment/mon-app` — Suivre la progression de la mise à jour des pods en direct (le plus courant)
- `kubectl rollout undo deployment/mon-app` — Annuler immédiatement le dernier déploiement et revenir à la version précédente
- `kubectl rollout restart deployment/mon-app` — Forcer le redémarrage progressif de tous les pods d'un deployment sans interruption de service
- `kubectl rollout history deployment/mon-app` — Afficher l'historique des révisions du deployment
**Origine :** Kubernetes 1.2 (2016) — automatisation des mises à jour sans temps d'arrêt (*zero-downtime deployment*).
**Subtilités/confusions :**
- `kubectl rollout restart` est le moyen propre et officiel d'appliquer de nouvelles variables de ConfigMap/Secret à vos pods.
- `rollout undo` revient à la révision précédente (`revision=N-1`) enregistrée dans le ReplicaSet.
**Urgences/dangers :** — (permet au contraire de sortir d'une crise de déploiement en quelques secondes)
**Précautions :** Vérifier `kubectl rollout status` dans vos scripts de CI/CD pour faire échouer le pipeline si les nouveaux pods ne démarrent pas.
**Équivalents :** helm rollback, oc rollout
**Voir aussi :** kubectl scale, kubectl apply, kubectl get

## `kubectl top` — Afficher les métriques de consommation [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 92 | **Aliases :** —
**Contextes :** identifier quel pod consomme trop de CPU/RAM, vérifier la charge globale des nœuds du cluster
**Rôle :** Afficher en temps réel la consommation actuelle de processeur (CPU) et de mémoire (RAM) des pods ou des nœuds du cluster.
**Syntaxe :** `kubectl top <node|pod> [options]`
**Cas réguliers :**
- `kubectl top pods` — Lister la consommation des pods du namespace courant (le plus courant)
- `kubectl top nodes` — Afficher la consommation CPU/RAM de chaque nœud physique ou virtuel du cluster
- `kubectl top pods -A --sort-by=memory` — Afficher tous les pods du cluster triés par consommation de mémoire décroissante
- `kubectl top pod mon-pod --containers` — Afficher la consommation détaillée conteneur par conteneur à l'intérieur du pod
**Origine :** Kubernetes 1.8 (2017) — s'appuie sur le serveur de métriques officiel (*Metrics Server*).
**Subtilités/confusions :**
- Nécessite impérativement que le composant `metrics-server` soit installé et actif sur le cluster Kubernetes.
- Les valeurs CPU sont exprimées en millicœurs (`100m` = 10% d'un cœur CPU) et la mémoire en Mébioctets (`Mi`).
**Urgences/dangers :** — (lecture seule)
**Précautions :** Si la commande retourne `error: Metrics API not available`, installer `metrics-server` sur le cluster.
**Équivalents :** docker stats, podman stats, crictl stats
**Voir aussi :** kubectl describe node, kubectl get, metrics-server

## `kubectl cp` — Copier des fichiers avec un Pod [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 86 | **Aliases :** —
**Contextes :** récupérer un fichier de dump de base de données depuis un pod distant, envoyer une archive de test dans un pod
**Rôle :** Copier des fichiers et répertoires entre un pod s'exécutant sur le cluster et votre machine locale.
**Syntaxe :** `kubectl cp <source> <destination> [-c <conteneur>]`
**Cas réguliers :**
- `kubectl cp mon-pod:/var/log/app.log ./app.log` — Télécharger un fichier du pod vers la machine locale (le plus courant)
- `kubectl cp ./dump.sql mon-pod:/tmp/dump.sql` — Envoyer un fichier local vers le pod distant
- `kubectl cp mon-pod:/var/www/ ./backup/ -c web` — Copier tout un dossier depuis un conteneur spécifique du pod
**Origine :** Kubernetes 1.4 (2016) — transfert de fichiers basé sur un stream d'archive tar via le canal `exec`.
**Subtilités/confusions :**
- Exige que la commande `tar` soit présente à l'intérieur du conteneur cible du pod pour fonctionner.
- La syntaxe impose d'indiquer d'abord le pod suivi de deux points `<pod>:<chemin>`.
- Les fichiers copiés directement dans le pod disparaîtront si le pod est détruit ou recréé.
**Urgences/dangers :** — (écrase le fichier destination sans avertissement)
**Précautions :** Pour les données persistantes, utiliser des montages de volumes `PersistentVolumeClaim` au lieu de copies manuelles.
**Équivalents :** docker cp, podman cp, scp
**Voir aussi :** kubectl exec, kubectl logs

## `kubectl run` — Lancer un Pod individuel éphémère [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 91 | **Aliases :** —
**Contextes :** lancer un pod de test réseau (curl/dnsutils) temporaire, tester une image de conteneur rapidement sur le cluster
**Rôle :** Créer et exécuter un Pod individuel simple sur le cluster directement depuis la ligne de commande.
**Syntaxe :** `kubectl run <nom> --image=<image> [options] [-- <commande> [args]]`
**Cas réguliers :**
- `kubectl run test-net -it --rm --image=busybox -- sh` — Lancer un pod de test interactif détruit automatiquement à la sortie (`--rm`)
- `kubectl run tmp-curl --image=curlimages/curl -- curl -s http://mon-service` — Tester une requête HTTP interne au cluster
- `kubectl run mon-app --image=nginx:alpine --port=80` — Lancer un pod Nginx simple écoutant sur le port 80
**Origine :** Kubernetes 1.0 (2015) — commande impérative inspirée de `docker run`.
**Subtilités/confusions :**
- `kubectl run` crée désormais un simple **Pod**, et NON PLUS un Deployment (changement majeur depuis Kubernetes 1.18).
- L'option `--rm` garantit que le pod de test sera immédiatement nettoyé sur le cluster dès la fin de son exécution.
**Urgences/dangers :** — (idéal pour les sessions de diagnostic éphémères)
**Précautions :** Pour les applications durables de production, utiliser `kubectl apply -f` avec un Deployment au lieu de `kubectl run`.
**Équivalents :** docker run, podman run
**Voir aussi :** kubectl create, kubectl exec, kubectl delete

## `kubectl expose` — Exposer un Pod ou Deployment sous forme de Service [Linux/macOS/Windows]
**Niveau :** debutant | **Popularité :** 88 | **Aliases :** —
**Contextes :** créer un point d'accès réseau interne (ClusterIP) ou externe (NodePort/LoadBalancer) pour une application
**Rôle :** Prendre une ressource existante (Pod, Deployment, ReplicaSet) et créer automatiquement un Service Kubernetes pour équilibrer le trafic vers elle.
**Syntaxe :** `kubectl expose <type-ressource> <nom> [--port=<port>] [--target-port=<port>] [--type=<Type>]`
**Cas réguliers :**
- `kubectl expose deployment mon-app --port=80 --target-port=8080` — Exposer le deployment en interne sur le port 80 (ClusterIP)
- `kubectl expose deployment web --type=NodePort --port=80` — Exposer sur un port élevé de chaque nœud du cluster
- `kubectl expose deployment web --type=LoadBalancer --port=80` — Solliciter un Load Balancer Cloud (AWS/GCP/Azure)
**Origine :** Kubernetes 1.0 (2015) — génération automatique de la couche de routage de service (Service Discovery).
**Subtilités/confusions :**
- `--port` est le port exposé par le Service Kubernetes ; `--target-port` est le port sur lequel l'application écoute à l'intérieur du conteneur.
- Types de services disponibles : `ClusterIP` (interne par défaut), `NodePort` (port hôte 30000-32767), `LoadBalancer` (Cloud), `ExternalName`.
**Urgences/dangers :** ⚠️ Exposer un service avec `--type=LoadBalancer` sur un cluster Cloud public crée une IP publique immédiatement accessible sur Internet.
**Précautions :** Restreindre les accès réseau aux services sensibles en utilisant `ClusterIP` combiné à des politiques réseau (`NetworkPolicy`).
**Équivalents :** docker run -p (au niveau conteneur), oc expose
**Voir aussi :** kubectl get svc, kubectl apply, kubectl port-forward

## `helm` — Gestionnaire de paquets Kubernetes [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 95 | **Aliases :** —
**Contextes :** installer des applications complexes prêt-à-l'emploi (Prometheus, Grafana, NGINX Ingress, PostgreSQL) sur Kubernetes
**Rôle :** Définir, installer, mettre à jour et gérer le cycle de vie d'applications Kubernetes complètes empaquetées sous forme de *Charts Helm*.
**Syntaxe :** `helm <install | upgrade | uninstall | list | repo | search | template>`
**Cas réguliers :**
- `helm repo add bitnami https://charts.bitnami.com/bitnami` — Ajouter un dépôt de charts Helm distant (le plus courant)
- `helm install ma-bdd bitnami/postgresql` — Déployer une base PostgreSQL complète avec ses paramètres par défaut
- `helm upgrade --install mon-app ./chart-local -f values-prod.yaml` — Déployer ou mettre à jour un chart avec surcouche de valeurs
- `helm list -A` — Lister toutes les applications Helm installées sur le cluster
**Origine :** Deis / CNCF (2015) — l'équivalent de `apt` ou `brew` pour l'écosystème Kubernetes.
**Subtilités/confusions :**
- Helm v3 (actuel) fonctionne 100% côté client sans composant serveur lourd (suppression de Tiller).
- Un *Chart* contient des gabarits YAML paramétrés par un fichier central `values.yaml`.
- Permet l'annulation facile d'une livraison défectueuse avec `helm rollback <release> <revision>`.
**Urgences/dangers :** ⚠️ `helm uninstall <release>` supprime toutes les ressources rattachées au chart, y compris les volumes persistent selon les règles définies.
**Précautions :** Toujours vérifier le résultat d'un chart avant déploiement en exécutant `helm template ./chart` ou `--dry-run`.
**Équivalents :** Kustomize, Carvel ytt, Operator Framework
**Voir aussi :** kubectl apply, kubectl get, kustomize

## `podman` — Moteur de conteneurs sans démon et sans root [Linux/macOS/Windows]
**Niveau :** intermediaire | **Popularité :** 90 | **Aliases :** —
**Contextes :** exécuter des conteneurs en toute sécurité sans privilèges root, remplacer Docker par un outil compatible sans démon
**Rôle :** Développer, gérer et exécuter des conteneurs et pods OCI sans nécessiter de démon en arrière-plan et en mode non-root (*Rootless*).
**Syntaxe :** `podman <run | ps | build | images | stop | rm | generate kube>` (100% compatible CLI Docker)
**Cas réguliers :**
- `podman run -d -p 8080:80 nginx` — Lancer un conteneur exactement comme avec la commande `docker run` (le plus courant)
- `podman pod create --name mon-pod -p 8080:80` — Créer un Pod local regroupant plusieurs conteneurs (concept Kubernetes local)
- `podman generate kube mon-pod > pod.yaml` — Générer un manifest Kubernetes YAML à partir d'un pod Podman local !
- `alias docker=podman` — Remplacer Docker en toute transparence dans vos scripts shell
**Origine :** Red Hat / Podman Project (2018) — conçu pour éliminer le SPOF (*Single Point of Failure*) du démon Docker root.
**Subtilités/confusions :**
- N'a AUCUN DÉMON permanent en arrière-plan : chaque conteneur est simplement un processus fils direct du processus Podman.
- Le mode *Rootless* permet aux utilisateurs standards non-root de lancer des conteneurs sans aucun privilège d'administration sudo.
- Gère nativement la notion de **Pod** (groupe de conteneurs partageant la même adresse IP et le même réseau), comme Kubernetes.
**Urgences/dangers :** — (considérablement plus sécurisé que Docker grâce à l'absence de privilèges root)
**Précautions :** En mode rootless, les ports d'écoute inférieurs à 1024 (ex: 80, 443) exigent d'ajuster `net.ipv4.ip_unprivileged_port_start`.
**Équivalents :** docker, nerdctl, buildah
**Voir aussi :** buildah, skopeo, docker

## `nerdctl` — CLI Docker-compatible pour containerd [Linux/macOS/Windows]
**Niveau :** avance | **Popularité :** 82 | **Aliases :** —
**Contextes :** manipuler directement le runtime `containerd` de Kubernetes (Rancher Desktop, Lima, k3s), utiliser le chiffrement d'images
**Rôle :** Proposer une interface en ligne de commande ultra-compatible avec Docker CLI pour administrer le moteur de conteneurs `containerd`.
**Syntaxe :** `nerdctl <run | ps | build | images | compose | ipfs>`
**Cas réguliers :**
- `nerdctl run -d -p 8080:80 nginx:alpine` — Lancer un conteneur sur containerd avec la même syntaxe que Docker
- `nerdctl --namespace k8s.io ps` — Inspecter les conteneurs s'exécutant à l'intérieur d'un cluster Kubernetes local
- `nerdctl compose up -d` — Démarrer des stacks Docker Compose directement sur containerd
- `nerdctl run --gpus all nvidia/cuda` — Prise en charge native de l'accélération GPU
**Origine :** containerd Project / CNCF (2020) — créé pour offrir une expérience développeur type Docker CLI au-dessus de containerd.
**Subtilités/confusions :**
- Interagit directement avec les espaces de noms de `containerd` (ex: `k8s.io` pour Kubernetes ou `default` pour dev local).
- Supporte des fonctionnalités avant-gardistes comme le chargement d'images via IPFS, le chiffrement d'images et la paresse de démarrage (*lazy-pulling* avec Starlight/nydus).
**Urgences/dangers :** — (alternative moderne et légère)
**Précautions :** Utiliser le drapeau `--namespace k8s.io` pour voir les conteneurs gérés par Kubernetes sur le même nœud.
**Équivalents :** docker, podman, crictl
**Voir aussi :** containerd, crictl, docker

## `crictl` — CLI d'inspection pour l'interface CRI [Linux/macOS/Windows]
**Niveau :** expert | **Popularité :** 78 | **Aliases :** —
**Contextes :** déboguer un nœud Kubernetes en panne au niveau du runtime de conteneur (containerd/CRIO) sans passer par le kubelet
**Rôle :** Interagir directement avec le runtime de conteneurs d'un nœud Kubernetes via l'interface standard CRI (*Container Runtime Interface*).
**Syntaxe :** `crictl <pods | ps | images | logs | exec | inspectp | stats>`
**Cas réguliers :**
- `crictl pods` — Lister les pods s'exécutant sur le nœud local au niveau du runtime (le réflexe d'urgence sysadmin)
- `crictl ps` — Lister tous les conteneurs de niveau bas actifs sur le nœud
- `crictl logs <container-id>` — Consulter les logs directs d'un conteneur lorsque `kubectl logs` ne répond plus
- `crictl inspectp <pod-id>` — Inspecter le bac à sable (*sandbox*) d'un pod Kubernetes au niveau du noyau
**Origine :** Kubernetes SIG-Node / CNCF (2017) — conçu comme l'outil de diagnostic de bas niveau officiel pour les nœuds Kubernetes.
**Subtilités/confusions :**
- `crictl` est conçu pour les ADMINISTRATEURS DE NŒUDS : il s'exécute directement en SSH sur la machine hôte du nœud Kubernetes.
- Ne passe PAS par le serveur d'API Kubernetes : il parle directement au socket du runtime (`/run/containerd/containerd.sock` ou `/run/crio/crio.sock`).
- Ne pas utiliser `crictl` pour créer des conteneurs de prod : Kubernetes ne serait pas au courant des modifications apportées dans son dos.
**Urgences/dangers :** ⚠️ Supprimer un conteneur avec `crictl rm` sur un nœud actif perturbe la boucle de réconciliation du kubelet.
**Précautions :** Réservé exclusivement au débogage post-mortem ou d'urgence lorsque l'API Server de Kubernetes est inaccessible.
**Équivalents :** nerdctl, podman, docker
**Voir aussi :** kubectl logs, containerd, kubelet



