import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))

    charge = 0      # 가장 마지막으로 충전을 실행한 정류장 번호
    count = 0       # 충전 횟수
    while charge + K < N:   # 마지막으로 충전했던 정류장 번호 + K가 종점 정류장 번호보다 작을때동안 반복
        check = charge
        for i in range(K, 0, -1):   # K = 3이라면 i = 3, 2, 1 (최대한 멀리 가는 경우부터 생각)
            if (charge + i) in stations:    # charge + i가 stations에 있으면 충전 가능
                charge += i
                count += 1
                break       # 한번 충전하면 나머지 i는 확인할 필요 없음
        if check == charge:     # for in 반복을 했음에도 charge의 변화가 없다면 충전에 실패한 것
            count = 0
            break
        if charge + K >= N:    # charge + K가 종점 정류장 번호보다 커지면 도착
            break

    print(f'#{tc} {count}')
