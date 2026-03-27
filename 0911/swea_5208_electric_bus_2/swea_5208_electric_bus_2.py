import sys
sys.stdin = open('5208_input.txt')

def find_min_swap(cnt, idx):
    global min_cnt
    if cnt >= min_cnt:  # cnt가 이미 min_cnt의 값을 초과했으면 return
        return

    if idx == N:        # 버스가 목적지에 도달하면, cnt와 min_cnt를 비교
        if min_cnt > cnt:
            min_cnt = cnt
        return

    for j in range(nums[idx-1], 0, -1):     # j는 idx번 정류장에서 충전해서 이동할 수 있는 범위(역순으로 탐색)
        if idx + j <= N:
            find_min_swap(cnt+1, idx + j)
        else:
            find_min_swap(cnt+1, N)

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    N = nums.pop(0)

    p = []
    min_cnt = float('inf')

    find_min_swap(0,1)
    print(f'#{tc} {min_cnt - 1}')

