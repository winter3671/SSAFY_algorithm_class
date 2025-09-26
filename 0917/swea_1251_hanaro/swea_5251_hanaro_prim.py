from heapq import heappop, heappush
import sys
sys.stdin = open('re_sample_input.txt')

def find_min():
    pq = [(0, 0)]
    dists = [INF] * N
    dists[0] = 0
    visited = [False] * N
    min_dist = 0
    while pq:
        dist, node = heappop(pq)
        if visited[node]:
            continue

        visited[node] = True
        min_dist += dist

        for i in range(N):
            if visited[i]:
                continue

            new_dist = E * ((island_x[i] - island_x[node]) ** 2 + (island_y[i] - island_y[node]) ** 2)

            if new_dist >= dists[i]:
                continue

            dists[i] = new_dist
            heappush(pq, (new_dist, i))

    return round(min_dist)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    INF = float('inf')
    result = find_min()

    print(f'#{tc} {result}')