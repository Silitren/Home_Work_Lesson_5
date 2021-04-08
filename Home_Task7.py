import json

average_profit = {}
total_profit = {}
total_loss = {}
all_values = []
average = 0

with open("Task7.txt", "r", encoding="UTF-8") as t:
    while True:
        stroka = t.readline()
        i = 1
        if not stroka:
            break
        else:
            index = stroka.split()
            print(index)
            profit = int(index[2]) - int(index[3])
            if profit >= 0:
                total_profit.setdefault(index[0], profit)
            else:
                total_loss.setdefault(index[0], profit)
            average += profit
            i += 1

average = average / i
average_profit.setdefault(f"Middle profit firm", average)
all_values.append(average_profit)
all_values.append(total_profit)
all_values.append(total_loss)
with open("Task7_Json.json", "w") as tj:
    json.dump(all_values, tj)