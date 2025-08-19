import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    A = []      # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(12):
        A.append(i+1)

    count = 0
    for i in range(1 << 12):    # 2^12
        empty_list = []

        for j in range(len(A)):  # 부분집합의 개수만큼 반복
            if i & (1 << j):  # 2^0, 2^1, 2^2가 i에 있는가?
                empty_list.append(A[j])

        if len(empty_list) == N:
            sum_count = 0
            for i in range(N):
                sum_count += empty_list[i]
            if sum_count == K:
                count += 1

    print(f'#{tc} {count}')
