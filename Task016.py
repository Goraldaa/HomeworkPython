#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

a = int(input('Введите число кол-во цифр:'))
numbers = []
for i in range(a):
    numbers.append(int(input("Введите число:")))
print(numbers)
num = int(input("Введите искомое число:"))
count = 0
for i in numbers:
    if i == num:
        count +=1
print(f"число {num} встречается {count} раз")