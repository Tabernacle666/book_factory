---
id: "12.01"
title: "Vision permanente et conventions globales"
parent: "12"
level: section
status: draft
owner_concept: "prompt-layering-openai-01"
summary: >
  Formalise la couche de conventions stables qui évite de redéfinir la vision,
  les règles et les formats à chaque tâche locale.
---

# Vision permanente et conventions globales

## Idée centrale

Un bon système de prompts ne recommence pas le projet à chaque requête. Il s'appuie sur une **vision permanente** et sur des **conventions globales** qui restent vraies d'une tâche à l'autre. Cette couche n'est pas là pour produire du style ou de la rhétorique. Elle sert à stabiliser le terrain commun: langage, niveau d'exigence, structure des sorties, règles de collaboration, interdits et critères de qualité.

Sans cette couche, chaque tâche repart presque de zéro. L'agent doit inférer seul ce qui compte, ce qui est interdit, le niveau de précision attendu et la manière de remettre son travail. On obtient alors des sorties parfois bonnes localement, mais hétérogènes à l'échelle du projet.

## Pourquoi c'est important

La vision permanente réduit la variabilité inutile. Elle évite d'avoir à réenseigner à chaque fois les mêmes invariants: ne pas ouvrir de front latéral, ne pas dupliquer un concept propriétaire, respecter les conventions d'écriture, produire un livrable localement vérifiable. Plus ces éléments sont stables, plus les tâches locales peuvent rester courtes.

Cette couche protège aussi les humains. Elle permet à plusieurs rédacteurs ou agents de contribuer sur un même corpus sans que chacun réinvente sa propre définition du travail bien fait. Ce n'est pas un supplément cosmétique; c'est une couche de cohérence inter-tâches.

## Erreur classique

L'erreur classique consiste à tout mettre dans le prompt de tâche. On mélange alors vision éditoriale, règles générales, contexte local, objectif ponctuel et validation attendue dans un seul bloc. Ce gros prompt peut sembler complet, mais il rend la maintenance difficile: dès qu'une convention change, il faut corriger partout.

Autre erreur: réduire les conventions globales à un "ton" ou à un style rédactionnel. La vraie couche permanente contient surtout des invariants de collaboration: ce qui fait autorité, ce qui est interdit, comment découper, comment rendre, comment signaler un doute.

## Méthode concrète

Pour construire une vision permanente utile, il suffit d'un noyau court et stable:

1. **Mission durable** — ce que le projet essaie de produire.
2. **Règles globales** — ce qu'on ne doit pas faire, même si une tâche locale semble l'encourager.
3. **Conventions de sortie** — format, niveau de densité, type de trace attendue.
4. **Critères de qualité** — ce qui fait qu'un livrable est recevable.
5. **Règles de relais** — comment passer la main au prochain acteur.

Cette couche doit rester petite. Si elle grossit sans cesse, elle cesse d'être une vision permanente et redevient un grenier. Son rôle est d'apporter des invariants, pas de transporter tout l'historique du projet.

## Mini exemple

Dans ce livre, le `README.md`, les conventions et la queue jouent ce rôle de couche stable. Le rédacteur n'a pas besoin de redemander à chaque release s'il faut ouvrir les use-case, refondre tout le chapitre ou créer un nouveau fichier. La vision globale le borne déjà: une release, un objectif, pas de dérive latérale, retour en évaluation à la version prévue.

Le prompt de tâche peut alors rester local: "densifier 12.01" ou "compléter le premier item ouvert de la passe active". Il fonctionne parce qu'une couche plus haute a déjà fixé les invariants.

## Règle pratique

Ce qui doit rester vrai pour **plusieurs tâches successives** ne doit pas être répété dans chaque prompt local. Il doit vivre dans une couche permanente courte et stable.

## Renvoi éventuel

La séparation entre conventions stables, rôle, tâche et validation est détaillée dans `02-Prompt-de-rôle,-prompt-de-tâche,-prompt-de-validation.md`. Le prompt comme couche de gouvernance plus large est prolongé dans `03-Le-prompt-comme-couche-de-gouvernance.md`.
