import math
n = int(input())
dot = []
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    add = r1 + r2
    sub = r1 - r2 if r1 > r2 else r2 - r1
    if (r1 == r2 and d == 0):
        print(-1)
    elif (sub == d or add == d):
        print(1)
    elif (add > d and sub < d):
        print(2)
    else:
        print(0)