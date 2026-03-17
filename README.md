# Books Factory

Ce dépôt est la mémoire canonique de la factory.

## rôles

- Direction : décide l’intention, tranche les arbitrages.
- Gouvernance : gère le contenant, la cohérence, l’évaluation, les lots.
- Rédaction : gère le fond, le contenu, la matière.
- Continuité : lit `current_state.md` et relance le bon rôle.

## règle d’état

La vérité opérationnelle vit dans `current_state.md`.

Format :
`vNN|role|status`

Rôles :
- `redac`
- `gouv`

Status :
- `lock`
- `free`

Sens :
- `vNN|redac|lock` : relancer rédaction sur vNN
- `vNN|redac|free` : lancer gouvernance sur vNN
- `vNN|gouv|lock` : relancer gouvernance sur vNN
- `vNN|gouv|free` : lancer rédaction sur la version indiquée

## règle d’idempotence

Le cron ne crée aucun état intermédiaire.
Il lit l’état courant.
Il déclenche le rôle correspondant.
Si panne avant commit, le même état sera rejoué au prochain passage.

## fichiers stables

- `README.md`
- `bootstrap_redac.md`
- `bootstrap_gouv.md`
- `continuity_pulse.py`

## fichiers dynamiques

- `current_state.md`
- `from_redac_to_gouv.md`
- `from_gouv_to_redac.md`