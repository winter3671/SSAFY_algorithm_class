import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    expression = input()

    top = -1
    stack = [0] * (N + 1)
    postfix = ''

    for i in range(N):      # 후위 표기법 변환
        if expression[i] == '+':    # '+'이 오면, top을 1 올리고 stack에 추가
            top += 1
            stack[top] = expression[i]
        else:   # 숫자면 postfix에 추가
            postfix += expression[i]
            if top != -1:  # 만약 top이 올라가있는 상태라면('+'가 stack에 추가되어있다면)
                postfix += stack[top]   # 숫자 추가 이후에 stack에 있는 '+'도 추가하고, top과 stack를 초기화
                stack[top] = 0
                top -= 1

    for i in range(N):      # 후위 표기법 계산
        if postfix[i] != '+':   # postfix[i]가 숫자면
            top += 1
            stack[top] = postfix[i]     # top을 1 올리고 stack에 그 숫자를 추가
        else:   # postfix[i]가 '+'이면
            plus_stack = int(stack[top-1]) + int(stack[top])  # stack의 두 수를 합하고
            stack[top] = 0
            stack[top-1] = 0     # stack의 두 수를 pop하고
            top -= 1    # top보다 1 작은 곳에
            stack[top] = plus_stack     # 두 수의 합을 넣음

    result = stack[top]
    stack[top] = 0
    top -= 1

    print(f'#{tc} {result}')