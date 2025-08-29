import sys
sys.stdin = open('5177_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for i in nums:
        last += 1
        heap[last] = i

        c = last
        p = c // 2      # c의 부모

        while heap[p] and heap[p] >= heap[c]:   # 부모가 존재하고, 부모의 값이 c보다 더 크다면
            heap[c], heap[p] = heap[p], heap[c]     # 교환
            c = p
            p = c // 2

    c = last
    sum_p = 0
    while (c // 2) >= 1:
        c //= 2
        sum_p += heap[c]

    print(f'#{tc} {sum_p}')