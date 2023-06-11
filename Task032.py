#Определить индексы элементов массива (списка), 
#значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [int(i) for i in input("Введите числа: ").split()]
min_number = int(input())
max_number = int(input())
result = [] 
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
           result.append(i) 
print(result)