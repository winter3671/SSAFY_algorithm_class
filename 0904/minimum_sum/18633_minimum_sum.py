import sys
sys.stdin = open('5188_input.txt')

def min_sum(x, y, sum_num):
    global minimum_sum

    if x == N-1 and y == N-1:   # 목표 지점에서
        if sum_num < minimum_sum:   # 현재 합이 minimum_sum보다 작으면 갱신
            minimum_sum = sum_num
        return

    if x+1 < N:     # 아래로
        min_sum(x+1, y, sum_num + arr[x+1][y])

    if y+1 < N:     # 오른쪽으로
        min_sum(x, y+1, sum_num + arr[x][y+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minimum_sum = float('inf')

    min_sum(0, 0, arr[0][0])

    print(f'#{tc} {minimum_sum}')