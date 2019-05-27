lista=[1,3,-1,15,9]

def esPar(x):
    return x%3==0


listaDobles=map(lambda x:x*2, lista)

listaPares=filter(lambda x:x%2==0, lista)

listaPares1=filter(esPar,lista)

from functools import reduce

sumatorio=reduce(lambda x,y:x+y, lista)

suma100=reduce(lambda x,y:x+y,range(101))

print(list(listaPares))
print(list(listaPares1))


print(sumatorio)
print(suma100)
