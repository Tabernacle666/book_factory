---
id: "04.03"
title: "Ce que les LLM ne feront jamais tels quels"
parent: "04"
level: section
status: draft
owner_concept: "03-ce-que-les-llm-ne-feront-jamais-tels-quels"
summary: >
  Précise les limites fortes des LLM sans prophétie fragile ni effet dramatique.
---

# Ce que les LLM ne feront jamais tels quels

Un LLM ne devient pas, par simple accumulation de contexte, une conscience stable, un sujet responsable, ni un système de vérité autonome.

## Pourquoi c'est important

Cette limite impose une architecture de contrôle: contrats, validation, tests, revue, et découpage en livrables auditables. Tant qu'on oublie cela, on construit des workflows fondés sur l'illusion qu'un texte plus long produit mécaniquement plus de lucidité.

## Erreur classique

Imaginer qu'un très long prompt remplace une méthode de projet. L'autre erreur est de faire des prophéties vagues du type « bientôt il fera tout ». Ce genre d'énoncé n'aide ni à concevoir un système utile aujourd'hui, ni à former une discipline de travail.

## Méthode concrète

Parler de limites structurelles plutôt que de science-fiction. Un LLM, tel quel, ne fournit pas de garantie native sur:
- la vérité du monde;
- la stabilité de ses critères;
- la responsabilité morale de ses décisions;
- la mémoire fiable à long terme;
- la compréhension implicite de contraintes non écrites;
- la continuité d'un objectif complexe sans instrumentation externe.

La bonne réponse n'est pas de l'humilier ni de l'idolâtrer. La bonne réponse est d'externaliser la vérité dans les artefacts stables et de garder le modèle dans un rôle borné.

## Mini exemple

Le modèle peut proposer une architecture; il ne peut pas garantir seul qu'elle satisfait toutes les contraintes réelles non écrites, qu'elle survivra aux changements futurs, ni qu'elle engage une responsabilité claire en cas d'erreur. C'est pour cela qu'on lui demande un livrable, pas une souveraineté.

## Règle pratique

Ce qu'un humain ne peut pas auditer localement ne doit pas être délégué aveuglément à un LLM.

## Renvoi éventuel

La manière d'exploiter tout de même très fortement ces systèmes apparaît dans `05-nailgun-et-changement-de-posture/01-Pourquoi-la-métaphore-du-nailgun-fonctionne.md`.
