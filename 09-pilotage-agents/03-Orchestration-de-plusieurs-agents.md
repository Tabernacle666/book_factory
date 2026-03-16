---
id: "09.03"
title: "Orchestration de plusieurs agents"
parent: "09"
level: section
status: draft
owner_concept: "pilotage-agents-03"
summary: >
  Donne une séquence simple pour piloter plusieurs agents sans collision ni brouillard.
---

# Orchestration de plusieurs agents

## Idée centrale

Plusieurs agents ne deviennent utiles que si leur ordre d'intervention, leur périmètre et leurs critères de sortie sont plus clairs que leur talent de génération.

## Pourquoi c'est important

Sans séquence, plusieurs agents produisent surtout du bruit parallèle. Ils dupliquent, se contredisent, se corrigent mutuellement sans fin ou gonflent le contexte commun. L'orchestration n'est pas une multiplication magique de puissance ; c'est une discipline de circulation des artefacts.

Dans une équipe, le vrai gain n'apparaît pas quand tout le monde travaille en même temps sur la même consigne vague. Il apparaît quand chaque intervention réduit l'ambiguïté pour la suivante. Un bon enchaînement d'agents ressemble donc moins à une table ronde qu'à une chaîne de relais courte, où chaque passage livre un objet utilisable par le rôle suivant.

## Erreur classique

Lancer trois ou quatre agents sur la même tâche vague en espérant qu'une vérité émergera de la compétition. Ce modèle peut donner des idées, mais il est mauvais pour une production régulière.

L'autre erreur consiste à laisser chaque agent relire tout l'historique, reformuler la mission à sa manière puis modifier librement le résultat précédent. On croit alors créer du contrôle croisé. En réalité, on supprime la responsabilité locale : personne ne sait plus qui décide, qui vérifie, ni à quel moment une sortie devient stable.

## Méthode concrète

Utiliser une séquence simple en quatre temps :
1. **cadreur** : reformule la tâche, fixe les intrants autorisés, le format de sortie et le point exact de handoff ;
2. **producteur** : génère le livrable local demandé, sans corriger le reste du système ;
3. **vérificateur** : audite le livrable selon les critères explicites, sans réinventer la tâche ;
4. **intégrateur** : décide si le résultat entre dans la structure du projet, demande une correction locale ou rejette.

Chaque agent reçoit un rôle étroit. Chaque passage laisse un artefact court : tâche clarifiée, livrable, rapport d'audit, décision d'intégration. Le handoff ne doit pas être une conversation diffuse, mais un paquet minimal transmis d'un rôle au suivant : ce qui entre, ce qui sort, ce qui reste interdit, et la question exacte à trancher.

Quand plusieurs équipes interviennent, il faut en plus verrouiller le moment où la responsabilité change de mains. Tant que le producteur n'a pas livré un artefact borné, le vérificateur ne commence pas à réécrire. Tant que le rapport d'audit n'est pas clos, l'intégrateur ne transforme pas l'observation en nouvelle mission générale. Cette discipline évite qu'un handoff inter-équipe se transforme en brouillard collectif.

## Mini exemple

Prenons une équipe marketing qui prépare une campagne de relance clients après une baisse de réachat. Le cadreur produit un brief très court : segment visé, offre autorisée, ton de marque, indicateurs à améliorer, format de sortie attendu pour l'email et la landing page. Le producteur rédige uniquement les messages et la structure de la page. Le vérificateur contrôle la cohérence des promesses, l'alignement avec l'offre réelle, la présence d'un appel à l'action mesurable et l'absence de claims non validés. L'intégrateur, côté direction marketing ou opérations CRM, décide alors soit de faire entrer la campagne dans le calendrier, soit de renvoyer une correction locale sur un point précis, par exemple une promesse trop large ou un segment mal ciblé.

Le handoff inter-équipe devient ici concret : l'équipe contenu ne transmet pas "une campagne à revoir", mais un paquet borné avec brief validé, version produite, points d'audit et décision attendue. L'équipe CRM n'a donc pas à reconstituer l'intention initiale dans un long fil de messages. Elle reçoit un artefact prêt à arbitrer.

## Règle pratique

Un agent de plus ne vaut que s'il retire une ambiguïté de rôle, de handoff ou de vérification. Sinon il ajoute du brouillard.

## Renvoi éventuel

Cette séquence devient bien plus fiable quand les tâches restent courtes, bornées et faciles à reprendre localement. Pour savoir à quel moment la boucle doit être interrompue et reprise par un pilote, voir `09-pilotage-agents/02-Quand-déléguer-et-quand-reprendre-la-main.md`.
