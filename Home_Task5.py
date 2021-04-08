import random

with open("Task5.txt", "+w") as t:
    a = str()
    while len(a) < 50:
        a += str(random.randrange(1, 501, 1)) + " "
    t.write(str(a))
    t.seek(0)
    a = t.readline().split()
    print(a)
    summa = 0
    for el in a:
        summa += int(el)
    print(f"Cумма чисел {summa}")
