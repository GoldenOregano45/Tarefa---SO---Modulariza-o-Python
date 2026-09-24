a = 0
b = 0
eh_multiplo = False
 
def entrada():
    global a, b
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
 
def processamento():
    global eh_multiplo
    maior = max(a, b)
    menor = min(a, b)
    eh_multiplo = (maior % menor == 0)
 
def saida():
    if eh_multiplo:
        print("O maior número é múltiplo do menor.")
    else:
        print("O maior número não é múltiplo do menor.")
 
def main():
    entrada()
    processamento()
    saida()
 
