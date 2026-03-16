---
id: "08.03"
title: "Journal de décisions et coordination"
parent: "08"
level: section
status: draft
owner_concept: "collaboration-orthogonale-03"
summary: >
  Fait du journal de décisions un livrable léger mais central pour la
  coordination, la reprise et l'audit local des contributions.
---

# Journal de décisions et coordination

## Idée centrale

Dans une collaboration orthogonale, le journal de décisions n'est pas un compte rendu décoratif. C'est un **livrable de coordination**. Il sert à dire ce qui a été décidé, pourquoi, sur quel périmètre, et ce que cela change pour les autres contributeurs.

Sans ce journal, chaque acteur doit reconstruire l'état du projet à partir d'indices dispersés: fichiers modifiés, traces conversationnelles, versions implicites, habitudes d'équipe. Avec lui, la coordination cesse de dépendre d'une mémoire flottante. Elle repose sur une chaîne de décisions relisible.

## Pourquoi c'est important

Plus les tâches sont distribuées, plus la valeur d'une décision dépend de sa transmissibilité. Un bon découpage peut échouer non parce que les rôles sont mal définis, mais parce qu'aucune trace légère ne permet de savoir quelles hypothèses sont devenues stables, lesquelles restent locales, et quels impacts doivent être propagés.

Le journal de décisions réduit ce coût de reprise. Il aide un rédacteur, un intégrateur ou un pilote à comprendre rapidement: ce qui a changé, ce qui reste vrai, et ce qu'il n'a pas besoin de rouvrir. Il évite aussi les faux conflits, quand deux acteurs semblent se contredire alors qu'ils travaillent simplement sur des versions mentales différentes du même problème.

## Erreur classique

L'erreur classique consiste à confondre journal de décisions et historique exhaustif. On note tout: hésitations, pistes abandonnées, digressions, commentaires intermédiaires. Le document devient alors un grenier narratif de plus, presque aussi coûteux à relire que l'historique brut.

Autre erreur: ne rien journaliser parce que "la décision est visible dans le fichier". Le fichier montre parfois **ce qui est là**, mais rarement **pourquoi** ce choix a été retenu, ce qu'il remplace, et jusqu'où il engage les autres nœuds.

## Méthode concrète

Un bon journal de décisions reste court et suit toujours la même forme.

1. **Décision** — ce qui est désormais tenu pour vrai localement.
2. **Raison** — pourquoi cette décision a été prise.
3. **Périmètre** — quels fichiers, contrats ou nœuds sont concernés.
4. **Conséquence** — ce que les acteurs voisins doivent considérer comme stable.
5. **Ouverts** — ce qui n'est pas tranché et ne doit pas être supposé.

L'idée n'est pas de documenter tout le travail, mais de capturer les points qui évitent aux autres de réinterpréter le système. Une décision journalisée doit être assez courte pour être relue avant une reprise, et assez précise pour empêcher une double reconstruction du contexte.

## Mini exemple

Supposons qu'une release densifie `06.03` pour faire de l'unité de travail une fiche minimale `intrants → livrable → validation → reprise`. Le journal utile ne doit pas raconter toute la rédaction. Il peut simplement dire:

- décision: la fiche minimale devient la forme canonique des unités de travail locales;
- raison: réduire les tâches floues confiées à des agents;
- périmètre: `06.03`, `07.03`, `10.03`;
- conséquence: les prochains nœuds peuvent s'y référer sans redéfinir la structure;
- ouverts: la transmission d'état et le nettoyage du contexte restent à expliciter en `11.01` et `11.02`.

Cette trace suffit à coordonner la suite sans rejouer tout le débat.

## Règle pratique

Journalise les **décisions qui changent le terrain des autres**, pas toute l'activité qui a conduit à ces décisions.

## Renvoi éventuel

La stabilité des points de contact est posée dans `02-Définir-des-contrats-stables.md`. La transmission d'état propre qui permet de reprendre un nœud sans hériter du bruit historique est prolongée dans `../11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md`.
