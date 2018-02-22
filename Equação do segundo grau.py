import math
# Entrada de dados
print("---EquaÃ§Ã£o do Segundo Grau, formula de baskara---")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

#Valor de /\
print("")
print("Valor de Delta:")
print("/\ = b²-4ac")
print("/\ = " + str(b) + "²" + "-4" + "." + "(" + str(a) + ")" + "." + "(" + str(c) + ")")

vb1 = b * b #calculo do (b²)
vb2 = (-4 * a) * c #calculo do (-4.(a).(c))

if (vb2 > 0): # se os valor vb2 for menos que zero então adciona o sinal positivo
    print("/\ = " + str(vb1) + " + " + str(vb2))
elif(vb2 < 0): # se os valor vb2 for menos que zero então adciona so o valor
    print("/\ = " + str(vb1) + str(vb2))

#regra de sinais para decidir se vai somar ou diminuir vb1 por vb2 = /\
if (a < 0):
    d = vb1 + vb2
    print("/\ = " + str(d))
elif (c < 0):
    d = vb1 + vb2
    print("/\ = " + str(d))
elif (b, a < 0):
    d = vb1 + vb2
    print("/\ = " + str(d))
elif (b, c < 0):
    d = vb1 + vb2
    print("/\ = " + str(d))
#------------------------------------------------------------------------------
#Valor de X
print("")
print("Valor de X:")
print("X = -b +- rq /\ ")
print("   --------------")
print("       2.(a)")

#X'
if (b < 0): #se valor de b for negativo então o b vai ser positivo pela regra
    print("")
    print("X' = -(" + str(b) + ")" + " + rq " + str(d))
    print("     --------------")
    print("       2.(" + str(a) + ")")

    if (d < 0):
        #Calculando a raiz de Delta
        d = d * (-1)        #deixando o numero positvo para pode achar a raiz
        raiz = math.sqrt(d) #calculo da raiz
        raiz = -raiz        #deixando o resultado da raiz negativa

        #
        b = b * (-1)        #deixando o numero positivo para obedecer a regra
        a2 = 2 * a          #calculando o valor de baixo

        print("")
        print("X' = " + str(b) + " " + str(raiz))
        print("     --------------")
        print("          " + str(a2))

        vv1 = b + raiz
        d = d * (-1)
    
        if (raiz < 0):
            resu2 = b - (raiz)
            print("")
            print("X' = " + str(resu2))
        
        elif (raiz > 0):
            resu2 = b + raiz
            print("")
            print("X' = " + str(resu2))
        
    elif (d > 0):
        raiz = math.sqrt(d) #calculo da raiz

        b = b * (-1)        #deixando o numero positivo para obedecer a regra
        a2 = 2 * a          #cauculando o valor debaixo
        vv1 = b + raiz      #soma do resto
    
        print("")
        print("X' = " + str(b) + " " + str(raiz))
        print("     --------------")
        print("          " + str(a2))
    
        if (raiz < 0): #se a raiz for negativa
            resu2 = b - (-raiz) #então repete o sinal do maior numero e diminui

            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))

        elif (raiz > 0):
            resu2 = b + raiz

            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))

elif (b > 0): #se o b for positivo então ele vai ser negativo pela regra
    print("")
    print("X' = -" + str(b) + " + rq " + str(d))
    print("   --------------")
    print("       2.(" + str(a) + ")")

    if (d < 0):
        
        d = d * (-1)
        raiz = math.sqrt(d)
        raiz = -raiz
    
        print("")
        print("X' = " + str(-b) + " + " + str(raiz))
        print("   --------------")

        a2 = 2 * a

        print("")
        print("X' = " + str(b) + " + " + str(raiz))
        print("     --------------")
        print("          " + str(a2))

        vv1 = b - raiz

        if (raiz < 0):
            resu2 = b - (raiz)
            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))
        
        elif (raiz > 0):
            resu2 = b + raiz
            print("")
            print("     --------------")
            print("          " + str(a2))
            
            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))

    elif (d > 0):
        raiz = math.sqrt(d) #calculo da raiz
        a2 = 2 * a
        
        print("")
        print("X' = " + str(b) + " " + str(raiz))
        print("     --------------")
        print("          " + str(a2))

        if (raiz > 0):
            resu2 = b + raiz
            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            print("")
            print("X' = " + str(resu3))
#X"
if (b < 0): #se valor de b for negativo então o b vai ser positivo pela regra
    print("")
    print("X' = -(" + str(b) + ")" + " - rq " + str(d))
    print("     --------------")
    print("       2.(" + str(a) + ")")

    if (d < 0):
        #Calculando a raiz de Delta
        d = d * (-1)        #deixando o numero positvo para pode achar a raiz
        raiz = math.sqrt(d) #calculo da raiz
        raiz = -raiz        #deixando o resultado da raiz negativa

        b = b * (-1)        #deixando o numero positivo para obedecer a regra
        a2 = 2 * a          #calculando o valor de baixo

        print("")
        print("X' = " + str(b) + " " + str(raiz))
        print("     --------------")
        print("          " + str(a2))

        vv1 = b + raiz
        d = d * (-1)
    
        if (raiz < 0):
            resu2 = b - (raiz)
            print("")
            print("X' = " + str(resu2))
        
        elif (raiz > 0):
            resu2 = b + raiz
            print("")
            print("X' = " + str(resu2))
        
    elif (d > 0):
        raiz = math.sqrt(d) #calculo da raiz

        b = b * (-1)        #deixando o numero positivo para obedecer a regra
        a2 = 2 * a          #cauculando o valor debaixo
        vv1 = b + raiz      #soma do resto
    
        print("")
        print("X' = " + str(b) + " " + str(raiz))
        print("     --------------")
        print("          " + str(a2))
    
        if (raiz < 0): #se a raiz for negativa
            resu2 = b - (-raiz) #então repete o sinal do maior numero e diminui

            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))

        elif (raiz > 0):
            resu2 = b + raiz

            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))

elif (b > 0): #se o b for positivo então ele vai ser negativo pela regra
    print("")
    print("X' = -" + str(b) + " + rq " + str(d))
    print("   --------------")
    print("       2.(" + str(a) + ")")

    if (d < 0):
        
        d = d * (-1)
        raiz = math.sqrt(d)
        raiz = -raiz
    
        print("")
        print("X' = " + str(-b) + " + " + str(raiz))
        print("   --------------")

        a2 = 2 * a

        print("")
        print("X' = " + str(b) + " + " + str(raiz))
        print("     --------------")
        print("          " + str(a2))

        vv1 = b - raiz

        if (raiz < 0):
            resu2 = b - (raiz)
            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))
        
        elif (raiz > 0):
            resu2 = b + raiz
            print("")
            print("     --------------")
            print("          " + str(a2))
            
            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu3))

    elif (d > 0):
        raiz = math.sqrt(d) #calculo da raiz
        a2 = 2 * a
        
        print("")
        print("X' = " + str(b) + " " + str(raiz))
        print("     --------------")
        print("          " + str(a2))

        if (raiz > 0):
            resu2 = b + raiz
            resu3 = resu2 / a2

            print("")
            print("X' = " + str(resu2))
            print("     --------------")
            print("          " + str(a2))

            print("")
            print("X' = " + str(resu3))
