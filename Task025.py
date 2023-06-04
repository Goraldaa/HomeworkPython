#Напишите программу, которая принимает на вход строку, и отслеживает, 
#сколько раз каждый символ уже встречался. 
#Количество повторов добавляется к символам с помощью постфикса формата _n.
array = input("Введите массив: ").split()
for i in range(len(array)):
    count = 1
    for j in range(i + 1, len(array)):
        if array[j]==array[i]:
            array[j] += "_"+str(count)
            count+=1
print(array)

word = input("Введите строку: ").split()
result = {}
for i in word:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
        result[i] += 1
    else:
        print(i, end=' ')
        result[i] = 1