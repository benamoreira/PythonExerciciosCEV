from datetime import date
ano = int(input('Digite um ano? Coloque 0 pra analisar o ano atual! '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É um ano Bissexto!'.format(ano))
else:
    print('{} NÃO é um ano bissexto!'.format(ano))
