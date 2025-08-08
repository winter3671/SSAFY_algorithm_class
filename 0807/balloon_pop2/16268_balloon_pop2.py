import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    max_count = 0
    for i in range(N):
        for j in range(M):
            count = 0
            count += arr[i][j]      # 가운데를 더함

            delta_x = [1, 0, -1, 0]
            delta_y = [0, 1, 0, -1]
            for di, dj in zip(delta_x, delta_y):    # 탐색 위치의 상하좌우를 더함
                if 0 <= i+di < N and 0 <= j+dj < M:     # N과 M의 범위가 다름에 주의할 것
                    count += arr[i+di][j+dj]

            if max_count < count:
                max_count = count

    print(f'#{tc} {max_count}')
