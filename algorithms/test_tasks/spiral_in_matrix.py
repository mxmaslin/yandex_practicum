def up(ur_start, i, matrix):
    step_range_start, step_range_end = ur_start - i, ur_start + i
    step_range = reversed(range(step_range_start, step_range_end + 1))
    for j in step_range:
        pass
        # print(f'x + {j}')


def right(ur_start, i, matrix):
    step_range_start, step_range_end = ur_start - i, ur_start + i
    step_range = range(step_range_start, step_range_end + 1)
    for _ in step_range:
        pass
        # print(ur_start - i)


def down(d_start_1, d_start_2, i, matrix):
    step_range_start, step_range_end = d_start_1 - i, d_start_2 + i
    step_range = range(step_range_start, step_range_end + 1)
    for j in step_range:
        pass
        # print(f'x + {j}')



def left(x, i, matrix):
    l1, l2 = x, x + 1
    step_range_start, step_range_end = l1 - i, l2 + i
    step_range = range(step_range_start, step_range_end + 1)
    for _ in step_range:
        pass
        # print(f'x + {x + i + 1}')


def spiral(matrix):
    side_length = len(matrix)
    half_side = side_length // 2
    x = y = half_side
    ur_start = x - 1
    d_start_1 = x
    d_start_2 = d_start_1 + 1


    # print(matrix[x][y])
    for i in range(half_side):
        up(ur_start, i, matrix)
        right(ur_start, i, matrix)
        down(d_start_1, d_start_2, i, matrix)
        left(x, i, matrix)
        print()
    # up(up_start, i, matrix)




matrix = [
    [4, 10, 7, 10, 9, 2, 1],
    [5, 9,  0, 9,  8, 3, 3],
    [8, 3,  6, 0,  2, 5, 5],
    [8, 10, 3, 'x + 3',  0, 8, 9],
    [0, 9,  0, 7,  4, 9, 6],
    [0, 9,  0, 7,  4, 9, 6],
    [0, 9,  0, 7,  4, 9, 6],        
]

spiral(matrix)
