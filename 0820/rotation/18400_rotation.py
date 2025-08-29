import sys
from collections import deque

sys.stdin = open('5097_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = deque(map(int, input().split()))

    for i in range(M):
        nums.append(nums.popleft())

    print(f'#{tc} {nums[0]}')