count = int(input("Введите количество монет: "))
orel = 0
reshka = 0
for i in range(count):
    side = int(input("Какой стороной лежит монетка {}? 1 - орёл, 0 - решка: ".format(i + 1)))
    if side == 1:
        orel += 1
    else: reshka += 1
if orel <= reshka: 
    count = orel
else: count = reshka
print("Нужно перевернуть {} монет".format(count))