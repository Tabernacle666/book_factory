# Conventions éditoriales et protocole de contribution

## Principe directeur

Chaque fichier doit **maximiser sa clarté locale** et **minimiser son recouvrement global**.

## Rôle des niveaux

- `main.md` : navigation globale, cadrage du cours
- `chapitre.md` : carte locale d'un chapitre, thèse, sections, renvois
- `*.md` d'un niveau inférieur : développement d'un point unique

## Propriété conceptuelle

Chaque concept important doit avoir un **fichier propriétaire**.

Règle :
- le fichier propriétaire développe le concept en profondeur
- les autres fichiers peuvent le mentionner brièvement
- les autres fichiers doivent renvoyer vers le propriétaire au lieu de le redévelopper

## Périmètre d'un agent rédacteur

Un agent travaille sur **un seul nœud à la fois**.

Contexte autorisé :
- le fichier cible
- son parent immédiat
- éventuellement ses sections sœurs

Contexte interdit par défaut :
- le reste du dépôt si cela n'est pas nécessaire
- la réécriture du plan global
- la refonte opportuniste de plusieurs fichiers

## Obligations d'une contribution

1. modifier uniquement le fichier cible
2. respecter le rôle du fichier dans l'arborescence
3. ne pas dupliquer le contenu des fichiers voisins
4. signaler brièvement les renvois utiles
5. garder le texte dense, clair, sobre, sans remplissage
6. produire un **change log court** séparé du texte pédagogique

## Interdits

- duplication de fond
- inflation verbale
- digression historique dans un fichier pratique
- digression pratique dans un fichier purement historique si non pertinente
- changement de ton global sans mandat
- renommage de fichiers sans justification explicite
- création de nouveaux fichiers sans instruction

## Structure rédactionnelle par défaut pour une section

1. idée centrale
2. pourquoi c'est important
3. erreur classique
4. méthode concrète
5. mini exemple
6. règle pratique
7. renvoi éventuel

## Style

- français clair et dense
- peu de phrases décoratives
- pas de marketing
- pas de promesses floues
- définitions nettes
- exemples courts
- transitions sobres

## Signaler le travail sans alourdir

Toute contribution doit inclure un change log séparé avec :
- objectif
- ajouté
- évité
- renvois
- statut

## Politique de modification locale

L'agent peut :
- enrichir le fichier cible
- proposer des impacts ailleurs en note courte

L'agent ne peut pas :
- modifier d'autres fichiers sans instruction
- déplacer un concept propriétaire
- fusionner des chapitres
- casser la granularité existante


## Métadonnées de release et de relais

Toute nouvelle release doit :
- conserver `CHANGELOG.md`
- conserver `RELEASES.md`
- mettre à jour `RELEASE_STATE.yaml`
- ne jamais supprimer l'historique des releases antérieures
- laisser `README.md` comme point d'entrée principal pour le prochain rédacteur

Toute contribution locale doit :
- mettre à jour le fichier cible
- laisser une trace courte dans `CHANGELOG.md`
- ajuster `QUEUE.md` si le prochain pas change
