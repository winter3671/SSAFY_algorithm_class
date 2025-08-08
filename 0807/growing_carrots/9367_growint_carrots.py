import sys
sys.stdin = open('carrot_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C_list = list(map(int, input().split()))

    count = 1
    max_count = 1

    for i in range(1, N):
        check = C_list[i-1]
        if check < C_list[i]:   # 바로 전보다 C_list[i]가 더 크다면,
            count += 1      # count를 1 올린다
            if max_count < count:
                max_count = count
        else:   # 아니라면 count를 1로 초기화한다
            count = 1

    print(f'#{tc} {max_count}')