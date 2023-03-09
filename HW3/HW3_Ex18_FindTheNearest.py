list1 = [int(input("Введите число номер {}: ".format(i + 1))) for i in range(int(input("Введите количество элементов списка: ")))]
num = int(input("Введите число для поиска ближайшего значения из списка: "))
difference = abs(num - list1[0])
result = list1[0]
for i in range(1, len(list1)):
    currentDiff = abs(num - list1[i])
    if currentDiff < difference:
        difference = currentDiff
        result = list1[i]
print(result)
