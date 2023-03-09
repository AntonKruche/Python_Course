list1 = [int(input("Введите число номер {}: ".format(i + 1))) for i in range(int(input("Введите количество символов в списке: ")))]
num = int(input("Введите искомое число: "))
count = 0
for i in list1:
    if i == num:
        count += 1
print(count)