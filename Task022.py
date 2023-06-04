#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. 
#n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите число кол-во цифр в первом множестве:'))
numbersN = set([int(input("Введите число:")) for i in range(n)])

m = int(input('Введите число кол-во цифр во втором множестве:'))
numbersM = set([int(input("Введите число:")) for i in range(m)])

result = []
for i in numbersN:
    if i in numbersM:
        result.append(i)

print(result)