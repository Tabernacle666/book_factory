---
id: "02.03"
title: "Intégration contre fabrication"
parent: "02"
level: section
status: draft
owner_concept: "evolution-du-code-03"
summary: >
  Montre que l'histoire du code déplace progressivement la valeur de la
  fabrication ex nihilo vers l'intégration de briques existantes.
---

# Intégration contre fabrication

## Idée centrale

L’histoire du code n’est pas celle d’une pure accumulation de puissance individuelle. C’est aussi l’histoire d’un déplacement de valeur: plus les bibliothèques, frameworks, services et standards se sont accumulés, moins il devenait rationnel de tout fabriquer soi-même. La compétence décisive s’est donc déplacée, peu à peu, vers l’intégration.

## Pourquoi c'est important

Beaucoup de discours nostalgiques présentent l’intégration comme une forme inférieure de programmation, comme si le vrai mérite résidait uniquement dans l’invention de chaque brique. C’est une erreur. Dans un système réel, faire coopérer des composants hétérogènes, sous contraintes de performance, de sécurité, de dette et de maintenance, demande un jugement supérieur à celui d’une simple fabrication isolée.

## Erreur classique

Confondre "j’ai moins écrit" avec "j’ai moins produit de valeur". Un projet peut contenir moins de code inédit et pourtant exiger davantage d’intelligence structurelle: choix d’outils, compatibilité d’interfaces, découpage du domaine, protocole de validation, orchestration des dépendances, gouvernance du changement.

## Méthode concrète

Pour évaluer proprement une tâche technique, demande toujours:

1. **Cette brique existe-t-elle déjà de façon fiable ?**
2. **Le coût principal est-il dans la fabrication ou dans l’assemblage ?**
3. **La différenciation du projet vient-elle du code lui-même ou de la bonne composition du système ?**
4. **Qu’est-ce qui sera le plus cher à maintenir dans six mois ?**

Quand la réponse montre que l’assemblage domine, la bonne posture n’est pas de reconstruire par orgueil. C’est de définir des contrats stables, de choisir des briques adaptées et de limiter la dette d’intégration.

## Mini exemple

Créer un moteur d’authentification, un ORM, un système de journalisation et une couche de transport maison peut flatter l’ego d’une équipe. Mais si le projet réel consiste surtout à faire coopérer des services, des règles métier et des validations, la valeur ne vient plus de la fabrication de chaque pièce. Elle vient de la capacité à articuler des éléments fiables sans faire exploser la complexité.

## Règle pratique

Plus l’écosystème mûrit, plus la compétence noble devient: **choisir, cadrer, relier et vérifier**.

## Renvoi éventuel

Pour la suite logique vers l’ère des LLM, voir `05-nailgun-et-changement-de-posture/01-Pourquoi-la-métaphore-du-nailgun-fonctionne.md`.
