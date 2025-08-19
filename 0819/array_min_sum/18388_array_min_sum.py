import sys
sys.stdin = open('4881_input.txt')

def f(i, s):
    global min_sum
    if i == N:
        if s < min_sum:
            min_sum = s
            return
    if s >= min_sum:
        return
    for j in range(i, N):
        p[i], p[j] = p[j], p[i]
        f(i+1, s + arr[i][p[i]])
        p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    min_sum = float('inf')

    p = [i for i in range(N)]
    f(0, 0)

    print(f'#{tc} {min_sum}')