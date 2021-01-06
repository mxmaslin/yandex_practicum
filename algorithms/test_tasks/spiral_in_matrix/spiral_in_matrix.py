def up(x_minus, i, matrix):
    step_range_start, step_range_end = x_minus - i, x_minus + i
    step_range = reversed(range(step_range_start, step_range_end + 1))
    for j in step_range:
        print(matrix[j][x_minus + 1 - i])


def right(x_minus, i, matrix):
    step_range_start, step_range_end = x_minus - i, x_minus + i
    step_range = range(step_range_start, step_range_end + 1)
    for j in step_range:
        print(matrix[x_minus - i][j + 2])


def down(x, x_plus, i, matrix):
    step_range_start, step_range_end = x - i, x_plus + i
    step_range = range(step_range_start, step_range_end + 1)
    for j in step_range:
        print(matrix[j][x + i + 1])


def left(x, i, matrix):
    l1, l2 = x, x + 1
    step_range_start, step_range_end = l1 - i, l2 + i
    step_range = range(step_range_start, step_range_end + 1)
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
