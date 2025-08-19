import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    expression = input()

    top = -1
    stack = [0] * (N+1)
    postfix = ''

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    # postfix 구하기
    for i in expression:
        if i not in '(+-*/)':
            postfix += i
        else:
            if top == -1:
                top += 1
                stack[top] = i
            else:
                if i != ')':
                    if isp[stack[top]] < icp[i]:
                        top += 1
                        stack[top] = i
                    else:
                        while top > -1 and isp[stack[top]] >= icp[i]:
                            postfix += stack[top]
                            stack[top] = 0
                            top -= 1
                        top += 1
                        stack[top] = i
                else:
                    while stack[top] != ')':
                        postfix += stack[top]
                        stack[top] = 0
                        top -= 1
                    stack[top] = 0
                    top -= 1

    while top > -1:
        postfix += stack[top]
        stack[top] = 0
        top -= 1

    # postfix 계산하기
    result = 0

    for i in postfix:
        if i not in '+-*/':
            top += 1
            stack[top] = i
        else:
            if i == '+':
                stack[top-1] = int(stack[top-1]) + int(stack[top])
                stack[top] = 0
                top -= 1
            elif i == '-':
                stack[top-1] = int(stack[top-1]) - int(stack[top])
                stack[top] = 0
                top -= 1
            if i == '*':
                stack[top-1] = int(stack[top-1]) * int(stack[top])
                stack[top] = 0
                top -= 1
            if i == '/':
                stack[top-1] = int(stack[top-1]) // int(stack[top])
                stack[top] = 0
                top -= 1

    result = stack[top]
    stack[top] = 0
    top -= 1

    print(f'#{tc} {result}')