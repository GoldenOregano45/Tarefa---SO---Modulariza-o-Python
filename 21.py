n1 = 0.0
n2 = 0.0
n3 = 0.0
n4 = 0.0
media = 0.0
situacao = ""
 
def entrada():
    global n1, n2, n3, n4
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    n4 = float(input("Digite a 4ª nota: "))
 
def processamento():
    global media, situacao
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 6.0:
        situacao = "APROVADO"
    elif media >= 3.0:
        situacao = "EXAME"
    else:
        situacao = "RETIDO"
 
def saida():
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
 
def main():
    entrada()
    processamento()
    saida()
 
main()
