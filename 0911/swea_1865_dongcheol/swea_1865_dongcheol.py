import sys
sys.stdin = open('input.txt')

def set_one(cnt, lst, per):
    global max_clear
    if len(lst) >= 1:
        per *= (arr[cnt-1][lst[cnt-1]] / 100)       # per에 가능한 확률을 곱해주고,
        if per <= max_clear:     # 만약 그 곱한 값이 이미 최댓값보다 작아지면 return
            return

    if cnt == N:        # cnt가 N일 때 최댓값 비교
        if per > max_clear:
            max_clear = per
        return

    for i in range(N):      # 가능한 경우의 수를 탐색
        if visited[i] == 0:
            lst.append(i)
            visited[i] = 1
            set_one(cnt+1, lst, per)
            visited[i] = 0
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    q = []
    max_clear = 0

    set_one(0, q, 1)

    max_clear *= 100

    print(f'#{tc} {max_clear:.6f}')     # 소수점 6자리 고정출력
