text = []
t = open("Task1.txt", "+w")
while True:
    vvod = input("Введите текст для записи в файл:\n").split()
    if not vvod:
        break
    else:
        text.append(vvod)
for el in text:
        t.writelines(f"{el}\n")
t.close()
