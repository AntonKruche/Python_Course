def power(num1, num2):
    if num2 == 0:
        result = 1
        return result
    elif num2 == 1:
        result = num1
        return result
    return power(num1, num2 - 1) * power(num1, 1)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(power(a,b))