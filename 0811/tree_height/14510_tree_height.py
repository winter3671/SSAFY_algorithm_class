import sys
sys.stdin = open('Sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree_list = list(map(int, input().split()))
    i = 0

    while True:
        if max(tree_list) == min(tree_list):
            break

        if i % 2 == 1:  # i가 홀수일때
            for i in range(N):  # 최솟값의 index인 i에 대해
                if tree_list[i] == min(tree_list):
                    tree_list[i] += 1   # 최솟값 + 1
            i += 1

        elif i % 2 == 0:    # i가 짝수일때
            for i in range(N):
                if tree_list[i] == min(tree_list):  # 최솟값의 index인 i에 대해
                    if max(tree_list) - min(tree_list) >= 2:     # 최댓값과 최솟값의 차가 2 이상이면
                        tree_list[i] += 2   # 최솟값 +2
            i += 1


    print(f'#{tc} {i}')

