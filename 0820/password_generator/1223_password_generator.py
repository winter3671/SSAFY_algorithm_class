import sys
from collections import deque

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    datas = deque(map(int, input().split()))

    while datas[7] > 0:   # 마지막 숫자가 0이 될때까지
        for i in range(1, 6):   # i는 1~5까지
            datas.append(datas.popleft() - i)   # datas의 첫번째 숫자를 i만큼 줄이고 뒤로 보낸다
            if datas[7] <= 0:   # for 반복 중에 마지막숫자가 0보다 작아지면 중지
                datas[7] = 0
                break

    print(f'#{tc_num} {" ".join(map(str, datas))}')