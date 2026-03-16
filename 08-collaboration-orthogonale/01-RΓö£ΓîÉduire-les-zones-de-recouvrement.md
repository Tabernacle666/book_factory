---
id: "08.01"
title: "Réduire les zones de recouvrement"
parent: "08"
level: section
status: draft
owner_concept: "collaboration-orthogonale-01"
summary: >
  Rend opérationnelle la notion de recouvrement en montrant comment identifier,
  limiter et traiter les chevauchements de responsabilité entre contributeurs humains et agents.
---

# Réduire les zones de recouvrement

## Idée centrale

Une collaboration devient orthogonale quand chaque contributeur peut avancer sans réécrire, contredire ou polluer le travail des autres. Le recouvrement n'est pas seulement un doublon de contenu. C'est toute zone où plusieurs acteurs croient posséder la même décision, la même responsabilité ou le même morceau de vérité. Plus ces zones sont larges, plus la coordination devient coûteuse et plus les sorties deviennent incohérentes.

## Pourquoi c'est important

Avec plusieurs agents et plusieurs humains, le recouvrement produit un faux sentiment de productivité. Beaucoup de choses bougent, mais elles bougent sur les mêmes objets. On obtient alors des collisions de conventions, des duplications de logique, des fichiers touchés par trop de mains et une inflation de contexte parce qu'il faut sans cesse expliquer qui décide quoi. Réduire ces zones n'est donc pas une obsession bureaucratique. C'est une condition directe de vitesse propre.

## Erreur classique

L'erreur classique consiste à répartir le travail par thèmes vagues: frontend, backend, qualité, documentation, recherche. Ces labels sont utiles, mais ils restent trop larges si l'on ne précise pas ce qui appartient réellement à chacun. Deux agents peuvent ainsi modifier la même interface sous des justifications différentes. Chacun pense aider; ensemble, ils créent une dette de coordination.

## Méthode concrète

Pour rendre le recouvrement visible, cartographie trois choses pour chaque nœud de travail: le propriétaire de la décision, le périmètre de modification autorisé et l'artefact source de vérité. Dès qu'un autre acteur touche au même triplet, tu as une zone de recouvrement potentielle. Tu peux ensuite la traiter de trois façons: scinder l'objet, clarifier la hiérarchie de décision ou transformer l'un des acteurs en simple relecteur plutôt qu'en coproducteur.

## Mini exemple

Supposons qu'un agent rédige la documentation d'une API pendant qu'un autre ajuste la forme des réponses JSON. Si la spécification de l'interface n'a pas un propriétaire clair, la documentation et l'implémentation vont diverger en silence. En revanche, si un seul nœud possède la vérité de l'interface et que les autres se contentent d'y faire référence, le recouvrement chute immédiatement.

## Règle pratique

Quand deux contributeurs ont le droit d'éditer le même concept, le même fichier ou la même décision sans protocole explicite, considère que tu as déjà une zone de recouvrement à réduire.

## Renvoi éventuel

Pour transformer cette réduction du recouvrement en contrats explicites, voir `08-collaboration-orthogonale/02-Définir-des-contrats-stables.md`. Pour le journal de coordination qui permet d'arbitrer les exceptions, voir `08-collaboration-orthogonale/03-Journal-de-décisions-et-coordination.md`.
