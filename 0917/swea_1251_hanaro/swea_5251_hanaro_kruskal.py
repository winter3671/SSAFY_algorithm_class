import sys
sys.stdin = open('re_sample_input.txt')

def make_set(x):
    parents = [i for i in range(x)]
    return parents

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())

    # kruskal
    # 가중치가 가장 낮은 간선부터 투입
    # 사이클이 완성되는 간선은 continue

    costs = []
    for i in range(N):
        for j in range(i+1, N):
            cost = E * ((island_x[i] - island_x[j]) ** 2 + (island_y[i] - island_y[j]) ** 2)
            costs.append((i, j, cost))

    costs.sort(key=lambda x: x[2])      # 가중치가 낮은 순으로 정렬

    parents = make_set(N)
    cnt = 0
    min_cost = 0

    for s, e, w in costs:
        if find_set(s) == find_set(e):      # 사이클이 완성되면 continue
            continue

        union(s, e)

        min_cost += w
        cnt += 1

        if cnt == N - 1:        # N-1개의 간선을 순회하면 종료
            break

    print(f'#{tc} {round(min_cost)}')