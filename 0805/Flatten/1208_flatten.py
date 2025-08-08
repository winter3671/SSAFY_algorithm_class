import sys

sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    N = int(input())
    box_list = list(map(int, input().split()))

    for i in range(N+1): # N번 덤프, 마지막은 덤프 없이 최댓값과 최솟값만 탐색
        max_box = box_list[0]     # for in 구문 밖에 넣었다가 계속 오답이 나옴
        min_box = box_list[0]
        index_max = 0
        index_min = 0
        for j in range(1, 100):     # 최댓값, 최솟값과 그 인덱스를 탐색
            if max_box < box_list[j]:
                max_box = box_list[j]
                index_max = j
            if min_box > box_list[j]:
                min_box = box_list[j]
                index_min = j

        if i != N:
            box_list[index_max] -= 1    # box_list의 최댓값에 -1 해줌
            box_list[index_min] += 1    # box_list의 최솟값에 +1 해줌


        result = box_list[index_max] - box_list[index_min]
        if result <= 1:     # 최댓값과 최솟값의 차가 1 이하라면 break
            break

    print(f'#{tc} {result}')