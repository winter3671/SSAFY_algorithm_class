from heapq import heappop, heappush
import sys
sys.stdin = open('sample_input.txt')

def dijkstra(start_node):
    pq = [(0, start_node)]  # 누적연료, 노드
    dists = [INF] * (N ** 2)
    dists[start_node] = 0   # 시작노드 값을 0으로 설정

    while pq:
        dist, node = heappop(pq)

        if dists[node] < dist:  # dist의 누적거리가 더 길면 continue
            continue

        for target_dist, target_node in graph[node]:
            sum_dist = dist + target_dist

            if dists[target_node] <= sum_dist:      # dist와 목표 dist의 합보다 이미 더 작은 값이 있다면
                continue

            dists[target_node] = sum_dist
            heappush(pq, (sum_dist, target_node))

    return dists[N ** 2 - 1]

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')

    graph = [[] for _ in range(N ** 2)]

    for x in range(N):
        for y in range(N):
            for dx, dy in zip(delta_x, delta_y):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] > arr[x][y]:
                        graph[x * N + y].append((arr[nx][ny] - arr[x][y] + 1, nx * N + ny))
                    else:
                        graph[x * N + y].append((1, nx * N + ny))

    result = dijkstra(0)
    print(f'#{tc} {result}')
