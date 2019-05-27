class Perro():
    def __init__(self, nombre , edad, peso):
        self.nombre = nombre
        self.edad  = edad
        self.peso = peso
    def ladrar(self, c):
        if self.peso >8:
            print ('GUAU ' * c)
        else:
            print('guau, guau')
            
    def __str__(self):
        return "Nombre: {}, Edad: {}, Peso: {}".format(self.nombre,self.edad,self.peso)
        
        