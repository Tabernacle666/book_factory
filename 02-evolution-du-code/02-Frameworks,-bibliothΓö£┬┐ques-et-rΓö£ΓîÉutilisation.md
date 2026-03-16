---
id: "02.02"
title: "Frameworks, bibliothèques et réutilisation"
parent: "02"
level: section
status: draft
owner_concept: "evolution-du-code-02"
summary: >
  Montre comment la réutilisation augmente fortement la vitesse de production,
  tout en déplaçant la dette vers les interfaces, la dépendance et la compréhension partielle.
---

# Frameworks, bibliothèques et réutilisation

## Idée centrale

L'histoire du code est aussi l'histoire d'une délégation croissante. À mesure que les langages, bibliothèques et frameworks se sont accumulés, une part de plus en plus grande du travail n'a plus consisté à tout fabriquer, mais à réutiliser des briques existantes. Cette réutilisation a décuplé la vitesse de production, mais elle a aussi changé la nature du risque: on gagne du temps sur la fabrication brute, puis on le reperd si l'on ne maîtrise pas les dépendances, les limites d'abstraction et les effets de bord.

## Pourquoi c'est important

Beaucoup de débats sur les LLM répètent en réalité un vieux débat sur la réutilisation. Chaque couche d'abstraction a semblé, à son arrivée, menacer la pureté du métier. Pourtant, personne ne regrette sérieusement d'avoir dû réécrire les primitives de plus bas niveau pour prouver sa compétence. Comprendre la logique des frameworks et des bibliothèques permet de voir que le métier évoluait déjà depuis longtemps vers l'intégration. Les LLM prolongent ce mouvement, ils ne le créent pas de zéro.

## Erreur classique

L'erreur classique est double. D'un côté, certains croient que réutiliser des briques revient à ne plus rien comprendre. De l'autre, certains empilent des dépendances en pensant que la réutilisation supprime l'obligation de comprendre. Les deux positions sont bancales. Une bonne réutilisation n'est ni un retour à la fabrication totale, ni un abandon de la responsabilité. C'est un usage sélectif d'abstractions dont on connaît assez bien les contrats, les hypothèses et les zones d'instabilité.

## Méthode concrète

Quand tu introduis une bibliothèque ou un framework, évalue-le selon quatre questions simples. Quel problème local résout-il réellement? Quel contrat impose-t-il à ton projet? Quelle dette introduit-il en termes de version, de migration ou de couplage? Et quelle profondeur de compréhension te faut-il pour l'utiliser sans aveuglement? Cette grille évite deux excès: l'orgueil de tout refaire et la paresse de tout déléguer.

## Mini exemple

Un développeur peut gagner deux semaines en adoptant un framework web mature plutôt qu'en réécrivant la gestion des routes, des sessions et de la sérialisation. Mais si ce framework dicte aussi l'organisation des modules, le cycle de vie des objets, la stratégie de tests et les conventions de déploiement, il ne s'agit plus d'un simple gain local. Le projet a accepté une forme de gouvernance technique. Ce n'est pas forcément mauvais; il faut juste le voir clairement.

## Règle pratique

Réutiliser vite n'est bon que si tu sais nommer la dette que tu viens d'acheter. Toute brique réutilisée économise de la fabrication et achète en échange des contraintes d'intégration.

## Renvoi éventuel

Pour le déplacement explicite de valeur vers l'intégration, voir `02-evolution-du-code/03-Intégration-contre-fabrication.md`. Pour la manière de faire travailler des briques séparées sans recouvrement inutile, voir `08-collaboration-orthogonale/01-Réduire-les-zones-de-recouvrement.md`.
