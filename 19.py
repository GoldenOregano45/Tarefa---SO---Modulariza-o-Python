a = 0.0
b = 0.0
maior = 0.0
 
def entrada():
    global a, b
    a = float(input("Digite o primeiro valor: "))
    b = float(input("Digite o segundo valor: "))
 
def processamento():
    global maior
    maior = a if a > b else b
 
def saida():
    print(f"O maior valor é: {maior}")
 
def main():
    entrada()
    processamento()
    saida()
 
main()
