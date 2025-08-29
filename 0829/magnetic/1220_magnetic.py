import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for lst in zip(*arr):
        check = False
        for i in lst:
            if i == 1:
                check = True
            if check is True and i == 2:
                cnt += 1
                check = False

    print(f'#{tc} {cnt}')