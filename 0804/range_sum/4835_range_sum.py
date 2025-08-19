import sys

sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    max_count = 0
    for num in range(M):
        max_count += ai[num]    # ai[0]부터 이웃한 M개의 합
    min_count = 0
    for num in range(M):
        min_count += ai[num]    # ai[0]부터 이웃한 M개의 합

    for i in range(N-M+1):      # 마지막 이웃한 M개의 합을 위한 범위 조정
        test = 0
        for num in range(i, i+M):
            test += ai[num]
        if max_count < test:
            max_count = test
        if min_count > test:
            min_count = test

    result = max_count - min_count

    print(f'#{tc} {result}')
