import UserInterface
import DataOperations

def run():
    op = 0
    while True:
        op = UserInterface.getOp()
        
        if op == 1:
            string = str(input("Введите данные в формате Фамилия Имя Отчество Номер телефона:\n"))
            DataOperations.addInfo(string)
        
        elif op == 2:
            char = UserInterface.getChar()
            if char == 5:
                DataOperations.getInfo(char)
            else:
                id = UserInterface.getId()
                DataOperations.getInfo(char, id)
        
        elif op == 3:
            DataOperations.deleteInfo(UserInterface.getInfoForDelete())

        elif op == 4:
            id = UserInterface.getInfoForUpdate()
            DataOperations.editInfo(id)
        elif op == 5:
            print("Конец работы")
            break
run()
