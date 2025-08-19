import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc_num, N = map(int, input().split())
    nums = list(map(int, input().split()))

    data1 = [0] * 100
    data2 = [0] * 100
    visited_list = [0] * (100 + 1)
    stack = [0]
    result = 0

    for i in range(0, N*2, 2):
        if data1[nums[i]] == 0:
            data1[nums[i]] = nums[i+1]
        else:
            data2[nums[i]] = nums[i+1]

    now = 0
    while True:
        if data1[now] == 99 or data2[now] == 99:
            result = 1
            break

        if visited_list[now] == 0:
            visited_list[now] = 1
            if data1[now] != 0:
                stack.append(data1[now])
            if data2[now] != 0:
                stack.append(data2[now])
                now = data2[now]

    print(f'#{tc} {result}')