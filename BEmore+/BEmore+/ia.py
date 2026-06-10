import ollama

while True:

    pergunta = input("Você: ")

    resposta = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': pergunta
            }
        ]
    )

    print("\nIA:", resposta['message']['content'])