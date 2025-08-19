import sys
sys.stdin = open('ex1_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    sum = 0
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:       # 방향 설정
                if 0 <= i+di < N and 0 <= j+dj < N:     # i+di와 j+dj가 범위안에 포함되어 있다면
                    sum += abs(arr[i][j] - arr[i+di][j+dj])     # 차의 절대값의 합을 sum에 합함

    print(f'#{tc} {sum}')