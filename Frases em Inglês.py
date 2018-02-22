'''criar um programa que registre quais as frases que eu estou acertando'''

print("Acerte o Maximo de Frases em Inglês!")

phase1 = input ("are you awake?: ")
p1 = ("você esta acordado?")

phase2 = input ("not at all: ")
p2 = ("de modo algum")

phase3 = input ("what a nice day: ")
p3 = ("que dia bonito")

phase4 = input ("I'm feeling sick today: ")
p4 = ("eu estou doente hoje")

phase5 = input ("I'm hungry: ")
p5 = ("eu estou com fome")

phase6 = input ("what day is it today?: ")
p6 = ("que dia é hoje?")

total = 0

if (phase1 == p1):
    ponto1 = 1
    total = ponto1 + total
else:
    total = total
    
if (phase2 == p2):
    ponto2 = 1
    total = ponto2 + total
else:
    total = total

if (phase3 == p3):
    ponto3 = 1
    total = ponto3 + total
else:
    total = total

if (phase4 == p4):
    ponto4 = 1
    total = ponto4 + total
else:
    total = total

if (phase5 == p5):
    ponto5 = 1
    total = ponto5 + total
else:
    total = total

if (phase6 == p6):
    ponto6 = 1
    total = ponto6 + total
else:
    total = total


print("Total:", total, "Pontos")
