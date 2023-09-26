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
    print("\n", end="")
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

def check_winner(matris):
    return ((len(matris[0]) == 1) and (len(matris[1]) == 0))

def ask_cell_number(matris):
    while(0 != -1):
        num = str(input("vilken ruta?"))
        for i in range(len(matris)):
            rad = matris[i]
            for j in range(len(rad)):
                element = rad[j]
                if(element == num):
                    return (i, j)
        print("uh oh")

def run_game():
    turn_count = 0
    _rader = int(input("hur många rader?"))
    _kolumner = int(input("hur många kolumner?"))

    _matris = create_chocolate_bar(_rader, _kolumner)

    while(check_winner(_matris) == False):
        turn_count += 1
        print_chocolate_bar(_matris)
        _rad, _kolumn = ask_cell_number(_matris)
        _matris = chomp(_matris, _rad, _kolumn)
    print_chocolate_bar(_matris)
    print("\nspelare", ((turn_count % 2 == 0) and "1" or "2"), "vann!")
        
    
run_game()
