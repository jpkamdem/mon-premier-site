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

   > HyperText Transfert Protocol. Requête = client (navigateur), réponse = serveur (donc pythonanywhere) 

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > GET presentation.html, GET style.css, GET favicon.ico 

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > 2** = succès de la requête. 404 = erreur côté client, ressource non trouvée 

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > C'est en local 

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > param = search_query, value = chat

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > On peut pas additionner une chaîne de caractère à un nombre, faut que les 2 params soient forcément des nombres 

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > C'est une porte d'entrée permettant à un utilisateur malveillant d'exécuter du code sur le serveur, et donc d'en compromettre la sécurité 

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > `GET` permet de récupérer une ressource, tandis que `POST` permet de créer une nouvelle ressource. 

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > Recherche = GET car on ne crée pas de ressource mais on cherche à accéder à une donnée de façon pécise, connexion = POST car on va créer une nouvelle ressource, ici une connexion via une requête dans laquelle on stocke les données à envoyer 

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > Non, visibles directement dans l'onglet réseau, requête 

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > 4xx = erreur client donc la requête est en cause (pas forcément l'utilisateur, p-e une erreur de prog dans la création de la requête par les devs), 5xx = erreur serveur (pb côté serveur, bug à corriger par les devs ou même interne à certains outils) 

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > Le navigateur 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > Lorsque la page `/home` est une page de connexion mais que la session de l'utilisateur est encore active, récupérée dans le local/sessionstorage / cookies le session/token_id afin de récupérer l'user, l'identifier, et rediriger le client vers la page `/profil` par exemple

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > Mon OS, mon hôte (pythonanywhere) et les systèmes de compressions supportés 

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > wikipedia peut inspecter ces données et directement m'afficher le site dans une de mes langues supportées 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > Pas une page mais le `favicon.ico`

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > Un non-sens 

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > Une page HTML est rendue à un utilisateur final pour être facilement lisible (et aidée par du css). Json est un format de fichier simple à lire par les humains et les machines, et est utilisé pour transmettre des données entre serveurs 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > serveur = récupération de l'heure, de la date et affichage du message "bonjour depuis mon api", navigateur = remplissage du span#heure avec le contenu des données récupérées via l'api et la variable response, et activation seconde par seconde via setInterval() et mettreAJour() 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > N'importe quelle application connectée à Internet permettant de consulter des données, donc je dirai mon application méteo. Elle récupère mon emplacement/les villes favorites, en récupère les données météorologiques et ensuite me les rend dans un affichage jolie 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> Alors quand tu tentes d'accéder à un site, dans le jargon on va dire que tu envoies une requête, ici pour récupérer la page https://monsite.com . A partir de là, le serveur chargé de gérer cet URL (on appelle ça comme ça aussi une adresse) va aller construire la page correspondant au chemin renseigné. Le chemin c'est ce qui suit un slash /, bon ici il n'y en a pas mais voilà. Après selon comment l'équipe de développement a géré le routage (la façon dont les pages sont joignables comme des routes), tu vas être amenée à une page spécifique qui contient du HTML donc un langage qui balise les éléments sur la page (genre ici il y a un bouton, là un paragaphe, ici une barre de navigation...), du CSS qui permet d'ajouter de la personnalisation et du style à la page (ce titre va être de telle couleur, avec telle police, cet élément va afficher à la verticale tous les éléments avec tel espace vide autour, le tout de façon centrée par rapport à l'élément dans lequel il est, ajouter un style différent selon l'action que tu fais avec ta souris comme un survol ou un clic, adapter la taille d'un élément à la taille de l'écran, etc il y a une flopée de règles possibles). Enfin on peut aussi rajouter du javascript qui permet de rajouter un peu d'intéractivité (par exemple un élément qui s'actualise en temps réel comme une horloge, le fait d'envoyer un formulaire et de déclencher une autre action par la suite, ajouter des éléments à un panier, trier les éléments d'une liste...).
