from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    frutas = ["Morango", "Uva", "Maçã", "Mamão", "Pera", "Melão", "Caju", "Mirtilo"]
    return render_template("index.html", frutas=frutas)
    # por padrão, é comum chamarmos com o mesmo nome função=idade(nome=nome)

@app.route('/sobre')
def sobre():
    notas = {"Fulano": 5.0, "Beltrano": 6.0, "Aluno": 7.0, "Sicrano": 8.5, "Rodrigo": 9.5}
    return render_template("sobre.html", notas=notas)

if __name__ == "__main__":
    app.run(debug=True)