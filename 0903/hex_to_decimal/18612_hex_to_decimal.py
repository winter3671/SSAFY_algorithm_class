import sys
sys.stdin = open('input.txt')

def hex_to_binary(n):       # 16진수를 10진수로 변환
    global hex_list
    set_num = [0, 0, 0, 0]
    n_idx = hex_list.index(str(n))

    for i in range(3, -1, -1):
        remain = n_idx % 2
        set_num[i] = str(remain)
        n_idx //= 2

    return set_num

def binary_to_decimal(binary_str):      # 10진수를 2진수로 변환
    decimal_num = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == "1":
            decimal_num += 2 ** pow
        pow += 1

    return decimal_num

T = int(input())
for tc in range(1, T+1):
    nums = input()

    hex_list = '0123456789ABCDEF'
    binary_num = ''

    for i in nums:
        binary_list = hex_to_binary(i)
        binary_num += "".join(binary_list)      # 결과가 list형태이므로, str로 풀어서 나열

    hex_idx = len(binary_num) // 7
    print(f'#{tc}', end = " ")
    for i in range(hex_idx):
        print(binary_to_decimal(binary_num[i*7:(i+1)*7]), end = " ")

    print(binary_to_decimal(binary_num[hex_idx * 7:]))