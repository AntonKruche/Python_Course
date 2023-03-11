def mergesort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

countArr = [int(input("Введите количество элементов в массиве {}: ".format(i + 1))) for i in range(2)]
arr1 = []
arr2 = []
for i in range(len(countArr)):
    if i == 0:
        arr1 = str(input("Введите {} чисел через пробел: ".format(countArr[i]))).split(" ")
    else:
        arr2 = str(input("Введите {} чисел через пробел: ".format(countArr[i]))).split(" ")
arr1 = set(arr1)
arr2 = set(arr2)
Intersection = list(arr1.intersection(arr2))
resultArr = []
for i in Intersection:
    resultArr.append(int(i))
mergesort(resultArr)
for i in resultArr:
    print(i, end = " ")
