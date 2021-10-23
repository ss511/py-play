from itertools import combinations

n = int(input())
ch = input().split()
k = int(input())

combs = combinations(''.join(ch), k)
total_comb, total_a = 0, 0

for i in combs:
    print(i)
    total_comb += 1
    if 'a' in i:
        total_a += 1
print(round((total_a/total_comb), 3))

