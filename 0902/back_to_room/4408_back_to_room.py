import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    corr = [0] * 201

    for lst in arr:
        [a, b] = lst
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1

        if a < b:
            for i in range(a // 2, (b // 2) + 1):
                corr[i] += 1
        else:
            for i in range(b // 2, (a // 2) + 1):
                corr[i] += 1

    print(f'#{tc} {max(corr)}')
