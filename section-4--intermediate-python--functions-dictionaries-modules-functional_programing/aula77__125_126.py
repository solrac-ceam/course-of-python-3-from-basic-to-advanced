# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

acertos = 0
for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}?")
    
    print()

    print("Opções:")
    for index, opcao in enumerate(pergunta["Opções"]):
        print(f"{index}) {opcao}")
    print()
    
    opcao_escolhida = input("Escolha uma opção: ")
    
    try:
        opcao_escolhida = int(opcao_escolhida)
        acertou = pergunta["Opções"][opcao_escolhida] == pergunta["Resposta"]
        if acertou:
            acertos += 1
            print("Acertou ✅")
        else:
            print("Errou ❌")
    except:
        print("Errou ❌")
    
    print()

print(f"Você acertou {acertos}")
print(f"de {len(perguntas)} perguntas.")
