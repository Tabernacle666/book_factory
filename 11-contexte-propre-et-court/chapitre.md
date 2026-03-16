---
id: "11"
title: "Maintenir un contexte propre et court"
parent: null
level: chapter
status: draft
owner_concept: "contexte-propre-et-court"
summary: >
  Ce chapitre montre que le contexte n'est pas un grenier où l'on empile tout ce
  qui a été dit, mais un instrument de travail à garder propre, court et orienté
  vers la tâche. Il explique comment distinguer l'utile du bruit, transmettre un état
  sans traîner tout l'historique, puis composer des context packs minimaux. Il prépare
  le chapitre sur les couches de prompt en stabilisant ce qui relève du contexte et ce
  qui relève des conventions permanentes.
sections:
  - "11.01"
  - "11.02"
  - "11.03"
---

# Maintenir un contexte propre et court

## Thèse du chapitre
Lorsqu'une équipe travaille avec des IA, la tentation est grande de tout conserver : discussions précédentes, décisions anciennes, variantes abandonnées, notes intermédiaires, morceaux de code, rappels de stratégie, hypothèses temporaires. Cette accumulation rassure parfois, parce qu'elle donne l'impression de ne rien perdre. En pratique, elle dégrade souvent la qualité du travail : les signaux se mélangent, les priorités deviennent moins lisibles, les contradictions restent cachées et le modèle consomme une masse de texte qui augmente la plausibilité apparente sans augmenter la précision locale.

Ce chapitre défend donc une règle fondamentale : un bon contexte n'est pas le plus volumineux, mais le plus **pertinent et propre**. Le contexte doit aider une tâche locale à produire une sortie gouvernable. Tout ce qui n'améliore pas directement cette tâche menace de devenir du bruit, du poids ou une source de contamination. Maintenir un contexte court n'est pas amputé de mémoire ; c'est une manière d'améliorer la lecture, la validation et la reprise.

## Pourquoi ce chapitre existe
Le chapitre précédent montrait que la validation dépend d'artefacts vérifiables et de tâches mieux bornées. Mais cette validation devient vite coûteuse si l'agent travaille sur un terrain informationnel saturé. Un contexte sale n'est pas seulement un problème de longueur : c'est un problème de mélange entre instructions stables, historique périmé, hypothèses non tranchées et détails sans rôle clair. Il fallait donc un chapitre pour apprendre à nettoyer, transmettre et reconstruire le contexte au lieu de l'accumuler indéfiniment.

Ce chapitre existe aussi pour préparer le chapitre 12. Avant de parler des couches de prompt comme gouvernance, il faut séparer ce qui relève du **contexte de travail local** de ce qui relève des conventions permanentes, du rôle, ou de la validation. Sans cette distinction, on utilise le contexte comme une mémoire universelle, puis on demande au modèle de trier seul ce qui compte vraiment.

## Ce que le lecteur doit comprendre en sortant
À la fin de ce chapitre, le lecteur doit pouvoir tenir ensemble six idées :
- un contexte utile contient ce qu'il faut pour produire ou vérifier une tâche locale, pas l'intégralité du passé du projet ;
- la longueur n'est pas synonyme de richesse ; au-delà d'un certain point, elle devient un facteur de confusion et de coût ;
- résumer l'état ne consiste pas à condenser tout l'historique, mais à transmettre ce qui reste vivant, contraignant et actionnable ;
- nettoyer le contexte est un travail normal de l'orchestration, pas une perte de temps secondaire ;
- un context pack minimal vaut mieux qu'une conversation traînée si l'on veut permettre une reprise propre ;
- la gouvernance par prompts fonctionne mieux quand le contexte local cesse de porter ce qui devrait être stable ailleurs.

## Sections
- [Contexte utile contre contexte grenier](01-Contexte-utile-contre-contexte-grenier.md)
- [Résumer l'état sans traîner l'historique](02-Résumer-l'état-sans-traîner-l'historique.md)
- [Construire des context packs minimaux](03-Construire-des-context-packs-minimaux.md)

## Place dans la progression du livre
Le chapitre 10 installait la validation comme discipline. Le chapitre 11 montre maintenant que cette discipline dépend aussi d'un environnement de travail propre. Une validation locale se dégrade vite lorsque l'agent hérite d'un historique trop lourd, de décisions contradictoires ou d'instructions redondantes. Une fois le contexte rendu plus court, plus transmissible et plus propre, le livre peut ouvrir le chapitre 12 sur les couches de prompt : ce prochain pas devient alors beaucoup plus intelligible, parce que l'on distingue enfin ce qui doit rester permanent de ce qui doit rester local.

## Erreur de lecture à éviter
Il ne faut pas lire ce chapitre comme un culte artificiel de la brièveté, où toute information non minimale deviendrait suspecte. Le problème n'est pas d'avoir "peu de texte" ; le problème est d'avoir le **bon texte au bon endroit**. Un contexte trop maigre fait perdre des contraintes importantes. Un contexte trop chargé les noie. La compétence visée ici est l'ajustement, pas l'ascèse verbale.

## Mini exemple
Deux agents doivent reprendre un chantier interrompu. Le premier reçoit l'intégralité d'un long fil de discussion, plusieurs versions de décisions et des notes de brainstorming. Le second reçoit un court état structuré : objectif actif, contraintes non négociables, interface concernée, décision déjà prise, point restant à trancher. Le second a moins d'information brute, mais davantage d'information exploitable. Ce n'est pas un appauvrissement du contexte ; c'est une purification de son rôle.

## Règle pratique
À chaque reprise, distinguer trois blocs : **ce qui est stable**, **ce qui est encore ouvert**, **ce qui peut être jeté**. Si ce troisième bloc n'existe jamais, le contexte est probablement en train de devenir un grenier.

## Passage explicite au chapitre suivant
Le chapitre 11 purifie donc le terrain sur lequel une tâche locale peut réellement être produite ou vérifiée. Une fois cette distinction acquise entre contexte vivant et contexte grenier, le chapitre 12 peut séparer ce qui doit rester **stable** de ce qui doit rester **local**. Le passage suivant ne parle pas d'un meilleur texte magique ; il parle d'une architecture de commande plus gouvernable.

## Renvois utiles
- [Limiter les hallucinations et maintenir la validation](../10-hallucinations-et-validation/chapitre.md)
- [Exploiter la structure projet et les couches de prompt](../12-prompt-layering-openai/chapitre.md)
- [Piloter les collègues IA](../09-pilotage-agents/chapitre.md)
- [Scinder le travail en quanta 1D](../13-quanta-1d/chapitre.md)
