# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula127_a__207_208 import Person, JSON_PATH

# Reading person
person_dicts = []
with open(JSON_PATH, "r", encoding="utf8") as file:
    person_dicts = json.load(file)

bd2 = [Person(**p_dict) for p_dict in person_dicts]
for person in bd2:
    print(person.name, person.last_name)
