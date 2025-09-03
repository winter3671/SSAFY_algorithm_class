import sys
sys.stdin = open('5185_input.txt')

def hex_to_binary(n):   # 16진수를 10진수로 변경하고, 2진수로 변경
    hex_list = '0123456789ABCDEF'
    for i in range(16):
        if hex_list[i] == n:
            hex_idx = i
            break

    bin_list = ['0'] * 4
    for i in range(3, -1, -1):
        if hex_idx % 2 == 1:
            bin_list[i] = '1'
        hex_idx //= 2

    return "".join(bin_list)

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)

    bin_num = ''
    for num in hex_num:
        bin_num += hex_to_binary(num)

    print(f'#{tc} {bin_num}')