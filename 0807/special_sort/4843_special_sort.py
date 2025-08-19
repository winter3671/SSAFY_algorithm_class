import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    new_list = [0] * N

    for i in range(N):  # numbers 리스트를 내림차순으로 정렬
        index_num = i
        for j in range(1+i, N):
            if numbers[index_num] < numbers[j]:
                index_num = j
        numbers[i], numbers[index_num] = numbers[index_num], numbers[i]

        if i < N/2:    # N의 절반보다 i가 작으면
            new_list[2*i] = numbers[i]    # new_list의 홀수번째 인덱스에 numbers의 수가 들어감
        elif i >= N/2:
            new_list[2*(N-i)-1] = numbers[i]    # 짝수번째 인덱스에 추가

    print(f'#{tc} {" ".join(map(str, new_list[0:10]))}')    # new_list를 10개까지 슬라이싱해서 출력