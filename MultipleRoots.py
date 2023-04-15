import math

"""
Verificando o valor obtido e quantidade de funções avaliadas
"""
erro = 10 ** -6

def funcao(x):

    return (abs(x - 9) ** 4.5) / (1 + math.sin(x) ** 2)

def derivada(x):

    f1 = (4.5 * abs(x - 9) ** 3.5 * ((x - 9) / (abs(x - 9))) * (1 + math.sin(x) ** 2)) - (math.sin(2 * x ) * abs(x - 9) ** 4.5)
    f2 = (1 + math.sin(x) ** 2) ** 2

    return f1 / f2

''' Note que o limite de iterações nos métodos é meramente para que um looping infinito não ocorra'''
def secante(x0, x1):
    global erro
    cont = 1
    f_ev = 0

    while(cont <= 50):

        f_x0 = funcao(x0)
        f_x1 = funcao(x1)
        f_ev += 2

        # Veridicando se a raiz está nos intervalos
        if abs(funcao(x0)) <= erro:
            return x0, cont
        f_ev += 1

        if abs(funcao(x1)) <= erro or abs(x1 - x0) <= erro:
            return x1, cont
        f_ev += 1

        # Atualizando os valores
        x2 = x1 - ((f_x1 / (f_x1 - f_x0)) * (x1 - x0))
        x0 = x1
        x1 = x2

        cont += 1


def secante_mult(x0, x1):
    global erro
    cont = 1
    p = 4.5
    f_ev = 0

    while(cont <= 15):

        f_x0 = funcao(x0)
        f_x1 = funcao(x1)
        f_ev += 2

        # Veridicando se a raiz está nos intervalos
        if abs(funcao(x0)) <= erro:
            return x0, f_ev
        f_ev += 1

        if abs(funcao(x1)) <= erro or abs(x1 - x0) <= erro:
            return x1, f_ev
        f_ev += 1

        # Atualizando os valores
        x2 = (x1 - (p * f_x1 * (x1 - x0))) / (f_x1 - f_x0)
        x0 = x1
        x1 = x2

        cont += 1

def newton(inicio):

    cont = 1
    global erro
    x_atual = inicio
    f_ev = 0
    while (abs(funcao(x_atual)) >= erro):
        f_ev += 1

        # Atualizando o valor de x
        x_atual = x_atual - (funcao(x_atual) / derivada(x_atual))
        cont += 1
        f_ev += 2

        if cont > 500:
            return False

    return x_atual, f_ev

def newton_mult(inicio):

    f_ev = 0
    p = 4.5
    cont = 1
    global erro
    x_atual = inicio
    while (abs(funcao(x_atual)) >= erro):
        f_ev += 1

        # Atualizando o valor de x
        x_atual = x_atual - (p * (funcao(x_atual)) / derivada(x_atual))
        f_ev += 2
        cont += 1

        if cont > 500: 
            print(cont)
            return False

    return x_atual, f_ev

result = []

result = newton(6)
if result:
    print("NEWTON:")
    print("x =", result[0], "\nf(x) =", funcao(result[0]), "\nf avaliadas:", result[1], "\n")

result = newton_mult(6)
if result:
    print("NEWTON MULTIPLO:")
    print("x =", result[0], "\nf(x) =", funcao(result[0]), "\nf avaliadas:", result[1], "\n")

result = secante(6, 6.1)
if result:
    print("SECANTE:")
    print("x =", result[0], "\nf(x) =", funcao(result[0]), "\nf avaliadas:", result[1], "\n")

result = secante_mult(6, 6.1)
if result:
    print("SECANTE MULTIPLO:")
    print("x =", result[0], "\nf(x) =", funcao(result[0]), "\nf avaliadas:", result[1], "\n")
