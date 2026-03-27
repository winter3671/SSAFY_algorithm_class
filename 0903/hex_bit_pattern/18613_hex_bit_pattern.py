import sys
sys.stdin = open('input.txt')

def hex_to_binary(n):       # 16진법을 10진법으로 바꾸고, 2진법으로 바꿈
    hex_list = '0123456789ABCDEF'
    for i in range(len(hex_list)):      # 16진법을 10진법으로 바꿈
        if n == hex_list[i]:
            hex_idx = i

    zero_list = ['0'] * 4       # 10진법을 2진법으로 바꿈
    for i in range(3, -1, -1):
        if hex_idx % 2 == 1:
            zero_list[i] = '1'
        hex_idx //= 2
        if hex_idx == 0:
            break

    return "".join(zero_list)

def password(num_str):
    if num_str == '001101':
        return 0
    elif num_str == '010011':
        return 1
    elif num_str == '111011':
        return 2
    elif num_str == '110001':
        return 3
    elif num_str == '100011':
        return 4
    elif num_str == '110111':
        return 5
    elif num_str == '001011':
        return 6
    elif num_str == '111101':
        return 7
    elif num_str == '011001':
        return 8
    elif num_str == '101111':
        return 9

T = int(input())
for tc in range(1, T+1):
    hex_num = input().strip()

    num_list = ''
    for num in hex_num:       # 16진수 input을 2진법으로 바꿔서 이어붙임
        num_list += hex_to_binary(num)

    pw_list = []
    pass_i = 0
    for i in range(len(num_list)-1, -1, -1):        # 뒤에서부터 탐색
        if pass_i == 0:
            if num_list[i] == '1':      # 1을 발견하면
                pw_list.append(password(num_list[i-5:i+1]))     # 암호비트를 풀어서 pw_list에 저장
                pass_i = 5      # 6번만큼 pass
        else:
            pass_i -= 1

    print(f'#{tc}', end = " ")
    for i in range(len(pw_list)-1, -1, -1):
        print(pw_list[i], end = " ")
    print()