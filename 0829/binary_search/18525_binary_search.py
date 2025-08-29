import sys
sys.stdin = open('5176_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    cnt = 1

    def in_order(i):
        global cnt
        if i <= N:
            in_order(2*i)       # 왼쪽 자식
            tree[i] = cnt       # 현재 노드 값 채우기
            cnt += 1
            in_order(2*i+1)     # 오른쪽 자식

    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')