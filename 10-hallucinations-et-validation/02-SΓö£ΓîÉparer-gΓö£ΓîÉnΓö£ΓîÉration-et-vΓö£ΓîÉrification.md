---
id: "10.02"
title: "Séparer génération et vérification"
parent: "10"
level: section
status: draft
owner_concept: "hallucinations-et-validation-02"
summary: >
  Décrit une méthode simple d'audit local: un acteur produit, un autre vérifie,
  puis seulement on intègre.
---

# Séparer génération et vérification

## Idée centrale

Un des moyens les plus simples de réduire les hallucinations consiste à refuser qu’un même mouvement mental fasse à la fois la production, l’autojustification et la validation finale. Quand un agent génère puis se valide lui-même dans le même souffle, il a tendance à confondre cohérence apparente et conformité réelle.

Séparer la génération et la vérification ne demande pas forcément deux modèles différents. Il faut surtout deux **moments distincts**, deux consignes distinctes et, si possible, deux formats de sortie distincts. On produit d’abord un artefact borné. Ensuite, on l’audite selon une grille locale.

## Pourquoi c'est important

Cette séparation évite de transformer la plausibilité en vérité opérationnelle. Elle ralentit un peu la boucle locale, mais elle économise beaucoup de temps en aval, car elle réduit l’intégration de fragments séduisants mais faux, imprécis ou hors périmètre.

Dans un projet modulaire, l’enjeu n’est pas seulement de produire du texte, du code ou un plan. L’enjeu est de produire quelque chose qu’un autre acteur peut reprendre sans hériter d’hypothèses cachées.

## Erreur classique

L’erreur classique consiste à demander à l’agent: “rédige cela et assure-toi que c’est correct”. Cette consigne semble raisonnable, mais elle fusionne deux tâches qui devraient rester distinctes. Le modèle optimise alors une réponse qui paraît correcte, au lieu d’exposer clairement ce qui est sûr, ce qui est supposé et ce qui reste à vérifier.

Autre erreur: faire une “vérification” purement rhétorique. Si l’audit se limite à reformuler le texte ou à répéter qu’il respecte la demande, on n’a pas séparé la vérification; on a juste ajouté une couche de prose.

## Méthode concrète

Utilise une boucle locale en trois temps.

1. **Génération**: demander un artefact borné avec un format strict.
2. **Audit**: relire cet artefact contre une grille locale fixe.
3. **Intégration**: n’accepter l’artefact que s’il passe la grille.

La grille d’audit peut rester courte. Par exemple: respecte-t-il le périmètre? Duplique-t-il un concept déjà traité ailleurs? Introduit-il des affirmations non justifiées? Le format demandé a-t-il été respecté? Une vérification simple mais répétable bat une impression générale de qualité.

## Mini exemple

Un agent rédige une section Markdown de 600 mots. Un second passage — idéalement avec un prompt de vérification, ou un second agent — ne lui demande pas d’améliorer le style. Il doit seulement vérifier: présence des rubriques attendues, absence de duplication lourde avec les sections sœurs, cohérence avec le `chapitre.md`, renvois corrects, absence de débordement de périmètre.

Si l’audit échoue, on corrige localement avant d’intégrer. On ne laisse pas l’erreur se propager dans le reste du cours.

## Règle pratique

La génération produit une proposition. La vérification décide si cette proposition mérite d’entrer dans la source de vérité. Tant que ces deux rôles restent confondus, les hallucinations trouvent toujours un passage.

## Renvoi éventuel

La réduction du périmètre des tâches est traitée dans `01-Réduire-le-périmètre-des-tâches.md`. La production d’artefacts vérifiables est développée dans `03-Exiger-des-artefacts-vérifiables.md`.
