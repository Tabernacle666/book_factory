---
id: "10.03"
title: "Exiger des artefacts vérifiables"
parent: "10"
level: section
status: draft
owner_concept: "hallucinations-et-validation-03"
summary: >
  Transforme la validation en demande de preuve locale: un bon résultat doit
  laisser derrière lui un artefact qu'un autre acteur peut contrôler.
---

# Exiger des artefacts vérifiables

## Idée centrale

Un résultat n'est pas fiable parce qu'il sonne juste. Il devient fiable lorsqu'il laisse une **trace contrôlable**. Exiger des artefacts vérifiables consiste à demander non seulement une sortie, mais aussi la forme de preuve qui permet à un autre acteur de la relire rapidement.

Cette exigence déplace la discussion. On ne demande plus « est-ce que c'est convaincant ? », mais « qu'est-ce que je peux vérifier, localement, pour accepter ou refuser ce livrable ? ».

## Pourquoi c'est important

Les hallucinations prospèrent quand le produit final ne laisse que de la prose, du code ou une synthèse sans protocole de contrôle. Plus le résultat est opaque, plus la validation retombe sur une intuition générale.

Un artefact vérifiable réduit cette opacité. Il rend visibles les hypothèses, les critères, les écarts et parfois même les limites du résultat. Il ne garantit pas l'infaillibilité, mais il réduit fortement la place du bluff plausible.

## Erreur classique

L'erreur classique consiste à demander « une réponse correcte » sans préciser sous quelle forme cette correction sera testée. Le modèle produit alors quelque chose de cohérent en surface, mais sans point d'appui pour l'audit.

Autre erreur: confondre longueur et preuve. Une réponse très détaillée n'est pas un artefact vérifiable si elle ne permet pas de contrôler rapidement ses affirmations principales.

## Méthode concrète

À chaque tâche déléguée, ajoute une contrainte de preuve. Cette preuve peut prendre des formes différentes selon le nœud, mais elle doit toujours rester locale.

Exemples d'artefacts vérifiables:
- une checklist de conformité;
- une table intrants/extrants;
- un diff ciblé;
- un jeu de tests ou une commande de reproduction;
- une liste d'hypothèses explicites;
- un statut d'écarts: respecté, partiel, non couvert.

La question utile n'est pas « quelle preuve idéale voudrais-je dans un monde parfait ? », mais « quelle preuve minimale permet à quelqu'un d'autre de contrôler ce livrable sans tout refaire ? ».

## Mini exemple

Si un agent propose une modification de chapitre, l'artefact ne devrait pas être seulement le nouveau texte. Il devrait inclure, implicitement ou explicitement:
- le fichier touché;
- le périmètre de modification;
- la présence des rubriques attendues;
- l'absence de duplication majeure avec les sections sœurs;
- le renvoi éventuel vers le concept voisin.

Si un agent propose un changement de code, l'artefact vérifiable peut être un diff ciblé accompagné du test local à lancer et de la promesse exacte du changement.

Dans les deux cas, on ne valide pas une impression. On valide une trace.

## Règle pratique

N'accepte pas une sortie que tu ne saurais pas faire relire rapidement par quelqu'un d'autre.

## Renvoi éventuel

La réduction du périmètre qui rend cette preuve possible est traitée dans `01-Réduire-le-périmètre-des-tâches.md`. La séparation entre production et audit est posée dans `02-Séparer-génération-et-vérification.md`. La grammaire des livrables associés est explicitée dans `../06-repenser-un-projet/03-Interfaces,-validations-et-livrables.md`.
