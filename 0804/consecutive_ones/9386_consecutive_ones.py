import sys

sys.stdin = open("input1.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().strip()))
    count = 0
    max_count = 0
    for i in range(N):
        if ai[i] == 1:     # ai[i]가 1일 때
            count += 1      # count에 1을 추가
            if i == N-1 and max_count < count:
                max_count = count
        elif ai[i] == 0:   # ai[i]가 0일 때
            if count != 0 and max_count < count:     # count가 0이 아니고(바로 앞이 1로 끝남) max_count가 count보다 작을 때
                max_count = count    # max_count를 count값으로 바꾼다
            count = 0       # count를 0으로 초기화

    print(f'#{tc} {max_count}')
