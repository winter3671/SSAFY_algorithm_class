import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = N ** (1/3)

    result = -1
    check_X = int(X) + 1
    for i in range(int(X), check_X+1):
        if i**3 == N:
            result = i

    print(f'#{tc} {result}')