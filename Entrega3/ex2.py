from xml.etree.ElementTree import tostring


poema = 'Ai que prazer / Nao cumprir um dever, / Ter um livro para ler / E nao fazer! / Ler e macada, / Estudar e nada. / Sol doira / Sem literatura / O rio corre, bem ou mal, / Sem edicao original. / E a brisa, essa, / De tao naturalmente matinal, / Como o tempo nao tem pressa...'
a = [0, "a"]
e = [0, "e"]
i = [0, "i"]
o = [0, "o"]
u = [0, "u"]
aux = [0, ""]
poema = poema.lower()



def counter():
    counter = 0
    global a
    global e
    global i
    global o
    global u
    for alphabet in poema:

            if alphabet == "a":
                counter = counter + 1
                a[0] = a[0] + 1
            if alphabet == "e":
                counter = counter + 1
                e[0] = e[0] + 1
            if alphabet == "i":
                counter = counter + 1
                i[0] = i[0] + 1
            if alphabet == "o":
                counter = counter + 1
                o[0] = o[0] + 1
            if alphabet == "u":
                counter = counter + 1
                u[0] = u[0] + 1
    print("Numero de vogais = "+ str(counter)) 

def prints():
    global aux
    print("Ocorrencia de cada vogal:\n a = " + str(a[0]) + "\n e = " + str(e[0]) + "\n i = " + str(i[0]) + "\n o = " + str(
        o[0]) + "\n u = " + str(u[0]))
    helper = False
    array = [a, e, i, o, u]
    vencedores = []
    for letter in array:
        
        if aux[0] < letter[0]:
            aux = letter
            continue
        if aux[0] == letter[0]:
            helper = True
            if not aux[1] in vencedores:
                vencedores.append(aux[1])
            if not letter[1] in vencedores:
                vencedores.append(letter[1])  
    if(helper):
        print("Há vários vencedores, que são: "+ str(vencedores))
        return
    print("Vencedor : " + aux[1]) 




if __name__ == '__main__':
    counter()
    prints()