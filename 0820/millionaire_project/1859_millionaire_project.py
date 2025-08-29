import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    q = deque()
    save = 0
    benefit = 0

    for i in range(N-1, -1, -1):    # 뒤에서부터 탐색
        q.append(nums[i])
        if len(q) == 1:     # q에 넣은 수가 유일한 수일 때
            save = nums[i]
        else:
            if nums[i] >= save:
                save = nums[i]
                for _ in range(len(q)-1):
                    q.popleft()
            else:
                benefit += save - nums[i]

    print(f'#{tc} {benefit}')