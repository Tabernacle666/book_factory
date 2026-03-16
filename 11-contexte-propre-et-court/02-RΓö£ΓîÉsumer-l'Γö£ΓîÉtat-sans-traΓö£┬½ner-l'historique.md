---
id: "11.02"
title: "Résumer l'état sans traîner l'historique"
parent: "11"
level: section
status: draft
owner_concept: "contexte-propre-et-court-02"
summary: >
  Formalise le résumé d'état comme transmission courte et exploitable, distincte
  de l'historique brut, afin de permettre une reprise propre.
---

# Résumer l'état sans traîner l'historique

## Idée centrale

Transmettre l'état d'un travail ne signifie pas transporter toute son histoire. Un **résumé d'état** est une reconstruction courte de ce qui doit être tenu pour vrai maintenant: où en est le nœud, ce qui est stable, ce qui manque, et ce qui est interdit d'inventer. Il remplace l'historique brut par une vue exploitable.

Cette distinction est décisive pour les équipes hybrides. L'historique montre comment on en est arrivé là. Le résumé d'état dit ce qu'un nouvel acteur doit savoir pour agir correctement sans rejouer les étapes intermédiaires.

## Pourquoi c'est important

Les agents et les rédacteurs reprennent mieux un travail quand ils héritent d'un état clair plutôt que d'une suite de traces. Sans résumé, chacun doit faire sa propre archéologie: il lit les anciennes releases, interprète les hésitations, et reconstruit lui-même la hiérarchie entre décisions fermes, essais provisoires et pistes abandonnées.

Le résumé d'état réduit ce coût. Il sert de point de passage entre deux itérations, entre un rédacteur et le suivant, ou entre une production locale et une intégration. Il est donc un outil de continuité, pas un luxe documentaire.

## Erreur classique

L'erreur classique consiste à utiliser le dernier échange ou le dernier diff comme résumé implicite. Or un diff ne dit pas toujours le statut conceptuel du nœud, et une conversation mélange souvent décision, exploration et bruit.

Autre erreur: produire un résumé trop narratif. S'il raconte tout, il redevient un historique déguisé. Un bon résumé n'explique pas chaque détour; il reconstruit un état actionnable.

## Méthode concrète

Un résumé d'état utile peut tenir en six lignes.

1. **Statut** — rédigé, partiel, à reprendre, verrouillé.
2. **Noyau stable** — ce qui est désormais acquis.
3. **Manque principal** — ce qui reste à compléter.
4. **Périmètre de reprise** — quels fichiers regarder pour continuer.
5. **Interdits** — ce qu'il ne faut pas rouvrir ni déplacer.
6. **Prochain pas** — l'action locale attendue.

Ce format permet à un nouvel acteur d'entrer vite dans le bon niveau de détail. Il évite aussi d'utiliser la mémoire conversationnelle comme système de passation.

## Mini exemple

Un bon résumé pour une release intermédiaire peut dire:

- statut: passe 2B ouverte;
- noyau stable: la fiche `intrants → livrable → validation → reprise` est désormais canonique;
- manque principal: formaliser la transmission d'état propre et le tri du contexte utile;
- périmètre de reprise: `08.03`, `11.01`, `11.02`, plus `11.03` pour le voisinage;
- interdits: ne pas ouvrir les use-case, ne pas relancer un diagnostic global;
- prochain pas: compléter `11.02` avec une méthode de résumé exploitable.

Cette synthèse permet une reprise immédiate. Relire tout l'historique des releases précédentes n'est plus nécessaire pour agir proprement.

## Règle pratique

Quand tu passes le relais, transmets un **état reconstruit** et non une pile de traces.

## Renvoi éventuel

Le tri entre contexte utile et contexte grenier est traité dans `01-Contexte-utile-contre-contexte-grenier.md`. La forme compacte du pack local à transmettre est posée dans `03-Construire-des-context-packs-minimaux.md`.
