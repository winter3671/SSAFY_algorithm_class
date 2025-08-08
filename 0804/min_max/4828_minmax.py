import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    min_ai = ai[0]
    for i in range(1, N):
        if min_ai > ai[i]:
            min_ai = ai[i]

    max_ai = ai[0]
    for i in range(1, N):
        if max_ai < ai[i]:
            max_ai = ai[i]

    result = max_ai - min_ai

    print(f'#{tc} {result}')
