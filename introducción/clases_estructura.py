# Ejercicio ya hecho en otro archivo
# Practicar como distribuir el código.

class Vehiculo:

    # Método constructor.
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        #return "Vehículo: ", type(self).__name__ ,"\n\tColor: {}\n\tRuedas".format(self.color, self.ruedas)
        return "\n\tColor: {} \n\tRuedas: {}".format(self.color, self.ruedas)

class Coche(Vehiculo):

    # Método constructor:
    def __init__(self, color, ruedas, velocidad, cilindrada):
        # super (). nos devuelve uun objeto temporal de la superclase que permite invocar a los atributos y métodos definidos en la misma.
        super().__init__(color, ruedas)
        # Atributos de una instancia sólo para objetos de la clase Coche.
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + "\n\tVelocidad: {} k/m\n\tCilindrada: {} cc".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):

    # Método constructor:
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + "\n\tCarga: {} kg".format(self.carga)

class Bicicleta(Vehiculo):

    # Método contructor:
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + "\n\tTipo {}".format(self.tipo)


class Motocicleta(Bicicleta):

    # Método constructor:
    def __init__(self, color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + "\n\tVelocidad: {} k/m\n\tCilindrada: {} cc".format(self.velocidad, self.cilindrada)



