# Workflow de rédaction itérative

## Cycle unique

1. choisir le prochain item dans `QUEUE.md`
2. lire le contexte minimum autorisé
3. rédiger le fichier cible
4. vérifier absence de duplication
5. journaliser en 5 lignes maximum dans `CHANGELOG.md`
6. mettre à jour le statut dans `RELEASE_STATE.yaml`
7. passer le relais

## Contexte autorisé par défaut

- le fichier cible
- le `chapitre.md` parent
- les sections sœurs si nécessaire

## Ce qu'il ne faut pas faire

- ouvrir tout le dépôt sans nécessité
- réécrire plusieurs chapitres à la fois
- déplacer des concepts propriétaires
- renommer des chemins sans mandat explicite

## Format de change log

- date ou release
- fichier cible
- objectif
- ajouté
- évité
- prochain pas

## Définition du prochain pas

Le prochain pas doit être formulé comme une action locale et finie, pas comme une intention vague.
