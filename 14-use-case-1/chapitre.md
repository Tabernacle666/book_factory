---
id: "14"
title: "Use case 1 — Besoin flou vers architecture d'agents"
parent: null
level: chapter
status: draft
owner_concept: "use-case-1"
summary: >
  Ce chapitre ouvre le premier cas pratique du livre. Il montre comment traduire
  un besoin encore flou en séquence de travail exploitable: clarification du mandat,
  découpage en sous-systèmes, définition des interfaces, attribution des rôles,
  validations locales et intégration finale. Il sert de démonstration guidée des
  chapitres 05 à 12 sans encore ouvrir le deuxième cas pratique.
sections:
  - "14.01"
  - "14.02"
  - "14.03"
---

# Use case 1 — Besoin flou vers architecture d'agents

## Thèse du chapitre
Le premier cas pratique existe pour montrer qu'un besoin initialement vague n'a pas besoin d'être parfaitement spécifié pour devenir actionnable. Ce qui compte n'est pas de tout savoir d'avance, mais de transformer l'ambiguïté en **cadre de décision progressif**: ce que l'on cherche à produire, ce qui reste encore hypothétique, ce qui devra être validé localement et ce qui devra être tenu hors périmètre tant que les frontières ne sont pas stables.

Ce chapitre défend donc une idée simple: on ne passe pas d'un besoin flou à une architecture d'agents par inspiration ou par empilement de prompts. On y passe en reconstruisant une chaîne courte et vérifiable: clarifier le besoin, découper en unités contrôlables, attribuer rôles et validations, puis intégrer sans perdre la maîtrise du système. Le cas pratique vaut comme démonstration parce qu'il force à appliquer la méthode du livre sur un terrain encore imparfait.

## Pourquoi ce chapitre existe
Jusqu'ici, le livre a construit les conditions de possibilité d'un travail hybride humain+IA: changement de posture, découpage, contrats, pilotage, validation, contexte propre, gouvernance textuelle et quanta 1D. Il fallait maintenant montrer ce que ces principes produisent lorsqu'on part d'une demande réaliste, c'est-à-dire incomplète, chargée d'implicites et potentiellement trompeuse si on la prend au pied de la lettre.

Ce chapitre existe aussi pour éviter un malentendu fréquent: croire qu'un use-case sert à illustrer après coup une théorie déjà comprise. Ici, le cas pratique est un **instrument de consolidation**. Il rend visibles les endroits où la méthode tient réellement, où elle exige une reprise de main, et où une bonne décision consiste à ne pas déléguer trop tôt. Il prépare la deuxième moitié du cas en montrant que le premier gain n'est pas la production de code, mais la stabilisation d'un problème.

## Ce que le lecteur doit comprendre en sortant
À la fin de ce chapitre, le lecteur doit pouvoir tenir ensemble six idées:
- un besoin flou n'est pas un défaut à effacer immédiatement, mais une matière à structurer par questions et hypothèses ;
- la première réussite d'un cas pratique n'est pas la solution finale, mais la construction d'un mandat exploitable ;
- les sous-systèmes utiles apparaissent après clarification du besoin, pas avant ;
- le découpage n'a de valeur que s'il prépare des validations locales et des handoffs nets ;
- une bonne attribution de rôles sépare production, vérification et intégration au lieu de les mélanger ;
- un use-case pédagogique doit montrer la méthode en action sans réintroduire de magie ni de raccourcis héroïques.

## Sections
- [Clarifier le besoin](01-Clarifier-le-besoin.md)
- [Découper en sous-systèmes et interfaces](02-Découper-en-sous-systèmes-et-interfaces.md)
- [Attribuer rôles, validations et intégration](03-Attribuer-rôles,-validations-et-intégration.md)

## Place dans la progression du livre
Le chapitre 14 ouvre maintenant la première preuve opératoire du livre. Il ne répète pas les chapitres précédents: il les **compose**. Le lecteur doit y voir comment les notions dispersées dans les chapitres 05 à 13 deviennent une séquence de travail continue sur un problème réaliste. Après le chapitre 13, l'attente n'est plus seulement de voir une méthode correcte, mais de constater qu'un besoin flou peut être reconstruit en trajectoires distinctes, chacune assez nette pour être déléguée, vérifiée puis reconnectée proprement.

Le fil interne du chapitre doit donc rester simple et visible. La section 14.01 ne cherche qu'à rendre le besoin exploitable. La section 14.02 transforme ce mandat en frontières, contrats et points de reprise. La section 14.03 n'ajoute pas une théorie supplémentaire : elle fait converger ces blocs vers une chaîne d'exécution responsable. Cette gradation est importante, parce qu'elle montre que la qualité du cas vient de l'ordre des décisions, pas d'une sophistication soudaine des agents.

## Erreur de lecture à éviter
Il ne faut pas lire ce cas comme la recette universelle d'une équipe d'agents déjà prête à l'emploi. Le but n'est pas de fournir un template magique qui transformerait n'importe quelle demande en organigramme fixe. Le but est d'apprendre à reconnaître les étapes minimales qui rendent une délégation sérieuse possible. Ce chapitre vaut moins comme modèle figé que comme démonstration de discipline.

## Mini exemple
Une demande telle que « on voudrait un assistant pour aider l'équipe support à traiter plus vite les tickets » paraît immédiatement exploitable. En réalité, elle mélange plusieurs questions: quels tickets, quelle aide, quel niveau d'autonomie, quelle preuve de qualité, quelle reprise humaine, quel système d'intégration ? Tant qu'on ne clarifie pas ces points, toute proposition d'architecture d'agents reste décorative. Le premier travail consiste donc à produire un cadre bref: objectif local, hors-périmètre, hypothèses ouvertes, critères d'acceptation et premiers intrants autorisés.

## Règle pratique
Quand un cas pratique démarre sur un besoin flou, ne cherche pas d'abord la meilleure architecture. Cherche d'abord le **plus petit cadre de décision** qui permet de distinguer ce qui est déjà exploitable de ce qui reste encore à découvrir.

## Passage explicite à la section suivante
La première étape consiste donc à rendre le besoin lisible sans lui faire dire plus qu'il ne dit déjà. La section 14.01 prend ce relais: elle montre comment passer d'une formulation vague à un mandat local, testable et transmissible.

## Renvois utiles
- [Repenser un projet de développement informatique](../06-repenser-un-projet/chapitre.md)
- [Scinder le travail proprement](../07-decoupage-du-travail/chapitre.md)
- [Piloter des collègues IA](../09-pilotage-agents/chapitre.md)
- [Limiter les hallucinations et maintenir la validation](../10-hallucinations-et-validation/chapitre.md)
