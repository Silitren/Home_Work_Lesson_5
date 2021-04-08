with open("Task6.txt", "r", encoding="UTF-8") as t:
    spisok = {}
    zanyt_count = []
    zanyt = str()
    while True:
        stroka = t.readline()
        if not stroka:
            break
        else:
            for el in range(len(stroka) - 1):
                if stroka[el].isdigit():
                    zanyt += stroka[el]
                else:
                    if zanyt.isdigit():
                        zanyt_count.append(int(zanyt))
                    zanyt = ''
            zanyt_count = sum(el for el in zanyt_count)
            a = str(stroka.split(":")[0])
            spisok.setdefault(a, zanyt_count)
            zanyt_count = []
    print(f"Учебный предмет и количество занятий: {spisok}")



