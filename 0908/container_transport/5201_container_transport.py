import sys
sys.stdin = open('5201_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)   # 화물 리스트를 내림차순으로 정렬
    ti.sort(reverse=True)   # 트럭 리스트를 내림차순으로 정렬

    sum_weight = 0
    container_idx = 0

    for truck in ti:
        cnt = 1
        for i in range(container_idx, N):
            if truck >= wi[i]:      # 트럭의 적재용량이 화물보다 크다면
                sum_weight += wi[i]     # sum_weight 에 화물의 무게를 더하고,
                container_idx += cnt    # container_idx 에 cnt를 더해 다음 화물부터 탐색
                break
            cnt += 1      # if를 만족하지 않더라도 다음 화물을 탐색

    print(f'#{tc} {sum_weight}')