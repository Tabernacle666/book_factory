---
id: "10"
title: "Limiter les hallucinations et maintenir la validation"
parent: null
level: chapter
status: draft
owner_concept: "hallucinations-et-validation"
summary: >
  Ce chapitre montre que les hallucinations ne se traitent pas comme un défaut
  marginal du modèle mais comme un risque normal de production. Il transforme la
  validation en discipline continue, articulée avec le périmètre des tâches, la
  séparation entre génération et vérification, et l'exigence d'artefacts testables.
  Il prépare le chapitre sur le contexte en montrant qu'une bonne validation dépend
  aussi de la propreté des intrants.
sections:
  - "10.01"
  - "10.02"
  - "10.03"
---

# Limiter les hallucinations et maintenir la validation

## Thèse du chapitre
Le problème des hallucinations n'est pas seulement que les modèles peuvent se tromper. Le vrai problème est qu'ils peuvent produire des sorties **plausibles**, fluides et localement convaincantes alors même qu'elles ne reposent pas sur une base suffisante, qu'elles excèdent leur mandat, ou qu'elles prennent silencieusement des décisions qui n'ont jamais été validées. Tant que ce risque est traité comme une anomalie ponctuelle, on réagit trop tard : on corrige après coup, on renforce les consignes, puis on s'étonne que le système reste fragile.

Ce chapitre défend donc une idée plus dure : la validation n'est pas l'étape terminale où l'on rassure un résultat déjà produit. C'est une **discipline de conception** qui commence dès le cadrage de la tâche, se poursuit dans la séparation des rôles entre produire et vérifier, puis s'achève dans l'exigence d'artefacts contrôlables. Réduire les hallucinations, ici, ne veut pas dire espérer des sorties parfaites ; cela veut dire rendre les erreurs plus rares, plus visibles, plus localisées et moins coûteuses à reprendre.

## Pourquoi ce chapitre existe
Le chapitre précédent montrait comment piloter des collègues IA : borner leur rôle, choisir leurs intrants, décider quand déléguer et quand reprendre la main. Mais même bien piloté, un agent reste capable de formuler des réponses fausses, incomplètes ou prématurément assurées. Il fallait donc un chapitre qui transforme cette limite connue en architecture de travail plutôt qu'en source de méfiance diffuse.

Ce chapitre existe pour éviter deux dérives symétriques. La première consiste à croire qu'un bon prompt suffit à éliminer le risque. La seconde consiste à conclure qu'un modèle non parfaitement fiable ne peut pas entrer dans un dispositif sérieux. Le point juste est intermédiaire : on ne supprime pas le risque, on **l'organise**. Cette organisation prépare directement le chapitre 11 sur le contexte. En effet, une validation rigoureuse dépend aussi de la qualité du terrain informationnel sur lequel le modèle travaille : contexte trop large, historique sale, intrants mélangés et preuves implicites rendent toute vérification plus coûteuse.

## Ce que le lecteur doit comprendre en sortant
À la fin de ce chapitre, le lecteur doit pouvoir tenir ensemble six idées :
- une hallucination n'est pas seulement une erreur factuelle ; c'est toute sortie qui affirme au-delà de ce qui est légitimement fondé ou vérifiable ;
- on réduit la dérive en diminuant le périmètre confié avant même de discuter de la qualité du modèle ;
- produire et vérifier sont deux fonctions différentes, qu'il faut séparer au moins mentalement et souvent opérationnellement ;
- une sortie utile n'est pas seulement plausible : elle doit laisser derrière elle une forme de preuve, de trace ou d'artefact contrôlable ;
- la validation coûte moins cher quand elle porte sur un objet local, borné et bien documenté ;
- la qualité du contexte conditionne directement la qualité de la validation à venir.

## Sections
- [Réduire le périmètre des tâches](01-Réduire-le-périmètre-des-tâches.md)
- [Séparer génération et vérification](02-Séparer-génération-et-vérification.md)
- [Exiger des artefacts vérifiables](03-Exiger-des-artefacts-vérifiables.md)

## Place dans la progression du livre
Le chapitre 9 expliquait comment cadrer et piloter les collègues IA. Le chapitre 10 ajoute maintenant la discipline qui empêche ce pilotage de rester nominal. C'est ici que le livre rend explicite une règle structurante : aucune délégation n'est réellement maîtrisée si la sortie produite ne peut pas être vérifiée localement, contestée proprement et réintégrée sans foi aveugle. Une fois ce cadre posé, le chapitre 11 peut traiter la gestion du contexte, non comme un sujet séparé, mais comme l'une des conditions matérielles de cette validation continue.

## Erreur de lecture à éviter
Il ne faut pas lire ce chapitre comme un plaidoyer pour une suspicion généralisée où chaque sortie d'IA devrait être présumée inutilisable. Le but n'est pas de neutraliser tout rendement sous prétexte de prudence. Le but est de construire un régime où la confiance ne repose ni sur l'enthousiasme ni sur le scepticisme, mais sur des dispositifs de preuve proportionnés. Une bonne validation ne ralentit pas aveuglément la production ; elle empêche surtout que des erreurs plausibles deviennent des dettes opaques.

## Mini exemple
Si un agent reçoit la consigne vague de « proposer l'architecture d'un module et commencer l'implémentation », il peut produire à la fois des choix de structure, des hypothèses techniques et du code prématuré, sans qu'on sache exactement quoi vérifier d'abord. Si au contraire on lui demande de produire seulement une proposition d'interface, une liste d'hypothèses explicites et trois critères de validation, la relecture devient courte, locale et décisive. Le problème n'était pas la bonne volonté du modèle ; c'était l'absence de frontière claire entre génération, décision et preuve.

## Règle pratique
Avant d'accepter une sortie, poser trois questions simples : **qu'est-ce qui a été produit, sur quelle base, et comment puis-je le vérifier sans relire tout le projet ?** Si l'une de ces trois réponses reste floue, la tâche est probablement trop large, le contexte trop sale, ou l'artefact de sortie mal choisi.

## Passage explicite au chapitre suivant
Le chapitre 10 montre ainsi que la validation n'est pas un contrôle terminal ajouté après coup, mais une propriété préparée par le découpage, le pilotage et les artefacts demandés. Il devient alors nécessaire de traiter le support informationnel lui-même. Le chapitre 11 prend le relais sur ce point : sans contexte propre, même une bonne validation finit par coûter trop cher et trop tard. Autrement dit, avant même de demander au système de mieux raisonner, il faut cesser de le nourrir avec des intrants qui mélangent preuve, historique, bruit et consignes périmées.

## Renvois utiles
- [Piloter les collègues IA](../09-pilotage-agents/chapitre.md)
- [Maintenir un contexte propre et court](../11-contexte-propre-et-court/chapitre.md)
- [Exploiter la structure projet et les couches de prompt](../12-prompt-layering-openai/chapitre.md)
- [Scinder le travail en quanta 1D](../13-quanta-1d/chapitre.md)
