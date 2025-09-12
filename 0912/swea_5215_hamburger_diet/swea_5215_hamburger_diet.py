import sys
sys.stdin = open('sample_input.txt')

def search_best(sum_flavor, sum_cal, start):
    global max_flavor
    if sum_cal > L:
        return

    if sum_flavor > max_flavor:
        max_flavor = sum_flavor

    for i in range(start, N):
        search_best(sum_flavor + arr[i][0], sum_cal + arr[i][1], i + 1)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flavor = 0

    search_best(0, 0, 0)

    print(f'#{tc} {max_flavor}')