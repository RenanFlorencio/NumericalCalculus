import numpy
from matplotlib import pyplot as plt

def PolyCoefficients(x, coeffs):
    # Código obtido da internet em https://stackoverflow.com/questions/37352098/plotting-a-polynomial-using-matplotlib-and-coeffiecients
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {o - 1}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

def g(x, i):
    return x ** i


def produto_interno(function1, a1, function2, a2, x):
    ''' Internal product between two functions '''
    soma = 0
    for i in range(len(x)):
        soma += function1(x[i], a1) * function2(x[i], a2)
    return soma

def produto_f(function, a1, x, f_x):
    ''' Product of f(x) with the given function '''
    soma = 0
    for i in range(len(f_x)):
        soma += function(x[i], a1) * f_x[i]
    return soma

x = [float(i) for i in range(1,101)]

f_x = [5.0, 4.965, 4.496, 4.491, 4.566, 4.585, 4.724, 4.951, 4.917, 4.888, 5.087, 5.082, 5.039, 5.054, 4.94, 4.913, 4.871, 4.901, 4.864, 4.75,
       4.856, 4.959, 5.004, 5.415, 5.55, 5.657, 6.01, 6.109, 6.052, 6.391, 6.798, 6.74, 6.778, 7.005, 7.045, 7.279, 7.367, 6.934, 6.506, 6.374,
       6.066, 6.102, 6.204, 6.138, 5.938, 5.781, 5.813, 5.811, 5.818, 5.982, 6.132, 6.111, 5.948, 6.056, 6.342, 6.626, 6.591, 6.302, 6.132, 5.837,
       5.572, 5.744, 6.005, 6.239, 6.523, 6.652, 6.585, 6.622, 6.754, 6.712, 6.675, 6.882, 7.011, 7.14, 7.197, 7.411, 7.233, 6.958, 6.96, 6.927,
       6.814, 6.757, 6.765, 6.87, 6.954, 6.551, 6.022, 5.974, 6.052, 6.033, 6.03, 5.944, 5.543, 5.416, 5.571, 5.571, 5.627, 5.679, 5.455, 5.443]

def adjust(grau):
    plt.ion()
    plt.clf()
    funcoes = [g for i in range(grau + 1)]

    # Matrix 'a' (Summing internal products <g_i, g_j> for all x)
    a = []
    for i in range(len(funcoes)):
        linha = []
        for j in range(len(funcoes)):
            linha.append(produto_interno(funcoes[i], i, funcoes[j], j, x))
        a.append(linha)
    a = numpy.asarray(a)

    # Matrix 'b' (Summing internal products <g_i, f> for all x)
    b = []
    for i in range(len(funcoes)):
        b.append(produto_f(funcoes[i], i, x, f_x))

    b = numpy.asarray(b)

    # Solving the associate linear system
    sol = numpy.linalg.solve(a, b)
    lista = []
    for i in range(len(sol)):
        lista.append(float(sol[i]))

    print("Coeficients:", sol)
    print("Condition number:", numpy.linalg.cond(a))

    # Plotting the graph
    x_array = numpy.linspace(1, 100, 100)
    plt.plot(x_array, PolyCoefficients(x_array, lista))
    plt.scatter(x_array, f_x, s = 10, color = 'red')
    plt.title(f"Degree: {grau}")
    plt.show()
    plt.pause(1)
    grau += 1

    global grau_final
    if grau_final == grau:
        plt.savefig("Adjust")

grau_final = 17
for i in range(grau_final + 1):
    adjust(i)