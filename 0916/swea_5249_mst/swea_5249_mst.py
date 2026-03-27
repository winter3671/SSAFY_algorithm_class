from heapq import heappop, heappush
import sys
sys.stdin = open('sample_input.txt')

def prim(start_node):
    pq = [(0, start_node)]      # 가중치, 노드
    MST = [0] * (V+1)           # visited
    min_weight = 0

    while pq:       # BFS
        weight, node = heappop(pq)      # heappop: pq에서 가장 작은 값을 pop

        if MST[node]:       # 방문한 노드면 continue
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V+1):
            if graph[node][next_node] == 0:
                continue

            if MST[next_node]:
                continue

            heappush(pq, (graph[node][next_node], next_node))       # pq에 (가중치, 다음 노드)를 append

    return min_weight

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1][n2] = w
        graph[n2][n1] = w

    result = prim(0)
    print(f'#{tc} {result}')