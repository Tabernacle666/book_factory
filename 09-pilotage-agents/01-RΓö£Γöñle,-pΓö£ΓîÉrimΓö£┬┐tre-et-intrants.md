---
id: "09.01"
title: "Rôle, périmètre et intrants"
parent: "09"
level: section
status: draft
owner_concept: "pilotage-agents-01"
summary: >
  Donne un contrat minimal d'agent pour éviter la dérive, le débordement de périmètre
  et la consommation inutile de contexte.
---

# Rôle, périmètre et intrants

## Idée centrale

Un agent utile n'est pas un esprit libre à qui l'on demande de faire au mieux. C'est un contributeur cadré par un rôle, un périmètre et des intrants définis. Le rôle indique la fonction attendue. Le périmètre dit ce qu'il a le droit de toucher ou de décider. Les intrants précisent sur quoi il peut fonder sa réponse. Sans ces trois éléments, l'agent compense par de l'invention, du débordement ou de la paraphrase.

## Pourquoi c'est important

Quand un agent reçoit seulement un objectif final, il tente souvent de combler seul les manques: il reformule le besoin, suppose des contraintes, réécrit d'autres zones du projet ou invente un contexte implicite. C'est précisément ce qui augmente les hallucinations et les sorties difficiles à intégrer. À l'inverse, un contrat minimal d'agent réduit la latitude inutile et augmente la qualité des artefacts produits.

## Erreur classique

L'erreur classique est de croire qu'un prompt plus long suffit à cadrer l'agent. En réalité, un texte volumineux sans frontières nettes produit souvent l'effet inverse. L'agent voit beaucoup d'information, mais ne sait plus laquelle est normative. Il faut donc distinguer clairement ce qu'il est, ce qu'il traite, ce qu'il reçoit et ce qu'il ne doit pas faire.

## Méthode concrète

Pour chaque agent, rédige un mini contrat en six lignes maximum: rôle, objectif local, périmètre de modification, intrants autorisés, format de sortie, interdits. Ce format oblige à cadrer l'autonomie sans noyer l'agent dans la prose. Si le contrat ne tient pas en quelques lignes, c'est souvent que la tâche n'est pas encore assez découpée. Tu peux alors réduire le périmètre ou déplacer certaines décisions vers un nœud amont.

## Mini exemple

Un agent de rédaction peut recevoir le contrat suivant: rôle = rédacteur d'une section; objectif local = compléter `09-pilotage-agents/01-Rôle,-périmètre-et-intrants.md`; périmètre = modifier ce fichier uniquement; intrants = le fichier cible, le chapitre parent et les deux sections sœurs; format = markdown final + change log court; interdits = pas de réécriture globale, pas de nouveau fichier. Ce simple contrat réduit déjà une grande partie de la dérive habituelle.

## Règle pratique

Si tu ne peux pas écrire le rôle, le périmètre et les intrants d'un agent en quelques lignes nettes, ne lui délègue pas encore la tâche.

## Renvoi éventuel

Pour savoir quand un agent doit être repris en main, voir `09-pilotage-agents/02-Quand-déléguer-et-quand-reprendre-la-main.md`. Pour la réduction du périmètre comme protection contre les hallucinations, voir `10-hallucinations-et-validation/01-Réduire-le-périmètre-des-tâches.md`.
