---
id: "06.01"
title: "Projet continu ou hiérarchie de décisions"
parent: "06"
level: section
status: draft
owner_concept: "repenser-un-projet-01"
summary: >
  Déplace la perception du projet logiciel: d'une masse continue de travail vers
  une hiérarchie de décisions, d'interfaces et de validations.
---

# Projet continu ou hiérarchie de décisions

## Idée centrale

Beaucoup de développeurs perçoivent encore un projet comme une longue bande de travail continu: on avance, on corrige, on rajoute des couches, puis on espère qu’à force d’efforts la forme correcte apparaîtra. Cette perception convenait déjà mal aux grands projets humains; elle devient franchement coûteuse quand on travaille avec des agents IA.

À l’ère des LLM, un projet se pilote beaucoup mieux comme une **hiérarchie de décisions**. Au sommet, on fixe l’intention, les contraintes et les critères de réussite. En dessous, on définit des sous-problèmes, des interfaces, des validations et des livrables. Tout en bas, on laisse les agents ou les humains exécuter des tâches courtes, bornées et vérifiables.

## Pourquoi c'est important

Si tu vois le projet comme un flux continu, tu demandes trop vite à l’IA de “faire avancer le projet”. C’est flou, donc la sortie devient floue. L’agent remplit les trous avec de la plausibilité. Il semble productif, mais il dérive.

Si tu vois le projet comme une hiérarchie de décisions, tu peux isoler ce qui doit rester humain, ce qui peut être exploré automatiquement, et ce qui doit être validé avant intégration. Tu rends l’autonomie locale possible sans perdre le contrôle global.

## Erreur classique

L’erreur classique consiste à confondre mouvement et progression. On ouvre un dépôt, on ajoute des tickets, on lance des générations successives, et l’on croit que l’accumulation finira par produire une architecture. En réalité, sans hiérarchie explicite, on obtient surtout des fragments qui se gênent entre eux.

Une autre erreur fréquente est de placer trop bas des décisions qui devraient être prises plus haut. Par exemple, laisser un agent choisir implicitement le découpage des responsabilités, la forme des contrats ou la stratégie de validation, alors que ces choix structurent tout le reste.

## Méthode concrète

Pour reframer un projet, pars de quatre niveaux.

Le premier niveau est **directionnel**: but, contraintes, non-objectifs, critères de réussite. Le deuxième est **architectural**: grands sous-systèmes, interfaces, flux, risques majeurs. Le troisième est **opérationnel**: tâches bornées, livrables, critères d’acceptation. Le quatrième est **exécutif**: production locale, vérification, intégration.

Chaque fois qu’un nœud te paraît trop gros, demande-toi: s’agit-il d’une décision de niveau supérieur mal explicitée, ou d’une vraie tâche locale? Souvent, ce que l’on appelait “avancer sur le projet” mélange en fait les deux.

## Mini exemple

Supposons un projet de portail interne. Dans une vision continue, on demande: “construis le portail avec authentification, recherche et tableau de bord”. Dans une vision hiérarchique, on décide d’abord quels modules existent, quelles données ils manipulent, quels contrats les relient, quels risques sont critiques, puis seulement on découpe en quanta courts. L’IA peut alors travailler sur un module d’authentification, une page de dashboard ou un schéma de sortie sans réinventer le reste.

Le deuxième mode paraît plus lent au départ. En réalité, il réduit les collisions, la dette de contexte et les réécritures en chaîne.

## Règle pratique

Quand un lot de travail ne peut pas être relié à une décision supérieure explicite, il est probablement mal cadré. Un projet bien piloté ressemble moins à une rivière qu’à un arbre: chaque branche a une origine, une portée et une validation.

## Renvoi éventuel

Le passage du “faire” au “faire faire proprement” est développé dans `02-Du-faire-au-faire-faire-proprement.md`. Le découpage concret du travail vient ensuite dans `../07-decoupage-du-travail/chapitre.md`.
