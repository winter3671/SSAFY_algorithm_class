import sys
from collections import deque

sys.stdin = open('5102_input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]      # 0번째를 빈 공간으로 두고, 나머지 노드만큼 생성
    for _ in range(E):
        v1, v2 = map(int, input().split())
        arr[v1].append(v2)
        arr[v2].append(v1)
    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    q = deque()
    q.append(S)

    result = 0

    while q:
        t = q.popleft()     # q의 가장 앞의 수를 pop
        for w in arr[t]:        # t와 연결된 수들 중에서
            if not visited[w]:      # 방문한적이 없는 수가 있으면
                q.append(w)     # 그 수를 q에 추가
                visited[w] = visited[t] + 1     # 그 수의 거리는 t까지의 거리보다 1 더 멀음

    if visited[G] != 0:
        result = visited[G]

    print(f'#{tc} {result}')