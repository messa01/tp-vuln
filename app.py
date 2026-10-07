from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>CyberLab</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: white;
        }

        header {
            background: #111827;
            padding: 20px 50px;
            border-bottom: 1px solid #334155;
        }

        header h1 {
            margin: 0;
        }

        nav {
            margin-top: 10px;
        }

        nav a {
            color: #94a3b8;
            text-decoration: none;
            margin-right: 25px;
        }

        nav a:hover {
            color: white;
        }

        main {
            max-width: 900px;
            margin: 60px auto;
            padding: 20px;
        }

        .card {
            background: #1e293b;
            padding: 25px;
            border-radius: 12px;
            margin-top: 25px;
        }

        input {
            padding: 12px;
            width: 70%;
            border-radius: 6px;
            border: none;
        }

        button {
            padding: 12px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }

        .warning {
            color: #fbbf24;
        }
    </style>
</head>

<body>

<header>
    <h1>🛡️ CyberLab</h1>

    <nav>
        <a href="/">Accueil</a>
        <a href="/search">Recherche</a>
        <a href="/admin">Administration</a>
    </nav>
</header>

<main>
    <div class="card">
        <h2>Bienvenue sur CyberLab</h2>

        <p>
            CyberLab est une plateforme pédagogique dédiée
            à la sensibilisation à la cybersécurité.
        </p>

        <p>
            Découvrez les risques liés aux applications web
            et apprenez à mieux les sécuriser.
        </p>
    </div>

    <div class="card">
        <h2>🔎 Recherche</h2>

        <form action="/search" method="get">
            <input
                type="text"
                name="q"
                placeholder="Rechercher une ressource..."
            >

            <button type="submit">Rechercher</button>
        </form>
    </div>

    <div class="card">
        <h2>📊 Sécurité</h2>

        <p>Statut de la plateforme :</p>

        <p>🟢 Application disponible</p>
        <p>🟡 Analyse de sécurité en cours</p>

        <p class="warning">
            Environnement pédagogique
        </p>
    </div>
</main>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/search")
def search():
    query = request.args.get("q", "")

    return f"""
    {HTML}

    <script>
        document.querySelector("main").innerHTML =
        `<div class="card">
            <h2>Résultats de recherche</h2>
            <p>Recherche : {query}</p>
            <p>3 ressources trouvées.</p>
        </div>`;
    </script>
    """


@app.route("/admin")
def admin():
    return """
    <h1>🔐 Administration CyberLab</h1>

    <p>Bienvenue dans l'espace administrateur.</p>

    <p>Nombre d'utilisateurs : 42</p>
    <p>Alertes de sécurité : 3</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
