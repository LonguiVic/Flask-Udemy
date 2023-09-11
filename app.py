from flask import Flask, render_template, request, redirect, url_for
import urllib.request
import json

app = Flask(__name__)

frutas = []
registros = []

@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
            return redirect(url_for("principal"))  # Redireciona após o POST
    return render_template("index.html", frutas=frutas)

@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
            return redirect(url_for("sobre"))  # Redireciona após o POST
    return render_template("sobre.html", registros=registros)

@app.route('/filmes/<propriedade>')
def filmes(propriedade):

    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=f55e4895d1b273b5a84d1d5d5a7c9f2b"
    elif propriedade == 'kids':
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=f55e4895d1b273b5a84d1d5d5a7c9f2b"
    elif propriedade == '2010':
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=f55e4895d1b273b5a84d1d5d5a7c9f2b"
    elif propriedade == 'drama':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=f55e4895d1b273b5a84d1d5d5a7c9f2b"
    elif propriedade == 'tom_cruise':
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=f55e4895d1b273b5a84d1d5d5a7c9f2b"
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])

if __name__ == "__main__":
    app.run(debug=True)



# app = Flask(__name__)

# # abri uma lista global para armazenar meus dados recebidos frutas = []
# frutas = []
# registros = []


# @app.route('/', methods=["GET", "POST"])
# def principal():
#     # frutas = ["Morango", "Uva", "Maçã", "Mamão",
#     # "Pera", "Melão", "Caju", "Mirtilo"]
#     # Lógica de funcionamento:
#     # se o seu request.method for POST
#     if request.method == "POST":
#         # se sua requisição estiver no caminho form.get."fruta"
#         if request.form.get("fruta"):
#             # então adicione na lista frutas um item "fruta"
#             frutas.append(request.form.get("fruta"))
#     return render_template("index.html", frutas=frutas)
#     # por padrão, é comum chamarmos com o mesmo nome função=idade(nome=nome)


# @app.route('/sobre', methods=["GET", "POST"])
# def sobre():
#     # notas = {"Fulano": 5.0, "Beltrano": 6.0, "Aluno": 7.0,
#     # "Sicrano": 8.5, "Rodrigo": 9.5}
#     if request.method == "POST":
#         if request.form.get("aluno") and request.form.get("nota"):
#             registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
#     return render_template("sobre.html", registros=registros)
#     # 


# if __name__ == "__main__":
#     app.run(debug=True)