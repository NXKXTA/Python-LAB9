import os
import re

s_path = './file_2_input.txt'

if not os.path.isfile(s_path):
    print("Файла нет")
    exit()

with open(s_path, "r") as f:
    s_line = f.readline()

predlojeniya = re.split(r"[!?.]", s_line)

try:
    mini_words_len = int(input('Введите минимальную длину предложения: '))
except ValueError:
    print('Введено не натуральное число!')
    exit()

s = ''
print('\nПодходящие по длине предложения:\n')
for i in predlojeniya:
    if len(i.split()) > mini_words_len:
        s += f'{i}\n'
        with open("./file_2_output.txt", "w") as f:
            f.write(s)
        print(i)
