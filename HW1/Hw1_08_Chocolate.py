a = int(input("Введите первую сторону прямоугольника: "))
b = int(input("Введите вторую сторону прямоугольника: "))
c = int(input("Введите количество долек: "))
if c >= a * b :
    print("no")
elif c % a == 0 or c % b == 0 : print("yes")
else: print("no")