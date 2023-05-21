i = int(input("Номер вагона по счёту: "))
j = int(input("Номер внутри вагона: "))
if j==i:
    print("Не хватает информации")
else:
    print(i+j-1)