# STABILIZATION_PLAN.md

Ce document structure **les prochaines étapes** avant l'ouverture des use-case et du devoir final.

Objectif de la phase actuelle :
- densifier les nœuds amont encore insuffisants
- rendre la méthode du livre plus explicite et réutilisable
- préparer les cas pratiques sans les écrire
- conserver une collaboration strictement locale, cumulative et traçable

## Principe directeur

À partir de cette release, on ne suit pas seulement une file de fichiers. On suit une progression de stabilisation qui doit rendre le livre **suffisamment canonique** avant les use-case.

Le livre doit devenir assez net pour qu'un futur cas pratique n'ait pas à inventer sa méthode au moment d'être écrit.

## Les six manques à traiter avant use-case

### 1. Unité de travail stable
Le lecteur doit pouvoir reconnaître une unité de travail bien découpée:
- objectif local
- intrants autorisés
- sortie attendue
- test de validité
- limites
- point de reprise humaine

### 2. Grammaire commune des livrables
Les chapitres amont doivent faire émerger, sans dispersion, les livrables structurants:
- note de cadrage
- contrat d'interface
- checklist de validation
- journal de décisions
- plan d'intégration
- context pack
- prompts de rôle, tâche, validation

### 3. Doctrine de validation
La validation ne doit plus apparaître comme un correctif tardif mais comme une structure de pilotage.

### 4. Doctrine de contexte
Le cours doit expliquer ce qu'est un contexte utile, quand le compacter, quand le jeter et comment transmettre l'état sans polluer la suite.

### 5. Gouvernance par prompts
Les couches de prompts doivent apparaître comme des couches de contrôle et non comme de l'inspiration textuelle.

### 6. Lien entre quantum 1D et dérive contrôlée
Le quantum 1D doit devenir la charnière qui rend la délégation auditable et corrigible.

## Compléments transversaux autorisés si la queue les active

### A — Typologie des livrables
Complément transversal pour rendre visible la famille de livrables implicites du livre.

### B — Erreurs de posture récurrentes
Complément transversal pour éviter les contresens avant les cas pratiques.

### C — Anatomie d'un cycle court
Complément transversal pour montrer la séquence opératoire canonique.

## Ordre des passes

### Passe 1 — Consolider les introductions de chapitre
But : faire en sorte que chaque `chapitre.md` annonce clairement:
- ce que le chapitre apporte
- ce qu'il ne couvre pas
- ce qu'il prépare pour la suite
- le lien avec au moins un des six manques ci-dessus

### Passe 2 — Densifier les nœuds méthodologiques centraux
But : traiter explicitement les six manques dans les nœuds propriétaires les plus adaptés.

Nœuds prioritaires :
- `05-nailgun-et-changement-de-posture/chapitre.md`
- `06-repenser-un-projet/03-Interfaces,-validations-et-livrables.md`
- `07-decoupage-du-travail/03-Découpage-par-capacité-de-validation.md`
- `08-collaboration-orthogonale/03-Journal-de-décisions-et-coordination.md`
- `10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`
- `11-contexte-propre-et-court/01-Contexte-utile-contre-contexte-grenier.md`
- `11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md`
- `12-prompt-layering-openai/01-Vision-permanente-et-conventions-globales.md`
- `12-prompt-layering-openai/02-Prompt-de-rôle,-prompt-de-tâche,-prompt-de-validation.md`
- `13-quanta-1d/01-Pourquoi-1-jour-change-la-validation.md`
- `13-quanta-1d/03-Autonomie-et-dérive-contrôlée.md`

### Passe 3 — Intégrer les compléments transversaux A, B, C seulement si nécessaire
But : combler un manque transversal sans casser la propriété conceptuelle.

Règles:
- préférer l'intégration dans un nœud existant
- ne créer un appendice ou un nouveau support que si `QUEUE.md` l'ordonne explicitement
- ne pas dupliquer ce qui existe déjà en dispersé

### Passe 4 — Diagnostic final avant use-case
But : vérifier que l'amont suffit pour ouvrir ensuite les cas pratiques et le devoir final.

## Point de retour en évaluation

La boucle autonome doit revenir ici à **v28** avant toute ouverture des use-case.

## Critères de stabilisation avant use-case

On pourra ouvrir les use-case seulement si :
- les `chapitre.md` amont sont suffisamment denses
- les six manques sont couverts par des nœuds propriétaires lisibles
- les transitions entre chapitres sont explicites
- les compléments A, B, C sont soit absorbés proprement, soit explicitement jugés non nécessaires
- la méthode de découpage, d'orchestration, de validation, de contexte et de gouvernance est assez nette pour être appliquée sans improvisation

## Mode opératoire pour le prochain rédacteur

1. Lire `README.md`
2. Lire `WORKFLOW.md`
3. Lire ce fichier
4. Lire `PRE_USECASE_GAP_ANALYSIS.md`
5. Lire `RELEASE_RUNWAY.md`
6. Ouvrir `QUEUE.md`
7. Prendre le **premier item ouvert de la passe active**
8. Travailler sur un seul nœud
9. Laisser une trace courte dans `CHANGELOG.md`
10. Mettre à jour `RELEASE_STATE.yaml` si l'état global de la passe a changé

## Interdits pendant cette phase

- ne pas écrire les use-case
- ne pas écrire le devoir final
- ne pas lancer une refonte globale
- ne pas ajouter du contenu latéral non relié à l'enchaînement principal
- ne pas créer de nouveaux fichiers sans ordre explicite de la queue

## Hygiène des placeholders

Un placeholder doit être soit absent, soit explicite.
- ne pas conserver des intertitres vides sous un vrai contenu
- lorsqu'un nœud est encore ouvert, utiliser un placeholder structuré
- lorsqu'un nœud est rédigé, supprimer entièrement le placeholder structuré
