---
id: "07"
title: "Scinder le travail proprement"
parent: null
level: chapter
status: draft
owner_concept: "decoupage-du-travail"
summary: >
  Ce chapitre montre comment transformer un projet bien recadré en unités de travail
  réellement délégables, intégrables et vérifiables. Il prépare la collaboration
  orthogonale en imposant un découpage par responsabilité, interface et validation.
sections:
  - "07.01"
  - "07.02"
  - "07.03"
---

# Scinder le travail proprement

## Thèse du chapitre
Une fois le projet repensé comme hiérarchie de décisions, d'interfaces, de validations et de livrables, il reste la question la plus opératoire de toutes : **où couper**. Beaucoup d'échecs attribués aux agents viennent en réalité d'un mauvais découpage. On délègue des blocs trop larges, des responsabilités entremêlées, des objectifs mal bornés ou des tâches impossibles à valider localement. Le problème n'est alors ni la bonne volonté, ni la puissance du modèle, mais l'absence d'une unité de travail exploitable.

Ce chapitre défend une idée simple : on ne découpe pas proprement selon le confort narratif du projet, mais selon ce qui peut être confié, contrôlé, repris et intégré sans ambiguïté. Autrement dit, un bon découpage réduit les zones floues avant même de produire quoi que ce soit. Il donne à chaque acteur un périmètre lisible, des intrants bornés, une sortie attendue, et surtout une manière de savoir si le morceau livré est acceptable.

## Pourquoi ce chapitre existe
Le chapitre précédent reconstruisait le projet comme une architecture de décisions. Celui-ci traduit cette architecture en unités locales de travail. C'est une étape décisive, parce qu'un projet bien pensé peut encore échouer s'il est distribué sous une forme impropre. Une équipe hybride humain+IA ne devient pas robuste parce qu'elle dispose de plus de capacité d'exécution ; elle le devient quand cette capacité est canalisée dans des morceaux assez nets pour être validés indépendamment puis recomposés.

Ce chapitre existe donc pour faire le pont entre la forme générale du projet et la coopération concrète. Il prépare non seulement la collaboration orthogonale du chapitre suivant, mais aussi tout ce qui viendra ensuite : pilotage d'agents, validation, gestion du contexte, couches de prompt, quanta courts. Sans un découpage propre, toutes ces disciplines arrivent trop tard et servent seulement à limiter des dégâts déjà installés.

## Ce que le lecteur doit comprendre en sortant
À la fin de ce chapitre, le lecteur doit pouvoir tenir ensemble six idées :
- un bon découpage ne suit pas seulement les composants techniques ; il suit aussi les responsabilités et les preuves attendues ;
- une tâche mal découpée force les acteurs à interpréter, négocier ou réinventer des frontières qui auraient dû être explicites ;
- une interface utile ne sépare pas seulement deux modules : elle stabilise aussi la collaboration entre deux producteurs ;
- une unité de travail n'est propre que si elle peut être validée localement avant intégration ;
- plus la validation d'un morceau dépend d'un grand contexte implicite, plus le découpage est suspect ;
- le but n'est pas de morceler artificiellement, mais de produire des morceaux assez petits pour être gouvernables et assez complets pour être utiles.

## Sections
- [Découpage par responsabilité](01-Découpage-par-responsabilité.md)
- [Découpage par interface](02-Découpage-par-interface.md)
- [Découpage par capacité de validation](03-Découpage-par-capacité-de-validation.md)

## Place dans la progression du livre
Le chapitre 6 redéfinissait ce qu'est un projet. Le chapitre 7 montre maintenant comment en dériver des unités d'action concrètes. C'est le moment où l'architecture générale devient une mécanique de travail. Cette transition est essentielle : tant que le découpage reste flou, la collaboration crée du recouvrement, le pilotage devient bavard, la validation arrive trop tard et le contexte gonfle inutilement. Une fois les coupes mieux placées, le livre peut avancer vers le chapitre 8, qui traite de la collaboration sans recouvrement et des contrats stables entre acteurs.

## Erreur de lecture à éviter
Il ne faut pas lire ce chapitre comme une défense du micro-découpage systématique. Couper trop fin peut être presque aussi mauvais que couper trop large : on fragmente le sens, on multiplie les interfaces et on transforme la coordination en coût dominant. Le bon découpage n'est ni maximaliste ni minimaliste ; il cherche le point où une unité devient assez autonome pour être validée localement, sans perdre la cohérence de ce qu'elle sert.

## Passage explicite au chapitre suivant
Le chapitre 7 établit ainsi des unités de travail délégables et validables. Mais ces unités peuvent encore se gêner ou se recouvrir si leurs raccords restent implicites. Le chapitre 8 prend donc le relais pour montrer comment faire coexister ces morceaux sans refaire entrer le flou par la coordination elle-même.

## Renvois utiles
- [Repenser un projet de développement informatique](../06-repenser-un-projet/chapitre.md)
- [Maintenir une collaboration orthogonale](../08-collaboration-orthogonale/chapitre.md)
- [Piloter des collègues IA](../09-pilotage-agents/chapitre.md)
- [Limiter les hallucinations et maintenir la validation](../10-hallucinations-et-validation/chapitre.md)
