student_num = int(input())
student_list = [input().strip() for _ in range(student_num)]

for cnt in range(1, len(student_list[0]) + 1):
    tmp = []
    for i in range (0, student_num):
        tmp.append(student_list[i][-cnt:])

    if len(set(tmp)) == len(tmp):
        print(cnt)
        break