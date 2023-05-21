a = int(input("Введите количесво учеников в первом классе: "))
b = int(input("Введите количесво учеников в первом классе: "))
c = int(input("Введите количесво учеников в первом классе: "))
aa = int(a/2) + a%2 
bb = int(b/2) + b%2
cc = int(c/2) + c%2

print(aa+bb+cc)

countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
part1 = (countStudents1 + 1) // 2
part2 = (countStudents2 + 1) // 2
part3 = (countStudents3 + 1) // 2
print(part1 + part2 + part3)

countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
part = (countStudents1 // 2 + countStudents1 % 2) + (countStudents2 // 2 + countStudents2 % 2) + (countStudents3 // 2 + countStudents3 % 2)
print(part)