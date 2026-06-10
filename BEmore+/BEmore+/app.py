from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

# HISTÓRICO DAS CONVERSAS

historico = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        pergunta = request.form["pergunta"]

        resposta = ollama.chat(

            model="phi3",

            messages=[

                {
                    "role": "system",
                    "content": """
                    Você é a BEmore+, uma assistente virtual de saúde e bem-estar.

                    Você ajuda com:
                    - hábitos saudáveis
                    - alimentação
                    - hidratação
                    - sono
                    - rotina saudável
                    - exercícios leves

                    Seja breve, clara e acolhedora.
                    NÃO PESSA DESCULPAS TODAS AS VEZES, VOCÊ É UMA IA DE AJUDA, NÃO SE DESCULPE.
                    """
                },

                {
                    "role": "user",
                    "content": pergunta
                }

            ],

            options={
                "num_predict": 1000
            }

        )

        resposta_ia = resposta["message"]["content"]

        # SALVAR HISTÓRICO

        historico.append({

            "pergunta": pergunta,

            "resposta": resposta_ia

        })

    return render_template(

        "index.html",

        historico=historico

    )

if __name__ == "__main__":
    app.run(debug=True)