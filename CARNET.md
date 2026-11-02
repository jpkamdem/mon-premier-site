# 📒 Mon carnet de bord

**Nom :** 

**Prénom :** 

**Adresse de mon site :** https://______.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ 

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ 

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ 

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > La page n'existe pas, le serveur n'a pas prévu de réponse pour le chemin que le client a tenté d'accéder. C'est envoyé par le serveur 

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > Error code: 502-backend, donc ça vient du serveur  

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > Le serveur envoie le code source, tandis que le navigateur affiche sa version propre je dirai 

2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > h1 pour un titre très important (jusqu'à h6), p pour paragraphe, ul pour une liste non ordonnée (contre ol pour ordonnée) et li un item d'une liste (ul comme ol). Techniquement on peut faire un site qu'avec des `<div>` et des `<p>` mais c'est pas bien pour plusieurs raisons. Déjà au niveau sémantique, certaines balises indiquent la nature de ce qu'elles contiennent (`<form>`, `<header>`, `<aside>`, `<nav>`, etc.), tandis que certains n'indiquent rien du tout (`<div>`, `<span>`, etc.). Niveau référencement c'est nul de ne pas les utiliser, donc vaut mieux le faire. Aussi c'est pratique pour les humains niveau lisibilité. Compliqué de se retrouver dans un océan de `<div>` imbriquées, alors qu'un `<main>` contenant une `<div>` dans laquelle se trouve 2 `<section>` qui contiennent chacune 3 `<article>` composées elles-même de `<div>` et `<span>`, c'est plus propre. Ca fatigue moins l'esprit et profite à tous donc faut faire attention 

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > la balise `<img>` interprête le lien passé à l'attribut `src` et rend donc l'image. C'est comme si le site téléchargeait l'image. Pratique pour ne pas remplir le dépôt d'images, mais problématique si le service fournissant le lien vers l'image tombe 

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > Question de propreté, c'est pas pratique d'avoir tout le code au même endroit, c'est toujours mieux d'avoir des fichiers plus petits qui s'occupent d'une seule tâche qu'un super fichier de 400 lignes. De plus, dans un contexte d'équipes aux compétences complémentaires, le développeur front Typescript utilisant React et intervenant sur le front n'a pas à intéragir avec le code du serveur, de même que le développeur back python n'a pas à intéragir avec le code d'interface, pour que chacun des 2 puissent travailler sans se gêner

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > C'est le serveur, le code source ne montre jamais `{{ prenom }}` et `{{ nom }}` donc je suppose que ça s'opère en amont 

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > `html` est un langage de balisage, il indique la présence d'éléments sur la page : paragraphe, formulaire, navigation, header/footer... `css` permet de personnaliser l'affichage de la page : changer la taille des éléments (bloc, police), changer l'emplacement des éléments à l'intérieur d'un élément parent, modifier l'affichage selon la taille de l'écran du client, changer les couleurs...

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > 3 : `favicon`, `presentation.html` et `style.css`

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > Pour télécharger la nouvelle version à jour du fichier `style.css` 

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ 

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ 

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ 

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ 

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ 

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ 

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ 

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ 

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ 

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ 

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ 

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ 

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ 
