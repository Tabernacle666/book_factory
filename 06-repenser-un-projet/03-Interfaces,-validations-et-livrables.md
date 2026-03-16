---
id: "06.03"
title: "Interfaces, validations et livrables"
parent: "06"
level: section
status: draft
owner_concept: "repenser-un-projet-03"
summary: >
  Formalise la grammaire minimale d'une unité de travail: interface,
  livrable, validation locale et point de reprise.
---

# Interfaces, validations et livrables

## Idée centrale

Une unité de travail n'est pas réellement délégable tant qu'on ne sait pas trois choses: **ce qui entre**, **ce qui sort** et **comment on juge la sortie**. Les interfaces, les validations et les livrables ne sont donc pas des détails administratifs. Ils constituent la forme minimale qui transforme une intention vague en travail transmissible.

Avec des agents IA, cette structure devient encore plus importante. Sans interface, le contexte déborde. Sans livrable, la tâche se dissout dans une conversation. Sans validation, on ne sait pas si l'on a produit quelque chose d'utile ou seulement quelque chose de plausible.

## Pourquoi c'est important

Beaucoup d'échecs attribués aux modèles viennent en réalité d'une unité de travail mal définie. On demande une amélioration, une analyse ou une implémentation sans préciser le contrat d'entrée, la sortie attendue et la preuve locale. L'agent remplit alors les blancs avec des hypothèses implicites. Le résultat peut sembler intelligent, mais il reste fragile à l'intégration.

À l'inverse, quand une tâche est décrite comme un petit contrat, elle devient beaucoup plus stable. On peut la confier, la reprendre, la vérifier et la réutiliser sans recharger tout le projet.

## Erreur classique

L'erreur classique consiste à ne définir que l'action: « rédige », « corrige », « améliore », « implémente ». Cette formulation ne dit rien sur les intrants autorisés, la forme du livrable ni le test de validité.

Autre erreur fréquente: croire que le livrable est le texte produit lui-même. En réalité, un bon livrable comprend souvent au moins deux couches: le contenu demandé et les éléments qui permettent de l'intégrer correctement, comme un périmètre, des hypothèses, une checklist ou un statut.

## Méthode concrète

Pour chaque unité de travail, formule une fiche minimale en cinq lignes:

1. **Objectif local** — ce que le nœud doit produire ou clarifier.
2. **Intrants autorisés** — fichiers, décisions, conventions, hypothèses explicites.
3. **Livrable attendu** — forme de sortie stable et courte.
4. **Validation locale** — test qui permet de dire oui/non sans relire tout le projet.
5. **Point de reprise** — ce qui reste humain ou ce qui doit être intégré ailleurs.

Cette fiche n'a pas besoin d'être lourde. Elle sert à empêcher qu'un acteur invente son propre terrain de jeu. Une interface claire limite ce qu'il peut consommer. Un livrable clair limite ce qu'il peut produire. Une validation claire limite ce que l'on accepte.

## Grammaire minimale des livrables

Avant les use-case, il suffit d'une famille courte de livrables récurrents:

- **note de cadrage locale**: but, périmètre, non-objectifs;
- **contrat d'interface**: intrants, extrants, format, responsabilité;
- **artefact produit**: texte, code, tableau, schéma, checklist;
- **preuve locale**: test, audit, checklist de conformité, écart signalé;
- **handoff**: ce qui est prêt à intégrer et ce qui reste ouvert.

Le point important est qu'un livrable ne vaut pas seulement par son contenu, mais par sa capacité à être repris sans ambiguïté.

## Mini exemple

Supposons qu'un agent doive compléter une section du cours.

Une demande floue dirait: « améliore la section 06.03 ».

Une unité de travail propre dirait plutôt:
- intrants: `chapitre.md`, `06.01`, `06.02`, conventions;
- livrable: une section Markdown complète avec idée centrale, erreur classique, méthode, mini exemple, règle pratique;
- validation: pas de duplication lourde avec `07.02`, présence d'un renvoi utile, possibilité de juger le texte localement;
- reprise: intégration éditoriale et vérification de cohérence globale.

Le second format ne rend pas l'agent plus brillant. Il rend la collaboration moins fragile.

## Règle pratique

Quand un nœud ne peut pas être décrit par **intrants → livrable → validation**, il n'est pas encore prêt à être délégué proprement.

## Renvoi éventuel

Le découpage d'une tâche par capacité de validation locale est développé dans `../07-decoupage-du-travail/03-Découpage-par-capacité-de-validation.md`. L'exigence de preuve concrète est prolongée dans `../10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`.
