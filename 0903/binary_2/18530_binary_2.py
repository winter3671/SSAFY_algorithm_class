import sys
sys.stdin = open('5186_input.txt')

def float_to_bin(n):        # 소수점 아래부분의 2진수 판별
    cnt = 0
    bin_num = ''
    while cnt < 12:
        if n * 2 < 1:   # n * 2가 1보다 작으면 0을 추가
            bin_num += '0'
            n *= 2
        elif n * 2 > 1:     # n * 2가 1보다 크면 1을 추가
            bin_num += '1'
            n *= 2
            n -= 1
        else:       # n * 2가 1이라면, bin_num을 return
            bin_num += '1'
            return bin_num
        cnt += 1

    return 'overflow'       # 12자리 이내로 표현이 불가능하면 overflow

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    print(f'#{tc} {float_to_bin(N)}')
