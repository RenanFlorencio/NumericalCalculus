import math
erro = 10 ** -8

# Caso a função que se procura o zero não cruze o eixo x, é necessário transladá-la para que os métodos funcionem
def funcao(x):

    f1 = (1.9 * math.sin(3.12 * x))  / (3.0 * math.cos(3.12 * x))
    f2 = (2.1 * math.sin(2.35 * x))  / (5.3 * math.cos(2.35 * x))

    return f1 - f2

def derivada(x):

    return 1.976 * (1 / math.cos(3.12 * x) ** 2) - 0.93113 * (1 / math.cos(2.35 * x) ** 2)

def imprimir_tabela(result):
        print("x =", result[0])
        print("f(x) =", funcao(result[0]))
        print("b - a =", abs(result[2]))
        print("iterações =", result[1])


def secante(x0, x1):
    global erro
    cont = 1

    while(cont <= 15):

        f_x0 = funcao(x0)
        f_x1 = funcao(x1)

        # Veridicando se a raiz está nos intervalos
        if abs(funcao(x0)) <= erro:
            return x0, cont
        
        if abs(funcao(x1)) <= erro or abs(x1 - x0) <= erro:
            return x1, cont

        # Atualizando os valores
        x2 = x1 - ((f_x1 / (f_x1 - f_x0)) * (x1 - x0))
        x0 = x1
        x1 = x2

        cont += 1


def newton(inicio):

    cont = 1
    global erro
    x_atual = inicio
    while (abs(funcao(x_atual)) >= erro):

        # Atualizando o valor de x
        x_atual = x_atual - (funcao(x_atual) / derivada(x_atual))
        cont += 1

        if cont > 5:
            return False

    return x_atual, cont


def bisseção(intervalo):

    cont = 0
    esquerda = intervalo[0]
    direita = intervalo[1]
    global erro

    while (esquerda >= direita):

        # Atualizando o valor de x
        x_atual = (esquerda + direita) / 2

        # Verificando as condições e retornando a raiz
        if (abs(funcao(x_atual)) <= erro) and abs(funcao(direita) - funcao(x_atual)) < 10 and direita - esquerda < erro:
            return x_atual, cont, (direita - esquerda)

        # Atualizando os intervalos
        else:
            if funcao(x_atual) * funcao(direita) < 0:
                esquerda = x_atual
            elif funcao(x_atual) * funcao(esquerda) < 0:
                direita = x_atual                
        
        cont += 1
        if cont > 50:
            return False


def posicao_falsa(intervalo):

    cont = 1
    esquerda = intervalo[0]
    direita = intervalo[1]
    global erro

    while (esquerda >= direita):

        # Atualizando o valor de x
        f_esq = funcao(esquerda)
        f_dir = funcao(direita)
        x_atual = (esquerda * f_dir - direita * f_esq) / (f_dir - f_esq)

        # Verificando as condições e retornando a raiz
        if (direita - esquerda) <= erro:
            if abs(funcao(direita)) <= erro:
                return direita, cont, (direita - esquerda)

            elif abs(funcao(esquerda)) <= erro:
                return esquerda, cont, (direita - esquerda)

        if (abs(funcao(x_atual)) <= erro) and abs(funcao(direita) - funcao(x_atual)) < 10:
            return x_atual, cont, (direita - esquerda)

        # Atualizando os intervalos
        else:
            if funcao(x_atual) * funcao(direita) < 0:
                esquerda = x_atual
            elif funcao(x_atual) * funcao(esquerda) < 0:
                direita = x_atual                
        
        cont += 1
        if cont >= 200:
            return False


def verif_intervalos():

    valores = []
    passo = 0.1
    
    # Verifica intervalos de tamanho "passo" e adiciona seu valor e o valor da função no intervalo
    i = 100 * math.pi
    while(i >= 0):
        valores.append([i, funcao(i)])
        i -= passo

    pares = []
    for k in range(len(valores) - 1):

        # Filtrando intervalos com troca de sinal e com pequena variação em Y
        if valores[k][1] * valores[k + 1][1] < 0 and abs(funcao(valores[k][0]) - funcao(valores[k + 1][0])) < passo * 10:
            pares.append([valores[k][0], valores[k + 1][0]])

    return pares

intervalos = verif_intervalos()

for intervalo in intervalos:    
    result = []
    
    result = (bisseção(intervalo))
    if result:
        print("#################")
        print()
        print("BISSEÇÃO:")
        imprimir_tabela(result)
        print()
   
    # O método de newton ainda tá conseguindo correr pra outras raizes em intervalos maiores
    result = newton((intervalo[1] + intervalo[0]) / 2)
    if result:
        print("NEWTON:")
        print("x =", result[0])
        print("f(x) =", funcao(result[0]))
        print("iterações =", result[1])
        print()

    result = secante(intervalo[1], (intervalo[1] + intervalo[0]) / 2)
    if result:
        print("SECANTE:")
        print("x =", result[0])
        print("f(x) =", funcao(result[0]))
        print("iterações =", result[1])
        print()
       
    result = posicao_falsa(intervalo)
    if result:
        print("POSIÇÃO FALSA:")
        imprimir_tabela(result)
        print()
