from datetime import datetime, date
def datas_ant(parametro):
    antecedencia_de_dias = 2 
    d = datetime.strptime(parametro, "%Y-%m-%d").date()#converte string em data
    print(d)
    hj = date.today()
    print(hj)
    diferenca = d - hj
    dias = diferenca.days
    print(dias)
    if dias > antecedencia_de_dias - 1:
        print('pode agendar')
    else:
        print('nao pode agendar')

datas_ant("2018-05-21")
