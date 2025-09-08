from collections import deque
import sys
sys.stdin = open('sample_input.txt')

def search_pipe(q, time):
    global result
    if time == L:
        result = len(arrived)
        return

    now = q.popleft()
    arrived.append(now)
    x, y = now
    if arr[x][y] == 1:
        delta_idx = [0, 1, 2, 3]
    elif arr[x][y] == 2:
        delta_idx = [1, 3]
    elif arr[x][y] == 3:
        delta_idx = [0, 2]
    elif arr[x][y] == 4:
        delta_idx = [0, 3]
    elif arr[x][y] == 5:
        delta_idx = [0, 1]
    elif arr[x][y] == 6:
        delta_idx = [1, 2]
    elif arr[x][y] == 7:
        delta_idx = [2, 3]

    for i in delta_idx:
        dx = delta_x[i]
        dy = delta_y[i]
        if arr[x + dx][y + dy] != 0 and (x + dx, y + dy) not in arrived:
            q.append([x + dx, y + dy])
    search_pipe(q, time + 1)

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arrived = []
    q_deque = deque([[R, C]])
    arrived.append([R, C])

    delta_x = [0, 1, 0, -1]
    delta_y = [1, 0, -1, 0]

    result = 0
    search_pipe(q_deque, 1)

    print(result)
