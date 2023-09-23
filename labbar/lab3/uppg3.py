antalTärningarString = "Hur många tärningar vill du använda? "
print(antalTärningarString)
antalTärningar = int(input(antalTärningarString))

antalKastString = "Hur många kast per spelare? "
print(antalKastString)
antalKast = int(input(antalKastString))

from random import *


def TärningsKast(antal):
    resultLista = []
    for i in range(antal):
        resultLista.append(randint(1,6))
    return resultLista

while (1 < 2):
    avbrytString = "Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A"
    print(avbrytString)
    avbryt = input(avbrytString)

    if(avbryt == "A"):
        print("hejdå")
        break

    resultatLista = []
    for i in range(antalKast):
        #om man får 2+ kast per spelare och det nuvarande kastet inte är det första
        if(i > 0):
            kastaIgenString = "Vill du kasta igen? (j/n)"
            print(kastaIgenString)
            kastaIgen = input(kastaIgenString)
            print("")
            
            if(kastaIgen == "n"):
                break

        resultatLista = TärningsKast(antalTärningar)

        j = 1
        for k in resultatLista:
            print("Tärning", str(j) + ":", k)
            j += 1

    print("Du fick: ", end="")
    for j in range(len(resultatLista)):
        if(j == len(resultatLista) - 1):
            print(str(resultatLista[j]) + ".")
            print("")
        else:
            print(resultatLista[j], end=", ")
