import sys
from collections import deque

sys.stdin = open('5099_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = deque(map(int, input().split()))   # 대기중인 남은 피자
    Ci_index = deque(i for i in range(1, M+1))      # 대기중인 피자의 번호
    q = deque()     # 화덕 안의 피자
    q_index = deque()       # 화덕 안의 피자의 번호

    for _ in range(N):
        q.append(Ci.popleft())
        q_index.append(Ci_index.popleft())

    while len(q) > 1:    # 대기중인 피자가 없을 때 까지
        q[0] //= 2
        if q[0] != 0:       # //2의 결과가 0이 아니면 다음 피자를 탐색
            q.append(q.popleft())
            q_index.append(q_index.popleft())
        else:       # //2의 결과가 0이면 피자를 제거
            q.popleft()
            q_index.popleft()
            if len(Ci) > 0:     # 대기중인 피자가 있다면
                q.append(Ci.popleft())
                q_index.append(Ci_index.popleft())

    print(f'#{tc} {q_index[0]}')