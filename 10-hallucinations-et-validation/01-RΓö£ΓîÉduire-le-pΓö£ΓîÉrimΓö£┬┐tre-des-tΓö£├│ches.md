---
id: "10.01"
title: "Réduire le périmètre des tâches"
parent: "10"
level: section
status: draft
owner_concept: "hallucinations-et-validation-01"
summary: >
  Explique pourquoi la réduction du périmètre est l'un des moyens les plus simples
  et les plus fiables pour protéger la qualité des sorties.
---

# Réduire le périmètre des tâches

## Idée centrale

Plus une tâche est large, plus un LLM doit combler des zones de flou, inventer des transitions et prendre des décisions implicites. Réduire le périmètre n'est donc pas seulement un choix d'organisation; c'est une mesure directe de contrôle qualité. Une tâche étroite force la production à rester proche de l'objet traité, limite les hypothèses cachées et rend la validation locale beaucoup plus simple.

## Pourquoi c'est important

Beaucoup d'hallucinations spectaculaires viennent de consignes trop vastes: "refais le module", "résous le problème", "rédige le chapitre", "conçois l'architecture". L'agent doit alors deviner ce qui compte, ce qui est déjà décidé, ce qu'il peut modifier et la profondeur attendue. Cette liberté excessive produit des sorties séduisantes mais mal ancrées. En réduisant le périmètre, on remplace la magie espérée par une surface de travail vérifiable.

## Erreur classique

L'erreur classique consiste à croire qu'un agent devient plus intelligent lorsqu'on lui demande un bloc de travail plus large. En pratique, on mélange plusieurs opérations: exploration, génération, arbitrage, synthèse, intégration. Le modèle peut en réaliser certaines correctement, mais la tâche globale devient vite trop ouverte pour rester fiable. Ce n'est pas toujours un problème de modèle; c'est souvent un problème de cadrage.

## Méthode concrète

Réduis chaque tâche jusqu'à ce qu'elle puisse être validée par une lecture locale ou par un test local. Une bonne unité de travail nomme son fichier cible ou son artefact cible, son objectif précis, ses intrants autorisés et son critère d'acceptation. Si tu as besoin de relire tout le projet pour savoir si la tâche est correcte, alors le périmètre reste trop grand. Il faut le couper à nouveau.

## Mini exemple

Demander à un agent de "sécuriser l'authentification" l'oblige à interpréter des hypothèses métier, des choix d'interface, des dépendances et parfois même des politiques d'infrastructure. Lui demander au contraire de "rédiger la checklist de validation pour la rotation de session dans tel module, sans modifier le code" réduit brutalement la dérive. On passe d'une ambition floue à un artefact que quelqu'un d'autre peut contrôler rapidement.

## Règle pratique

Quand une tâche oblige l'agent à décider lui-même de son terrain de jeu, elle est déjà trop large. Réduis-la jusqu'à pouvoir nommer exactement ce qui peut changer et comment tu vas le vérifier.

## Renvoi éventuel

Pour la séparation entre génération et vérification, voir `10-hallucinations-et-validation/02-Séparer-génération-et-vérification.md`. Pour garder un découpage réellement praticable, vise des tâches courtes, bornées et faciles à auditer.
