import sys
from collections import deque

sys.stdin = open('input.txt')

V, E = map(int, input().split())
arr = list(map(int, input().split()))
arr_list = [[] for _ in range(V+1)]

for i in range(E):         # 방향 상관없이 arr_list의 index가 연결된 지점 표시
    v1, v2 = arr[i*2], arr[i*2+1]
    arr_list[v1].append(v2)
    arr_list[v2].append(v1)

visited = [0] * (V + 1)     # visited[0]은 사용하지 않는 더미 칸
q = deque([])
q.append(1)
result = []

visited[1] = 1

while q:
    t = q.popleft()
    result.append(t)

    for w in arr_list[t]:
        if not visited[w]:
            q.append(w)
            visited[w] = visited[t] + 1

print(f'#1 {" ".join(map(str, result))}')
