def isVowel(a):
    a = a.lower()
    a = ord(a)
    VowelArray = [1072, 1077, 1080, 1081, 1086, 1091, 1099, 1101, 1102, 1103]
    return a in VowelArray
s = " "
print(ord(s))
string = input("Введите стих: ")

def isItTRhythmic(string):
    count = 0
    resultArray = []
    for i in range(len(string)):
        if string[i] == " ":
            resultArray.append(count)
            count = 0
        else:
            if isVowel(string[i]):
                count += 1
    resultArray.append(count)
    resultArray = set(resultArray)
    if len(resultArray) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

#isItTRhythmic(string)