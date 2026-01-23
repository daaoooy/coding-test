while True:
    n = int(input())
    if n == 0:
        break

    str_list = [input().strip() for _ in range(n)]
    lower_list = []

    for i, word in enumerate(str_list):
        lower_list.append((word.lower(), i))

    lower_list.sort()
    print(str_list[lower_list[0][1]])