t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d2 = (x2-x1)**2 + (y2-y1)**2
    sum_r2 = (r1 + r2)**2
    diff_r2 = (abs(r1 - r2))**2

    if (d2 == 0) and (r1 == r2):
        print(-1)
    elif (diff_r2 < d2) and (d2 < sum_r2):
        print(2)
    elif (d2 == diff_r2) or (d2 == sum_r2):
        print(1)
    else:
        print(0)