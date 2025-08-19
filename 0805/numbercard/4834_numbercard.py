import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().strip()))

    empty_list = [0]*10     # 각 숫자의 개수를 세는 리스트
    for i in ai:
        empty_list[i] += 1

    max_num = empty_list[0]     # 리스트의 최댓값
    max_index = 0   # 리스트의 최댓값의 index
    for i in range(1, 10):
        if max_num <= empty_list[i]:
            max_num = empty_list[i]
            max_index = i

    print(f'#{tc} {max_index} {empty_list[max_index]}')