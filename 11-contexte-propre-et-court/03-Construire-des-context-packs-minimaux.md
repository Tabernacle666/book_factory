---
id: "11.03"
title: "Construire des context packs minimaux"
parent: "11"
level: section
status: draft
owner_concept: "contexte-propre-et-court-03"
summary: >
  Formalise le context pack minimal comme unité de contexte locale, courte,
  stable et réutilisable d'une itération à l'autre.
---

# Construire des context packs minimaux

## Idée centrale

Un bon contexte n’est pas un tas de texte accumulé. C’est un paquet court, ciblé, relisible, qui permet à un acteur local de faire correctement une tâche sans hériter de toute l’histoire du projet. Appelons cela un **context pack minimal**.

Le context pack minimal remplace la tentation de “tout donner au modèle pour être sûr qu’il comprenne”. En pratique, plus on verse d’historique dans le prompt, plus on augmente le bruit, les contradictions latentes et le coût cognitif. Un petit pack propre vaut mieux qu’un grenier narratif.

## Pourquoi c'est important

Les LLM travaillent mieux quand le contexte utile est proche de la tâche. Un contexte trop vaste dilue les signaux importants et encourage des reprises opportunistes. Pour un cours modulaire comme celui-ci, le context pack sert aussi à rendre la collaboration transmissible: n’importe quel rédacteur ou agent peut reprendre un nœud sans relire cent pages.

C’est également un outil de gouvernance. Si tu es capable de définir le plus petit contexte suffisant, c’est souvent que tu as compris le vrai périmètre de la tâche.

## Erreur classique

L’erreur classique consiste à utiliser l’historique conversationnel comme source de vérité. On colle les échanges précédents, les hésitations, les versions intermédiaires, les explications latérales, puis on demande au modèle de “tenir compte de tout cela”. On fabrique ainsi un contexte instable, coûteux et souvent contradictoire.

Une autre erreur est d’oublier ce qui manque vraiment: parfois le problème n’est pas que le contexte soit trop court, mais qu’il lui manque une contrainte décisive, un format de sortie ou le fichier propriétaire du concept.

## Méthode concrète

Un context pack minimal peut tenir en cinq blocs.

1. **But local** : la tâche précise à accomplir.
2. **Source de vérité locale** : le fichier cible.
3. **Contexte de voisinage** : parent immédiat, sections sœurs utiles, conventions essentielles.
4. **Critères d’acceptation** : ce qui permet de juger la sortie.
5. **Interdits** : ce que l’acteur ne doit ni toucher ni redévelopper.

Si un sixième bloc apparaît, il doit être justifié. Sinon, on est souvent en train de réinjecter du bruit historique. Le pack idéal tient sur une page ou moins.

## Mini exemple

Pour enrichir `10.02-Séparer génération et vérification`, le context pack contient: le fichier cible, `10-hallucinations-et-validation/chapitre.md`, les sections `01` et `03`, les conventions de contribution, et une consigne explicite disant de ne pas réexpliquer tout le chapitre sur les hallucinations. C’est suffisant pour produire une section cohérente sans relire le reste du cours.

Un pack plus gros donnerait l’illusion de sécurité. En réalité, il offrirait surtout plus d’occasions de dériver.

## Règle pratique

Le meilleur contexte est le plus petit contexte qui permet encore une bonne décision locale. Si tu dois ajouter de plus en plus d’historique pour qu’une tâche tienne debout, le vrai problème vient souvent du découpage, pas de la mémoire.

## Renvoi éventuel

La critique du contexte-grenier est développée dans `01-Contexte-utile-contre-contexte-grenier.md`. La manière de résumer l’état sans traîner l’historique est traitée dans `02-Résumer-l'état-sans-traîner-l'historique.md`.
