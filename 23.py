a = 0.0
b = 0.0
c = 0.0
d = 0.0
resultado = []
 
def entrada():
    global a, b, c, d
    a = float(input("Digite o 1º valor (menor): "))
    b = float(input("Digite o 2º valor: "))
    c = float(input("Digite o 3º valor (maior): "))
    d = float(input("Digite o 4º valor: "))
 
def processamento():
    global resultado
    if d <= a:
        resultado = [d, a, b, c]
    elif d <= b:
        resultado = [a, d, b, c]
    elif d <= c:
        resultado = [a, b, d, c]
    else:
        resultado = [a, b, c, d]
 
def saida():
    print("Ordem crescente:", resultado)
 
def main():
    entrada()
    processamento()
    saida()
 
main()
