distance = float(input("Ange körsträcka i km: "))
consumption = float(input("Ange mängden förbrukat bränsle i liter: "))

#converts liters per kilometer to deciliters per metric mile
consumptionRate = 100 * consumption / distance

print("Bilens bränsleförbrukning är ", round(consumptionRate, 3), "deciliter per mil")
