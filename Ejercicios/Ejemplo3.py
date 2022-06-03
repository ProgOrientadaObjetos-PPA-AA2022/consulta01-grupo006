print("**EJEMPLO 3**")
class apellidos:
    def __init__(self, apellido1, apellido2):
        self.apellido1 = apellido1
        self.apellido2 = apellido2


class profesor:
    sueldoTotal = 0
    def __init__(self, nombre, sueldo, horasExtra, apellidos):
        self.nombre = nombre
        self.sueldo = sueldo
        self.horasExtra = horasExtra
        self.apellidos = apellidos

    def calcularSueldoTotal(self):
        self.sueldoTotal = self.sueldo + (self.horasExtra * 11)
    

def main():
    nombre = "Arancha Estrella"
    sueldo = 600
    horasExtra = 10
    apellidosProfesor = apellidos("Rosillo", "Andagua")
    profesor1 = profesor(nombre, sueldo, horasExtra, apellidos)
    profesor1.calcularSueldoTotal()
    print(f"\nEl profesor {nombre} {apellidosProfesor.apellido1} {apellidosProfesor.apellido2} tiene un sueldo de {sueldo} dólares, considerando las horas extras asciende a {profesor1.sueldoTotal} dólares\n")
    
if __name__ == '__main__':
    main()