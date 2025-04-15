# Atividade 2 - Data

from datetime import datetime
from datetime import timedelta
from workalendar.america import Brazil


data_um = input("Digite a data no formato dd/mm/aaaa: ")
data_dois = input("Digite a data no formato dd-mm-aaaa: ")

date_format = "%d/%m/%Y"
data_um = datetime.strptime(data_um, date_format)
data_dois = datetime.strptime(data_dois, date_format)
diferenca = data_dois - data_um
dia_util = 0
calendario = Brazil()
feriados = calendario.holidays(data_um.year)

novo_feriado = input("Digite o feriado no formato dd/mm/aaaa: ")
novo_feriado = datetime.strptime(novo_feriado, date_format).date()
feriados.append((novo_feriado, "Feriado Adicionado"))
print(f"Feriado {novo_feriado} adicionado com sucesso!")


if (diferenca.days > 0):
    print(f"Dias corridos entre as datas é de {diferenca.days} dias.")
else:
    diferenca = -diferenca

for i in range(diferenca.days):
    if (data_um + timedelta(days=i)).weekday() >= 0 and (data_um + timedelta(days=i)).weekday() < 5:
        dia_util = dia_util + 1
    
print(f"Úteis entre as datas: {dia_util} dias")   

dia_util = 0
for i in range(diferenca.days):
    current_date = (data_um + timedelta(days=i)).date()
    if current_date.weekday() >= 0 and current_date.weekday() < 5 and current_date not in [holiday[0] for holiday in feriados]:
        dia_util += 1

print(f"Úteis com feriado!: {dia_util} dias.")

