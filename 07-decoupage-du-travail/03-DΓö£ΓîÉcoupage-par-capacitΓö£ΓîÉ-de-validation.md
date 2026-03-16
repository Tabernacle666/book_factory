---
id: "07.03"
title: "Découpage par capacité de validation"
parent: "07"
level: section
status: draft
owner_concept: "decoupage-du-travail-03"
summary: >
  Montre qu'une unité de travail doit être définie non par sa taille brute,
  mais par la possibilité d'une validation locale rapide et nette.
---

# Découpage par capacité de validation

## Idée centrale

On ne découpe pas correctement une tâche parce qu'elle est petite. On la découpe correctement parce qu'on peut la **valider localement**. La bonne unité de travail n'est donc pas « ce qui tient dans peu de lignes » ou « ce qui semble simple », mais ce qui peut être accepté ou rejeté sans replonger dans l'ensemble du système.

Cette logique change tout. Elle fait du découpage une discipline de contrôle plutôt qu'un simple partage de charge.

## Pourquoi c'est important

Une tâche peut être courte et pourtant impossible à juger localement. À l'inverse, une tâche un peu plus riche peut rester saine si sa validation est bornée. Avec des agents IA, cette distinction est essentielle, car l'autonomie acceptable dépend moins du volume produit que du coût de vérification.

Découper par capacité de validation permet de limiter la dérive. Chaque acteur sait non seulement quoi produire, mais aussi selon quel test local il sera relu. On réduit ainsi les faux progrès: ces sorties qui semblent faire avancer le projet mais qui demandent en réalité une réouverture globale.

## Erreur classique

L'erreur classique consiste à découper par taille apparente: un ticket, un fichier, une page, un module. Ce type de découpage rassure parce qu'il est visible, mais il ne garantit pas qu'une sortie soit vérifiable.

Autre erreur: découper une même unité en sous-tâches qui restent dépendantes d'un jugement global. On a alors l'illusion du travail parallèle, alors que chaque morceau reste suspendu à une relecture complète du système.

## Méthode concrète

Pour savoir si une unité est bien découpée, pose quatre questions:

1. **Qui peut valider ce résultat?**
2. **Avec quels intrants minimaux?**
3. **En combien d'étapes mentales?**
4. **Sans réexaminer quelle partie du système?**

Si la réponse suppose de recharger tout le projet, la tâche est encore trop large ou mal définie. Il faut soit la couper, soit remonter une décision dans un nœud supérieur.

En pratique, une bonne unité de validation locale possède:
- un périmètre stable;
- une sortie nommable;
- une grille courte de conformité;
- un impact limité à un voisinage connu.

## Mini exemple

Dire « auditer le chapitre 7 » est trop large, car il faut relire les trois sections, le `chapitre.md` et parfois les chapitres voisins pour savoir ce qui manque.

Dire « vérifier que `07.03` établit bien le lien entre découpage et validation locale, sans dupliquer `07.01` ni `07.02`, avec un exemple distinct » devient déjà une vraie unité de validation. Le lecteur sait ce qu'il doit regarder, ce qu'il n'a pas à rouvrir et selon quelle logique il accepte le résultat.

Même principe en logiciel: « refactorer le service » est trop vaste. « garantir que la fonction de parsing respecte le contrat d'entrée/sortie et passe tel jeu de tests » est vérifiable localement.

## Règle pratique

Ne découpe pas jusqu'à ce que ce soit petit. Découpe jusqu'à ce que ce soit **jugable sans tribunal général**.

## Renvoi éventuel

La structure minimale des livrables est posée dans `../06-repenser-un-projet/03-Interfaces,-validations-et-livrables.md`. La nature de la preuve attendue est détaillée dans `../10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`.
