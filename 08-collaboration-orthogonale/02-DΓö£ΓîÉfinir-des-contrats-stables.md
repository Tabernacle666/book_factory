---
id: "08.02"
title: "Définir des contrats stables"
parent: "08"
level: section
status: draft
owner_concept: "collaboration-orthogonale-02"
summary: >
  Donne un mini protocole pour définir des contrats stables entre agents, rôles
  ou modules afin de réduire les recouvrements et les régressions.
---

# Définir des contrats stables

## Idée centrale

Une collaboration orthogonale ne tient pas seulement à un bon découpage des responsabilités. Elle tient aussi à la stabilité des points de contact. Un **contrat** décrit ce qu’un acteur reçoit, ce qu’il doit produire, ce qu’il n’a pas le droit de modifier et comment son travail sera validé.

Sans contrats stables, même des contributeurs brillants se gênent mutuellement. Chacun compense les ambiguïtés à sa manière, réinterprète le besoin localement et finit par étendre son périmètre. Avec des agents IA, ce problème s’aggrave, car le modèle cherche spontanément à combler les zones floues au lieu de s’y arrêter.

## Pourquoi c'est important

Le contrat remplace une partie de l’accord implicite qui existerait parfois dans une petite équipe humaine. Il rend la collaboration moins dépendante du style individuel, de la mémoire informelle et de l’humeur du moment. Il permet aussi d’auditer une sortie sans relire tout le projet.

Plus le projet grandit, plus la stabilité des contrats compte davantage que l’intelligence locale de chaque contributeur. Un agent très capable mais mal borné crée plus de dégâts qu’un agent moyen contraint par de bons contrats.

## Erreur classique

L’erreur classique est d’écrire des contrats décoratifs. On note vaguement un objectif, mais on ne précise ni le format d’entrée, ni le format de sortie, ni les interdits. L’agent “a compris l’idée”, mais chacun comprend une idée différente.

Autre erreur: faire évoluer un contrat en silence. Une petite modification implicite dans un champ, un nom, une convention ou une hypothèse peut casser plusieurs contributions en aval, même si tout semble plausible à la lecture.

## Méthode concrète

Un contrat minimal tient en six éléments.

1. **Rôle** : qui agit et sur quel périmètre.
2. **Entrées** : quelles informations ou artefacts sont autorisés.
3. **Sortie attendue** : fichier, structure, format, granularité.
4. **Interdits** : ce que l’acteur ne doit pas toucher ou redéfinir.
5. **Critères d’acceptation** : comment vérifier localement que le travail est bon.
6. **Version** : comment signaler qu’un contrat a changé.

Dans ce cours, un bon contrat est assez court pour être relu avant chaque contribution, mais assez précis pour bloquer les interprétations opportunistes.

## Mini exemple

Un agent chargé d’une section du cours reçoit comme entrée le fichier cible, le `chapitre.md` parent et les sections sœurs. Sa sortie attendue est un unique fichier Markdown enrichi. Ses interdits: ne pas modifier le plan global, ne pas dupliquer un concept propriétaire d’un autre fichier, ne pas créer de nouveaux fichiers. Les critères d’acceptation: densité accrue, pas de redite, présence d’un renvoi éventuel, cohérence avec les conventions du cours.

Ce mini protocole suffit souvent à éviter qu’un agent transforme une simple rédaction locale en refonte latérale du projet.

## Règle pratique

Un contrat est bon quand il réduit les interprétations sans tout micro-manager. S’il est trop vague, il n’encadre rien. S’il est trop long, il n’est plus relu et redevient symbolique.

## Renvoi éventuel

Le principe général de réduction des recouvrements est traité dans `01-Réduire-les-zones-de-recouvrement.md`. La coordination légère entre contributions apparaît dans `03-Journal-de-décisions-et-coordination.md`.
