import sys
sys.stdin = open('sample_input.txt')

def divide_comb(start, cnt, my_list):
    global list_comb
    if cnt == N // 2:
        list_comb.append(my_list)
        return
    for i in range(start, N):
        divide_comb(i + 1, cnt + 1, my_list + [i])

def combination(start, cnt, my_list, lst):
    global subset, subset_cnt
    if subset_cnt >= len(subset):
        return

    if cnt == 2:
        subset[subset_cnt] = my_list
        subset_cnt += 1
        return

    for i in range(start, N // 2):
        combination(i + 1, cnt + 1, my_list + [lst[i]], lst)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    list_comb = []
    divide_comb(0, 0, [])

    list_idx1 = [[] for _ in range(len(list_comb) // 2)]
    list_idx2 = [[] for _ in range(len(list_comb) // 2)]

    for i in range(0, len(list_comb) // 2):
        list_idx1[i] = list_comb[i]
        list_idx2[i] = list_comb[len(list_comb) - 1 - i]

    # N // 2 가 집합의 길이
    # 집합의 길이가 2인 부분집합은 총 (N//2) C 2개
    # 부분집합이 들어갈 리스트에 ((N // 2) * (N // 2 - 1)) // 2개의 빈 공간을 만들어두면 append 를 사용하지 않아도 됨

    min_sum = float('inf')
    for i in range(len(list_comb) // 2):
        sum_synz = 0
        subset_cnt = 0
        subset = [[] for _ in range(((N // 2) * (N // 2 - 1)) // 2)]
        combination(0, 0, [], list_idx1)
        for sets in subset:
            sum_synz += arr[sets[0]][sets[1]]
            sum_synz += arr[sets[1]][sets[0]]
        combination(0, 0, [], list_idx2)
        for sets in subset:
            sum_synz += arr[sets[0]][sets[1]]
            sum_synz += arr[sets[1]][sets[0]]
        min_sum = min(min_sum, sum_synz)

    print(f'#{tc} {min_sum}')