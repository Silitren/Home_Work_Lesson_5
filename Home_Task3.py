from functools import reduce
with open("Task3.txt", "r", encoding="UTF-8") as t:
    familia_poor = []
    oklad_sred = []
    c = []
    while True:
        stroka = t.readline().split()
        # print(stroka)
        if not stroka:
            break
        else:
            for el in stroka:
                if el.isdigit():
                    oklad_sred.append(int(el))
                    if int(el) < 20000:
                        familia_poor.append(stroka[0])

    print(f"Фамилии сотрудников с окладом меньше 20000: {familia_poor}")
    print(f"Средний оклад: {reduce(lambda x,y: (x + y) / len(oklad_sred), oklad_sred)}")





                    # familia.append(el)
            # print(familia)
        # if not stroka:
        #     break
        # else:
        #     for el in stroka:
        #         if el.isdigit():
        #             c.append(int(el))
        #     oklad.append("".join(map(str, c)))
        #     c.clear()
        #
        # print(oklad)

