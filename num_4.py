import os
import re

chapters_path = "./file_4_input.txt"

if not os.path.isfile(chapters_path):
    print("Файла нет")
    exit()

with open(chapters_path, "r") as f:
    arr = f.readlines()

with open("./file_4_output.txt", "w") as f:
    f.write("Chapters:\n")
    for i in range(len(arr)):
        if re.match(r"Chapter*", arr[i]):
            f.write((arr[i] + arr[i + 1]).replace("\n", " ") + "\n")
