import datetime
from datetime import date
#hj=date.today()
dia = int(input('Digite o dia da pesquisa '))
mes = int(input('Digite o mes da pesquisa '))
ano = int(input('Digite o ano da pesquisa '))
data1 = datetime.date(day=dia, month=mes, year=ano)
#0 é seg
diasemana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
print(diasemana[data1.weekday()])



hj = date.today()
print('Pesquisa do dia: ',hj.day,hj.month,hj.year)




