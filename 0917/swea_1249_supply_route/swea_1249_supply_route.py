from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt')

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

def find_path(start_node):
    pq = [(0, start_node)]
    dists = [[INF] * N for _ in range(N)]       # 최단거리
    dists[0][0] = 0     # 시작점을 0으로 설정

    while pq:
        dist, (node_x, node_y) = heappop(pq)

        if dist > dists[node_x][node_y]:      # dist가 dists에 저장된 거리보다 더 크면 탐색 x
            continue

        for dx, dy in zip(delta_x, delta_y):
            nx = node_x + dx
            ny = node_y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = dist + arr[nx][ny]
                if new_dist < dists[nx][ny]:    # 새로 찾은 거리가 기존에 저장된 거리보다 작으면 재설정, heappush
                    dists[nx][ny] = new_dist
                    heappush(pq, (new_dist, (nx, ny)))

    return dists[-1][-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    INF = int(21e8)

    result = find_path((0, 0))
    print(f'#{tc} {result}')