from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

analises = []
contador_id = 1


def analisar_sentimento(texto):
    palavras_positivas = ["feliz", "bom", "ótimo", "maravilhoso", "excelente"]
    palavras_negativas = ["triste", "ruim", "péssimo", "horrível", "terrível"]

    texto_lower = texto.lower()

    for palavra in palavras_positivas:
        if palavra in texto_lower:
            return "positivo"

    for palavra in palavras_negativas:
        if palavra in texto_lower:
            return "negativo"

    return "neutro"


# FRONT
@app.route("/")
def index():
    return send_from_directory(".", "index.html")


# CREATE
@app.route("/analise", methods=["POST"])
def criar_analise():
    global contador_id

    dados = request.get_json()
    texto = dados.get("texto", "")

    sentimento = analisar_sentimento(texto)

    nova_analise = {
        "id": contador_id,
        "texto": texto,
        "sentimento": sentimento,
        "quantidade_palavras": len(texto.split()),
        "quantidade_caracteres": len(texto),
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    analises.append(nova_analise)
    contador_id += 1

    return jsonify(nova_analise), 201


# READ
@app.route("/analises", methods=["GET"])
def listar_analises():
    return jsonify(analises)


# DELETE
@app.route("/analise/<int:id>", methods=["DELETE"])
def deletar_analise(id):
    global analises

    analises = [a for a in analises if a["id"] != id]

    return jsonify({"mensagem": "Análise deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)