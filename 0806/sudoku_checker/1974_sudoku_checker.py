import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(9)]

    sample = set()     # 검사용 1~9 set
    for i in range(1, 10):
        sample.add(i)

    result = 1
    for i in range(9):      # 각 가로줄을 빈 세트에 넣고, 검사용 세트와 일치하는지 확인
        count = set()
        for j in range(9):
            count.add(arr[i][j])
        if sample != count:
            result = 0
            break

    for j in range(9):
        count = set()      # 각 세로줄에 대해서도 확인
        for i in range(9):
            count.add(arr[i][j])
        if sample != count:
            result = 0
            break

    for i in range(3):      # 3*3 정사각형 안의 숫자들에 대해서 확인
        for j in range(3):
            count = set()
            for k in range(3):
                for l in range(3):
                    count.add(arr[3*i + k][3*j + l])
            if sample != count:
                result = 0
                break

    print(f'#{tc} {result}')