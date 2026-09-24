import math
 
a = 0.0
b = 0.0
c = 0.0
delta = 0.0
x1 = 0.0
x2 = 0.0
tem_raizes = False
 
def entrada():
    global a, b, c
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))
 
def processamento():
    global delta, x1, x2, tem_raizes
    delta = b**2 - 4*a*c
    if delta < 0:
        tem_raizes = False
    else:
        tem_raizes = True
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
 
def saida():
    if tem_raizes:
        print("A equação possui raízes reais.")
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
    else:
         print("A equação não possui raízes reais.")
 
def main():
    entrada()
    processamento()
    saida()
 
main()
