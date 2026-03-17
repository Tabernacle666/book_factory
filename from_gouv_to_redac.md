<!-- from_gouv_to_redac.md -->

# FROM GOUV TO REDAC

## Nature du fichier
Handoff court de GOUV vers REDAC.
Ce fichier pilote le lot en cours.
Il est remplaçable à chaque cycle.

## Rôle
Dire au rédacteur :
- quoi faire maintenant ;
- quoi ne pas faire ;
- jusqu’où aller ;
- à quelle release revenir en évaluation.

## Format attendu
- build source : `rXX`
- build cible immédiate : `rYY`
- objet du lot
- priorités
- interdits
- point de retour en évaluation

## Gabarit minimal à réécrire à chaque cycle

- build_source: rXX
- build_cible: rYY
- nature_du_lot: rédaction / polish / gouvernance / nettoyage / évaluation différée
- objet: décrire le but du lot en 2 à 5 lignes
- priorite_1: cible la plus importante
- priorite_2: deuxième cible
- priorite_3: troisième cible si utile
- exemples_a_privilegier: marketing / finance / RH / opérations / direction / autre
- interdit_1: ne pas toucher à 15-use-case-2/*
- interdit_2: ne pas toucher à 16-devoir-final/*
- interdit_3: ne pas casser la continuité ni réduire massivement la publication
- consigne_speciale: vide si rien de particulier
- retour_en_evaluation: rZZ
- remarque_gouv: phrase finale courte pour cadrer le ton du lot

## Règles
- lot clair ;
- pas de flou ;
- pas de roadmap géante ;
- pas d’objectifs contradictoires ;
- ne jamais supposer que REDAC a compris un implicite ;
- si le projet a besoin d’un recadrage avant rédaction, le dire explicitement.