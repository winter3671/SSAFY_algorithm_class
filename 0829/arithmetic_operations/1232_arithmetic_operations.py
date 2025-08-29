import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())

    left = [0] * (N + 1)  # 부모 번호를 인덱스로 자식 번호 저장
    right = [0] * (N + 1)
    par = [0] * (N + 1)  # 자식 번호를 인덱스로 부모 번호 저장
    tree = [0] * (N + 1)    # tree 정점의 정보

    for _ in range(N):
        arr = list(input().split())
        if len(arr) == 4:
            par[int(arr[2])], par[int(arr[3])] = arr[0], arr[0]
            left[int(arr[0])] = arr[2]
            right[int(arr[0])] = arr[3]
        tree[int(arr[0])] = arr[1]

    ari_list = []
    cnt = 1
    def post_order(i):      # 후위순회
        global cnt
        if i > 0:
            post_order(int(left[i]))  # 왼쪽 자식
            post_order(int(right[i]))  # 오른쪽 자식
            ari_list.append(tree[i])
            i += 1
    post_order(1)

    top = -1
    stack = [0] * (N+1)

    for i in ari_list:  # 후위순회식 계산
        if i not in '+-*/':
            top += 1
            stack[top] = int(i)
        else:
            if i == '+':
                stack[top-1] += stack[top]
            elif i == '-':
                stack[top-1] -= stack[top]
            elif i == '*':
                stack[top-1] *= stack[top]
            elif i == '/':
                stack[top-1] /= stack[top]
            stack[top] = 0
            top -= 1

    result = int(stack[top])
    top -= 1
    print(f'#{tc} {result}')