import random
def InitArray():
    resultArray = []
    count = int(input("Введите количество элементов массива: "))
    min = int(input("Введите нижнюю границу для генератора случайных чисел: "))
    max = int(input("Введите верхнюю границу для генератора случайных чисел: ")) + 1
    for i in range(count):
        resultArray.append(random.randint(min, max))
    return resultArray
def HowMuchElementsInRange(array, min, max):
    resultArray = []
    for i in range(len(array)):
        if (array[i]) >= (min) and (array[i]) <= (max):
            resultArray.append(i)
    return resultArray
#array = InitArray()
array =  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input("Введите нижнюю границу диапазона: "))
max = int(input("Введите верхнюю границу диапазона: "))

print(HowMuchElementsInRange(array, min, max))
