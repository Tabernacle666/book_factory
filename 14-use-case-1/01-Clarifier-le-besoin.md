---
id: "14.01"
title: "Clarifier le besoin"
parent: "14"
level: section
status: draft
owner_concept: "use-case-1-01"
summary: >
  Transforme une demande encore vague en mandat local exploitable: objectif,
  périmètre, hypothèses, intrants autorisés et critères d'acceptation avant tout
  découpage plus technique.
---

# Clarifier le besoin

## Idée centrale
Avant de découper un système, il faut clarifier ce que la demande autorise vraiment à construire. Clarifier le besoin ne signifie pas rédiger un cahier des charges exhaustif. Cela signifie produire une **forme minimale de mandat** qui distingue l'objectif poursuivi, les limites immédiates, les hypothèses encore ouvertes et les critères qui permettront de juger si la prochaine étape est utile.

Dans un contexte hybride humain+IA, cette clarification est encore plus importante. Un besoin flou donne facilement l'illusion qu'un agent pourra "compléter les blancs". En pratique, il complète surtout avec ses propres interpolations. Si rien n'est stabilisé, la vitesse de génération fabrique surtout de la dérive plausible.

## Pourquoi c'est important
La plupart des échecs précoces ne viennent pas d'un manque de puissance, mais d'une confusion de mandat. On demande à un système de produire alors que personne n'a encore fixé le niveau d'autonomie acceptable, les intrants légitimes ou le point exact de reprise humaine.

Clarifier le besoin réduit cette confusion. Cela permet de séparer ce qui est déjà décidée de ce qui reste ouvert, et donc d'éviter que les agents, les rédacteurs ou les développeurs ne traitent comme acquise une décision qui n'a jamais été prise.

## Erreur classique
L'erreur classique consiste à croire qu'un besoin devient clair dès qu'on peut l'énoncer de manière fluide. Une phrase courte et convaincante n'est pas encore un mandat exploitable.

Autre erreur fréquente: demander immédiatement une architecture, un plan détaillé ou du code pour "voir". On obtient alors une sortie apparemment productive, mais qui repose sur des hypothèses implicites non auditées. Le travail avance en surface et se fragilise en profondeur.

## Méthode concrète
Avant tout découpage, produire une fiche de clarification courte avec cinq blocs:

1. **Objectif local** — quel problème précis essaie-t-on d'améliorer maintenant ?
2. **Hors-périmètre immédiat** — qu'est-ce qu'on refuse explicitement de résoudre dans cette passe ?
3. **Hypothèses ouvertes** — qu'est-ce qu'on suppose vrai faute d'information complète ?
4. **Intrants autorisés** — sur quelles sources, données ou documents la prochaine étape pourra-t-elle s'appuyer ?
5. **Critères d'acceptation** — qu'est-ce qui permettra de dire que cette clarification est suffisante pour passer à l'étape suivante ?

Cette fiche doit rester courte. Si elle devient trop longue, c'est souvent le signe que plusieurs problèmes ont été mélangés et qu'il faut d'abord réduire le périmètre.

## Mini exemple
Demande initiale: « on veut un agent qui aide à traiter les tickets support ».

Clarification minimale possible:
- **objectif local**: réduire le temps de qualification initiale des tickets entrants ;
- **hors-périmètre**: pas de réponse automatique au client, pas d'action en production ;
- **hypothèses ouvertes**: les tickets contiennent assez d'information pour une première catégorisation ;
- **intrants autorisés**: taxonomie existante des tickets, exemples historiques, règles de tri actuelles ;
- **critères d'acceptation**: être capable de proposer un flux de qualification avec reprise humaine explicite et points de validation locaux.

On n'a pas encore l'architecture finale, mais on a déjà un terrain stable pour la construire.

## Règle pratique
Si tu ne peux pas écrire le hors-périmètre immédiat en trois lignes, le besoin n'est pas encore assez clair pour être découpé proprement.

## Renvoi éventuel
Le passage de ce mandat minimal à des frontières de travail plus stables est traité dans `02-Découper-en-sous-systèmes-et-interfaces.md`. La grammaire des livrables et validations qui soutient cette clarification est posée dans `../06-repenser-un-projet/03-Interfaces,-validations-et-livrables.md`.
