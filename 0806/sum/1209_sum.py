import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    # print(arr)

    max_arr = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if max_arr < sum:
            max_arr = sum

    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
        if max_arr < sum:
            max_arr = sum

    diag_sum = 0
    for i in range(100):
        diag_sum += arr[i][i]
    if max_arr < diag_sum:
        max_arr = diag_sum

    diag_sum = 0
    for i in range(100):
        diag_sum += arr[i][100-i-1]
    if max_arr < diag_sum:
        max_arr = diag_sum

    print(f'#{tc_num} {max_arr}')