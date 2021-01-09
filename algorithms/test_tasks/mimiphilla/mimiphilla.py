from collections import defaultdict


bacterias_amount = int(input())
expected_growth = (2 ** x for x in range(bacterias_amount))
stats = defaultdict(list)
next_generation_skips = 0

for generation, expected_offsprings_amount in enumerate(expected_growth):
    bacterias_in_generation = expected_offsprings_amount - next_generation_skips
    next_generation_skips = 0
    for _ in range(bacterias_in_generation):
        try:
            bacteria_id, lifetime, child1, child2 = [int(x) for x in input().split()]
        except EOFError:
            break
        stats[generation].append(lifetime)
        if child1 == -1:
            next_generation_skips += 1
        if child2 == -1:
            next_generation_skips += 1


for k, v in stats.items():
    print('{:.2f}'.format(round(sum(v)/len(v), 2)), end=' ')
