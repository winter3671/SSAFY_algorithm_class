import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1):
        index_num = i   # 초기 정렬값의 인덱스를 범위의 첫번째로 잡음
        for j in range(1+i, N):
            if numbers[index_num] > numbers[j]:
                index_num = j   # index_num에 범위 내 최솟값의 인덱스를 넣음
        numbers[i], numbers[index_num] = numbers[index_num], numbers[i]     # 범위 내 첫번째 숫자와 최솟값의 위치를 교환

    str_numbers = map(str, numbers)
    print(f'#{tc} {" ".join(str_numbers)}')