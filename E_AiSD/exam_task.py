name_list = ["Иван", "Илья", "Федор", "Александр", "Григорий", "Денис", "Егор", "Алексей", "Антон", "Дмитрий"]


def surname(name):
    surname_list = {"Иван": "Иванов", "Илья": "Ильин", "Федор": "Федоров", "Александр": "Александров", "Григорий": "Григорьев", "Денис": "Денисов", "Егор": "Егоров", "Алексей": "Алексеев", "Антон": "Антонов", "Дмитрий": "Дмитриев"}
    return surname_list.get(name)


def patronymic(name):
    patronymic_list = {"Иван": "Иванович", "Илья": "Ильич", "Федор": "Федорович", "Александр": "Александрович", "Григорий": "Григорьевич", "Денис": "Денисович", "Егор": "Егорович", "Алексей": "Алексеевич", "Антон": "Антонович", "Дмитрий": "Дмитриевич"}
    return patronymic_list.get(name)


for i in range(10):
    for j in range(10):
        for h in range(10):
            print(f"{surname(name_list[j])} {name_list[i]} {patronymic(name_list[h])}")