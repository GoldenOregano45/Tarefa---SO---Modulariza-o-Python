n = 0
mensagem = ""
 
def entrada():
    global n
    n = int(input("Digite um número inteiro: "))
 
def processamento():
    global mensagem
    if n % 2 == 0 and n % 3 == 0:
        mensagem = "O número é divisível por 2 e por 3."
    elif n % 2 == 0:
        mensagem = "O número é divisível apenas por 2."
    elif n % 3 == 0:
        mensagem = "O número é divisível apenas por 3."
    else:
        mensagem = "O número não é divisível nem por 2 nem por 3."
 
def saida():
    print(mensagem)
 
def main():
    entrada()
    processamento()
    saida()
 
main()
