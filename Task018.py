#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#5В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input('Введите число кол-во цифр:'))
numbers = [int(input("Введите число:")) for i in range(n)]
print(numbers)
x = int(input("Введите любое число:"))
difference = abs(numbers[0] - x)
result = numbers[0]
for i in numbers:
    if abs(i - x) < difference:
        difference = abs(i - x)
        result = i
print(f"Ближе всего к числу {x} в последовательности находится число {result}")
