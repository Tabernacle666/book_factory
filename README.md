# README — point d'entrée unique pour le rédacteur

Lis ce fichier en premier. Ensuite, n'improvise ni la méthode ni la priorité: la release est déjà cadrée ici.

## Mission de cette release

Cette release est une **release d'évaluation et de réenlignement**.

Le lot `v65 -> v67` a bien renforcé le chapitre 13 et peut être considéré comme **fermé localement**. Le rôle du présent passage est maintenant de remettre toute la couche de pilotage au niveau de cette réalité et d'envoyer la rédaction sur le **prochain nœud de fond réellement utile**.

Le cycle suivant doit donc protéger quatre choses en même temps :
- la continuité cumulative de la branche ;
- l'isomorphie entre travail et publication ;
- la fermeture propre du lot chapitre 13 ;
- la reprise de la progression sur le prochain manque réel sans rouvrir le cadrage global.

## Ce que cette release doit réussir

1. **acter la fermeture locale du chapitre 13**
   - considérer `13-quanta-1d/chapitre.md` comme stabilisé localement ;
   - considérer `13-quanta-1d/02-Définir-un-quantum-actionnable.md` comme renforcé de manière suffisante pour sortir du cycle immédiat ;
   - ne plus remettre le prochain rédacteur sur ce chapitre sauf retour d'évaluation explicite.

2. **renvoyer la rédaction sur le vrai prochain nœud**
   - reprendre `11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md` ;
   - garder `02-evolution-du-code/01-De-l'assembleur-aux-langages-haut-niveau.md` visible comme dette source juste derrière ;
   - laisser les lots suivants enrichir le fond sans devoir réparer la gouvernance.

3. **préparer le point de bascule vers l'édition**
   - constater honnêtement que le livre est proche d'un passage en édition ;
   - ne pas déclarer la branche “prête” tant qu'un placeholder source réel reste ouvert ;
   - garder visible l'absence de tests manuels chapitre par chapitre.

4. **protéger le contrat travail / publication**
   - conserver dans l'édition publication presque toute la matière utile au lecteur ;
   - retirer seulement la cuisine interne, les placeholders et les balises de fabrication ;
   - ne pas réduire massivement le rendu publication.

## Règle d'or

Tu n'améliores pas « le livre » en général. Tu renforces **un seul nœud** ou **un seul dispositif de pilotage** à la fois.

## Séquence de travail obligatoire

1. Lire `preface.md` pour situer l'intention.
2. Lire `conventions.md`.
3. Lire `WORKFLOW.md`.
4. Lire `PUBLICATION_POLICY.md`.
5. Lire `BOOK_BLUEPRINT.md`.
6. Lire `faculta_boss.md`.
7. Lire `faculta_redacteur.md`.
8. Lire `EDITORIAL_MARKERS.md`.
9. Lire `RELEASE_RUNWAY.md`.
10. Ouvrir `QUEUE.md`.
11. Prendre **le premier item non terminé de la passe active**.
12. Si la tâche touche le pipeline, vérifier aussi `build/merge_course.py` et `build/build_pdf.py`.
13. Lire uniquement le **fichier cible**, son `chapitre.md` parent et, si nécessaire, les sections sœurs.
14. Rédiger localement sans dupliquer ni déborder.
15. Mettre à jour le fichier cible.
16. Ajouter une entrée courte dans `CHANGELOG.md`.
17. Si nécessaire, laisser un point orthogonal dans `faculta_redacteur.md`.
18. Mettre à jour `QUEUE.md`, `RELEASE_STATE.yaml` et `RELEASE_RUNWAY.md` si nécessaire.
19. Passer la release au prochain rédacteur.

## Priorité de lecture

- `README.md`
- `preface.md`
- `conventions.md`
- `WORKFLOW.md`
- `PUBLICATION_POLICY.md`
- `BOOK_BLUEPRINT.md`
- `faculta_boss.md`
- `faculta_redacteur.md`
- `EDITORIAL_MARKERS.md`
- `RELEASE_RUNWAY.md`
- `QUEUE.md`
- puis seulement le nœud cible

## Priorité effective du cycle qui s'ouvre

Le prochain cycle rédactionnel doit partir dans cet ordre :
1. `11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md`
2. `02-evolution-du-code/01-De-l'assembleur-aux-langages-haut-niveau.md`

Le chapitre 13 est considéré comme **fermé localement** à l'issue de `v67`, sauf retour d'évaluation contraire.

## Interdits pendant ce cycle

- ne pas rouvrir le cadrage de fond ;
- ne pas retomber dans la logique "1 jour" ;
- ne pas toucher à `15-use-case-2/*` ;
- ne pas toucher à `16-devoir-final/*` ;
- ne pas transformer la source en document monolithique ;
- ne pas effacer l'historique cumulatif ;
- ne pas faire du remplissage pour gagner artificiellement des pages.

## Générer les rendus

Mode simple depuis le dossier extrait:
- Windows: double-cliquer sur `make_pdf.bat`
- macOS / Linux: lancer `./make_pdf.sh`

Mode direct depuis un zip:
- `python build/build_pdf.py chemin/vers/release.zip --mode both`

Sorties générées:
- `output/cours-travail.pdf`
- `output/cours-travail.html`
- `output/cours-travail-merge.md`
- `output/livre-publication.pdf`
- `output/livre-publication.html`
- `output/livre-publication-merge.md`

Le PDF public doit garder presque toute la matière utile au lecteur.
Le PDF de travail ajoute seulement une couche de pilotage et de collaboration.
La différence entre les deux rendus doit rester faible en volume et nette en nature.

## Directive spéciale sur le lot v68

Cette release constate que le livre entre dans une phase plus mature :
- le rendu publication est désormais long et cohérent ;
- le lot chapitre 13 est refermé localement ;
- mais un nœud placeholder réel subsiste encore dans la source (`02.01`) ;
- et les tests manuels chapitre par chapitre ne sont toujours pas reconstitués.

Conséquence :
- on peut préparer la bascule vers l'édition ;
- mais il reste encore **un petit lot de contenu utile** avant de déclarer la branche prête à partir vers une édition augmentée.
