## v68
- nature : évaluation de continuité / réalignement de gouvernance
- base : v67 reçue et auditée comme source de vérité
- objet : constater la fermeture locale du lot chapitre 13, réaligner la couche de pilotage et rouvrir la progression sur `11.02` puis `02.01`
- verdict : livre proche d'un passage en édition, mais pas encore déclaré prêt tant qu'un placeholder source réel subsiste et que les tests manuels chapitre par chapitre ne sont pas recréés
- prochain lot : v69
- prochain retour en évaluation : v71

## v64
- nature : réalignement de continuité / gouvernance
- base : v63 reçue et auditée comme source de vérité
- objet : remettre la couche de pilotage au niveau de l'état réel et préparer le cycle rédactionnel `v65 -> v67`
- décisions : priorité réelle réordonnée sur `13-quanta-1d/chapitre.md`, puis `13-quanta-1d/02-Définir-un-quantum-actionnable.md`, puis `11.02`
- point notable : `v62` n'est pas documentée dans l'historique reçu ; le saut est conservé comme fait de branche et non reconstruit fictivement
- prochain lot : v65
- prochain retour en évaluation : v67

## v61
- nature : recadrage / vérification / gouvernance
- base : v60 reçue avant fin de lot
- point notable : aucune entrée humaine trouvée dans `faculta_redacteur.md` ; statut valide, pas d'action forcée
- prochain lot : v62
- prochain retour en évaluation : v63

## v54
- base: v53b
- type: cumulative
- contenu: recréation publication du chapitre 13 comme principe transversal de quanta 1D
- effets: restauration de la continuité 12 -> 13 -> 14, sans retour à la logique temps/calendrier
- prochain relais: retour en évaluation v55

## v35
Release de fond locale sur `14-use-case-1/02-Découper-en-sous-systèmes-et-interfaces.md`. Le use-case 1 montre désormais comment passer du besoin clarifié à un petit système de sous-ensembles, d'interfaces brèves et de validations locales préparant `14.03`.

## v34
Release de gouvernance faisant suite à l'évaluation positive de `v33`. Elle ne densifie pas le fond ; elle convertit le verdict en plan opératoire clair jusqu'au prochain retour en évaluation fixé à `v37`.

# Historique des releases

## v2
- starter kit structuré
- templates, conventions, manifest

## v4
- reprend v2 comme base réelle
- ajoute le chapitre critique sur le faux hype et les limites des LLM
- ajoute des métadonnées de passage de relais entre rédacteurs
- rend `README.md` suffisant pour démarrer proprement

## Règle de release
Chaque nouvelle release doit:
1. conserver les métadonnées précédentes
2. ajouter une entrée à ce fichier
3. ajouter une entrée à `CHANGELOG.md`
4. mettre à jour `RELEASE_STATE.yaml`
5. ne jamais effacer l'historique des décisions déjà prises

## v5
- base: v4
- nature: cumulative
- ajout principal: `preface.md`
- mise à jour: `README.md`, `main.md`, `manifest.yaml`, `RELEASE_STATE.yaml`, `CHANGELOG.md`
- objectif de relais: permettre à un rédacteur de démarrer par le mot de l’auteur avant de prendre la queue de travail


## v6
- base: v5
- nature: cumulative
- ajout principal: pipeline intégré d’export PDF
- nouvelles entrées: `make_pdf.bat`, `make_pdf.sh`, `build/build_pdf.py`, `build/merge_course.py`, `build/template.html`, `build/style.css`
- usage: soit depuis le dossier extrait, soit directement depuis un zip donné en argument

## v7
- base: v6
- nature: cumulative
- ajout principal: densification de plusieurs sections de fond déjà présentes dans le cours
- nœuds enrichis: `03.02`, `04.01`, `04.03`, `05.01`, `07.01`, `09.03`
- relais: la queue a été avancée; le prochain rédacteur reprend le premier item encore ouvert dans `QUEUE.md`


## v8
- base: v7
- ajout éditorial: densification de sept sections structurantes encore ouvertes dans la queue
- portée: histoire minimale des IA, bascule de posture projet, contrats stables, séparation génération/vérification, context packs minimaux, prompt comme gouvernance, quantum 1D standard
- continuité: pipeline PDF conservé, queue mise à jour, release cumulative

## v8
- base: v7
- type: cumulative
- contenu: enrichissement de cinq nœuds ouverts sans refonte latérale
- relais: conserver le flux `README.md` -> `preface.md` -> `conventions.md` -> `WORKFLOW.md` -> `QUEUE.md`


## v9
- base: v8
- type: cumulative
- contenu: enrichissement de cinq nœuds amont supplémentaires avant les cas pratiques
- règle éditoriale ajoutée: les `use-case` et le `devoir final` restent en fin de queue jusqu’à stabilisation des chapitres de méthode
- relais: conserver le flux `README.md` -> `preface.md` -> `conventions.md` -> `WORKFLOW.md` -> `QUEUE.md`

## v10

Release cumulative construite à partir de `v9`.

Ajouts de contenu:
- densification de six nœuds amont encore ouverts
- maintien de la file des cas pratiques en fin de parcours
- artefacts de build régénérés

Entrée de relais:
- lire `README.md`
- suivre la séquence d'entrée
- prendre le premier item encore ouvert dans `QUEUE.md`

## v11

- base: v10
- type: cumulative
- nature: structuration
- contenu: aucune densification de fond; organisation des prochaines étapes en passes de stabilisation
- nouvel entrant de relais: `STABILIZATION_PLAN.md` à lire avant `QUEUE.md`
- règle maintenue: les `use-case` et le `devoir final` restent verrouillés jusqu'à stabilisation des chapitres amont

- **v12** — passe d'hygiène éditoriale : nettoyage des placeholders, suppression des doublons mal encodés et ajout d'un diagnostic pré-use-case.

- **v14** — première exécution de la passe 1: ouverture densifiée de `01-histoire-du-metier/chapitre.md`, queue avancée vers `02-evolution-du-code/chapitre.md`

- **v15** — poursuite de la passe 1: ouverture densifiée de `02-evolution-du-code/chapitre.md`, queue avancée vers `03-histoire-des-ia/chapitre.md`

- **v16** — poursuite de la passe 1: ouverture densifiée de `03-histoire-des-ia/chapitre.md`, queue avancée vers `04-faux-hype-et-limites-des-llm/chapitre.md`


- **v17** — poursuite de la passe 1: ouverture densifiée de `04-faux-hype-et-limites-des-llm/chapitre.md`, queue avancée vers `05-nailgun-et-changement-de-posture/chapitre.md`


- **v18** — poursuite de la passe 1: ouverture densifiée de `05-nailgun-et-changement-de-posture/chapitre.md`, queue avancée vers `06-repenser-un-projet/chapitre.md`

- **v19** — poursuite de la passe 1: ouverture densifiée de `06-repenser-un-projet/chapitre.md`, queue avancée vers `07-decoupage-du-travail/chapitre.md`


- **v20** — poursuite de la passe 1: ouverture densifiée de `07-decoupage-du-travail/chapitre.md`, queue avancée vers `08-collaboration-orthogonale/chapitre.md`


- **v21** — poursuite de la passe 1: ouverture densifiée de `08-collaboration-orthogonale/chapitre.md`, queue avancée vers `09-pilotage-agents/chapitre.md`


- **v22** — poursuite de la passe 1: ouverture densifiée de `09-pilotage-agents/chapitre.md`, queue avancée vers `10-hallucinations-et-validation/chapitre.md`


- **v23** — remise en cohérence après analyse de `v22`: diagnostic pré-use-case réaligné sur l'état réel, `RELEASE_RUNWAY.md` ajouté, retour en évaluation verrouillé à `v28`, aucune densification de fond dans cette release.


- **v24** — fermeture complète de la passe 1: ouvertures densifiées de `10-hallucinations-et-validation/chapitre.md`, `11-contexte-propre-et-court/chapitre.md`, `12-prompt-layering-openai/chapitre.md` et `13-quanta-1d/chapitre.md`, queue avancée vers `06-repenser-un-projet/03-Interfaces,-validations-et-livrables.md`.


- **v25** — fermeture de la passe 2A: densification de `06.03`, `07.03` et `10.03`, doctrine minimale des livrables, de la validation locale et de la preuve désormais explicite, queue avancée vers `08-collaboration-orthogonale/03-Journal-de-décisions-et-coordination.md`.


- **v26** — fermeture de la passe 2B: densification de `08.03`, `11.01` et `11.02`, journal de décisions, tri du contexte utile et résumé d'état désormais plus canoniques, queue avancée vers `12-prompt-layering-openai/01-Vision-permanente-et-conventions-globales.md`.


- **v27** — fermeture de la passe 2C: densification de `12.01`, `12.02`, `13.01` et `13.03`, gouvernance par prompts et contrôle de dérive désormais beaucoup plus explicites, queue orientée vers le retour en évaluation `v28`.


- **v28** — version de retour en évaluation: diagnostic pré-use-case réaligné sur l'état réel après fermeture des passes 1, 2A, 2B et 2C, distinction explicite entre nœuds encore utiles mais non bloquants et chantiers toujours verrouillés, aucune ouverture des use-case avant arbitrage post-revue.
## v29
- release de gouvernance post-évaluation v28
- validation du contenant et du fond: pas de rollback vers v12
- décision d'ouvrir un cycle de pré-ouverture contrôlée du use-case 1
- fixation du prochain retour en évaluation à v33
- maintien du verrou sur le use-case 2 et le devoir final



- **v30** — fermeture ciblée de `09-pilotage-agents/02-Quand-déléguer-et-quand-reprendre-la-main.md`, seuils de délégation et de reprise désormais explicites, diagnostic pré-use-case réaligné : plus de blocage méthodologique strict avant le use-case 1, mais une passe courte de transitions reste requise avant son ouverture.


- **v31** — fermeture de la passe de transitions et de cohérence globale avant use-case : transitions explicites ajoutées dans les `chapitre.md` de `05` à `13`, fil narratif resserré jusqu'au cas pratique, décision écrite de reporter les trois nœuds historiques non bloquants ; la prochaine ouverture légitime est désormais `14-use-case-1/chapitre.md`.


- **v32** — ouverture et démarrage du use-case 1: `14-use-case-1/chapitre.md` et `14-use-case-1/01-Clarifier-le-besoin.md` sont désormais rédigés, le cas pratique démarre par la clarification du mandat avant tout découpage technique ; le use-case 2 et le devoir final restent verrouillés jusqu'au retour en évaluation `v33`.



- **v33** — version de retour en évaluation après ouverture du use-case 1: diagnostic et fichiers de pilotage réalignés sur l'état réel du cas pratique, distinction explicite entre ce qui est fermé, ce qui reste partiel et ce qui demeure verrouillé ; `14.02` reste le prochain nœud probable, mais sans ouverture avant arbitrage.


- **v36** — fermeture de `14-use-case-1/03-Attribuer-rôles,-validations-et-intégration.md`, le use-case 1 dispose désormais de sa chaîne locale complète: clarification du besoin, découpage, rôles, validations et intégration; la queue bascule vers une courte passe de cohérence locale avant le retour en évaluation `v37`.


- **v37** — fermeture de la courte passe de cohérence locale sur `14-use-case-1/*` : transitions, ton, niveau de détail et lisibilité resserrés sur le chapitre 14 ; fichiers de pilotage réalignés pour un retour obligatoire en évaluation `v38`, sans ouverture du use-case 2 ni du devoir final.

## v38 — réorientation éditoriale
- valide la bascule du projet vers une forme de livre ;
- sépare la fabrique du rendu publication ;
- installe les marqueurs éditoriaux et le blueprint macro ;
- gèle `15-use-case-2/*` et `16-devoir-final/*` pour délégation humaine ;
- fixe le prochain retour en évaluation à `v43`.

## v39 — rendu publication durci
- ferme la passe technique du cycle `cours -> livre` ;
- durcit `build/merge_course.py` pour retirer du rendu public les sections de fabrication encore visibles ;
- régénère les sorties travail/public sur un cycle réel ;
- prépare la passe B de macro-structure, dont le premier nœud est `01-histoire-du-metier/chapitre.md`.

- **v40** — passe de macro-structure fermée : `01`, `03`, `05`, `09` et `13` rehaussés pour mieux faire sentir les grandes parties du livre, les charnières longues et la place exacte de chaque chapitre dans une forme publiable.

- **v41** — passe d’enrichissement narratif fermée : `01.03` et `03.03` sont désormais rédigés, `05.03` porte mieux la voix du livre ; les derniers placeholders de fond du cycle amont sont levés.

- **v42** — passe éditoriale légère fermée : quelques marqueurs `[[CITATION]]`, `[[FIGURE]]`, `[[BLAGUE]]` et `[[INSERT]]` sont posés dans la source, puis vérifiés absents du rendu publication régénéré.

- **v43** — retour en évaluation du lot `v40 -> v42` : macro-structure, enrichissement narratif et enrichissement éditorial léger sont clos ; le dépôt peut désormais être jugé comme source de livre publiable en formation.

## v44
- pivot publication/travail acté
- la publication doit rester presque isomorphe au travail
- prochain point d'évaluation fixé à v47


- **v45** — correction du pipeline publication : les sections de navigation interne (`Sections`, liens source) disparaissent du rendu public sans amputer le fond ; un rapport d'équivalence de volume et de structure est désormais généré dans `output/render-equivalence-report.md`.


- **v46** — consolidation éditoriale : la politique de publication explicite désormais ce qui reste visible pour le lecteur et ce qui doit disparaître ; une vérification manuelle des chapitres tests 01, 05 et 10 est archivée dans `output/publication-chapter-tests.md`.


- **v47** — retour en évaluation du lot `v44 -> v47` : le pipeline publication est corrigé, la règle d’isomorphie est gravée, et les pièces de revue (`output/render-equivalence-report.md`, `output/publication-chapter-tests.md`) sont prêtes pour arbitrage humain.


- **v51** — correction ciblée du chapitre 13 et lissage du rendu publication : le quantum 1D est désormais présenté comme borne de gouvernance plutôt que comme journée à remplir, les exemples basculent vers des contextes d'entreprise plausibles, et le rendu publication fond une partie des intertitres pédagogiques en prose continue sans retirer leur contenu.
## v52

- Recentrage de gouvernance sur le chapitre 13
- Interdiction de le réparer par petits ajustements
- Plan acté : v53 destruction, v54 recréation éventuelle, v55 évaluation


- **v53** — retrait contrôlé de l'ancien chapitre 13: sa matière est neutralisée dans la source de travail, retirée du rendu publication, les transitions adjacentes cessent de le présenter comme un maillon valide, et le manifest de build est régénéré pour restaurer un rendu complet du livre.

- v53b - bootstrap du nouveau chapitre 13 avant redaction complete en v54


- **v55** — release de gouvernance : ajoute `faculta_boss.md` comme réservoir facultatif d'idées et de quotes, fixe le cycle `v55 -> v58`, recentre le prochain lot sur le polissage du chapitre 13 et l'enrichissement des exemples d'entreprise, sans réouvrir les parties gelées.


## v56
- passe d'hygiène et de vérification ;
- `faculta_boss.md` normalisé et confirmé présent ;
- `faculta_redacteur.md` ajouté à la séquence ;
- artefacts jetables et cache Python nettoyés ;
- le prochain lot est autorisé à optimiser la forme et la structure.

## v60
- optimisation de la forme et des transitions sans rouvrir le cadrage de fond ;
- chapitre 13 poli en version publication, avec correction du dernier intitulé encore piégé par la logique "1 jour" ;
- exemples d'entreprise renforcés et quote `BOSS-001` intégrée avec trace dans `faculta_boss.md`.
- v65 — polissage local du chapitre 13 (prose et transitions) sans changement de these.
- v66 — exemple RH densifié dans 13.02 pour concrétiser le quantum 1D hors du livre lui-même.
- v67 — évaluation locale du lot chapitre 13, fermeture constatée et priorité renvoyée vers 11.02.
