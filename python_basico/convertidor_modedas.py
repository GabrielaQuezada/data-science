def conversor(tipo_pesos, valor_dolar):
    pesos_mxn = float(input('¿Cuantos pesos ' + tipo_pesos + ' tienes?: '))
    dolares = pesos_mxn / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')


menu = """
Bienvenido al conversos de monedas💰

1 - Pesos Mexicanos
2 - Pesos Argentinos
3 - Pesos Colombianos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor('mexicanos', 22.60)
elif opcion == 2:
    conversor('argentinos', 65)
elif opcion == 3:
    conversor('colombianos', 3875)

else:
    print('ingresa una opcion correcta por favor')