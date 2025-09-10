import sys
sys.stdin = open('5207_input.txt')

def binary_search(l, r, target, check):
    m = (l + r) // 2
    if l > r:
        return -1

    if target == A[m]:
        return 1
    elif target < A[m]:
        if check == 0 or check is False:
            return binary_search(l, m - 1, target, True)
        else:
            return -1
    elif target > A[m]:
        if check == 0 or check is True:
            return binary_search(m+1, r, target, False)
        else:
            return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    result_cnt = 0
    for num in B:
        result = binary_search(0, N-1, num, 0)
        if result != -1:
            result_cnt += 1

    print(f'#{tc} {result_cnt}')