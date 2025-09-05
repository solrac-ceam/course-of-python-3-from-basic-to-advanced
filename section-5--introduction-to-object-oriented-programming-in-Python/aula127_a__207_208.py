# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


JSON_PATH = (
    "./aula127.json"
)

if __name__ == "__main__":
    # Saving person
    p1 = Person("Carlos Eduardo", "Alfaro Morales")
    p2 = Person("Marleny", "Luque Carbajal")
    p3 = Person("Nancy", "Morales Castro")
    bd = [vars(p1), p2.__dict__, vars(p3)]

    with open(JSON_PATH, "w", encoding="utf8") as file:
        json.dump(bd, file, indent=2, ensure_ascii=False)
