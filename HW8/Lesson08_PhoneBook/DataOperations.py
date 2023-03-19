def addInfo(string):
    data = open('PhoneBook.txt', "a")
    string = string + "\n"
    data.write(string)
    data.close()

def getInfo(character, id = 0):
    data = open("PhoneBook.txt", "r")
    while True:
        string = data.readline()
        array = (string.rstrip()).split(" ")
        if not string:
            break
        elif character == 5:
            print(string, end = "")
        elif array[character] == id:
            print(string, end = "")
    data.close()

def deleteInfo(id):
    linesArray = []
    resultArray = []
    with open("PhoneBook.txt", "r") as file1:
        for line in file1:
            linesArray.append(line)
    file1.close()
    for line in linesArray:
        if id not in line:
            resultArray.append(line)
    if linesArray == resultArray:
        print("Такой записи в книге нет")
    with open("PhoneBook.txt", "w") as file1:
        for line in resultArray:
            file1.write(str(line))
    file1.close()

def editInfo(id):
    deleteInfo(id)
    string = input("Введите данные, которые хотите добавить: \n")
    addInfo(string)