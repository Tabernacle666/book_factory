---
id: "14.02"
title: "Découper en sous-systèmes et interfaces"
parent: "14"
level: section
status: draft
owner_concept: "use-case-1-02"
summary: >
  Montre comment le besoin clarifié devient un petit système de sous-ensembles
  contrôlables avec des frontières nettes, des contrats de sortie simples et des
  points de reprise humaine explicites.
---

# Découper en sous-systèmes et interfaces

## Point de départ
Cette section reprend la fiche de clarification de `14.01` comme seule base légitime. On ne cherche pas encore à optimiser un organigramme d'agents ; on cherche à produire le plus petit système de blocs transmissibles qui permette une validation locale et une reprise propre. Le bon découpage ne vient donc pas d'une imagination architecturale abondante, mais d'une discipline de frontière.

## Idée centrale
Une fois le besoin clarifié, la question n'est pas encore « quel agent fait quoi ? ». La vraie question devient : **quelles sont les unités de travail qu'on peut isoler sans perdre la vérifiabilité du cas**. Découper en sous-systèmes ne consiste donc pas à multiplier les boîtes d'un schéma. Cela consiste à produire un petit nombre de blocs qui ont chacun un rôle lisible, des intrants autorisés, une sortie attendue et une frontière suffisamment stable pour qu'une validation locale soit possible.

Dans un use-case pédagogique, ce point est décisif. Si le découpage reste décoratif, tout semble avancer jusqu'au moment où l'on veut vérifier, intégrer ou reprendre la main. À ce moment-là, on découvre que plusieurs décisions ont été fusionnées dans le même bloc et que l'architecture n'est qu'une reformulation élégante du flou initial. Un bon sous-système n'est pas une abstraction séduisante ; c'est une **unité de responsabilité contrôlable**.

## Pourquoi c'est important
Le besoin clarifié en `14.01` donne un mandat local, mais il ne dit pas encore comment organiser le travail. Sans découpage, la demande reste monolithique. On demande alors à un même agent, ou à un même flux, de lire, interpréter, catégoriser, décider et parfois intégrer. Cette compression prématurée masque les erreurs et rend la reprise plus coûteuse.

Découper proprement sert trois objectifs en même temps :
- réduire la taille des décisions prises dans chaque bloc ;
- préparer des validations locales avant l'intégration ;
- rendre les handoffs lisibles pour un pilote humain.

Autrement dit, le découpage n'est pas un luxe d'architecte. C'est ce qui transforme un problème encore un peu vague en chaîne de travail réellement pilotable.

## Erreur classique
L'erreur classique consiste à découper par intuition fonctionnelle trop large : « un agent support », « un agent qualité », « un agent orchestration ». Ces intitulés peuvent paraître propres, mais ils cachent souvent plusieurs responsabilités hétérogènes. Le bloc paraît cohérent en surface, mais il devient impossible à valider localement.

Une deuxième erreur consiste à découper selon les outils disponibles plutôt que selon les décisions à sécuriser. On crée alors des sous-systèmes parce qu'un connecteur existe, parce qu'un modèle sait classifier, ou parce qu'une plateforme permet d'enchaîner des prompts. Le système reflète l'outillage plus que le besoin.

## Méthode concrète
À partir de la fiche de clarification, le découpage peut se faire avec quatre questions simples :

1. **Quelle décision locale faut-il prendre ici ?**  
   Chaque sous-système doit porter une décision identifiable, pas un agrégat diffus d'actions.

2. **Quelles sont ses entrées légitimes ?**  
   Il faut savoir exactement ce que le bloc a le droit de lire : ticket brut, taxonomie, historique, règles internes, etc.

3. **Quelle sortie doit-il produire pour le bloc suivant ?**  
   La sortie doit être assez courte et assez structurée pour devenir un contrat de passage, pas un nouveau contexte grenier.

4. **Comment vérifier localement que le bloc a bien travaillé ?**  
   Si aucune vérification locale n'est imaginable, le sous-système est probablement trop large ou trop flou.

Dans ce use-case, le bon réflexe est de chercher le **plus petit enchaînement suffisant**. Il ne s'agit pas d'atteindre d'emblée l'architecture finale parfaite. Il s'agit de stabiliser quelques frontières qui rendent la suite possible.

## Découpage du cas
En reprenant l'exemple d'un système d'aide à la qualification initiale de tickets support, un découpage local raisonnable peut ressembler à ceci :

### 1. Sous-système de lecture et d'extraction
Son rôle n'est pas de décider du traitement final, mais d'extraire les éléments utiles du ticket entrant : type apparent de problème, produit concerné, urgence suggérée, signaux d'incomplétude.

- **intrants autorisés** : ticket brut, métadonnées disponibles, taxonomie minimale ;
- **sortie attendue** : fiche courte d'extraction structurée ;
- **validation locale** : vérifier que chaque champ produit correspond bien à un élément effectivement lisible dans le ticket ou est marqué comme incertain.

### 2. Sous-système de qualification
Ce bloc prend la fiche d'extraction et propose une première orientation : catégorie probable, niveau de priorité suggéré, besoin ou non d'escalade humaine immédiate.

- **intrants autorisés** : fiche d'extraction, règles internes de tri, exemples historiques autorisés ;
- **sortie attendue** : proposition de qualification argumentée ;
- **validation locale** : vérifier que la proposition s'appuie sur les règles admises et qu'elle ne franchit pas le seuil d'autonomie fixé.

### 3. Sous-système de contrôle humain et d'intégration
Ce bloc n'est pas là pour tout refaire. Il vérifie les cas ambigus, arbitre les situations limites et transforme la qualification en action intégrable dans le flux support.

- **intrants autorisés** : proposition de qualification, indicateurs de confiance, motifs d'incertitude ;
- **sortie attendue** : qualification validée ou reprise explicite ;
- **validation locale** : vérifier que chaque cas non routinier déclenche bien le bon type de reprise.

Ce découpage n'est pas intéressant parce qu'il est « intelligent ». Il est intéressant parce que chaque bloc porte une responsabilité distincte, une sortie transmissible et une validation locale imaginable.

## Ce que doit contenir une interface
Une interface utile reste brève. Elle n'a pas besoin de ressembler à un document d'architecture lourd. Pour ce type de cas, une interface minimale peut tenir en quelques lignes :

- **nom du bloc émetteur** ;
- **nom du bloc récepteur** ;
- **format de sortie attendu** ;
- **champs obligatoires** ;
- **incertitudes autorisées** ;
- **motif explicite de reprise humaine**.

Par exemple, l'interface entre extraction et qualification peut exiger :
- résumé du ticket en 5 lignes maximum ;
- catégorie(s) candidates ;
- indicateur d'informations manquantes ;
- extraits source justifiant les signaux importants.

Ce format suffit déjà à empêcher deux dérives fréquentes : transmettre un blob narratif inutilisable, ou au contraire transmettre une conclusion sans trace de son ancrage.

## Mini exemple
Supposons un ticket disant : « Depuis la mise à jour d'hier, l'export CSV échoue pour certains comptes entreprise. Urgent, client bloqué avant clôture mensuelle. »

Un mauvais découpage demanderait à un seul agent : lire le ticket, qualifier la criticité, décider s'il faut escalader, rédiger une réponse et créer la tâche interne. Tout paraît rapide, mais la moindre erreur de lecture contamine tout le flux.

Un meilleur découpage sépare au moins :
- **extraction** : produit concerné, fonction cassée, contexte temporel, type de client, signal d'urgence ;
- **qualification** : incident probable, priorité suggérée, risque métier, ambiguïtés ;
- **contrôle/intégration** : confirmation humaine ou réorientation selon les règles internes.

Le gain n'est pas seulement la clarté. Le gain est qu'un pilote peut voir où une erreur est née, corriger localement et reprendre sans régénérer toute la chaîne.

## Règle pratique
Si un sous-système ne peut pas décrire sa sortie en moins de six lignes et sa validation locale en moins de trois, il est probablement trop large pour un use-case bien piloté.

## Ce que cette étape a réellement stabilisé
À la fin de cette section, le cas n'est pas encore prêt à être exécuté en autonomie. En revanche, il a cessé d'être une demande floue : il est devenu un petit système de passages obligés, avec des sorties courtes, des points d'arrêt identifiables et des zones où la reprise humaine a déjà une place écrite. C'est exactement ce qu'il faut avant d'attribuer les rôles.

## Passage explicite à la section suivante
Le découpage en sous-systèmes et interfaces stabilise les frontières du cas, mais il ne dit pas encore **qui produit quoi, qui vérifie quoi et comment l'ensemble converge vers une intégration fiable**. La section `03-Attribuer-rôles,-validations-et-intégration.md` prend ce relais en reliant les blocs du cas à des rôles, à des contrôles locaux et à une reprise de main explicite.

## Renvois utiles
- `../07-decoupage-du-travail/03-Découpage-par-capacité-de-validation.md`
- `../08-collaboration-orthogonale/02-Définir-des-contrats-stables.md`
- `../09-pilotage-agents/01-Rôle,-périmètre-et-intrants.md`
- `../10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`
