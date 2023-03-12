def getArithmeticProgression(start, count, disp):
    if count == 1:
        return start
    return  (start + (count - 1) * disp)
    
start = int(input("Введите первый элемент последовательности: "))
count = int(input("Введите количество элементов последовательности: "))
disp = int(input("Введите разницу: "))

resultArray = []
for i in range(1, count + 1): 
    resultArray.append(getArithmeticProgression(start, i,disp))
print(resultArray)
