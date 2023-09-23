weight = float(input("Hur mycket väger paketet? "))

#variable is used to minimize the number of print()´s needed
if(weight <= 2):
    pricePerKilo = 30
elif(weight <= 6):
    pricePerKilo = 28
elif(weight <= 12):
    pricePerKilo = 25
else:
    pricePerKilo = 23

#calculate the total price
price = weight * pricePerKilo
print("Det kommer att kosta", price , "kr")
