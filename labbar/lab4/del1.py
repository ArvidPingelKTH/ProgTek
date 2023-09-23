def create_chocolate_bar(rader, kolumner):
    matris = []
    for i in range(rader):

        rad = []
        #rad kan se ut så här:    ["11", "12", "13", "14"]

        for j in range(kolumner):
            element = (i == 0 and j == 0) and "P " or str(i + 1) + str(j + 1)
            rad.append(element)
        matris.append(rad)
    return matris

def print_chocolate_bar(matris):
    for i in range(len(matris)):
        rad = matris[i]
        for j in range(len(rad)):
            element = rad[j]

            if(j == len(rad) - 1):
                print(element)
            else:
                print(element, end=" ")
    return None

def chomp(matris, chompedRad, chompedKolumn):
    for i in range(chompedRad, len(matris)):
        rad = matris[i]
        while len(rad) > chompedKolumn:
            del rad[chompedKolumn]
    return matris
