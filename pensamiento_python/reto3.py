def enumeracion():
    objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


def busqueda_binaria():
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')


def aproximacion():
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'la raíz cuadrada de {objetivo} es {respuesta}')


def run():
    menu = """
        Bienvenido! A continuación te muestro 3 opcionoes para resolver raíz cuadrada

        1 - Enumeración
        2 - Busqueda binaria
        3 - Aproximación

        Elige una opción: """

    opcion = int(input(menu))

    if opcion == 1:
        enumeracion()

    elif opcion == 2:
        busqueda_binaria()

    elif opcion == 3:
        aproximacion()

    else:
        print('Ingresa una opción correcta por favor')

if __name__ == '__main__':
    run()