import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    area = [[0] * 10 for _ in range(10)]

    count = 0
    for i in range(N):
        cols = arr[i][2] - arr[i][0]        # 색칠하는 가로 범위
        rows = arr[i][3] - arr[i][1]        # 색칠하는 세로 범위

        if arr[i][4] == 1:
            for col in range(cols + 1):
                for low in range(rows + 1):
                    if area[arr[i][0] + col][arr[i][1] + low] != 2:     # 파란색으로 색칠이 되어 있지 않다면
                        area[arr[i][0] + col][arr[i][1] + low] = 1      # 빨간색으로 색칠
                    elif area[arr[i][0] + col][arr[i][1] + low] == 2:   # 파란색이 색칠되어있다면
                        area[arr[i][0] + col][arr[i][1] + low] = 3      # 보라색으로 색칠
                        count += 1

        if arr[i][4] == 2:
            for col in range(cols + 1):
                for low in range(rows + 1):
                    if area[arr[i][0]+col][arr[i][1]+low] != 1:
                        area[arr[i][0]+col][arr[i][1]+low] = 2
                    elif area[arr[i][0]+col][arr[i][1]+low] == 1:
                        area[arr[i][0] + col][arr[i][1] + low] = 3
                        count += 1

    print(f'#{tc} {count}')