import sys
sys.stdin = open('sample_input.txt')

# 1. B를 C보다 작게
# 2. A를 B보다 작게
T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    cnt = 0
    if B >= C:
        cnt += B - (C - 1)
        B = C-1

    if A >= B:
        cnt += A - (B - 1)
        A = B-1

    print(f'#{tc} {cnt}')
