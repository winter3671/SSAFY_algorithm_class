import sys
sys.stdin = open('in1.txt')

def fly(N, M, arr, delta1, delta2):
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = 0
            count += arr[i][j]

            for l in range(1, M ):
                for di, dj in zip(delta1, delta2):
                    if 0 <= i + di * l < N and 0 <= j + dj * l < N:
                        count += arr[i + di * l][j + dj * l]

            if max_count < count:
                max_count = count

    return max_count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]


    delta_x = [1, 0, -1, 0]
    delta_y = [0, 1, 0, -1]

    delta_diag_x = [1, 1, -1, -1]
    delta_diag_y = [1, -1, 1, -1]

    if fly(N, M, arr, delta_x, delta_y) >= fly(N, M, arr, delta_diag_x, delta_diag_y):
        result = fly(N, M, arr, delta_x, delta_y)
    else:
        result = fly(N, M, arr, delta_diag_x, delta_diag_y)

    print(f'#{tc} {result}')