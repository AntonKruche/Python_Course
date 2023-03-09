ticketNumber = input("Введите номер билета: ")
summ1 = 0
summ2 = 0
for i in range(int(len(ticketNumber))):
    if i < 3:
        summ1 += int(ticketNumber[i])
    else: summ2 += int(ticketNumber[i])
if summ1 == summ2:
    print("yes")
else: print("no")
