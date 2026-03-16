---
id: "09.02"
title: "Quand déléguer et quand reprendre la main"
parent: "09"
level: section
status: draft
owner_concept: "pilotage-agents-02"
summary: >
  Formalise les seuils de délégation utile, les seuils de reprise humaine et les
  signaux faibles qui annoncent une dérive avant qu'elle ne devienne coûteuse.
---

# Quand déléguer et quand reprendre la main

## Idée centrale

On délègue à un agent quand la tâche est assez claire pour produire un artefact local utile, et on reprend la main dès que la clarté du contrat devient inférieure au coût de correction. La bonne question n'est donc pas « est-ce que l'IA peut le faire ? », mais « puis-je encore vérifier, corriger ou rejeter cette contribution sans réouvrir tout le problème ? ». Tant que la réponse est oui, la délégation reste saine. Dès que la réponse devient non, il faut raccourcir la boucle et reprendre le pilotage humain.

## Pourquoi c'est important

Le danger principal n'est pas seulement l'erreur visible. C'est la dérive silencieuse : l'agent avance, produit beaucoup, semble cohérent, mais s'éloigne progressivement du vrai besoin, des bonnes hypothèses ou du bon périmètre. Plus cette dérive dure, plus le coût de reprise augmente. On ne corrige plus un artefact local ; on doit remonter plusieurs décisions implicites, des simplifications douteuses et parfois une architecture entière de réponses plausibles mais mal fondées.

C'est pour cela qu'une bonne délégation n'est jamais une disparition du pilote. C'est une délégation sous surveillance légère, avec possibilité de reprise rapide. Le rôle du pilote est moins de corriger phrase par phrase que de détecter assez tôt les moments où l'agent commence à travailler à la place du projet plutôt qu'à son service.

## Erreur classique

L'erreur classique consiste à déléguer trop tôt une tâche encore mal découpée, puis à persister trop longtemps parce que l'agent « produit quand même quelque chose ». Cette persistance rassure à court terme, mais elle masque un fait simple : une sortie abondante n'est pas une preuve que la tâche était bien délégable. Souvent, c'est l'inverse. Plus l'agent compense des zones floues, plus il remplit les vides par ses propres choix implicites.

L'autre erreur, symétrique, consiste à reprendre la main beaucoup trop tard, au moment où plusieurs livrables dépendants ont déjà été produits sur une base incertaine. À ce stade, la reprise humaine n'est plus une vérification locale. C'est une opération de sauvetage.

## Quand déléguer

On peut déléguer une tâche si quatre conditions minimales sont réunies :

1. **l'objectif local est explicite** ;
2. **le périmètre de modification est borné** ;
3. **les intrants légitimes sont connus** ;
4. **la sortie attendue peut être validée sans reconstituer tout le contexte**.

Autrement dit, on délègue surtout quand la tâche ressemble déjà à un module court avec contrat clair. L'agent est alors bon pour produire, comparer, reformuler, structurer, auditer localement ou proposer des options dans un espace déjà borné. Il est beaucoup moins fiable quand on lui demande d'inventer à la fois la mission, la structure de la mission, les critères de réussite et la preuve que cette réussite est réelle.

## Quand reprendre la main

Il faut reprendre la main dès qu'un des seuils suivants est franchi :

- **le périmètre déborde** : l'agent modifie ou réécrit au-delà de la zone autorisée ;
- **les hypothèses se multiplient** : il commence à compléter le besoin au lieu de traiter le besoin ;
- **la vérification devient trop chère** : relire ou auditer la sortie coûte presque autant que refaire correctement la tâche ;
- **la traçabilité disparaît** : on ne sait plus sur quelles sources, conventions ou décisions la sortie repose ;
- **la correction locale ne suffit plus** : pour réparer une erreur, il faut réouvrir plusieurs sous-problèmes en chaîne.

Reprendre la main ne signifie pas forcément refaire soi-même. Cela peut vouloir dire : reclarifier le contrat, réduire le quantum, changer les intrants, séparer production et vérification, ou transformer une tâche de génération en tâche de comparaison. Mais dans tous les cas, le pilote réintervient pour restaurer la gouvernabilité locale.

## Signaux faibles de dérive

La dérive n'apparaît pas toujours sous forme de faute flagrante. Elle commence souvent par de petits indices :

- le texte devient plus lisse que précis ;
- des généralités remplacent les contraintes concrètes ;
- l'agent répond à la catégorie du problème au lieu de répondre au problème lui-même ;
- les formulations semblent plausibles, mais on ne voit plus quelle preuve les soutient ;
- l'agent introduit des micro-décisions qui n'étaient ni demandées ni autorisées ;
- chaque itération corrige une surface locale sans réduire l'incertitude de fond.

Ces signaux sont précieux parce qu'ils arrivent avant l'échec massif. Ils servent à raccourcir la boucle tant qu'il est encore peu coûteux de le faire.

## Méthode concrète

Une règle simple consiste à piloter la délégation avec un test en trois questions avant et après chaque boucle courte.

### Avant de déléguer
- **Que doit produire l'agent, exactement ?**
- **Que n'a-t-il pas le droit d'inventer, modifier ou décider ?**
- **Comment sa sortie sera-t-elle validée localement ?**

Si l'une des trois réponses est floue, la tâche n'est pas prête. Il faut la réduire ou la redéfinir.

### Après la production
- **La sortie répond-elle bien au contrat local ?**
- **Le coût de vérification reste-t-il faible ?**
- **La prochaine étape est-elle plus claire qu'avant ?**

Si la sortie rend la suite plus floue, plus chère à vérifier ou plus dépendante d'un contexte implicite, il faut reprendre la main immédiatement. Un bon cycle de délégation doit réduire l'incertitude, pas la déplacer.

## Mini exemple

Supposons qu'un agent doive compléter une section de cours. La délégation est saine si on lui confie un seul fichier, avec chapitre parent, sections sœurs et format attendu. Le pilote peut alors vérifier rapidement : idée centrale, absence de duplication, mini exemple, règle pratique, cohérence locale.

En revanche, si on lui demande de « renforcer le chapitre 9 pour préparer les cas pratiques » sans autre borne, la délégation devient mauvaise. L'agent peut toucher plusieurs sections, réorganiser les concepts, déplacer des frontières éditoriales et créer une dette de relecture disproportionnée. Dans ce cas, le bon geste n'est pas d'insister. C'est de reprendre la main, de réduire la mission à un nœud précis, puis de relancer une boucle plus courte.

## Règle pratique

Délègue seulement ce que tu peux auditer rapidement et reprendre localement. Dès que la reprise exige de remonter plusieurs décisions implicites, la délégation était trop large.

## Renvoi éventuel

Cette logique devient encore plus robuste quand la tâche reste courte, locale et rapidement auditable. Pour transformer cette reprise en discipline de preuve plutôt qu'en intuition de pilote, voir `../10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`.
