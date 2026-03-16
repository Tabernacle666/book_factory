---
id: "11.01"
title: "Contexte utile contre contexte grenier"
parent: "11"
level: section
status: draft
owner_concept: "contexte-propre-et-court-01"
summary: >
  Distingue le contexte qui aide réellement à décider du contexte accumulé qui
  ajoute du bruit, de la contradiction et du coût de reprise.
---

# Contexte utile contre contexte grenier

## Idée centrale

Tout contexte n'a pas la même valeur. Un **contexte utile** augmente la qualité d'une décision locale. Un **contexte grenier** accumule au contraire des éléments hétérogènes, anciens, contradictoires ou simplement non nécessaires. Il donne l'impression d'être prudent, alors qu'il rend souvent le travail moins fiable.

Dans un environnement avec agents IA, cette distinction devient structurante. Le modèle ne sait pas naturellement quels fragments doivent dominer les autres. S'il reçoit un grenier, il doit improviser une hiérarchie implicite. On obtient alors une réponse plausible, mais bâtie sur un terrain trop bruyant.

## Pourquoi c'est important

Le bon contexte n'est pas celui qui contient "le plus d'informations". C'est celui qui contient **les bonnes contraintes pour la décision en cours**. Plus on surcharge le contexte, plus on augmente le coût cognitif, les ambiguïtés et les occasions de dérive.

Cette discipline protège aussi les humains. Un rédacteur qui reprend un nœud avec cinquante éléments d'arrière-plan finit par ne plus savoir ce qui est source de vérité, hypothèse temporaire ou simple bruit historique. La qualité de la collaboration dépend donc moins de la mémoire totale disponible que de la netteté du tri.

## Erreur classique

L'erreur classique consiste à penser: "mieux vaut trop que pas assez". On colle alors conversation, anciennes versions, notes de cadrage, fichiers voisins, consignes latérales, objections passées, jusqu'à produire un contexte trop vaste pour être réellement gouvernable.

Autre erreur: croire qu'un élément est utile parce qu'il est vrai. Beaucoup d'éléments vrais ne sont pas utiles à la tâche locale. Ils deviennent même nocifs s'ils déplacent l'attention vers des détails qui n'appartiennent pas au bon périmètre.

## Méthode concrète

Pour qualifier un contexte, applique trois filtres simples.

1. **Décisif** — cet élément change-t-il réellement la décision locale?
2. **Propriétaire** — vient-il d'une vraie source de vérité du nœud?
3. **Actif** — est-il encore valable dans l'état courant du projet?

Si la réponse est non à l'un des trois, l'élément doit souvent sortir du pack local ou être reformulé en contrainte plus courte.

En pratique, un contexte utile contient surtout:
- le fichier cible;
- le parent immédiat;
- les sections sœurs réellement pertinentes;
- les conventions nécessaires;
- les critères d'acceptation.

Le reste n'entre que s'il change concrètement l'action attendue.

## Mini exemple

Pour reprendre `11.02`, donner tout l'historique des releases n'aide pas beaucoup. En revanche, fournir `11/chapitre.md`, `11.01`, `11.03`, les conventions, et l'exigence de formaliser une transmission d'état propre est utile. La première approche charge la mémoire. La seconde charge le jugement.

Même chose en développement: fournir tout le dépôt pour modifier une fonction locale est souvent un contexte grenier. Fournir le contrat, les tests proches et le fichier touché est un contexte utile.

## Règle pratique

N'ajoute pas un élément au contexte parce qu'il existe. Ajoute-le seulement s'il **change la bonne décision locale**.

## Renvoi éventuel

La construction positive d'un contexte court et relisible est traitée dans `03-Construire-des-context-packs-minimaux.md`. La manière de transmettre l'état sans traîner tout l'historique est développée dans `02-Résumer-l'état-sans-traîner-l'historique.md`.
