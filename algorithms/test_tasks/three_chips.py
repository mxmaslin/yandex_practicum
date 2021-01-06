import math

from itertools import permutations


target = int(input())
chips = [int(x) for x in input().split()]

number_of_chips = 3

perms = permutations(chips, number_of_chips)

fittest_diff = math.inf
fittest_sum_of_perm = None

for perm in perms:
    sum_of_perm = sum(perm)
    diff = abs(sum_of_perm - target)
    if diff < fittest_diff:
        fittest_diff = diff
        fittest_sum_of_perm = sum_of_perm
    if diff == 0:
        break

print(fittest_sum_of_perm)