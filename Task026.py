#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

#*Пример:*

#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8 

def PowRec(numA, numB):
    if numB == 0:
        return 1
    return PowRec(numA, numB-1) * numA


a = int(input())
b = int(input())
print(PowRec(a, b))