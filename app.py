from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    frutas = ["Morango", "Uva", "Maçã", "Mamão"]
    return render_template("index.html", frutas=frutas)
    # por padrão, é comum chamarmos com o mesmo nome função=idade(nome=nome)

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)