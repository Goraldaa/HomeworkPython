#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
#Если А не является числом Фибоначчи, выведите число -1.

#Input:     5
#Output:  6

number = int(input("Введите число:"))
firstNum = 0
secondNum = 1
result = 0
count = 2
while result < number:
    result = firstNum + secondNum
    count += 1
    temp = firstNum
    firstNum = secondNum
    secondNum += temp 
if result != number:
    print("-1")
else:
    print(count)