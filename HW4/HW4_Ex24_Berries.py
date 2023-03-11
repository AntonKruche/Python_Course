def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1 : ] if i <= pivot]
    greater = [i for i in array[1 : ] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

arr = [int(input("Введите количество ягод на кусте номер {}: ".format(i + 1))) for i in range(int(input("Введите количество кустов на грядке: ")))]
print(arr)
result = 0
arr = quicksort(arr)
if len(arr) > 3:
    result = (arr[-1] + arr[-2] + arr[-3])
else:
    for i in arr:
        result += i
print(result)
