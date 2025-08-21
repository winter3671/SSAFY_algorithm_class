import sys
from collections import deque

sys.stdin = open('5105_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = set()
    q = deque()
    dist = 0

    for i in range(N):      # 3의 좌표를 q에 저장 (i, j)
        for j in range(N):
            if arr[i][j] == 3:
                q.append([(i, j), dist])
                break
        if q != deque():
            break

    delta_x = [0, 1, 0, -1]
    delta_y = [1, 0, -1, 0]

    while q:
        tx, ty = q.popleft()
        visited.add((tx, ty))
        for dx, dy in zip(delta_x, delta_y):
            if 0 <= tx + dx < N and 0 <= ty + dy < N:
                if arr[tx + dx][ty + dy] == 0 and arr[tx + dx][ty + dy] not in visited:
                    q.append([(tx + dx, ty + dy), dist + 1])
                    dist += 1
    print(f'#{tc} {dist}')