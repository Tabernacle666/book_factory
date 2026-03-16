---
id: "06"
title: "Repenser un projet de développement informatique"
parent: null
level: chapter
status: draft
owner_concept: "repenser-un-projet"
summary: >
  Ce chapitre transforme le projet logiciel en système de décisions, d'interfaces,
  de validations et de livrables. Il prépare le découpage propre du travail au lieu
  de laisser les agents dériver dans un flux continu.
sections:
  - "06.01"
  - "06.02"
  - "06.03"
---

# Repenser un projet de développement informatique

## Thèse du chapitre
Le changement de posture introduit par les LLM ne suffit pas. Une fois admis que la valeur se déplace du geste direct vers le cadrage, encore faut-il disposer d'une forme de projet compatible avec cette nouvelle réalité. Or beaucoup d'équipes continuent à traiter le développement comme un flux continu de fabrication : on avance, on ajoute, on corrige, on discute, puis on espère que la cohérence émergera. Cette vision était déjà fragile avec des humains seuls ; elle devient franchement coûteuse avec des agents, parce qu'elle délègue implicitement aux couches d'exécution des décisions qui auraient dû être rendues explicites plus haut.

Ce chapitre propose donc une rupture nette : un projet n'est pas d'abord une masse de tâches, mais une **hiérarchie de décisions**, d'interfaces, de validations et de livrables. Tant que cette hiérarchie n'est pas visible, la délégation reste floue, les sorties sont difficiles à intégrer et la responsabilité s'évapore dans la continuité apparente du travail.

## Pourquoi ce chapitre existe
Le chapitre précédent expliquait pourquoi le professionnel doit remonter d'un niveau de responsabilité. Celui-ci montre maintenant ce que cette montée implique sur l'objet même que l'on pilote. Repenser un projet, ici, ne veut pas dire adopter un nouveau jargon de gestion ou remplacer la technique par de l'organisation abstraite. Cela veut dire rendre explicites les points où se prennent les vraies décisions, les endroits où les acteurs se rencontrent, les preuves minimales qu'une sortie est acceptable, et la forme sous laquelle un morceau de travail devient réellement intégrable.

Ce chapitre existe donc pour convertir une intuition de posture en architecture de travail. Sans lui, la suite du livre risquerait d'être lue comme une collection de bonnes pratiques séparées : découpage, contrats, contexte, prompts, validation. Avec lui, ces éléments apparaissent comme les conséquences d'une même idée : un projet bien piloté n'est pas un courant continu, mais un système de nœuds explicites où chaque contribution a une portée, un format, une preuve et une place.

## Ce que le lecteur doit comprendre en sortant
À la fin de ce chapitre, le lecteur doit pouvoir tenir ensemble six idées :
- un projet mal cadré dérive moins par manque d'effort que par manque de structure de décision ;
- demander à un agent de “faire avancer le projet” est presque toujours trop vague pour produire une progression fiable ;
- faire faire proprement suppose de transformer une intention globale en unités locales, chacune avec des intrants, une sortie attendue et une validation ;
- les interfaces ne servent pas seulement à connecter du code : elles servent aussi à stabiliser la collaboration ;
- un livrable n'est pas un document administratif de plus, mais la forme concrète sous laquelle une décision ou une production devient vérifiable et transmissible ;
- la qualité de la suite dépendra du découpage, et le découpage dépend d'abord de cette relecture du projet.

## Sections
- [Projet continu ou hiérarchie de décisions](01-Projet-continu-ou-hiérarchie-de-décisions.md)
- [Du faire au faire faire proprement](02-Du-faire-au-faire-faire-proprement.md)
- [Interfaces, validations et livrables](03-Interfaces,-validations-et-livrables.md)

## Place dans la progression du livre
Le chapitre 5 déplaçait la posture du professionnel. Le chapitre 6 déplace maintenant la forme du projet. C'est une transition décisive : on quitte le terrain de l'identité et du repositionnement pour entrer dans celui des structures opératoires. Une fois le projet reconstruit comme hiérarchie de décisions et de livrables, le livre peut passer au chapitre suivant, qui traite du découpage lui-même. Ce passage est important : on ne découpe pas proprement un projet tant qu'on le voit encore comme un bloc continu.

## Erreur de lecture à éviter
Il ne faut pas lire ce chapitre comme un plaidoyer pour "plus de process" au sens bureaucratique. Le propos est inverse. Il s'agit de rendre le projet plus léger à piloter en rendant explicites seulement les points qui conditionnent l'autonomie locale : qui décide quoi, quelle sortie compte réellement, comment on la valide, et ce qu'un autre acteur peut reprendre sans réinventer le contexte. La formalisation utile réduit la friction ; la formalisation décorative l'augmente.

## Passage explicite au chapitre suivant
Une fois le projet reconstruit comme hiérarchie de décisions et de livrables, une question devient immédiatement concrète : **où couper** pour déléguer sans diluer la responsabilité. Le chapitre 7 prend donc le relais sur le terrain du découpage. Il ne change pas de sujet ; il applique la forme nouvelle du projet à l'unité réelle de travail.

## Renvois utiles
- [Le nailgun et le changement de posture](../05-nailgun-et-changement-de-posture/chapitre.md)
- [Scinder le travail proprement](../07-decoupage-du-travail/chapitre.md)
- [Maintenir une collaboration orthogonale](../08-collaboration-orthogonale/chapitre.md)
- [Limiter les hallucinations et maintenir la validation](../10-hallucinations-et-validation/chapitre.md)
