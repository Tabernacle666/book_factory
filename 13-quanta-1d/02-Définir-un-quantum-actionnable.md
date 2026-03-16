---
id: "13.02"
title: "Décomposer en ligne droite"
parent: "13"
level: section
status: draft
owner_concept: "quanta-1d"
summary: >
  Cette section définit le quantum 1D comme une unité de parcours suivie du début
  à la fin sans changement de problème en cours de route.
---

# Décomposer en ligne droite

Un quantum 1D peut se définir de manière très simple: **une entrée principale, une transformation principale, une sortie principale et un critère de validation principal**. Cette définition est volontairement austère. Elle évite de retomber dans des descriptions vagues du type « tâche bien cadrée » ou « petit lot raisonnable ». Ce qui compte n'est pas le sentiment de simplicité, mais la possibilité de suivre la trajectoire sans bifurquer vers un autre problème en cours de route.

Prenons un exemple en opérations. Un centre de services reçoit des signalements d'incidents hétérogènes. Transformer un incident brut en ticket structuré, classé et assignable selon une taxonomie déjà définie forme un quantum 1D robuste. L'entrée est le signalement brut. La transformation est la structuration selon des règles connues. La sortie est un ticket normalisé. La validation principale consiste à vérifier que les champs requis sont remplis correctement, que la classe est cohérente et que l'assignation potentielle correspond bien au référentiel. En revanche, si la même mission demande en plus de diagnostiquer la cause racine, de proposer un plan d'amélioration du processus, d'estimer le coût d'interruption et de préparer la communication client, elle cesse d'être un quantum 1D.

Cette manière de décomposer ne demande pas de réduire artificiellement toute activité à des gestes minuscules. Elle demande de choisir le bon niveau où une trajectoire reste gouvernable. Une direction financière peut très bien confier un travail substantiel à un agent tant que la ligne est claire: par exemple transformer des écritures déjà contrôlées en note de synthèse standardisée sur les écarts de marge par région. La mission peut être longue et demander de la rigueur, mais elle reste une ligne si elle ne doit pas en même temps décider de la politique commerciale, renégocier les hypothèses comptables et préparer les éléments de défense pour les actionnaires. De la même manière, une équipe marketing peut demander une cartographie des variantes de messages testées sur une campagne et de leurs performances relatives ; elle cesse d'être en 1D au moment où elle exige dans le même mouvement une nouvelle stratégie de marque, un plan média révisé et un arbitrage entre acquisition et fidélisation.

Le critère le plus utile pour repérer un vrai quantum n'est pas sa taille apparente, mais la qualité de la reprise possible. Si la sortie est contestée, peut-on corriger ce morceau sans rouvrir tout le reste ? Si oui, on tient probablement une bonne unité. Si non, c'est souvent que l'on a compressé plusieurs trajectoires sous un seul intitulé. C'est ici que le chapitre 7 sur le découpage et le chapitre 10 sur la validation se rejoignent le plus nettement: un bon morceau n'est pas seulement délégable, il est aussi **réparable localement**.

Le 1D aide également à mieux distribuer le travail entre humain et agent. Certaines trajectoires peuvent être largement confiées à un agent parce qu'elles reposent sur des règles stables et des validations fermes. D'autres doivent rester plus humaines parce qu'elles impliquent un arbitrage, une responsabilité politique ou une lecture du contexte organisationnel plus large. Le quantum 1D ne dit pas que tout doit être automatisé. Il dit que toute délégation sérieuse commence par l'identification d'une trajectoire nette.

## Mini exemple
Une DRH veut réduire le temps de mise en route des nouvelles recrues sur trois sites. Une demande mal découpée serait: « analyse les retours des managers, propose le nouveau parcours d'onboarding, chiffre le budget de formation, arbitre ce qui doit être centralisé ou local, rédige la note au comité exécutif et prépare la communication pour les équipes ». Tout cela appartient au même sujet, mais pas à la même trajectoire. La demande mélange diagnostic, conception, arbitrage budgétaire, décision d'organisation et communication.

Une trajectoire 1D plus saine commencerait par un lot beaucoup plus net: « à partir des questionnaires d'intégration, des tickets RH et des entretiens de fin de première semaine, regroupe les frictions récurrentes en sept catégories, mesure leur fréquence par site et livre un tableau consolidé avec trois verbatims anonymisés par catégorie ». L'entrée principale est un corpus de retours déjà collectés. La transformation principale consiste à classer et consolider selon une grille fixée. La sortie principale est un tableau comparable entre sites. La validation principale vérifie la traçabilité des catégories, l'absence de doublons évidents, la cohérence des volumes et l'anonymisation correcte des verbatims.

À partir de cette sortie, une deuxième trajectoire pourra demander quels irritants doivent être traités en central et lesquels relèvent d'ajustements locaux. Une troisième trajectoire, distincte, préparera ensuite la note de décision et les éléments de communication. La direction RH traite toujours le même problème d'onboarding, mais elle évite de demander au même flux de faire en une seule passe le diagnostic, l'arbitrage et la traduction politique du résultat.

## Règle pratique
Pour tester un quantum, essaie de compléter mentalement cette phrase: « à partir de X, transformer selon Y, pour livrer Z, validé par W ». Si l'un de ces éléments se dédouble immédiatement, la trajectoire est probablement encore trop mélangée.
