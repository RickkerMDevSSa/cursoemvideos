
#Programa para ler Seno, Cosseno e Tangente

import math

an = float (input('Digite o ângulo que voce deseja: '))
seno = math.sin(math.radians(an))
print ('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print ('O angulo de {} tem o Cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print ('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))
