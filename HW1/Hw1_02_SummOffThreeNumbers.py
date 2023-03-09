num = input("Введите трёхзначное число: ")
summ = 0
for i in range(len(num)):
    summ += int(num[i])
print(summ)