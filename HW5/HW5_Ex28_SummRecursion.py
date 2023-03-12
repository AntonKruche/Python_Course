def summ(num1, num2):
    if num2 == 0:
        result = num1
        return result
    return summ(num1, num2 - 1) + 1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(summ(a,b))