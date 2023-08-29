from flask import Flask, render_template, request

app = Flask(__name__)

# abri uma lista global para armazenar meus dados recebidos frutas = []
frutas = []
registros = []


@app.route('/', methods=["GET", "POST"])
def principal():
    # frutas = ["Morango", "Uva", "Maçã", "Mamão",
    # "Pera", "Melão", "Caju", "Mirtilo"]
    # Lógica de funcionamento:
    # se o seu request.method for POST
    if request.method == "POST":
        # se sua requisição estiver no caminho form.get."fruta"
        if request.form.get("fruta"):
            # então adicione na lista frutas um item "fruta"
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)
    # por padrão, é comum chamarmos com o mesmo nome função=idade(nome=nome)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    # notas = {"Fulano": 5.0, "Beltrano": 6.0, "Aluno": 7.0,
    # "Sicrano": 8.5, "Rodrigo": 9.5}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)
    # 


if __name__ == "__main__":
    app.run(debug=True)