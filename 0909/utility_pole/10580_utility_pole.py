import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key = lambda x:x[0])
    cnt = 0

    for idx in range(N):
        start = arr[idx][1]
        for line_idx in range(idx+1, N):
            if arr[line_idx][1] < start:
                cnt += 1

    print(f'#{tc} {cnt}')
