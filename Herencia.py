class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad  = None
        self.peso = None
        self.trabajando=False
    def ladrar(self):
        if self.peso == None:
            print ('Soy un fantasma')
        else:
            print('guau, guau')
            
    def __str__(self):
        return "Nombre: {}, Edad: {}, Peso: {}".format(self.nombre,self.edad,self.peso)


class Perro():
    def __init__(self, nombre , edad, peso):
        self.nombre = nombre
        self.edad  = edad
        self.peso = peso
    def ladrar(self,c):
        if self.peso >8:
            print ('GUAU ' * c)
        else:
            print('guau, guau')
            
    def __str__(self):
        return "Nombre: {}, Edad: {}, Peso: {}".format(self.nombre,self.edad,self.peso)

class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo=amo
        self.__trabajando=False
    
    def __str__(self):
        return "Soy {}, Perro de asistencia de {}".format(self.nombre,self.amo)
    
    def pasear(self):
        return "{} ayudo a mi {} a pasear".format(self.nombre,self.amo)
    
    def ladrar(self,c):
        if self.__trabajando:
            print('ahhhh, no puedo ladrar')
        else:
            Perro.ladrar(self,c)
            
    def trabajando(self,valor=None):
        if valor==None:
            return self.__trabajando
        else:
            self.__trabajando=valor
        
         