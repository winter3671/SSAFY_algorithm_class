import sys
sys.stdin = open('sample_input.txt')

def subset_sum(cnt, subset):    # 완전탐색으로 부분집합 구하기
    global sum_cnt
    if cnt == N:
        if sum(subset) == K:    # 부분집합의 합이 K와 일치하면
            sum_cnt += 1    # cnt += 1
        return

    subset_sum(cnt + 1, subset + [A[cnt]])
    subset_sum(cnt + 1, subset)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_cnt = 0

    subset_sum(0, [])

    print(f'#{tc} {sum_cnt}')