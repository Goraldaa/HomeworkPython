#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#5В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
a = int(input('Введите число кол-во цифр:'))
numbers = []
for i in range(a):
    numbers.append(int(input("Введите число:")))
print(numbers)
num = int(input("Введите любое число:"))
difference = abs(numbers[0] - num)
result = numbers[0]
for i in numbers:
    if abs(i - num) < difference:
        difference = abs(i - num)
        result = i
print(f"ближе всего к числу {num} в последовательности находится число {result}")
