import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('sample_input.txt')

def find_path(cnt):     # 가능한 등산로까지의 거리를 측정하는 함수
    global max_count

    x, y = q.popleft()
    check = False
    for dx, dy in zip(delta_x, delta_y):    # 상하좌우
        nx = dx + x
        ny = dy + y
        if 0 <= nx < N and 0 <= ny < N:
            if arr_copy[nx][ny] < arr_copy[x][y]:   # 상하좌우의 칸 중 더 작은 칸이 있다면,
                q.append([nx, ny])      # q에 추가하고
                find_path(cnt + 1)      # cnt + 1으로 재귀
                check = True
    if check is False:      # 더이상 이동이 불가능하다면
        if max_count < cnt:     # 최대값과 비교하고 return
            max_count = cnt
        return

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_height = 0
    max_height_idx = []

    delta_x = [0, 1, 0, -1]
    delta_y = [1, 0, -1, 0]

    for x in range(N):      # 최댓갑 구하기
        for y in range(N):
            if arr[x][y] >= max_height:
                max_height = arr[x][y]
    for x in range(N):      # 최댓값의 index가 있는 list 만들기
        for y in range(N):
            if arr[x][y] == max_height:
                max_height_idx.append([x, y])

    max_count = 0
    for dig_depth in range(1, K+1):     # 깎는 깊이
        for x in range(N):
            for y in range(N):
                arr_copy = deepcopy(arr)
                if arr_copy[x][y] - dig_depth >= 0:    # 깎은 지형이 음수가 아니고, 최고높이 지형이 아니라면
                    arr_copy[x][y] -= dig_depth
                for idx in max_height_idx:
                    q = deque()
                    q.append(idx)
                    find_path(1)

    print(f'#{tc} {max_count}')
    # print(max_height)
    # print(max_height_idx)