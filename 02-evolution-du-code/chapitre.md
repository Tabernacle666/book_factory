---
id: "02"
title: "Évolution historique du code"
parent: null
level: chapter
status: draft
owner_concept: "evolution-du-code"
summary: >
  Ce chapitre retrace le déplacement progressif de la valeur technique, depuis la
  fabrication manuelle du code vers l'abstraction, la réutilisation et
  l'intégration de briques existantes.
sections:
  - "02.01"
  - "02.02"
  - "02.03"
---

# Évolution historique du code

Le chapitre précédent montrait que le métier de codeur ne peut pas être compris comme une essence immobile. Celui-ci prolonge cette idée sur le plan technique: **la valeur ne s'est jamais contentée de rester dans l'écriture brute du code**. L'histoire du développement est une histoire de compression de la friction. À chaque étape, une partie du travail pénible, répétitif ou trop bas niveau a été absorbée par des couches d'abstraction plus puissantes. Cette dynamique n'a pas supprimé la compétence. Elle a déplacé le lieu où cette compétence compte le plus.

L'enjeu du chapitre est donc de corriger une illusion fréquente: croire que plus on s'éloigne du bas niveau, moins on travaille vraiment. En réalité, l'élévation du niveau d'abstraction change surtout la nature de la responsabilité. On écrit souvent moins d'instructions élémentaires, mais on prend davantage de décisions sur le découpage, la compatibilité, les dépendances, les contrats et l'intégration. Ce déplacement de valeur est essentiel pour lire correctement la suite du livre. Sans lui, les LLM risquent d'apparaître comme une rupture absolue, alors qu'ils arrivent dans une histoire déjà marquée par la délégation et par la montée de l'orchestration.

Les trois sections du chapitre suivent cette trajectoire. La première doit rappeler qu'entre l'assembleur et les langages haut niveau, le gain n'a jamais été une simple commodité: il a modifié la part de l'effort consacrée à la traduction mécanique. La deuxième montre que bibliothèques, frameworks et réutilisation ont encore déplacé la frontière entre fabriquer et composer. La troisième resserre la thèse: dans les systèmes réels, la difficulté noble se loge de plus en plus dans l'intégration, c'est-à-dire dans l'art de faire tenir ensemble des briques hétérogènes sous contraintes.

L'intérêt opératoire de ce chapitre est direct pour tout l'aval du cours. Il prépare le lecteur à une règle simple: **chaque fois qu'une couche absorbe de la fabrication, la valeur remonte vers le cadrage, le choix, l'assemblage et la vérification**. Ce n'est pas une déchéance du métier. C'est un déplacement de son centre de gravité. Cette lecture rend possible le chapitre suivant, qui élargit encore la focale: après l'évolution du code, il faut retracer l'évolution des systèmes d'IA eux-mêmes pour comprendre pourquoi les LLM ne tombent pas du ciel mais s'inscrivent dans une longue trajectoire de délégation cognitive.

## Sections du chapitre
- [De l'assembleur aux langages haut niveau](01-De-l'assembleur-aux-langages-haut-niveau.md)
- [Frameworks, bibliothèques et réutilisation](02-Frameworks,-bibliothèques-et-réutilisation.md)
- [Intégration contre fabrication](03-Intégration-contre-fabrication.md)

## Ce que ce chapitre doit laisser au lecteur
- la valeur technique s'est déplacée historiquement avec la montée des abstractions
- écrire moins de bas niveau ne signifie pas penser moins, mais décider à un autre étage
- la réutilisation n'annule pas la responsabilité; elle transforme surtout la nature du risque
- l'intégration devient progressivement un lieu central de compétence et de différenciation
- cette trajectoire prépare naturellement l'entrée dans l'histoire des IA et des délégations cognitives

## Transition vers le chapitre suivant
Le prochain chapitre ne parle plus seulement de l'évolution du code, mais de l'évolution des machines auxquelles on délègue une part croissante de travail cognitif. Après avoir vu comment l'informatique a comprimé la friction de fabrication, on peut retracer comment l'IA a cherché, par étapes, à compresser une autre friction: celle de la formalisation, de l'inférence et de la production symbolique. C'est ce passage qui permettra ensuite d'évaluer les LLM sans naïveté ni panique.
