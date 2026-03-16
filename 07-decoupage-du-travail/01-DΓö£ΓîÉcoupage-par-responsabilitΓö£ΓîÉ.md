---
id: "07.01"
title: "Découpage par responsabilité"
parent: "07"
level: section
status: draft
owner_concept: "decoupage-du-travail-01"
summary: >
  Définit le découpage par responsabilité avec critères de qualité et anti-patterns.
---

# Découpage par responsabilité

## Idée centrale

On découpe mal un projet quand on le partage par morceaux de code. On commence à bien le découper quand chaque morceau porte une responsabilité intelligible, stable et vérifiable.

## Pourquoi c'est important

Une responsabilité se laisse discuter, attribuer, auditer et améliorer. Un simple paquet de fichiers, lui, devient vite une frontière arbitraire. Avec des agents IA, cette différence devient critique: un agent opère beaucoup mieux quand son rôle correspond à une intention nette plutôt qu'à une zone technique floue.

## Erreur classique

Découper par commodité locale: un peu de backend ici, un peu de validation là, un peu de documentation ailleurs, sans propriétaire clair. Cela produit des chevauchements, des trous et des livrables impossibles à juger sans relire l'ensemble.

Anti-patterns fréquents:
- une responsabilité qui dépend d'une autre à chaque phrase;
- un nœud qui mélange production, vérification et intégration;
- une section définie par la technologie au lieu du rôle réel;
- plusieurs acteurs qui peuvent modifier la même vérité sans protocole.

## Méthode concrète

Pour qu'une responsabilité soit bien découpée, elle doit satisfaire au moins trois critères:
1. **nommable**: on peut dire en une phrase ce que ce nœud produit ou protège;
2. **bornée**: on peut dire ce qui n'est pas de son ressort;
3. **auditable**: on peut vérifier localement si le résultat est bon.

Ensuite, on formule pour chaque nœud:
- son objectif;
- ses intrants autorisés;
- son extrant attendu;
- son critère d'acceptation;
- son interdit principal.

## Mini exemple

Mauvais découpage: « agent API », « agent docs », « agent tests » si chacun touche la même logique métier sans frontière claire.

Meilleur découpage: « agent contrat d'interface », « agent implémentation locale », « agent vérification des cas limites ». Les trois peuvent utiliser des outils similaires, mais leurs responsabilités ne se confondent pas.

## Règle pratique

Si deux nœuds ont besoin d'expliquer longtemps pourquoi ils ne font pas la même chose, ils sont probablement mal découpés.

## Renvoi éventuel

Pour stabiliser les jonctions entre ces responsabilités, voir `08-collaboration-orthogonale/02-Définir-des-contrats-stables.md`.
