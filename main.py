import math
from info import  *

# Important global variables:
modoDidatico = False

print(
f"""
-- Calculadora de várias formulas --
1 - calculoProbabilidadeBinomial
2 - calculoProbabilidadeBinomialMultiplo
3 - calculoCombinacao
4 - calculoPermutacao (retorna o fatorial)
5 - calculoArranjo
6 - probabilidadeCondicional
d - informaçõesDidaticas (escrever junto da escolha do calculo)
""", end="")

def calculoProbabilidadeBinomial():
    """
    Calcula a probabilidade binomial
    """
    print("\n-- calculoProbabilidadeBinomial --")
    global modoDidatico
    if modoDidatico == True:
        print(informacoesDidaticasCalculoProbabilidadeBinomial)

    n = int(input("Insira n (quantidade de tentativas): "))
    p = float(input("Insira p (probabilidade): "))
    x = int(input("Insira x (eventos desejados): "))

    # Função de suporte:
    def f(number):
        """ Calcula o fatorial do parametro recebido. """
        return math.factorial(number)

    # Condicionais de validação:
    if p > 1:
        return print("      ERRO - P não pode ser maior que 1")
    elif n<x:
        return print("""    ERRO - x não pode ser maior que n, pois seria necessário calcular o fatorial de um número negativo.\n""")
    
    # Calculo:
    calcPt1 = (f(n)/(f(x)*f(n-x))) # n!/x!(n-x)!
    calcPt2 = (p**x) # p^x
    calcPt3 = (1-p)**(n-x) # (1-p)^(n-x)
    resultado = calcPt1 * calcPt2 * calcPt3 # P(x) = n!/x!(n-x)! * p^x * (1-p)^(n-x)

    # print(modoDidatico)
    # Retorno do resultado:
    return print(f"\nResultado:\nP(x = {x}) = {resultado}\nP(x = {x}) = {resultado*100} %")

def calculoProbabilidadeBinomialMultiplo():
    """
    Calcula a probabilidade binomial, levando em conta vários valores para x.
    """
    print("\n-- calculoProbabilidadeBinomialMultiplo --")
    global modoDidatico
    if modoDidatico == True:
        print(informacoesDidaticasCalculoProbabilidadeBinomialMultiplo)

    n = int(input("Insira n (quantidade de tentativas): "))
    p = float(input("Insira p (probabilidade): "))

    xStart = int(input("Insira onde o valor de x inicia: "))
    xEnd = int(input("Insira onde o valor de x termina: "))

    # Função de suporte:
    def f(number):
        """ Calcula o fatorial do parametro recebido. """
        return math.factorial(number)

    # Condicionais de validação:
    if p > 1:
        return print("      ERRO - P não pode ser maior que 1")
    elif n<xStart or n<xEnd:
        return print("""    ERRO - x não pode ser maior que n, pois seria necessário calcular o fatorial de um número negativo.\n""")
    elif xStart > xEnd:
        return print("""    ERRO - xStart > xEnd.""")
    
    # Calculo:
    vetorComResultados = []
    
    xValue = xStart
    while xValue != xEnd+1:
        calcPt1 = (f(n)/(f(xValue)*f(n-xValue)))
        calcPt2 = (p**xValue)
        calcPt3 = (1-p)**(n-xValue)
        resultado = calcPt1 * calcPt2 * calcPt3
        vetorComResultados.append(resultado)
        xValue += 1

    print("\nResultado:")
    xValue2 = xStart
    for i in vetorComResultados:
        print(f"P(x={xValue2}) = {i}")
        xValue2 += 1

    soma = sum(vetorComResultados)
    print(f"Soma = {soma}")
    print(f"SomaArredondada = {format(soma, 'f')}")
    return

def calculoCombinacao():
    """
    Calcula combinação simples.
    """
    print("\n-- calculoCombinação --")
    global modoDidatico
    if modoDidatico == True:
        print(informacoesDidaticasCalculoCombinatoriaCombinacao)

    # Função de suporte:
    def f(number):
        """ Calcula o fatorial do parametro recebido. """
        return math.factorial(number)

    n = int(input("Insira n: "))
    r = int(input("Insira r: "))

    resultado = f(n)/(f(r)*f(n-r))
    return print(f"\nResultado:\nC({n},{r}) = {resultado}")

def calculoPermutacao():
    """
    Calcula permutação.
    """
    print("\n-- calculoPermutação --")
    global modoDidatico
    if modoDidatico == True:
        print(informacoesDidaticasCalculoCombinatoriaPermutacao)
    n = int(input("Insira n: "))
    resultado = math.factorial(n)
    return print(f"\nResultado:\nP {n} = {resultado}")

def calculoArranjo():
    """
    Calcula arranjo.
    """
    print("\n-- calculoArranjo --")
    global modoDidatico
    if modoDidatico == True:
        print(informacoesDidaticasCalculoCombinatoriaArranjo)
    
    # Função de suporte:
    def f(number):
        """ Calcula o fatorial do parametro recebido. """
        return math.factorial(number)

    n = int(input("Insira n: "))
    r = int(input("Insira r: "))

    resultado = f(n)/(f(n-r))
    return print(f"\nResultado:\nA({n},{r}) = {resultado}")

def calculoProbabilidadeCondicional():
    """
    Calcula probabilidade condicional.
    """
    print("\n-- calculo --")
    global modoDidatico
    if modoDidatico == True:
        print(informacoesDidaticasCalculoProbabilidadeCondicional)
    return

# calculoProbabilidadeCondicional()

calculoEscolhido = input("Escolha um calculo: ")
if "d" in str(calculoEscolhido):
    modoDidatico = True
    calculoEscolhido = calculoEscolhido.replace("d", "")

# Definindo qual calculo será executado:
if calculoEscolhido == "1":
    calculoProbabilidadeBinomial()
elif calculoEscolhido == "2":
    calculoProbabilidadeBinomialMultiplo()
elif calculoEscolhido == "3":
    calculoCombinacao()
elif calculoEscolhido == "4":
    calculoPermutacao()
elif calculoEscolhido == "5":
    calculoArranjo()
elif calculoEscolhido == "6":
    calculoProbabilidadeCondicional()