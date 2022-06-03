print("*EJEMPLO 2*")

class dispositivoElectronico:
    costoFinal = 0

    def __init__(self, marca, valor, aniosAntiguedad, tipo):
        self.marca = marca
        self.valor = valor
        self.aniosAntiguedad = aniosAntiguedad
        self.tipo = tipo
        pass

    def establecerMarca(self, n):
        self.nombreEstudiante = n

    def establecerValor(self, a):
        self.valor = a

    def establecerAniosAntiguedad(self, b):
        self.aniosAntiguedad = b

    def establecerTipo(self, c):
        self.tipo = c

    def calcularCostoFinal(self):
        self.costoFinal = float(self.valor) * 1.12
    
    def obtenerMarca (self):
        return self.marca

    def obtenerValor(self):
        return self.valor
    
    def obtenerAniosAntiguedad(self):
        return self.aniosAntiguedad

    def obtenerTipo(self):
        return self.tipo
    
    def obtenerCostoFinal (self):
        return self.costoFinal

   
    def __str__(self):
        cadena = format(f"Marca del dispositivo: {self.obtenerMarca()}\n\
Valor del dispositivo: {self.obtenerValor()}\n\
Anios de antiguedad del dispositivo: {self.obtenerAniosAntiguedad()}\n\
Tipo de dispositivo: {self.obtenerTipo()}\n\
Costo final del dispositivo: {round(self.obtenerCostoFinal(),2)}")
            
             
        return cadena
    
def main():

    dispositivo1 = dispositivoElectronico("Apple", "1100", 10, "Celular")

    dispositivo1.calcularCostoFinal()

    print(dispositivo1.__str__())
    
    pass
if __name__ == "__main__":
    main()
