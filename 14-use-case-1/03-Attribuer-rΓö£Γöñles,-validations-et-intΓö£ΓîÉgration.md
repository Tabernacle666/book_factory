---
id: "14.03"
title: "Attribuer rôles, validations et intégration"
parent: "14"
level: section
status: draft
owner_concept: "use-case-1-03"
summary: >
  Fait converger les sous-systèmes du cas vers une chaîne exploitable: rôles
  distincts, validations locales, reprise humaine explicite et intégration finale
  dans le flux support sans confusion de responsabilité.
---

# Attribuer rôles, validations et intégration

## Idée centrale
Le découpage en sous-systèmes ne suffit pas encore à rendre le cas fiable. Il faut maintenant décider **qui produit, qui vérifie, qui arbitre et qui intègre**. Sans cette attribution, l'architecture reste un schéma propre mais inerte. Les blocs existent, les interfaces aussi, mais personne ne sait encore à quel moment une proposition devient actionnable, ni à quel moment elle doit être reprise, corrigée ou arrêtée.

Dans ce use-case, l'attribution des rôles n'a pas pour but de distribuer du prestige entre agents. Elle sert à préserver la lisibilité des responsabilités. Un bon rôle n'est pas une personnalité artificielle ; c'est une **fonction bornée** dans une chaîne de travail. Il reçoit des intrants précis, produit un artefact court, se soumet à une validation locale et ne décide pas au-delà de son seuil d'autonomie.

## Pourquoi c'est important
Beaucoup de systèmes paraissent cohérents tant qu'on parle seulement de découpage. Le problème apparaît au moment de l'exécution. Si le même rôle lit, interprète, qualifie, se valide lui-même puis pousse l'intégration, les erreurs deviennent difficiles à localiser. Le système va vite, mais il mélange production, contrôle et passage à l'action.

Attribuer proprement les rôles permet au contraire de faire trois choses en même temps :
- limiter ce qu'un agent peut affirmer ou déclencher seul ;
- rendre chaque validation locale visible et située ;
- éviter que l'intégration finale ne repose sur une confiance globale injustifiée.

Le gain n'est donc pas seulement organisationnel. C'est un gain de **traçabilité** et de **reprise de main**.

## Erreur classique
L'erreur classique consiste à attribuer les rôles par grands titres flatteurs : un agent analyste, un agent expert, un agent manager, un agent intégrateur. Ces noms peuvent rassurer, mais ils cachent souvent des responsabilités trop larges. Le rôle devient une boîte noire prestigieuse au lieu d'une unité de travail vérifiable.

Une autre erreur fréquente consiste à confondre validation et intégration. On croit qu'un bloc est validé parce qu'il a produit une sortie structurée ou parce qu'un second agent l'a reformulée proprement. Mais une sortie plausible n'est pas encore une sortie intégrable. La validation doit porter sur des critères explicites ; l'intégration doit rester une décision séparée.

## Méthode concrète
Pour attribuer les rôles dans ce cas pratique, il suffit de repartir du découpage de `14.02` et d'ajouter quatre colonnes mentales à chaque bloc :

1. **rôle producteur** — qui transforme les intrants autorisés en sortie attendue ;
2. **validation locale** — qui ou quoi vérifie que la sortie respecte le contrat ;
3. **motif de reprise** — qu'est-ce qui force l'arrêt du flux automatique ;
4. **point d'intégration** — à quel moment la sortie peut entrer dans le système support réel.

Cette grille évite de gonfler le cas. On ne réinvente pas une organisation entière ; on complète simplement chaque bloc avec les contrôles qui lui manquaient pour devenir exécutable.

## Attribution des rôles dans le cas
En reprenant le cas d'aide à la qualification initiale de tickets support, une attribution locale cohérente peut ressembler à ceci.

### 1. Extraction
Le rôle de production lit le ticket brut et produit une fiche d'extraction courte.

- **producteur** : agent d'extraction ou routine guidée par un prompt très borné ;
- **sortie** : résumé court, signaux utiles, informations manquantes, citations ou extraits source ;
- **validation locale** : contrôle de présence des champs requis et vérification qu'aucun élément important n'est inventé ;
- **motif de reprise** : ticket trop pauvre, contradictoire ou illisible ;
- **intégration** : aucune intégration métier directe à ce stade ; la sortie n'alimente que la qualification.

### 2. Qualification
Le rôle de production prend la fiche d'extraction et propose une catégorie, une priorité suggérée et un éventuel besoin d'escalade.

- **producteur** : agent de qualification distinct de l'extraction ;
- **sortie** : proposition argumentée, règles mobilisées, niveau d'incertitude ;
- **validation locale** : vérification de conformité aux règles internes et au seuil d'autonomie admis ;
- **motif de reprise** : conflit entre signaux, priorité à fort impact, absence de règle applicable ;
- **intégration** : seulement après validation, la proposition peut être transmise au bloc de contrôle humain.

### 3. Contrôle humain et intégration
Le rôle ici n'est pas de refaire tout le travail précédent, mais de décider si la proposition peut être intégrée dans le flux support réel.

- **producteur / arbitre** : opérateur humain ou pilote du flux ;
- **sortie** : qualification validée, corrigée ou rejetée avec motif ;
- **validation locale** : cohérence avec la politique de reprise, lisibilité des preuves et conformité du ticket final au système cible ;
- **motif de reprise** : doute résiduel, cas hors politique, impact élevé, preuve insuffisante ;
- **intégration** : création ou mise à jour du ticket selon le flux support existant.

Cette attribution montre l'idée essentielle du chapitre : les rôles ne sont pas alignés sur des noms séduisants, mais sur des **responsabilités bornées**. Chaque rôle sait ce qu'il produit, ce qu'il n'a pas le droit de faire seul et ce qui déclenche l'arrêt du flux.

## Ce que valide vraiment chaque étage
Pour que le cas reste contrôlable, il faut que les validations locales soient différentes selon les étages :

- l'**extraction** valide l'ancrage dans le ticket ;
- la **qualification** valide l'application correcte des règles ;
- le **contrôle humain** valide le droit d'intégrer dans le flux réel.

Autrement dit, les validations ne se répètent pas ; elles se **complètent**. Si chaque niveau essaie de tout revérifier, le système devient coûteux et flou. Si aucun niveau n'a un angle de validation propre, le système devient rapide mais aveugle.

## Mini exemple
Supposons un ticket contenant : « Depuis la mise à jour d'hier, l'export CSV échoue pour certains comptes entreprise. Client bloqué avant clôture mensuelle. »

- l'**extraction** doit isoler le produit concerné, la fonction cassée, le contexte temporel et le signal d'urgence, sans encore conclure à un incident critique ;
- la **qualification** peut proposer : incident probable sur fonctionnalité export, priorité élevée, besoin d'escalade rapide parce que le blocage touche une clôture mensuelle ;
- le **contrôle humain** vérifie que cette escalade respecte bien les règles internes et qu'aucune information essentielle n'est manquante avant d'intégrer la décision dans le flux support.

Le point important est que l'escalade n'est pas « décidée par le système » au sens vague. Elle devient intégrable parce qu'une chaîne courte de rôles et de validations l'a rendue lisible.

## Règle pratique
Un rôle est bien attribué s'il peut répondre en une phrase à trois questions : **qu'est-ce que je produis, qu'est-ce qui me valide, qu'est-ce qui m'oblige à m'arrêter**.

## Ce que le cas montre sans prétendre automatiser
Le point pédagogique important n'est pas de prouver qu'un flux support peut devenir autonome de bout en bout. Le point est de montrer comment une équipe hybride peut déléguer localement sans perdre le droit d'arrêter, de corriger et de réintégrer manuellement. L'intérêt du cas vient donc moins de son degré d'automatisation que de la netteté de ses limites.

## Passage explicite à la suite
Le use-case 1 dispose maintenant de son enchaînement complet : besoin clarifié, découpage en sous-systèmes, rôles, validations et intégration. La prochaine passe n'a donc plus besoin d'ajouter du fond. Elle doit seulement vérifier la cohérence locale de l'ensemble : transitions, densité, répétitions et lisibilité.

## Renvois utiles
- `../09-pilotage-agents/02-Quand-déléguer-et-quand-reprendre-la-main.md`
- `../10-hallucinations-et-validation/02-Séparer-génération-et-vérification.md`
- `../10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`
- `../13-quanta-1d/03-Autonomie-et-dérive-contrôlée.md`
