n = int(input())
l = list(map(int, input().split()))
count = 0

for a in l:
    if a < 2:
        continue

    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            break
    else:
        count += 1

print(count)