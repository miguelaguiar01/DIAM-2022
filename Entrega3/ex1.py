poema = 'Ai que prazer / Nao cumprir um dever, / Ter um livro para ler / E nao fazer! / Ler e macada, / Estudar enada. / Sol doira / Sem literatura / O rio corre, bem ou mal, / Sem edicao original. / E a brisa, essa, / De tao naturalmente matinal, / Como o tempo nao tem pressa...'

def ex1():
    aux = poema.split(" / ")
    print(aux[4] + " " + aux[5])

def ex2():
    return poema.replace(" / ", "\n")

def printex2():
    print(ex2())

def ex3():
    estrofe = "\nLivros sao papeis pintados com tinta. \nEstudar e uma coisa em que esta indistinta\nA distincao entre nada e coisa nenhuma."
    return ex2() + estrofe

def printex3():
    print(ex3())

def ex4():
    aux = ex3()
    n = aux.count('\n')
    aux2 = aux.split("\n")
    print(aux2[n-1] + " " +aux2[n])

if __name__ == '__main__':
    #ex1()
    #printex2()
    #printex3()
    ex4()