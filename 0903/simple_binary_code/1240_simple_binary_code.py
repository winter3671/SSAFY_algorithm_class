import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    password = ''

    for nums in arr:    # 암호화 된 암호코드의 숫자는 모두 1로 끝남
        for i in range(M-1, -1, -1):     # 뒤에서부터 탐색하다가
            if nums[i] == '1':      # 1을 발견하면
                password = nums[i-55:i+1]    # 1앞의 56개의 숫자를 가져옴
                break
        if password:
            break

    result_bool = True
    pw_lst = []

    for i in range(0, 56, 7):   # 암호 해독
        check = password[i:i+7]
        if check == '0001101':
            pw_lst.append(0)
        elif check == '0011001':
            pw_lst.append(1)
        elif check == '0010011':
            pw_lst.append(2)
        elif check == '0111101':
            pw_lst.append(3)
        elif check == '0100011':
            pw_lst.append(4)
        elif check == '0110001':
            pw_lst.append(5)
        elif check == '0101111':
            pw_lst.append(6)
        elif check == '0111011':
            pw_lst.append(7)
        elif check == '0110111':
            pw_lst.append(8)
        elif check == '0001011':
            pw_lst.append(9)
        else:
            result_bool = False
            break
    # print(pw_lst)
    secret_code_num = 0
    for i in range(0, 8, 2):    # 홀수자리는 3배해서 더함
        secret_code_num += pw_lst[i] * 3
    for i in range(1, 8, 2):    # 짝수자리는 그냥 더해줌
        secret_code_num += pw_lst[i]

    if secret_code_num % 10 == 0:   # 10의 배수이면
        result = 0
        for i in pw_lst:     # 각 자리의 숫자를 더한 값이 결과값
            result += i
    else:
        result_bool = False

    if result_bool is False:    # 암호화 된 것을 풀 수 없거나, 10의 배수가 아니면
        result = 0      # 결과값은 0

    print(f'#{tc} {result}')