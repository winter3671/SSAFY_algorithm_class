from collections import deque
import sys
sys.stdin = open('sample_input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def shoot(cnt, remains, now_arr):
    global min_blocks
    # 종료조건: N개의 구슬을 모두 발사 or 남은 벽돌이 0개
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    # 모든 열에 한줄씩 떨어트리기
    for col in range(W):
        # 기존 벽돌들의 상태를 저장
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 떨군다.
        # 3. cnt + 1번 상태로 이동할 때, copy_arr을 함께 전달
        copy_arr = [row[:] for row in now_arr]

        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if copy_arr[r][col]:  # 벽돌이 있으면
                row = r
                break
        if row == -1:
            continue

        # 해당 row, col의 숫자부터 시작해서 BFS
        # 행, 열, 숫자를 모두 담아야 함
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1
        copy_arr[row][col] = 0

        # 주변 벽돌을 순차적으로 파괴
        while q:
            r, c, p = q.popleft()
            # 상하좌우의 p 칸을 모두 제거
            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    # 범위 밖이면 pass
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue
                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))  # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0   # 벽돌 깨짐
                    now_remains -= 1   # 남은벽돌 숫자 감소
        # 빈 칸 메우기
        shoot(cnt + 1, now_remains, copy_arr)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = float('inf')
    blocks = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    shoot()
    print(f'#{tc} {min_blocks}')