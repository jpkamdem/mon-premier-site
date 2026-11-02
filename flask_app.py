# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return render_template("accueil.html")

# 3xx : une redirection
@app.get("/home")
def home():
    return redirect("/")

# 4xx : un accès interdit
@app.get("/secret")
def secret():
    abort(403)

# Une page d'erreur 404 personnalisée
@app.errorhandler(404)
def page_introuvable(erreur)
    return render_template("404.html"), 404

# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return render_template("presentation.html", prenom="Jean-Philippe", nom="Kamdem")

@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html")

@app.get("/loisirs")
def loisirs():
    return "J'aime bien les jeux vidéos du style FGC, Metroidvania et RPG, un peu les séries & films, beaucoup les films d'animations et les mangas de tout genre/catégorie."

@app.get("/calcul")
def calcul():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    op = str(request.args.get("op", "plus"))
    match op:
        case "moins":
            return f"{a} - {b} = {a - b}"
        case "fois":
            return f"{a} x {b} = {a * b}"
        case "div":
            return f"{a} / {b} = {a / b}"
        case "plus":
            return f"{a} + {b} = {a + b}"

@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/salut", methods=["GET", "POST"])
def salut():
    if request.method == "POST":
        prenom = request.form.get("prenom", "inconnu")
        ville = request.form.get("ville", "nulle part")
        couleur = request.form.get("couleur", "aucune")
    else:
        prenom = request.args.get("prenom", "inconnu")
        ville = request.args.get("ville", "nulle part")
        couleur = request.args.get("couleur", "aucune")
    return f"Bonjour {prenom}, qui vient de {ville} et qui aime la couleur {couleur} ! (reçu en {request.method})"

# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
