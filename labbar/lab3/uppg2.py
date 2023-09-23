rader = int(input("hur många rader?"))
kolumner = int(input("hur många kolumner?"))

maxMultipel = rader * kolumner #determines the largest number that will occur in the table, to accurately space all numbers.
tecken = len(str(maxMultipel)) + 1

#basically nästade for loops
i = 0
while i <= rader:
    j = 0
    while j <= kolumner:

        produkt = i * j
        #hur många mellanslag som hamnar efter varje tal, så att det är jämnt
        antalMellanslag = " " * (tecken - len(str(produkt)))

        #utnyttja första raden för att visa i- och j-axeln istället för massa 0or
        if(i * j == 0):
            produkt = i + j
        if(produkt == 0):
            produkt = " "

        #checkar om man ska hoppa ner en rad, eller annars vara kvar på samma
        if(j == kolumner):
            print(produkt)
        else:
            print(produkt, end = antalMellanslag)

        j = j + 1
    i = i + 1

