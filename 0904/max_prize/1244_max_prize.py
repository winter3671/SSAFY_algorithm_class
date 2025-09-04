from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    M = int(M)

    q = deque()
    visited = set()
    q.append((N, 0))
    visited.add((N, 0))

    max_num = 0

    while q:
        num, swap = q.popleft()

        if swap == M:
            max_num = max(max_num, int(num))
            continue


        for i in range(len(num)):
            for j in range(i+1, len(num)):
                num_list = list(num)
                num_list[i], num_list[j] = num_list[j], num_list[i]

                new_num = "".join(num_list)

                if (new_num, swap + 1) not in visited:
                    q.append((new_num, swap + 1))
                    visited.add((new_num, swap + 1))

    print(f'#{tc} {max_num}')









    # idx_N = [0] * 10
    # for i in N:
    #     lst_N.append(int(i))
    #     idx_N[int(i)] += 1
    # idx = 0
    # swap = 0
    #
    # while idx < len(lst_N)-1:
    #     if swap == M:
    #         break
    #     if max(lst_N[idx:]) != lst_N[idx]:
    #         for i in range(len(lst_N)-1, idx, -1):
    #             if lst_N[i] == max(lst_N[idx:]):
    #                 lst_N[idx], lst_N[i] = lst_N[i], lst_N[idx]
    #                 swap += 1
    #                 break
    #     idx += 1
    #
    # check_idx = True
    # for i in idx_N:
    #     if i != 1:
    #         check_idx = False
    #
    # if (M - swap) % 2 == 1 and check_idx is True:
    #     lst_N[-1], lst_N[-2] = lst_N[-2], lst_N[-1]
    # print(lst_N, swap, M)
    # print(f'#{tc} {lst_N}')
