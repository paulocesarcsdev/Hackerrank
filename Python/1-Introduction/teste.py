
year = int(input('Entre com o ano: '))

if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Ano bixesto')
else:
    print('Não')