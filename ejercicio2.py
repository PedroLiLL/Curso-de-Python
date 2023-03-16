class Alumno:
    #inicializar atributos
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
        
    def resultado(self):
        
        if self.nota >= 11:
            print("Resultado: APROBADO")
        else:
            print("Resultado: REPROBADO")


alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Pedro",10.3)
alumno2.inicializar("Claudia",16)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()