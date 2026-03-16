---
id: "03.01"
title: "Des systèmes experts aux modèles génératifs"
parent: "03"
level: section
status: draft
owner_concept: "histoire-des-ia-01"
summary: >
  Situe la trajectoire qui mène des systèmes experts aux modèles génératifs sans
  noyer l'étudiant dans une chronologie encyclopédique.
---

# Des systèmes experts aux modèles génératifs

## Idée centrale

L’histoire récente de l’IA peut se lire comme une succession de déplacements du lieu où l’on met l’intelligence. Avec les systèmes experts, on mettait surtout l’effort dans les règles écrites à la main. Avec l’apprentissage statistique, on a déplacé cet effort vers les données, les métriques et l’optimisation. Avec le deep learning puis les modèles génératifs, on a déplacé encore une fois le centre de gravité vers des modèles capables d’absorber d’immenses corpus et de produire des sorties plausibles dans des espaces beaucoup plus vastes.

Cette trajectoire n’est pas une marche magique vers une intelligence générale. C’est plutôt une série de compromis techniques qui ont rendu certaines tâches plus opérables, puis d’autres. Ce qui compte pour ce cours n’est donc pas de retenir toutes les dates, mais de comprendre que chaque étape a changé la manière de découper le travail humain autour de la machine.

## Pourquoi c'est important

Sans cette chronologie minimale, on interprète mal les LLM. Soit on les réduit à un simple auto-compléteur glorifié, soit on les confond avec une conscience logicielle en train d’émerger. Les deux lectures sont pauvres. Les LLM arrivent après des décennies de tentatives pour capturer, formaliser, optimiser puis généraliser des comportements utiles sur des tâches de plus en plus variées.

Comprendre cela aide à garder une posture adulte: les outils changent réellement d’échelle, mais ils ne surgissent pas hors de l’histoire. Ils héritent d’une longue évolution des abstractions, des capacités de calcul, des corpus disponibles et des manières de mesurer la performance.

## Erreur classique

L’erreur classique consiste à raconter l’histoire de l’IA comme une ligne droite allant de l’échec ancien vers le triomphe final. Ce récit efface les cycles d’enthousiasme, les périodes de refroidissement, les changements d’objectifs et les limites persistantes. Il pousse aussi à croire qu’un nouvel outil efface totalement les couches précédentes.

En pratique, les anciennes logiques ne disparaissent pas. Les règles explicites, les contrôles déterministes, les algorithmes spécialisés et les modèles statistiques classiques gardent une place. Les LLM n’abolissent pas tout cela; ils s’ajoutent à la pile et déplacent la frontière entre ce qu’on automatise par structure fixe et ce qu’on automatise par approximation guidée.

## Méthode concrète

Pour garder une chronologie utile, il suffit de retenir quatre paliers.

D’abord, les **systèmes experts**: on encode à la main des règles et des arbres de décision pour capturer un savoir métier local. Ensuite, le **machine learning statistique**: on apprend à partir d’exemples et on cherche des signaux robustes dans les données. Puis le **deep learning**: on augmente l’échelle des modèles et leur capacité à extraire des représentations complexes. Enfin, les **modèles génératifs à grande échelle**: on ne se contente plus de classer ou de prédire un score; on produit du texte, du code, des images ou des plans plausibles à partir d’un contexte.

Pour ce cours, cette grille suffit. À chaque palier, pose toujours les mêmes questions: qu’est-ce qui est codé explicitement, qu’est-ce qui est appris, qu’est-ce qui devient réutilisable, et quel type de supervision humaine reste nécessaire.

## Mini exemple

Un système expert pour le diagnostic suit un ensemble de règles du type « si symptôme A et symptôme B, alors piste C ». Un modèle statistique de scoring apprend, lui, à pondérer des variables observées à partir d’exemples passés. Un réseau profond de vision apprend des représentations intermédiaires à partir d’images. Un LLM, enfin, peut reformuler un problème, proposer une structure de document, générer un squelette de code ou résumer un échange, à condition d’être cadré.

L’exemple montre le déplacement principal: on passe d’une machine qui applique un savoir encodé localement à une machine qui manipule des régularités apprises à grande échelle. Cela change les usages possibles, mais aussi la façon dont un humain doit définir, vérifier et intégrer les sorties.

## Règle pratique

Retenir l’histoire de l’IA ne sert pas à briller avec des dates. Cela sert à éviter les contresens. Garde une chronologie courte, orientée par les changements de posture humaine autour de la machine, pas par l’accumulation de noms de chercheurs ou d’archives.

## Renvoi éventuel

La rupture opérationnelle spécifique des LLM est développée dans `02-Ce-que-change-le-LLM.md`. Les limites fortes et le faux hype sont traités dans `../04-faux-hype-et-limites-des-llm/chapitre.md`.
