class Vehiculo:
    
    def Color(self,c):
        return c
    
    def Ruedas(self,r):
        return r
    
    def Puertas(self,p):
        return p
    
class Coche(Vehiculo):
    def Velocidad(self,v):
        return v
    
    def Cilindrica(self, cil):
        return cil

C = Coche()
print("Color:",C.Color("Azul"))
print("Numero de ruedas:",C.Ruedas(4))
print("Numero de puertas:",C.Puertas(4))
print("Velocidad maxima:",C.Velocidad(350),"km/h")
print("Cilindrica:",C.Cilindrica(200))