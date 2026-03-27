import sys
sys.stdin = open('input.txt')

def subset(sum_num, idx):   # 부분집합의 합을 계산하는 함수
    global min_gap
    if sum_num >= B:    # sum_num이 B 이상일 때,
        if min_gap > sum_num - B:   # 최솟값을 비교
            min_gap = sum_num - B
        return

    for i in range(idx, N):
        sum_num += H_list[i]
        subset(sum_num, i + 1)
        sum_num -= H_list[i]


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H_list = list(map(int, input().split()))

    min_gap = float('inf')
    height_list = []
    # 부분집합을 만들고, 합이 더 큰 부분집합만 return
    subset(0, 0)
    print(f'#{tc} {min_gap}')

