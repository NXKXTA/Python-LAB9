import os.path


def pop_num(amount: int, vec: list):
    if amount > len(vec):
        print("Удалений больше, чем элементов")
        return
    elif amount < 0:
        print("Укажите натуральное целое число")
        return
    else:
        for i in range(amount):
            vec.pop()
        return vec


s_path = './file_1_input.txt'

if not os.path.isfile(s_path):
    print("Файла нет")
    exit()

with open(s_path, "r") as f:
    vector = [float(digit) for digit in f.readline().split(',')]

try:
    deletes = int(input("Введите количество удалений: "))
except ValueError:
    print("Укажите натуральное целое число")
    exit()

res = pop_num(deletes, vector)

with open("./file_1_output.txt", "w") as f:
    f.writelines(str(res).replace("[", "", 1).replace("]", "", 1))

print(res)
