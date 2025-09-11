import sys
sys.stdin = open('5209_input.txt')

def search_min(cost, cnt, lst):
    global min_cost

    if cost >= min_cost:
        return

    if cnt == N:
        if cost < min_cost:
            min_cost = cost
        return

    for i in range(N):
        if visited[i] == 0:
            lst.append(i)
            visited[i] = 1
            search_min(cost + arr[cnt][i], cnt+1, lst)
            visited[i] = 0
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    q = []
    visited = [0] * N
    min_cost = float('inf')

    search_min(0, 0, q)

    print(f'#{tc} {min_cost}')