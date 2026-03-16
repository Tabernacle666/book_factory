---
id: "12.03"
title: "Le prompt comme couche de gouvernance"
parent: "12"
level: section
status: draft
owner_concept: "prompt-layering-openai-03"
summary: >
  Explique qu'un prompt n'est pas une formule magique mais une couche de
  gouvernance qui fixe rôle, périmètre, contraintes et validation.
---

# Le prompt comme couche de gouvernance

## Idée centrale

Le prompt n'est pas une incantation destinée à faire apparaître l'intelligence correcte au bon moment. Dans un système de travail sérieux, c'est une couche de gouvernance. Il sert à fixer un rôle, à borner un périmètre, à rappeler des contraintes, à spécifier un format de sortie et à préparer la validation. Sa valeur ne vient donc pas de sa poésie, mais de sa fonction de cadrage.

## Pourquoi c'est important

Beaucoup de discours sur le prompting entretiennent l'idée qu'il existerait des formulations secrètes capables d'obtenir presque n'importe quoi d'un modèle. Cette vision rend le travail fragile, personnel et peu transmissible. Si au contraire on traite le prompt comme une couche de gouvernance, on peut le normaliser, le relire, le versionner et le transmettre à d'autres agents ou rédacteurs sans dépendre d'un "talent magique".

## Erreur classique

L'erreur classique consiste à entasser des demandes, du contexte, des préférences stylistiques, des exceptions, des rappels et des notes de projet dans un seul gros bloc textuel. Ce monolithe finit par mélanger vision, rôle, tâche locale et critères de validation. Le prompt devient alors long, contradictoire, difficile à maintenir et impossible à réutiliser proprement.

## Méthode concrète

Traiter le prompt comme une couche de gouvernance revient à le répartir par niveaux.

**Vision.** Quelques principes globaux: ton, conventions, limites du projet, objectifs permanents.

**Rôle.** Qui agit ici ? Rédacteur, intégrateur, vérificateur, architecte, gardien du contexte.

**Tâche locale.** Que faut-il produire maintenant, sur quel nœud, avec quels intrants ?

**Format de sortie.** Quelle structure doit prendre le résultat ?

**Validation.** Selon quels critères décider que la sortie est acceptable ?

Une fois ces couches séparées, le prompt cesse d'être un bloc opaque. Il devient un petit instrument de pilotage.

## Mini exemple

Pour faire rédiger une section du cours, la couche vision peut rappeler: "cours modulaire, dense, sans duplication". La couche rôle: "tu es rédacteur local d'un seul nœud". La tâche locale: "compléter `08.02` sur les contrats stables". Le format: "garder les sept rubriques standard". La validation: "ne pas réécrire les concepts propriétaires ailleurs, renvoyer brièvement si nécessaire". Cette combinaison est plus robuste qu'un long prompt improvisé.

## Règle pratique

Quand un prompt commence à ressembler à une conversation entière, il a déjà perdu une partie de sa valeur de gouvernance.

## Renvoi éventuel

Les context packs minimaux qui alimentent cette gouvernance sont décrits dans `11-contexte-propre-et-court/03-Construire-des-context-packs-minimaux.md`. Pour garder ces couches maniables, il faut ensuite confier des tâches assez courtes pour rester auditable et reprises localement si besoin.
