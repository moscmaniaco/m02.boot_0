class Termometro():
    def __init__(self):
         self.__unidadM = 'C'
         self.__temperatura = 0
    
    def __conversor(self, temperatura, unidadM):
        if unidadM == 'C':
            return '{} F'.format(temperatura * 9/5 +32)
        elif unidadM == 'F':
            return '{} C'.format((temperatura-32)*5/9)
        else:
            return 'Unidad incorrecta'
            
    def __str__(self):
        return '{} {}'.format(self.__temperatura,self.__unidadM)
    
    def unidadMedida(self,uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == 'C' or uniM == 'F':
                self.__unidadM=uniM
    
    def temp(self,temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura=temperatura
    
    def mide(self,uniM=None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == 'C' or uniM == 'F':
                return  self.__conversor(self.__temperatura,self.__unidadM)
            return self.__str__()
        