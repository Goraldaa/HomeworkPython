#Вводится десятичное число. 
#Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. 
#Нельзя использовать функцию bin()

#*Пример:*
    #10
#*Вывод:*
   #1010

def DecInBin(number):
    if number < 2:
        return str(number)
    return  DecInBin(number//2) + str(number%2)

print(DecInBin(13))