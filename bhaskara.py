a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))

import math

delta= (b**2) - ( 4*a*c)
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)


print("O valor da PRIMEIRA Raiz é:",round(raiz1,2))
print("O valor da SEGUNDA Raiz:",round(raiz2,2))
