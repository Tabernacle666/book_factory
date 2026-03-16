---
id: "07.02"
title: "Découpage par interface"
parent: "07"
level: section
status: draft
owner_concept: "decoupage-du-travail-02"
summary: >
  Montre comment découper un projet à partir des interfaces et contrats plutôt
  qu'à partir des ego, des personnes ou des intuitions vagues.
---

# Découpage par interface

## Idée centrale

Découper par interface consiste à séparer le travail selon les points de contact stables entre sous-systèmes, plutôt que selon les préférences personnelles, les technologies à la mode ou les frontières arbitraires d’équipe. Une interface bien définie permet à plusieurs acteurs d’avancer en parallèle sans se marcher dessus.

## Pourquoi c'est important

Quand plusieurs agents IA ou plusieurs personnes collaborent, le vrai problème n’est pas seulement “qui fait quoi”. C’est surtout “qu’est-ce qui se transmet entre eux, sous quelle forme, avec quelle stabilité et quelles hypothèses ?”. Sans interface nette, chaque contribution emporte du contexte implicite et crée du recouvrement.

## Erreur classique

Découper le projet par composants visibles du moment: un développeur prend “le backend”, un autre “le frontend”, un troisième “la QA”, sans définir précisément les contrats d’échange. Ce type de découpage semble naturel, mais il produit rapidement des allers-retours, des ambiguïtés sur les responsabilités et des corrections tardives.

## Méthode concrète

Pour découper par interface:

1. **Identifier les zones d’échange réelles.**
2. **Nommer les intrants et extrants attendus.**
3. **Fixer le format ou le contrat minimal.**
4. **Définir qui garantit quoi.**
5. **Prévoir un test local de conformité.**

Une interface n’a pas besoin d’être complexe. Elle doit surtout être explicite, stable et suffisante pour permettre un travail orthogonal.

## Mini exemple

Dans ce cours, un agent peut rédiger une section, un autre vérifier la non-duplication et un troisième intégrer dans le PDF final. Le découpage n’est pas “trois personnes travaillent sur le même chapitre”, mais “trois rôles échangent des artefacts définis: texte local, audit local, build final”. L’interface entre eux rend la collaboration propre.

## Règle pratique

Quand deux acteurs doivent beaucoup se parler pour comprendre ce qu’ils échangent, l’interface n’est pas encore assez claire.

## Renvoi éventuel

Pour le protocole plus général des contrats, voir `08-collaboration-orthogonale/02-Définir-des-contrats-stables.md`.
