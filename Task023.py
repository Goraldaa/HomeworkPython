#Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
#элементов массива, больших предыдущего (элемента с предыдущим номером)
#Input: [0, -1, 5, 2, 3]
#Output: 2 (-1 < 5, 2 < 3)

numbers = [int(i) for i in input().split()]
i = 1
count = 0
while i < len(numbers):
    if numbers[i]>numbers[i-1]:
        count+=1
    i += 1
print(count)


data = [int(i) for i in input("Введите числа: ").split()]
count = 0
# range(5) = [0, 1, 2, 3, 4]
# range(5 - 1) = [0, 1, 2, 3]
for i in range(len(data) - 1):
    if data[i + 1] > data[i]:
        count += 1
print(count)