import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    max_ai = ai[0]
    min_ai = ai[0]
    max_index = 0
    min_index = 0

    for i in range(1, N):
        if max_ai <= ai[i]:
            max_ai = ai[i]
            max_index = i
        if min_ai > ai[i]:
            min_ai = ai[i]
            min_index = i

    print(f'#{tc} {abs(max_index - min_index)}')