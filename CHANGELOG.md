## v68
- évalué: `v67` comme retour de rédaction valide ; fermeture locale du lot `13-quanta-1d` confirmée
- réaligné: `README.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `manifest.yaml`, `RELEASE_RUNWAY.md`, `QUEUE.md`, `BOOTSTRAP_PROMPT.md`
- acté: prochain cycle recentré sur `11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md` puis `02-evolution-du-code/01-De-l'assembleur-aux-langages-haut-niveau.md`
- noté: branche proche d'un passage en édition, mais encore retenue par `02.01` placeholder et par l'absence de tests manuels chapitre par chapitre

## v61

- recadrage de la numérotation après réception anticipée d'une release avant fin de lot ;
- vérification de `faculta_redacteur.md` : aucune entrée humaine détectée dans v60 ; usage confirmé comme facultatif ;
- confirmation et normalisation de `faculta_boss.md` dans la séquence de collaboration ;
- mise à jour de `README.md`, `RELEASE_RUNWAY.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md` ;
- prochain retour en évaluation fixé à v63.

## v54
- recréation publication du chapitre 13 comme vrai chapitre de fond, sans logique temps/calendrier
- nouveau noyau: quanta 1D comme unité de trajectoire, une dimension principale par rôle, mission, validation et reprise
- exemples d'entreprise ajoutés: direction, marketing, finance, RH, opérations
- raccords rétablis: chapitre 12 renvoie de nouveau vers 13, chapitre 14 compose désormais les chapitres 05 à 13
- métadonnées de release réalignées pour le retour en évaluation v55

## v47
- retour en évaluation du lot `v44 -> v47`
- état de runway et de queue basculé en fin de lot, sans ouverture d'un nouveau chantier
- base de revue fournie : `output/render-equivalence-report.md` et `output/publication-chapter-tests.md`
- intermédiaires conservés pour audit : `v45`, `v46`

## v46
- consolidation éditoriale : `PUBLICATION_POLICY.md` explicite désormais ce qui disparaît sans perte et ce qui doit rester visible dans la publication
- ajout : `output/publication-chapter-tests.md` pour la vérification des chapitres tests 01, 05 et 10
- maintenu : même matière utile au lecteur, moins la navigation source et la méta de fabrication
- prochain nœud : retour obligatoire en évaluation `v47`

## v45
- correction du pipeline publication : retrait des sections de navigation interne et conversion des liens markdown locaux en texte simple dans le rendu public
- ajout : `output/render-equivalence-report.md` avec mesure d'écart entre travail et publication
- régénéré : `output/cours-travail.*` et `output/livre-publication.*`
- prochain nœud : `PUBLICATION_POLICY.md` pour graver les règles observées sur l'ensemble du livre

## v44
- release de gouvernance : pivot publication/travail après discussion d'évaluation
- clarifié : la publication garde la pédagogie utile au lecteur ; elle retire seulement la cuisine interne
- mis à jour : `README.md`, `PUBLICATION_POLICY.md`, `BOOK_BLUEPRINT.md`, `RELEASE_RUNWAY.md`, `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `manifest.yaml`, `BOOTSTRAP_PROMPT.md`
- ajusté : `build/merge_course.py` pour conserver dans la publication les intertitres pédagogiques utiles
- prochain lot : `v45 -> v47`, avec retour en évaluation à `v47`

## v34
- release de gouvernance post-évaluation v33
- trajectoire `v34 -> v37` explicitée pour fermer proprement le use-case 1
- `QUEUE.md` recentrée sur `14.02`, `14.03` puis une passe de cohérence locale
- verrous maintenus sur `15-use-case-2/*` et `16-devoir-final/*` jusqu'après l'évaluation `v37`

# CHANGELOG

## v4
- base: import de la vraie `cours-ai-starter-kit-v2.zip` fournie par l'utilisateur
- ajout: chapitre `04-faux-hype-et-limites-des-llm`
- ajout: `README.md` comme point d'entrée unique pour les rédacteurs
- ajout: `WORKFLOW.md`, `QUEUE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`
- structure: renumérotation des anciens chapitres 04..15 vers 05..16 pour insérer le nouveau chapitre sans ambiguïté
- but: permettre une progression cumulative, locale, traçable, transmissible d'un rédacteur au suivant

## v5
- ajouté: `preface.md` avec un mot de l’auteur sur l’arrêt de carrière lié à la cerebral palsy et l’ouverture vers le changement de paradigme des LLM
- ajusté: `README.md` pour inclure la préface dans la séquence de lecture
- ajusté: `main.md` pour exposer la préface dans l’ouverture du cours
- enrichi: métadonnées de release pour renforcer la continuité inter-release


## v6
- ajouté: pipeline de build PDF intégré dans la release
- ajouté: génération de `output/cours.pdf`, `output/cours.html` et `output/cours-merge.md`
- ajouté: wrappers `make_pdf.bat` et `make_pdf.sh`
- ajusté: `README.md`, `manifest.yaml`, `RELEASE_STATE.yaml`, `RELEASES.md`

## v7
- densifié: `03-histoire-des-ia/02-Ce-que-change-le-LLM.md`
- densifié: `04-faux-hype-et-limites-des-llm/01-Le-faux-hype-autour-des-LLM.md`
- densifié: `04-faux-hype-et-limites-des-llm/03-Ce-que-les-LLM-ne-feront-jamais-tels-quels.md`
- densifié: `05-nailgun-et-changement-de-posture/01-Pourquoi-la-métaphore-du-nailgun-fonctionne.md`
- densifié: `07-decoupage-du-travail/01-Découpage-par-responsabilité.md`
- densifié: `09-pilotage-agents/03-Orchestration-de-plusieurs-agents.md`
- ajusté: `QUEUE.md`, `manifest.yaml`, `RELEASE_STATE.yaml`, `RELEASES.md`, `CURRENT_RELEASE.md`



## v8
- densifié: `03-histoire-des-ia/01-Des-systèmes-experts-aux-modèles-génératifs.md`
- densifié: `06-repenser-un-projet/01-Projet-continu-ou-hiérarchie-de-décisions.md`
- densifié: `08-collaboration-orthogonale/02-Définir-des-contrats-stables.md`
- densifié: `10-hallucinations-et-validation/02-Séparer-génération-et-vérification.md`
- densifié: `11-contexte-propre-et-court/03-Construire-des-context-packs-minimaux.md`
- densifié: `12-prompt-layering-openai/03-Le-prompt-comme-couche-de-gouvernance.md`
- densifié: `13-quanta-1d/02-Définir-un-quantum-actionnable.md`
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `CURRENT_RELEASE.md`

## v8
- densifié: `03-histoire-des-ia/01-Des-systèmes-experts-aux-modèles-génératifs.md`
- densifié: `06-repenser-un-projet/01-Projet-continu-ou-hiérarchie-de-décisions.md`
- densifié: `08-collaboration-orthogonale/02-Définir-des-contrats-stables.md`
- densifié: `10-hallucinations-et-validation/02-Séparer-génération-et-vérification.md`
- densifié: `11-contexte-propre-et-court/03-Construire-des-context-packs-minimaux.md`
- ajusté: `QUEUE.md`, `manifest.yaml`, `RELEASE_STATE.yaml`, `RELEASES.md`, `CURRENT_RELEASE.md`


## v9
- densifié: `01-histoire-du-metier/01-Le-codeur-avant-les-LLM.md`
- densifié: `02-evolution-du-code/03-Intégration-contre-fabrication.md`
- densifié: `05-nailgun-et-changement-de-posture/02-Crise-d'identité-ou-changement-de-niveau.md`
- densifié: `06-repenser-un-projet/02-Du-faire-au-faire-faire-proprement.md`
- densifié: `07-decoupage-du-travail/02-Découpage-par-interface.md`
- ajusté: `QUEUE.md` pour garder les use-case et le devoir final en fin de chaîne
- ajusté: `RELEASE_STATE.yaml`, `manifest.yaml`, `RELEASES.md`, `CURRENT_RELEASE.md`

## v10

- enrichissement de six nœuds amont encore ouverts avant les cas pratiques
- maintien explicite de la règle: use-case et devoir final après consolidation des chapitres structurants
- régénération des artefacts `output/cours-merge.md`, `output/cours.html` et `output/cours.pdf`

### Nœuds complétés
- `01-histoire-du-metier/02-Rareté,-prestige-et-limites.md`
- `02-evolution-du-code/02-Frameworks,-bibliothèques-et-réutilisation.md`
- `05-nailgun-et-changement-de-posture/03-Redevenir-central-sans-taper-tout-le-code.md`
- `08-collaboration-orthogonale/01-Réduire-les-zones-de-recouvrement.md`
- `09-pilotage-agents/01-Rôle,-périmètre-et-intrants.md`
- `10-hallucinations-et-validation/01-Réduire-le-périmètre-des-tâches.md`

## v11
- ajout: `STABILIZATION_PLAN.md` pour structurer les prochaines passes de travail
- réorganisation: `QUEUE.md` en passes A/B/C + verrou explicite des cas pratiques et du devoir final
- ajusté: `README.md` pour imposer la lecture du plan de stabilisation avant la queue
- ajusté: `RELEASE_STATE.yaml`, `manifest.yaml`, `CURRENT_RELEASE.md`
- aucun ajout de contenu de fond dans cette release

## v12
- nettoyage des placeholders vagues transformés en placeholders structurés
- suppression des doublons de fichiers aux noms mal encodés
- ajout de `PRE_USECASE_GAP_ANALYSIS.md` pour recenser les nœuds encore manquants avant les use-case
- mise à jour de `README.md`, `QUEUE.md`, `STABILIZATION_PLAN.md`, `RELEASES.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`

## v13
- fichier cible: README.md + cadrage de release
- objectif: rendre la mission de stabilisation autonome par simple lecture du README
- ajouté: six manques pré-use-case, cadrage A/B/C, passes recentrées dans la queue et le plan
- évité: refonte du contenu pédagogique des chapitres et ouverture prématurée des use-case
- prochain pas: prendre le premier item ouvert de la passe 1 dans QUEUE.md

## v14
- fichier cible: `01-histoire-du-metier/chapitre.md`
- objectif: ouvrir le livre avec une thèse historique explicite et une transition nette vers `02-evolution-du-code`
- complété: remplacement du placeholder structuré par une vraie ouverture de chapitre
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`
- prochain pas: prendre `02-evolution-du-code/chapitre.md`, premier item ouvert restant de la passe 1

## v15
- fichier cible: `02-evolution-du-code/chapitre.md`
- objectif: clarifier le déplacement historique de la valeur technique et préparer l'entrée vers `03-histoire-des-ia`
- complété: remplacement du placeholder structuré par une vraie ouverture de chapitre
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`
- prochain pas: prendre `03-histoire-des-ia/chapitre.md`, premier item ouvert restant de la passe 1


## v16
- fichier cible: `03-histoire-des-ia/chapitre.md`
- objectif: resserrer l'arc historique des IA et préparer l'entrée critique vers `04-faux-hype-et-limites-des-llm`
- complété: remplacement du placeholder structuré par une vraie ouverture de chapitre
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: prendre `04-faux-hype-et-limites-des-llm/chapitre.md`, premier item ouvert restant de la passe 1


## v17
- fichier cible: `04-faux-hype-et-limites-des-llm/chapitre.md`
- objectif: cadrer ce chapitre comme filtre mental avant la méthode opératoire et préparer l'entrée vers `05-nailgun-et-changement-de-posture`
- complété: ouverture densifiée avec thèse, rôle pédagogique, points de sortie et transition explicite
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: prendre `05-nailgun-et-changement-de-posture/chapitre.md`, premier item ouvert restant de la passe 1


## v18
- fichier cible: `05-nailgun-et-changement-de-posture/chapitre.md`
- objectif: expliciter la bascule de posture créée par les LLM et préparer l'entrée vers `06-repenser-un-projet`
- complété: ouverture densifiée avec thèse, rôle charnière, idées de sortie, erreur de lecture à éviter et transition explicite
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: prendre `06-repenser-un-projet/chapitre.md`, premier item ouvert restant de la passe 1

## v19
- fichier cible: `06-repenser-un-projet/chapitre.md`
- objectif: expliciter la rupture avec la vision continue du projet logiciel et préparer l'entrée vers `07-decoupage-du-travail`
- complété: ouverture densifiée avec thèse, rôle du chapitre, idées de sortie, erreur de lecture à éviter et transition explicite
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: prendre `07-decoupage-du-travail/chapitre.md`, premier item ouvert restant de la passe 1



## v20
- fichier cible: `07-decoupage-du-travail/chapitre.md`
- objectif: annoncer clairement les principes de découpage qui irriguent la suite et préparer l'entrée vers `08-collaboration-orthogonale`
- complété: ouverture densifiée avec thèse, rôle du chapitre, idées de sortie, erreur de lecture à éviter et transition explicite
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: prendre `08-collaboration-orthogonale/chapitre.md`, premier item ouvert restant de la passe 1


## v21

- densification de `08-collaboration-orthogonale/chapitre.md` avec une vraie ouverture de chapitre
- thèse du chapitre clarifiée autour de l'orthogonalité, des contrats stables et du journal de décisions
- transition explicite vers `09-pilotage-agents/chapitre.md`
- `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md` et `manifest.yaml` mis à jour pour chaîner la passe 1


## v22

- densification de `09-pilotage-agents/chapitre.md` avec une vraie ouverture de chapitre
- thèse du chapitre clarifiée autour du rôle, du périmètre, des intrants, de la reprise de main et de l'orchestration
- transition explicite vers `10-hallucinations-et-validation/chapitre.md`
- `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md` et `manifest.yaml` mis à jour pour chaîner la passe 1


## v23

- objectif: remise en cohérence du pilotage après analyse de la v22
- ajouté: diagnostic pré-use-case remis à jour, `RELEASE_RUNWAY.md`, queue réalignée, point de retour fixé à `v28`
- évité: aucune densification de fond dans cette release
- verrouillé: use-case et devoir final restent fermés jusqu'après évaluation `v28`
- prochain pas: prendre `10-hallucinations-et-validation/chapitre.md` pour finir la passe 1


## v24

- densification de `10-hallucinations-et-validation/chapitre.md` avec une vraie ouverture de chapitre
- densification de `11-contexte-propre-et-court/chapitre.md` avec une vraie ouverture de chapitre
- densification de `12-prompt-layering-openai/chapitre.md` avec une vraie ouverture de chapitre
- densification de `13-quanta-1d/chapitre.md` avec une vraie ouverture de chapitre
- `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md` et `manifest.yaml` mis à jour pour ouvrir la passe 2A


## v25
- densifié: `06-repenser-un-projet/03-Interfaces,-validations-et-livrables.md`
- densifié: `07-decoupage-du-travail/03-Découpage-par-capacité-de-validation.md`
- densifié: `10-hallucinations-et-validation/03-Exiger-des-artefacts-vérifiables.md`
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`


## v26
- densifié: `08-collaboration-orthogonale/03-Journal-de-décisions-et-coordination.md`
- densifié: `11-contexte-propre-et-court/01-Contexte-utile-contre-contexte-grenier.md`
- densifié: `11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md`
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`


## v27
- fichiers cibles: `12.01`, `12.02`, `13.01`, `13.03`
- objectif: fermer la passe 2C en clarifiant la gouvernance par prompts et le contrôle de dérive par quanta courts
- complété: remplacement des placeholders structurés par quatre sections rédigées et reliées entre elles
- ajusté: `QUEUE.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: préparer `v28` comme retour en évaluation contenu/contenant sans ouvrir les use-case


## v28
- objectif: fournir la version de retour en évaluation prévue par `RELEASE_RUNWAY.md`
- ajouté: diagnostic pré-use-case remis en phase avec l'état réel après fermeture des passes 1, 2A, 2B et 2C
- clarifié: distinction entre nœuds centraux déjà stabilisés, nœuds amont encore ouverts mais non bloquants, et use-case toujours verrouillés
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`
- prochain pas: attendre l'évaluation v28 et arbitrer la suite
## v29
- release de gouvernance post-évaluation v28
- validation du contenant et du fond: pas de rollback vers v12
- décision d'ouvrir un cycle de pré-ouverture contrôlée du use-case 1
- fixation du prochain retour en évaluation à v33
- maintien du verrou sur le use-case 2 et le devoir final



## v30
- fichier cible: `09-pilotage-agents/02-Quand-déléguer-et-quand-reprendre-la-main.md`
- objectif: fermer le dernier nœud méthodologique sensible avant l'ouverture du use-case 1
- complété: seuils de délégation utile, seuils de reprise humaine, signaux faibles de dérive et règle de reprise locale
- ajusté: `QUEUE.md`, `PRE_USECASE_GAP_ANALYSIS.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `RELEASES.md`, `manifest.yaml`
- prochain pas: prendre la passe 3 de transitions et de cohérence globale avant use-case


## v31
- objectif: fermer la passe de transitions et de cohérence globale avant use-case
- ajusté: transitions explicites ajoutées dans `05` à `13` pour rendre la chaîne méthodologique continue jusqu'au cas pratique
- clarifié: `PRE_USECASE_GAP_ANALYSIS.md` formalise le report des trois nœuds historiques encore ouverts
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`
- prochain pas: ouvrir `14-use-case-1/chapitre.md` en `v32` sans ouvrir le use-case 2 ni le devoir final


## v32
- objectif: ouvrir et démarrer le use-case 1 sans déverrouiller le use-case 2 ni le devoir final
- densifié: `14-use-case-1/chapitre.md`
- densifié: `14-use-case-1/01-Clarifier-le-besoin.md`
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`
- prochain pas: traiter `14-use-case-1/02-Découper-en-sous-systèmes-et-interfaces.md` en vue du retour d'évaluation `v33`



## v33
- objectif: fournir la release de retour en évaluation prévue après l'ouverture du use-case 1
- ajusté: `PRE_USECASE_GAP_ANALYSIS.md` pour distinguer ce qui est fermé, ce qui est partiel et ce qui reste verrouillé
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASE_RUNWAY.md`, `manifest.yaml`
- prochain pas: attendre l'évaluation v33 avant d'ouvrir `14-use-case-1/02-Découper-en-sous-systèmes-et-interfaces.md`


## v35
- densifié: `14-use-case-1/02-Découper-en-sous-systèmes-et-interfaces.md`
- clarifié: passage du besoin local à des sous-systèmes contrôlables, des interfaces brèves et des points de reprise humaine
- ajusté: `README.md`, `QUEUE.md`, `PRE_USECASE_GAP_ANALYSIS.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`

## v36
- densifié: `14-use-case-1/03-Attribuer-rôles,-validations-et-intégration.md`
- clarifié: convergence entre rôles bornés, validations locales, motifs de reprise et intégration finale
- ajusté: `README.md`, `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`


## v37
- objectif: fermer la courte passe de cohérence locale sur `14-use-case-1/*` et préparer le retour en évaluation `v38`
- ajusté: `14-use-case-1/chapitre.md`, `14-use-case-1/01-Clarifier-le-besoin.md`, `14-use-case-1/02-Découper-en-sous-systèmes-et-interfaces.md`, `14-use-case-1/03-Attribuer-rôles,-validations-et-intégration.md`
- ajusté: `README.md`, `QUEUE.md`, `CURRENT_RELEASE.md`, `PRE_USECASE_GAP_ANALYSIS.md`, `RELEASE_RUNWAY.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`
- prochain pas: attendre l'évaluation v38 avant toute ouverture du use-case 2 ou du devoir final

## v38
- réorientation éditoriale: passage explicite du projet de « cours modulaire » à « livre publiable »
- ajout d'un pipeline à deux rendus: édition de travail et édition publication
- ajout de `PUBLICATION_POLICY.md`, `BOOK_BLUEPRINT.md`, `EDITORIAL_MARKERS.md` et `BOOTSTRAP_PROMPT.md`
- gel explicite de `15-use-case-2/*` et `16-devoir-final/*` pour délégation humaine
- queue réorganisée jusqu'au prochain retour d'évaluation fixé à `v43`

## v39
- objectif: fermer la passe technique de rendu publication avant d'ouvrir la macro-structure du livre
- ajusté: `build/merge_course.py` pour retirer du rendu public les sections de fabrication visibles (`Renvois utiles`, `Passage explicite ...`, `Ce que cette étape a réellement stabilisé`)
- vérifié: cycle réel `build/build_pdf.py . --mode both` régénéré avec un merge public sans résidu de fabrication détecté
- ajusté: `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASES.md`, `manifest.yaml`
- prochain pas: ouvrir `01-histoire-du-metier/chapitre.md` dans la passe B — macro-structure du livre

## v40
- fichiers cibles: `01/chapitre.md`, `03/chapitre.md`, `05/chapitre.md`, `09/chapitre.md`, `13/chapitre.md`
- objectif: faire sentir plus nettement les grandes parties du livre et resserrer les transitions longues
- ajouté: ouvertures plus incarnées, fonctions macro-structurelles plus explicites et seuils de transition mieux marqués
- évité: ouverture du use-case 2, du devoir final ou d’un nouveau chantier de fond
- prochain pas: prendre `01-histoire-du-metier/03-Pourquoi-certains-vivent-l'IA-comme-une-perte.md`

## v41
- fichiers cibles: `01.03`, `03.03`, `05.03`
- objectif: remplacer les placeholders restants et rendre le livre plus incarné sans casser la structure modulaire
- ajouté: lecture plus juste de la perte symbolique, notion de compression cognitive et centralité par le cadrage
- évité: dilution du propos dans des anecdotes longues ou ouverture de nouveaux nœuds
- prochain pas: poser les marqueurs éditoriaux légers et vérifier leur disparition en édition publication

## v42
- fichiers cibles: `preface.md`, `01.03`, `03.03`, `05/chapitre.md`, `13/chapitre.md`
- objectif: semer quelques marqueurs éditoriaux utiles au futur livre sans alourdir le texte courant
- ajouté: marqueurs `[[CITATION]]`, `[[FIGURE]]`, `[[BLAGUE]]` et `[[INSERT]]` placés localement
- vérifié: les marqueurs disparaissent bien de `output/livre-publication-merge.md` après régénération work/public
- prochain pas: revenir en évaluation v43 avec un diagnostic propre du lot

## v43
- release de retour en évaluation du lot `v40 -> v42`
- diagnostic mis à jour pour distinguer le stabilisé, le souhaitable et le gelé
- QUEUE.md fermée sur le retour en évaluation, `RELEASE_RUNWAY.md` recentré sur le lot clos
- évité: ouverture d’un nouveau cycle sans arbitrage
- prochain pas: attendre la décision éditoriale post-v43


## v51
- fichiers cibles: `13-quanta-1d/chapitre.md`, `13-quanta-1d/01-Pourquoi-1-jour-change-la-validation.md`, `13-quanta-1d/02-Définir-un-quantum-actionnable.md`, `13-quanta-1d/03-Autonomie-et-dérive-contrôlée.md`, `build/merge_course.py`
- objectif: lever le contresens du quantum 1D, réaligner les exemples sur l'entreprise et lisser la publication vers une prose plus continue
- ajouté: clarification explicite de "1D" comme borne de gouvernance, exemples marketing/finance/RH/opérations/direction, transformation des intertitres pédagogiques en amorces de prose dans le rendu publication
- évité: ouverture de `15-use-case-2/*`, ouverture de `16-devoir-final/*`, réduction massive du rendu publication
- prochain pas: retour en évaluation v51 sur fond du chapitre 13 et lisibilité du rendu publication
## v52

- Recentrage de gouvernance sur le chapitre 13
- Interdiction de le réparer par petits ajustements
- Plan acté : v53 destruction, v54 recréation éventuelle, v55 évaluation


## v53
- fichiers cibles: `13-quanta-1d/chapitre.md`, `13-quanta-1d/01-*`, `13-quanta-1d/02-*`, `13-quanta-1d/03-*`, `12-prompt-layering-openai/chapitre.md`, `14-use-case-1/chapitre.md`, `09-pilotage-agents/02-*`, `09-pilotage-agents/03-*`, `10-hallucinations-et-validation/01-*`, `12-prompt-layering-openai/03-*`, `manifest.yaml`
- objectif: retirer l'ancien chapitre 13 sans casser la cohérence du livre ni le pipeline de rendu
- ajouté: placeholders de retrait côté travail, disparition du chapitre 13 en publication, transitions adjacentes recentrées vers le cas guidé, manifest complet régénéré
- évité: réparation à la marge de l'ancienne logique, réouverture de `15-use-case-2/*`, réouverture de `16-devoir-final/*`
- prochain pas: décider en v54 si une matière réellement nouvelle justifie la recréation complète du chapitre 13

## v53b
- ajoute un bootstrap de sens pour le nouveau chapitre 13
- remplace les fichiers retires du chapitre 13 par une base de redaction orientee quanta 1D
- met a jour README, QUEUE, RELEASE_RUNWAY et BOOTSTRAP_PROMPT


## v55
- objectif: planifier le prochain lot après validation de fond du nouveau chapitre 13
- ajouté: `faculta_boss.md` avec une première quote boss et règles d'intégration facultative
- ajusté: `README.md`, `QUEUE.md`, `RELEASE_RUNWAY.md`, `BOOTSTRAP_PROMPT.md`, `RELEASE_STATE.yaml`, `CURRENT_RELEASE.md`, `PUBLICATION_POLICY.md`
- évité: retoucher le fond des chapitres, rouvrir le use-case 2 ou le devoir final
- prochain pas: v56 polissage du chapitre 13, v57 enrichissement des exemples entreprise, v58 retour en évaluation


## v56
- passe d'hygiène et de vérification ;
- `faculta_boss.md` normalisé et confirmé présent ;
- `faculta_redacteur.md` ajouté à la séquence ;
- artefacts jetables et cache Python nettoyés ;
- le prochain lot est autorisé à optimiser la forme et la structure.

## v60
- objectif: optimiser la forme et les transitions sans rouvrir le cadrage de fond valide en v59
- fichiers cibles: `13-quanta-1d/chapitre.md`, `13-quanta-1d/01-Pourquoi-1-jour-change-la-validation.md`, `13-quanta-1d/02-Définir-un-quantum-actionnable.md`, `13-quanta-1d/03-Autonomie-et-dérive-contrôlée.md`, `10-hallucinations-et-validation/chapitre.md`, `12-prompt-layering-openai/chapitre.md`, `14-use-case-1/chapitre.md`, `faculta_boss.md`, `faculta_redacteur.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASE_RUNWAY.md`, `QUEUE.md`
- ajouté: prose plus continue dans le chapitre 13, exemples entreprise plus concrets, transition 12 -> 13 -> 14 plus nette, intégration tracée de la quote BOSS-001
- évité: réinvention de la thèse du chapitre 13, retour à la logique "1 jour", ouverture de `15-use-case-2/*` et `16-devoir-final/*`, réduction massive du rendu publication
- prochain pas: v61 poursuivre le lissage de forme dans les chapitres 10 a 12 et densifier les exemples de contexte, validation et handoff

## v63
- objectif: renforcer `09-pilotage-agents/03-Orchestration-de-plusieurs-agents.md` par un handoff inter-equipe concret sans reexpliquer toute la theorie
- ajouté: exemple entreprise marketing/CRM, baton de handoff plus net, responsabilites locales mieux separees entre cadreur, producteur, verificateur et integrateur
- évité: reouverture du cadrage de fond, duplication des sections 09.01 et 09.02, modification de `15-use-case-2/*` et `16-devoir-final/*`
- prochain pas: polir `13-quanta-1d/chapitre.md` ou renforcer `13-quanta-1d/02-Définir-un-quantum-actionnable.md` avec un exemple entreprise non technique


## v64
- objectif: réaligner la gouvernance documentaire sur l'etat reel de la release recue v63 sans retoucher le fond du livre
- ajusté: `README.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `manifest.yaml`, `RELEASE_RUNWAY.md`, `QUEUE.md`, `BOOTSTRAP_PROMPT.md`, `RELEASES.md`, `faculta_redacteur.md`
- clarifié: ordre reel des priorites `13/chapitre` puis `13.02` puis `11.02`, retour en evaluation decale a `v67`, saut de numerotation `v62` assume comme non documente dans l'historique
- signalé: `02-evolution-du-code/01-De-l'assembleur-aux-langages-haut-niveau.md` reste une dette source ouverte et `output/publication-chapter-tests.md` est absent de la release recue
- prochain pas: transmettre `v64` a la redaction pour `v65`, `v66`, `v67`

## v65
- objectif: polir `13-quanta-1d/chapitre.md` sans changer sa these
- ajusté: prose, transitions, enchainements 12 -> 13 -> 14, formulation du role transversal du quantum 1D
- évité: rethéorisation du chapitre, retour a la logique "1 jour", ouverture de `15-use-case-2/*` et `16-devoir-final/*`
- prochain pas: v66 densifier `13-quanta-1d/02-Définir-un-quantum-actionnable.md` par un exemple entreprise non technique plus net

## v66
- objectif: densifier `13-quanta-1d/02-Définir-un-quantum-actionnable.md` par un exemple entreprise non technique plus net
- ajusté: mini exemple remplace par un cas RH plus detaille, trajectoires diagnostic / arbitrage / communication mieux separées
- évité: rethéorisation du chapitre 13, retour a la logique "1 jour", ouverture de `15-use-case-2/*` et `16-devoir-final/*`
- prochain pas: v67 retour en evaluation du lot `v65 -> v66` et fermeture locale du chantier chapitre 13

## v67
- objectif: evaluer le lot `v65 -> v66` et renvoyer la redaction sur le prochain noeud reel sans rouvrir le cadrage
- constaté: chapitre 13 poli sans changement de these, exemple entreprise densifie, continuite cumulative et isomorphie travail / publication preservees
- ajusté: `README.md`, `QUEUE.md`, `CURRENT_RELEASE.md`, `RELEASE_STATE.yaml`, `RELEASE_RUNWAY.md`, `manifest.yaml`, `faculta_redacteur.md`
- prochain pas: v68 reprendre `11-contexte-propre-et-court/02-Résumer-l'état-sans-traîner-l'historique.md`
