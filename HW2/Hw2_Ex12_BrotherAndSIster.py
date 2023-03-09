summ = int(input("Введите сумму двух чисел: "))
product = int(input("Введите произведение двух чисел: "))
result1 = 0
result2 = 0
if product == 0:
    result1 = 0
    result2 = summ
else: 
    for i in range(1, summ):
        result1 = i
        result2 = summ - result1 
        if product == result1 * result2:
            print("Певрое число = {}, а второе = {}".format(result1, result2))
            break