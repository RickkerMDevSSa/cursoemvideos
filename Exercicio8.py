#Exercicio Calcular Catetos / Hipotenusa

import math 
#from math import hypot

co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2) - Calculo sem importação
hi = math.hypot(co, ca)
print ('A hipotenusa vai medir {:.2f}' .format(hi))

#by Rickker Marques