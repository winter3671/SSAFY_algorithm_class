import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    letters = [0] * 5   # a, b, c, d, e를 리스트로 저장하기 위한 빈 리스트
    num = [2, 3, 5, 7, 11]
    while N > 1:    # N이 1이 되면 while문을 종료
        for i in range(5):
            while True:
                if N % num[i] == 0:     # N이 num[i]으로 나누어 떨어지면
                    N //= num[i]    # N을 num[1]으로 나눈 값을 N에 저장
                    letters[i] += 1     # 승수를 기록
                else:
                    break   # N이 나누어 떨어지지 않을때까지 반복

    str_letters = map(str, letters)

    print(f'# {tc} {" ".join(str_letters)}')

    # print(f'# {tc}', *letters)  언패킹 사용방법