import sys
sys.stdin = open('input.txt')

def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):      # 뒤에서부터 탐색
        if digit == '1':
            decimal_number += 2 ** pow      # 1이 있으면 2의 pow승을 더함
        pow += 1

    return decimal_number

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = ''
    for _ in range(N):
        data += input().strip()

    print(f'#{tc}', end=" ")
    for i in range(0, N*10, 7):     # 숫자를 7개씩 끊음
        nums = data[i:i+7]
        print(binary_to_decimal(nums), end=" ")     # 숫자를 10진법으로 변환, 출력
    print()
