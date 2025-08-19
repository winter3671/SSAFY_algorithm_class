import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    expression = input().strip()

    ip = {'*': 2, '+': 1}

    top = -1
    stack = [0] * (N+1)
    postfix = ''

    for i in expression:    # 후위 표기법 변환
        if i not in '+*':   # i가 숫자일 경우
            postfix += i
        else:   # i가 기호일 경우
            if top == -1:
                top += 1
                stack[top] = i
            else:
                if ip[stack[top]] < ip[i]:
                    top += 1
                    stack[top] = i
                else:
                    while top > -1 and ip[stack[top]] >= ip[i]:
                        postfix += stack[top]
                        stack[top] = 0
                        top -= 1
                    top += 1
                    stack[top] = i

    while top > -1:
        postfix += stack[top]
        stack[top] = 0
        top -= 1

    for i in postfix:   # 후위표기법 계산
        if i not in '+*':   # i가 숫자인 경우
            top += 1
            stack[top] = i
        else:   # i가 기호인 경우
            if i == '+':    # i가 '+'일 때
                stack_cal = int(stack[top-1]) + int(stack[top])
            else:   # i가 '*'일 때
                stack_cal = int(stack[top-1]) * int(stack[top])
            stack[top-1] = 0
            stack[top] = 0
            top -= 1
            stack[top] = stack_cal

    print(f'#{tc} {stack_cal}')