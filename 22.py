a = 0
b = 0
menor = 0
maior = 0
 
def entrada():
    global a, b
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
 
def processamento():
    global menor, maior
    menor = min(a, b)
    maior = max(a, b)
 
def saida():
    print(f"{menor}, {maior}")
 
def main():
    entrada()
    processamento()
    saida()
 
main()
