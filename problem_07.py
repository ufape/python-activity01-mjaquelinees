# -- coding: utf-8 --

# Maria Jaqueline 
# UAG00098
# Problem Set 1 - Problem 7
# Description:


"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
O arquivo de entrada contém um número inteiro.
Exemplo: 
Digite a distância (em km) desejada: 30

Processes:
Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 km/h e o carro Y sai com velocidade constante de 90 km/h.

Em uma hora (60 min) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 min.

Leia a distância (em km) e calcule quanto tempo leva (em min) para o carro Y tomar essa distância do outro carro.

Output(s):
Imprima o tempo necessário seguido da mensagem "min".
Exemplo:
Levará 60 min.
"""


def main():
    distancia = int(input("Digite a distância (em km) desejada: "))
    X = 60 #km/h
    Y = 90 #km/h
    velocidade = Y - X
    tempo = distancia / velocidade
    tempo_em_min= tempo * 60
    print(f"Levará {int(tempo_em_min)} min.")


if _name_ == '_main_':
    main()