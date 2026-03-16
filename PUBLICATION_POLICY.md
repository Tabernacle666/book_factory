# PUBLICATION_POLICY.md

Ce dépôt a maintenant **deux rendus** distincts, mais ils doivent rester **presque isomorphes**.

## 1. Édition de travail

Visible pour les rédacteurs et les agents.

Elle contient :
- le manuscrit complet ;
- la structure pédagogique ;
- les repères de type `Idée centrale`, `Pourquoi c'est important`, `Erreur classique`, `Méthode concrète` quand ils servent la rédaction ;
- les placeholders de contenu ;
- les marqueurs éditoriaux ;
- les traces utiles à la coordination.

Fichiers générés :
- `output/cours-travail.pdf`
- `output/cours-travail.html`
- `output/cours-travail-merge.md`

## 2. Édition publication

Visible pour un lecteur final.

Elle doit contenir **la même matière utile au lecteur** que l'édition de travail, y compris la structure pédagogique quand elle aide réellement la lecture.

Elle ne doit pas montrer :
- les placeholders structurés ;
- les consignes du type « ce nœud doit » ;
- les journaux de fabrication ;
- les statuts, queues, release notes et marqueurs de collaboration ;
- les balises éditoriales brutes (`[[...]]`).

Elle doit conserver :
- les titres et sous-titres utiles au lecteur ;
- les transitions ;
- les explications pédagogiques ;
- les exemples ;
- les analogies ;
- les encadrés destinés au lecteur.

Fichiers générés :
- `output/livre-publication.pdf`
- `output/livre-publication.html`
- `output/livre-publication-merge.md`

## Règle de séparation

La source de vérité reste l'arborescence Markdown. Le PDF public n'est pas une source, seulement un artefact de build.

## Règle d'écart acceptable

La publication ne doit pas devenir une version abrégée du livre.
L'écart attendu entre travail et publication est **faible** et provient surtout de la disparition de la cuisine interne.

## Marqueurs éditoriaux autorisés dans la source

Pour enrichir le livre sans casser la structure, utiliser uniquement ces marqueurs :
- `[[EDITORIAL: ...]]`
- `[[CITATION: ...]]`
- `[[BLAGUE: ...]]`
- `[[FIGURE: ...]]`
- `[[INSERT: ...]]`

Ces marqueurs peuvent rester visibles dans l'édition de travail. Ils sont retirés du rendu publication.


## Ce qui peut disparaître sans perte pour le lecteur

Relèvent de la cuisine interne et peuvent être retirés du rendu publication :
- les placeholders et leurs checklists de rédaction ;
- les sections de navigation interne du type `Sections` ou `Sections du chapitre` quand elles ne font que lister des fichiers qui seront développés juste après ;
- les liens markdown locaux vers des fichiers source (`*.md`) ;
- les statuts, files d'attente, release notes, renvois de fabrication et balises de collaboration.

## Ce qui doit rester visible dans la publication

Relèvent de la matière utile au lecteur et doivent rester visibles :
- les intertitres pédagogiques qui structurent la compréhension (`Thèse du chapitre`, `Pourquoi ce chapitre existe`, `Erreur de lecture à éviter`, `Mini exemple`, `Règle pratique`) ;
- les transitions entre chapitres et entre sections quand elles éclairent la progression du livre ;
- les analogies, exemples, encadrés et notes destinées au lecteur.

## Règle d'écart opérationnelle

L'écart entre travail et publication doit rester faible et justifiable.
Au cours de ce lot, il est considéré sain si la différence provient surtout :
- de la disparition de la méta de fabrication ;
- des placeholders encore non rédigés ;
- des parties explicitement gelées pour délégation humaine.

À l'inverse, une baisse de volume provoquée par la suppression d'intertitres utiles, d'exemples, de transitions ou d'explications doit être traitée comme une régression.


## Exception stratégique : chapitre 13

Le chapitre 13 ne doit pas être conservé artificiellement pour protéger la pagination ou la continuité apparente.
Si sa logique est fausse, la bonne stratégie éditoriale est la destruction contrôlée puis la recréation.


## Réservoir facultatif de voix auteur

`faculta_boss.md` peut nourrir la publication, mais aucune entrée n'est intégrée automatiquement. Une quote ou note d'auteur n'entre dans le livre que si elle renforce un passage précis et laisse une trace d'intégration pour éviter les doublons.


## Décision v56

L'information de cadrage est désormais jugée suffisante.
Les prochains lots sont autorisés à optimiser la forme, la structure, la prose, les transitions et la mise en scène éditoriale, tant que la matière utile au lecteur reste présente dans la publication.
