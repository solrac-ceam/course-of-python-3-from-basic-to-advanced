# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


print("Minha solução ")
print("-------------")
data_empristemo = datetime(2020, 12, 20)
data_fim = datetime(data_empristemo.year + 5, data_empristemo.month, data_empristemo.day)
valor_emprestimo = 1000000
parcelas = 60  # 5 anos * 12 meses

valor_parcela = valor_emprestimo / parcelas

print(f"Data do empréstimo: {data_empristemo.strftime('%d/%m/%Y')}")
print(f"Data do final do empréstimo: {data_fim.strftime('%d/%m/%Y')}")
print("Datas de vencimento e valores das parcelas:")

data_vencimento = data_empristemo
for i in range(parcelas):
    if data_vencimento.month > 11:
        data_vencimento = datetime(data_vencimento.year + 1, 1, 20)
    else:
        data_vencimento = datetime(data_vencimento.year, data_vencimento.month + 1, 20)
    print(f"{data_vencimento.strftime('%d/%m/%Y')} - R$ {valor_parcela:.2f}")


print('\n\nSolução do professor')
print('-------------')
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)