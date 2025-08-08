import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    count = 0
    for i in range(N):

        check = True
        for l in range(K):   # 1열의 경우 탐색(1이 K만큼 연속, 그다음은 0)
            if arr[i][l] == 0:
                check = False
        if arr[i][K] == 1:
            check = False
        if check is True:
            count += 1

        for j in range(1, N-K):    # 중심점으로부터 오른쪽 3칸을 탐색하기 위한 공간 설정
            check = True        # 1이 K만큼 연속, 앞뒤로 0이 있어야 함
            for l in range(0, K):
                if arr[i][j+l] == 0:
                    check = False
            if arr[i][j+K] == 1 or arr[i][j-1] == 1:
                check = False
            if check is True:
                count += 1

        check = True    # 마지막 열 탐색(전열이 0, 그다음은 1이 K만큼 연속)
        if arr[i][N-K-1] == 1:
            check = False
        for l in range(0, K):
            if arr[i][N-K+l] == 0:
                check = False
        if check is True:
            count += 1

    for j in range(N):

        check = True
        for l in range(K):
            if arr[l][j] == 0:
                check = False
        if arr[K][j] == 1:
            check = False
        if check is True:
            count += 1

        for i in range(1, N-K):  # 중심점으로부터 오른쪽 3칸을 탐색하기 위한 공간 설정
            check = True
            for l in range(0, K):
                if arr[i+l][j] == 0:
                    check = False
            if arr[i+K][j] == 1 or arr[i-1][j]:
                check = False
            if check is True:
                count += 1

        check = True
        if arr[N-K-1][j] == 1:
            check = False
        for l in range(0, K):
            if arr[N - K + l][j] == 0:
                check = False
        if check is True:
            count += 1

    print(f'#{tc} {count}')
