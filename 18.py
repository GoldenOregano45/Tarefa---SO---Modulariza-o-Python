a = 0
b = 0
diferenca = 0
 
def entrada():
    global a, b
    a = int(input("Digite o primeiro valor inteiro: "))
    b = int(input("Digite o segundo valor inteiro: "))
 
def processamento():
    global diferenca
    diferenca = max(a, b) - min(a, b)
 
def saida():
    print(f"A diferença entre o maior e o menor valor é: {diferenca}")
 
def main():
    entrada()
    processamento()
    saida()
 
main()
