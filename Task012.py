#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#Помогите Кате отгадать задуманные Петей числа.
import math

s = int(input("Введите сумму чисел:"))
p = int(input("Введите произведение чисел:"))
d = s * s - 4 * p #Дискриминант от квадратного уравнения y^2 - s*y + p = 0
if d == 0:
    y = s // 2
    print(f"{y} и {y}")
elif d > 0:
    y = int((s + math.sqrt(d)) / 2)
    print(f"{s - y} и {y}")
else:
    print("Таких чисел не существует")