#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.


def Arithmetic_progression(a1, n, d):
    for i in range(n):
        print(a1 + i * d)

a_1 = int(input())
numD = int(input())
numN = int(input())
Arithmetic_progression(a_1, numN, numD)
