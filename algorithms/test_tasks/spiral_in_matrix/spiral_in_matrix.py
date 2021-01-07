def up(x_minus, i, matrix):
    step_range = range(x_minus - i, x_minus + i + 1)
    for j in reversed(step_range):
        print(matrix[j][x_minus + 1 - i])


def right(x_minus, i, matrix):
    step_range = range(x_minus - i, x_minus + i + 1)
    for j in step_range:
        print(matrix[x_minus - i][j + 2])


def down(x, x_plus, i, matrix):
    step_range = range(x - i, x_plus + i + 1)    
    for j in step_range:
        print(matrix[j][x + i + 1])


def left(x, i, matrix):
    step_range = range(x - i, x + i + 2)    
    for j in step_range:
        print(matrix[x + i + 1][x + x - j])


def spiral(matrix):
    side_length = len(matrix)
    half_side = side_length // 2
    x = y = half_side
    x_minus = x - 1
    x_plus = x + 1
    print(matrix[half_side][half_side])
    for i in range(half_side):
        up(x_minus, i, matrix)
        right(x_minus, i, matrix)
        down(x, x_plus, i, matrix)
        left(x, i, matrix)
    for i in reversed(range(side_length - 1)):
        print(matrix[i][0])


n = int(input())
matrix = []
for x in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)


spiral(matrix)
