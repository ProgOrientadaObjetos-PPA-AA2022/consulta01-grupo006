print("*EJEMPLO 1*")

class PromedioEstudiante:
    prom = 0

    def __init__(self):
        self.nombreEstudiante = "Ana Carolina Churo Briceño"
        self.calificacionMateria1 = 9.8
        self.calificacionMateria2 = 10
        self.calificacionMateria3 = 9.5
        pass

    def establecerNombreEstudiante(self, n):
        self.nombreEstudiante = n

    def establecerCalificacionMateria1(self, a):
        self.calificacionMateria1 = a

    def establecerCalificacionMateria2(self, b):
        self.calificacionMateria1 = b

    def establecerCalificacionMateria2(self, c):
        self.calificacionMateria1 = c

    def establecerPromedioCalificaciones(self):
        self.prom = (self.calificacionMateria1
        + self.calificacionMateria2 
        + self.calificacionMateria3)/3
    
    def obtenerNombreEstudiante (self):
        return self.nombreEstudiante

    def obtenerCalificacionMateria1(self):
        return self.calificacionMateria1
    
    def obtenerCalificacionMateria2(self):
        return self.calificacionMateria2

    def obtenerCalificacionMateria3(self):
        return self.calificacionMateria3
    
    def obtenerPromedioCalificaciones (self):
        return self.prom

   
    def __str__(self):
        cadena = format(f"Nombre del estudiante: {self.obtenerNombreEstudiante()}\n\
Calificación de materia 1: {self.obtenerCalificacionMateria1()}\n\
Calificación de materia 2: {self.obtenerCalificacionMateria2()}\n\
Calificación de materia 2: {self.obtenerCalificacionMateria3()}\n\
Promedio de Calificaciones: {round(self.obtenerPromedioCalificaciones(),2)}")
                  
        return cadena
    
def main():

    promEst = PromedioEstudiante()

    promEst.establecerPromedioCalificaciones()

    print(promEst.__str__())
    
    pass
if __name__ == "__main__":
    main()