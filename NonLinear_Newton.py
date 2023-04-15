import numpy
cont = 0

def F(x, y):
    # Nesse caso a F(x) é a o vetor gradiente da f(x)
    f1 = 2*x - 2
    f2 = 4 * (y - 2) ** 3

    return [f1, f2]

def J(x,y):
    # Vetor gradiente dos vetores gradiente
    f1_1 = 2
    f1_2 = 0
    f2_1 = 0
    f2_2 = 12 * (y - 2) ** 2

    return [[f1_1, f1_2], [f2_1, f2_2]]


def newton(inicio):
    ''' Implementação do Método de Newton para sistemas não lineares'''
    erro = 10 ** -6
    global cont

    while(cont <= 10 ** 5):
        Fx = F(inicio[0], inicio[1])
        vetor = numpy.asarray(Fx)

        # Verificando se a norma é menor que o erro
        if numpy.linalg.norm(vetor, numpy.inf) < erro:
            return inicio[0], inicio[1]

        # Calculando a Jacobiana e resolvendo o sistema
        # Note que Numpy.solve utiliza a matriz inversa para o cálculo da solução
        Jx = J(inicio[0], inicio[1])
        jacobiana = numpy.asarray(Jx)
        resp = numpy.linalg.solve(jacobiana, numpy.negative(vetor))
        
        # Verificando se a diferença de iterações é menor que o erro
        x0 = numpy.asarray(inicio)
        x1 = numpy.add(x0, resp)
        if numpy.linalg.norm(numpy.subtract(x1, x0)) < erro:
            return inicio[0] + resp[0], inicio[1] + resp[1]

        # Atualizando os valores
        inicio[0] += resp[0]
        inicio[1] += resp[1]

        cont += 1

    return inicio[0], inicio[1]

inicio = [0.5, 2.5]

print("Resultado da implementação por cálculo da matriz inversa")
print(newton(inicio))