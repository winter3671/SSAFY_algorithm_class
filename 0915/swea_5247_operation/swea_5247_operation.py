from collections import deque
import sys
sys.stdin = open('sample_input.txt')

def find_answer():
    cnt = 0
    now = 0
    while now != M:
        [now, cnt] = q.popleft()
        for i in range(4):
            if cal[i] == 'plus_1' and now + 1 not in visited:
                visited.add(now + 1)
                q.append([now+1, cnt + 1])
            elif cal[i] == 'minus_1' and now - 1 not in visited:
                visited.add(now - 1)
                q.append([now-1, cnt + 1])
            elif cal[i] == 'times_2' and now * 2 not in visited and now * 2 < 1000000:
                visited.add(now * 2)
                q.append([now*2, cnt + 1])
            elif cal[i] == 'minus_10' and now - 10 not in visited:
                visited.add(now - 10)
                q.append([now-10, cnt + 1])

    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cal = ['plus_1', 'minus_1', 'times_2', 'minus_10']
    q = deque([[N, 0]])
    visited = {N}
    print(f'#{tc} {find_answer()}')