from heapq import heappop, heappush
import sys
sys.stdin = open('sample_input.txt')

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * (N + 1)
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        if dist > dists[node]:
            continue

        for dist_i, node_i in graph[node]:
            sum_dist = dist + dist_i

            if sum_dist >= dists[node_i]:
                continue

            dists[node_i] = sum_dist
            heappush(pq, (sum_dist, node_i))

    return dists[-1]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    INF = float('inf')

    result = dijkstra(0)
    print(f'#{tc} {result}')