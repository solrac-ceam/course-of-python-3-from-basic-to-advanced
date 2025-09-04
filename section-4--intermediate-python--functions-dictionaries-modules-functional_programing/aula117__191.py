import json

pessoa = {
    "nome": "Luiz Otávio 2",
    "sobrenome": "Miranda",
    "enderecos": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2", "numero": 55},
    ],
    "altura": 1.8,
    "numeros_preferidos": (2, 4, 6, 8, 10),
    "dev": True,
    "nada": None,
}

caminho_pasta = "."
caminho_json = f"{caminho_pasta}/aula117.json"

with open(caminho_json, "w") as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,  # E melhor deixar ele True (default), por compatiobilidade.
        indent=2,
    )

pessoa2 = {}
with open(caminho_json, "r", encoding="utf-8") as arquivo:
    pessoa2 = json.load(arquivo)

print(pessoa2)
