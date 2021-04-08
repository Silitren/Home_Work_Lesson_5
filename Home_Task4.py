# Task4
# Частное(топорно, индуский код) решение, пытаюсь проработать решение со словарями из текстовых файлов.

with open("task4.txt", "r", encoding="UTF-8") as t:
    with open("Task4_write.txt", "w", encoding="UTF-8") as t_w:
        text = t.readlines()
        output = []
        # dictonary = dict(One = "Один",Two = "Два", Three = "Три", Four = "четыре" )
        for el in text:
            if "One" in el:
                output.append(el.replace("One", "один"))
            if "Two" in el:
                output.append(el.replace("Two", "два"))
            if "Three" in el:
                output.append(el.replace("Three", "три"))
            if "Four" in el:
                output.append(el.replace("Four", "четыре"))
        t_w.writelines(output)
