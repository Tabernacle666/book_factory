---
id: "09"
title: "Piloter les collègues IA"
parent: null
level: chapter
status: draft
owner_concept: "pilotage-agents"
summary: >
  Ce chapitre montre que piloter des collègues IA ne consiste ni à leur parler
  vaguement ni à leur abandonner un problème entier. Il s'agit d'assigner un rôle,
  de borner un périmètre, de choisir les intrants légitimes, puis de décider à quel
  moment déléguer, vérifier, reprendre la main ou orchestrer plusieurs contributions.
  Il prépare le chapitre sur la validation en rappelant qu'un bon pilotage réduit déjà
  une grande partie de la dérive.
sections:
  - "09.01"
  - "09.02"
  - "09.03"
---

# Piloter les collègues IA

À ce stade du livre, la posture a changé, le projet a été redécoupé et les interfaces ont été rendues plus nettes. Il reste pourtant un point où beaucoup de pratiques déraillent encore : **faire travailler concrètement des agents textuels sans tomber ni dans l'illusion d'autonomie, ni dans le micro-contrôle stérile**. Ce chapitre ouvre ce problème au cœur de la **Partie IV — Changer de posture**. Il marque le passage entre la grammaire générale d'une équipe hybride et le geste plus précis du pilotage local.

La thèse est simple. Une IA utile dans un projet n'est pas un oracle auquel on soumet indistinctement des problèmes. C'est un collègue sous contrainte, dont l'efficacité dépend de la précision du rôle attribué, de la netteté du périmètre confié, de la qualité des intrants fournis et de la possibilité de reprendre la main sans friction. Le pilotage ne commence donc pas au moment où l'on corrige une sortie décevante ; il commence bien plus tôt, au moment où l'on définit ce que cet agent peut faire, ce qu'il ne doit pas faire, sur quelle base il travaille et à quelles conditions sa contribution peut entrer dans le flux.

Ce chapitre a une fonction décisive dans la macro-structure du livre : il transforme la collaboration propre en **gouverne réelle**. Tant que ce point n'est pas stabilisé, la validation ressemble à une police de secours et le contexte ressemble à un sac de transport pour ambiguïtés. Une fois stabilisé, le lecteur peut comprendre que les chapitres suivants ne sont pas des rustines, mais le prolongement logique d'un pilotage bien conçu. Mieux piloter, c'est déjà diminuer la dérive avant qu'elle devienne visible, réduire la dette de vérification et rendre l'autonomie locale plus féconde.

Les trois sections suivent cette trajectoire. La première borne le rôle, le périmètre et les intrants. La deuxième montre quand déléguer et quand reprendre la main. La troisième aborde l'orchestration de plusieurs agents, non comme un spectacle de complexité, mais comme une composition sobre de contributions locales. Le lecteur doit sentir que la puissance d'un dispositif multi-agents ne vient pas de son nombre, mais de la qualité de sa gouverne.

Le chapitre 9 ferme ainsi la partie la plus directement organisationnelle du livre. Il donne un visage concret à l'idée de domestication : non pas empêcher l'outil d'exister, mais lui faire tenir une place utile, bornée, inspectable. À partir de là, la **Partie V — Domestiquer les LLM** peut s'ouvrir pleinement, avec ses disciplines de validation, de contexte, de gouvernance textuelle et de cadence courte.

## Sections
- [Rôle, périmètre et intrants](01-Rôle,-périmètre-et-intrants.md)
- [Quand déléguer et quand reprendre la main](02-Quand-déléguer-et-quand-reprendre-la-main.md)
- [Orchestration de plusieurs agents](03-Orchestration-de-plusieurs-agents.md)

## Ce que le lecteur doit comprendre en sortant
- un agent devient utile quand son rôle, son périmètre et ses intrants sont explicitement bornés ;
- déléguer n'est pas transférer un problème entier, mais confier une portion du travail dont la reprise reste maîtrisable ;
- la qualité du résultat dépend autant de l'architecture de la délégation que de la qualité intrinsèque du modèle ;
- reprendre la main n'est pas un échec du dispositif, mais une fonction normale du pilotage ;
- l'orchestration de plusieurs agents n'a de sens que si leurs contributions sont composables, auditables et reconnectables ;
- un bon pilote réduit déjà la dérive avant même l'étape formelle de validation.

## Place dans la progression du livre
Le chapitre 8 montrait comment plusieurs acteurs peuvent coopérer sans se recouvrir. Le chapitre 9 montre maintenant comment un humain pilote explicitement des collègues IA à l'intérieur de cette structure. Ce passage est décisif, parce que beaucoup d'usages échouent non faute de modèle performant, mais faute de gouverne locale : rôle trop large, intrants mal choisis, reprise tardive, ou orchestration prématurée. Une fois ce pilotage rendu plus lisible, le livre peut ouvrir le chapitre 10, qui formalise la validation et la lutte contre les hallucinations non comme une réaction de panique, mais comme une discipline continue.

## Erreur de lecture à éviter
Il ne faut pas lire ce chapitre comme un manuel de micro-management obsessionnel où l'humain devrait contrôler chaque mot produit. L'objectif n'est pas d'étouffer l'agent sous des consignes infinies, ni d'interdire toute autonomie locale. L'objectif est de calibrer correctement cette autonomie pour qu'elle reste réversible, vérifiable et productive. Un pilotage trop vague crée de la dérive ; un pilotage trop étroit tue le rendement. Le bon niveau est celui qui maximise la contribution locale tout en gardant le système gouvernable.

## Transition vers le chapitre suivant
Le chapitre 9 clarifie donc la fonction du pilote : cadrer, déléguer localement, surveiller les signaux faibles et reprendre la main au bon moment. La suite logique est le chapitre 10, qui transforme cette gouverne en discipline de preuve : une contribution pilotée ne devient acceptable qu'à condition de pouvoir être vérifiée, contestée et réintégrée sans foi aveugle.
