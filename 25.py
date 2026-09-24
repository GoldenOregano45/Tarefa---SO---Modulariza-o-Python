h_ini = 0
m_ini = 0
h_fim = 0
m_fim = 0
horas = 0
minutos = 0
 
def entrada():
    global h_ini, m_ini, h_fim, m_fim
    h_ini = int(input("Digite a hora de início (HH): "))
    m_ini = int(input("Digite o minuto de início (MM): "))
    h_fim = int(input("Digite a hora de término (HH): "))
    m_fim = int(input("Digite o minuto de término (MM): "))
 
def processamento():
    global horas, minutos
    minutos_ini = h_ini * 60 + m_ini
    minutos_fim = h_fim * 60 + m_fim
    if minutos_fim <= minutos_ini:
        minutos_fim += 24 * 60
    duracao = minutos_fim - minutos_ini
    horas = duracao // 60
    minutos = duracao % 60
 
def saida():
    print(f"Duração do jogo: {horas}h{minutos:02d}min")
 
def main():
    entrada()
    processamento()
    saida()
 
main()
