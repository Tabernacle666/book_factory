---
id: "12.02"
title: "Prompt de rôle, prompt de tâche, prompt de validation"
parent: "12"
level: section
status: draft
owner_concept: "prompt-layering-openai-02"
summary: >
  Sépare les couches de prompt selon leur fonction: posture, objectif local et
  contrôle de recevabilité.
---

# Prompt de rôle, prompt de tâche, prompt de validation

## Idée centrale

Un bon prompt n'est pas un texte unique bien tourné. C'est un **assemblage de couches** qui n'ont pas la même fonction. Le prompt de rôle fixe la posture et le périmètre. Le prompt de tâche définit l'objectif local et les intrants utiles. Le prompt de validation précise ce qui doit être vérifié avant d'accepter la sortie.

Quand ces couches sont mélangées, les erreurs deviennent plus difficiles à diagnostiquer. On ne sait plus si une mauvaise réponse vient d'un rôle mal défini, d'une tâche ambiguë ou d'une validation absente. La séparation rend la collaboration plus lisible et les corrections plus locales.

## Pourquoi c'est important

Dans un travail humain+IA, le problème n'est pas seulement de "demander quelque chose". Le problème est de contrôler ce que l'on autorise, ce que l'on attend et ce que l'on considère comme recevable. Sans séparation, la consigne gonfle, le modèle improvise des priorités implicites et la reprise humaine devient confuse.

Cette séparation aide aussi à réutiliser proprement ce qui mérite de l'être. Un rôle peut rester stable sur toute une phase. Une tâche change souvent. Une validation peut être réappliquée à plusieurs tâches voisines. On gagne donc à ne pas tout recoder à chaque fois.

## Erreur classique

L'erreur classique consiste à écrire un gros paragraphe qui dit à la fois qui l'agent est, ce qu'il doit faire, ce qu'il ne doit pas faire, quel format rendre et comment vérifier le résultat. Ce type de prompt peut marcher ponctuellement, mais il reste difficile à maintenir et presque impossible à auditer.

Autre erreur: croire que la validation est une simple demande finale du type "fais attention aux erreurs". Une vraie couche de validation énonce des tests explicites: présence des éléments requis, absence de duplication, conformité à l'interface, signalement des limites.

## Méthode concrète

Utilise trois blocs distincts, même s'ils sont courts.

### 1. Prompt de rôle
Il répond à la question: **dans quelle posture travailles-tu?**

Il contient par exemple:
- responsabilité locale;
- périmètre;
- interdits;
- niveau d'exigence;
- manière de signaler l'incertitude.

### 2. Prompt de tâche
Il répond à la question: **que dois-tu produire ici et maintenant?**

Il contient par exemple:
- objectif local;
- fichiers ou intrants autorisés;
- type de livrable;
- contraintes de format;
- renvoi éventuel vers un nœud voisin.

### 3. Prompt de validation
Il répond à la question: **qu'est-ce qui rend la sortie acceptable?**

Il contient par exemple:
- checklist minimale;
- test de cohérence locale;
- absence de duplication lourde;
- limites à signaler;
- point de reprise humaine.

## Mini exemple

Pour densifier une section du cours:

- **Rôle**: tu es rédacteur local, tu renforces un seul nœud sans ouvrir de front latéral.
- **Tâche**: complète `12.02` en ajoutant idée centrale, erreur classique, méthode, mini exemple, règle pratique.
- **Validation**: le texte doit rester local, ne pas dupliquer `12.03`, et permettre à un lecteur de distinguer clairement rôle, tâche et validation.

Le texte produit sera souvent meilleur non parce que la demande est plus longue, mais parce que chaque couche joue un rôle non ambigu.

## Règle pratique

Si tu ne peux pas dire séparément **qui agit**, **sur quoi il agit** et **comment on juge la sortie**, ton prompt est encore trop fusionné.

## Renvoi éventuel

Les conventions stables qui encadrent ces trois couches sont posées dans `01-Vision-permanente-et-conventions-globales.md`. Leur prolongement comme couche de gouvernance est traité dans `03-Le-prompt-comme-couche-de-gouvernance.md`.
