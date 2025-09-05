# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
indice_primeiro_dia, numero_dias = calendar.monthrange(2022, 12)  # Retorna o primeiro dia do mês e o número de dias no mês
print(list(enumerate(calendar.day_name)))  # Lista os dias da semana
print(calendar.day_name[indice_primeiro_dia])  # Nome do primeiro dia do mês
indice_ultimo_dia = calendar.weekday(2022, 12, numero_dias)  # Dia da semana do último dia do mês
print(calendar.day_name[indice_ultimo_dia])  # Nome do último dia do mês
print()
print(calendar.monthcalendar(2022, 12))  # Matriz com os dias do mês
print()
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            print("   ", end="")  # Espaço para dias que não pertencem ao mês
        else:
            print(f"{day:2d} ", end="")  # Formatação para alinhar os dias
    print()  # Nova linha após cada semana
