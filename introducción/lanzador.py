from clases_estructura import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta

# Función catalogar(): reciba lista de vehículos y los recorra mostrando el nombre de su clase y sus traibutos.
print("\nImprimiendo lista_vehiculos: ")

def catalogar(lista_vehiculos):

    for x in lista_vehiculos:
        print(type(x).__name__, x)


def catalogar_nueva_version(lista_vehiculos, ruedas = None):

    contador = 0

    print("\n*******************************\nListado de vehículos de {} ruedas\n".format(ruedas))

    for x in lista_vehiculos:
        # No habría que poner nada? porq no hay vehículos que no tienen ruedas.
        if ruedas == None:
            print(type(x).__name__, x)
        
        else:
            if x.ruedas == ruedas:
                print(type(x).__name__, x)
                contador += 1

    print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))  


def ejecutar():
    coche = Coche("negro", 4, 190, 1150)
    camioneta = Camioneta("azul", 4, 120, 1200, 1300)
    bicicleta = Bicicleta("blanco", 2, "urbana")
    motocicleta = Motocicleta("rojo", 2, "urbana", 120, 1000)

    lista_vehiculos = []

    lista_vehiculos.append(coche)
    lista_vehiculos.append(camioneta)
    lista_vehiculos.append(bicicleta)
    lista_vehiculos.append(motocicleta)

    catalogar(lista_vehiculos)
    catalogar_nueva_version(lista_vehiculos)
    catalogar_nueva_version(lista_vehiculos, 0)
    catalogar_nueva_version(lista_vehiculos, 2)
    catalogar_nueva_version(lista_vehiculos, 4)
