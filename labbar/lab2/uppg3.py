numPackages = int(input("Hur många paket ska skickas? "))

#price variable is assigned before the while-loop to manage all prices
price = 0

#index is set to 1 to make convertion to swedish easier
index = 1
while index <= numPackages:
    weight = float(input("Hur mycket väger paket " + str(index) + "? "))
    pricePerKilo = 0
    if(weight <= 2):
        pricePerKilo = 30
    elif(weight <= 6):
        pricePerKilo = 28
    elif(weight <= 12):
        pricePerKilo = 25
    else:
        pricePerKilo = 23

    #calculate total price
    price += weight * pricePerKilo
    index += 1
print("Det kommer att kosta", price , "kr")
