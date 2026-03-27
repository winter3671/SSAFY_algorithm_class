import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    K = 1

    while K <= 2*N:
        cost = K ** 2 + (K - 1) ** 2
        for i in range(N):
            for j in range(N):
                center = arr[i][j]  # 중심을 arr 위의 한 점으로 잡고,
                cnt = 0
                for arr_x in range(N):
                    for arr_y in range(N):
                        if abs(arr_x - i) + abs(arr_y - j) < K and arr[arr_x][arr_y] == 1:      # K 이내 범위의 점들 중 1인 점이 있으면
                            cnt += 1    # cnt 를 1 센다.
                if cost <= cnt * M:     # 비용과 cnt * 집 갯수를 비교
                    if max_cnt < cnt:
                        max_cnt = cnt
        K += 1

    print(f'#{tc} {max_cnt}')

