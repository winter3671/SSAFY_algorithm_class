import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    for j in range(100):
        if arr[99][j] == 2:
            now = j      # 2가 적힌 열을 now에 저장

    for i in range(98, -1, -1):     # 아래에서부터 순회하며 양옆을 검증
        if now > 0:     # 맨 왼쪽줄을 이동중이면 왼쪽을 볼 필요 X
            if arr[i][now-1] == 1:      # 이동중에 왼쪽에 1이 있으면,
                while arr[i][now-1] == 1:       # 왼쪽에 1이 없을때까지
                    now -= 1        # now를 1감소시킴(왼쪽으로 이동)
                    if now == 0:        # 맨 왼쪽줄까지 이동했다면 break
                        break
                continue        # 왼쪽으로 이동했으면, 다시 오른쪽으로 이동하지 않기 위해 continue 사용

        if now < 99:
            if arr[i][now+1] == 1:      # 마찬가지로, 오른쪽 검증
                while arr[i][now+1] == 1:
                    now += 1
                    if now == 99:
                        break

    print(f'#{tc_num} {now}')

