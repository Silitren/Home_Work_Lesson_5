with open("task2.txt", "r", encoding='UTF-8') as t:
    text = t.readlines()
    print(f"Количество строк: {len(text)}")
    for el in text:
        str_text = el.replace("\n", '')
        str_text = str_text.replace(" ", '')
        print(f"Количество символов в {text.index(el) + 1}-й строке: {len(str_text)}")
