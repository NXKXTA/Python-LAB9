import os


def transpose(mat):
    mat_transposed = [[0 for _ in range(len(mat))] for __ in range(len(mat[0]))]
    for stroka in range(len(mat)):
        for column in range(len(mat[0])):
            mat_transposed[stroka][column] = mat[column][stroka]
    return mat_transposed


matrix_lines = './file_3_input.txt'

if not os.path.isfile(matrix_lines):
    print("Файла нет")
    exit()

with open(matrix_lines, "r") as f:
    s_line = f.readlines()

s_line = [one_line.replace('\n', '', 1) for one_line in s_line]
matrix = [i.split() for i in s_line]
transposed_matrix = transpose(matrix)

with open("./file_3_output.txt", "w") as f:
    for i in transposed_matrix:
        for j in i:
            f.write(j + " ")
        f.write("\n")

print(f"Транспонированная матрица: \n{transposed_matrix}")
