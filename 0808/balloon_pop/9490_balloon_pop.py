import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    max_count = 0
    for i in range(N):
        for j in range(M):
            count = arr[i][j]   # 탐색지점 본인을 count에 추가
            for l in range(1, arr[i][j]+1):     # 탐색지점의 숫자만큼 풍선을 더 터트림
                delta_x = [1, 0, -1, 0]
                delta_y = [0, 1, 0, -1]
                for di, dj in zip(delta_x, delta_y):
                    if 0 <= i+di*l < N and 0 <= j+dj*l < M:
                        count += arr[i+di*l][j+dj*l]

                        if max_count < count:
                            max_count = count

    print(f'#{tc} {max_count}')
