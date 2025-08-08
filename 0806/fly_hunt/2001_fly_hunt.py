import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    max_count = 0
    for i in range(N):
        for j in range(N):
            count = 0
            for k in range(M):
                for l in range(M):
                    if 0 <= i+k < N and 0 <= j+l < N:   # 인덱스 범위 검증
                        count += arr[i+k][j+l]
            if max_count < count:
                max_count = count

    print(f'#{tc} {max_count}')