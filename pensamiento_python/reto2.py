def run():
    user = input('Cual es tu nombre?: ')
    age = int(input('¿Cual es tu edad?: '))

    MAYORIA_EDAD = 18

    if age >= MAYORIA_EDAD:
        print(f'{user} es mayor de edad')
    else:
        print(f'{user} es menor de edad')
 

if __name__ == '__main__':
    run()