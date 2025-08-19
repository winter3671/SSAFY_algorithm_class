import sys
sys.stdin = open('4874_input.txt')

T = int(input())
for tc in range(1, T+1):
    expression = input().rstrip('.').split()

    top = -1
    stack = [0] * len(expression)
    stack_cal = None
    result = None

    for i in expression:
        if i not in '+-*/':     # i가 숫자라면
            top += 1
            stack[top] = i
        else:    # i가 연산기호라면
            if top > -1:
                if i == '+':
                    stack_cal = int(stack[top-1]) + int(stack[top])
                elif i == '-':
                    stack_cal = int(stack[top - 1]) - int(stack[top])
                elif i == '*':
                    stack_cal = int(stack[top - 1]) * int(stack[top])
                elif i == '/':
                    stack_cal = int(stack[top - 1]) / int(stack[top])

                stack[top] = 0
                top -= 1
                stack[top] = stack_cal
            else:
                result = 'error'
                break

    while stack[top] != 0:
        stack[top] = 0
        top -= 1

    result = stack_cal

    if top != -1:
        result = 'error'

    if stack_cal is None:
        result = 'error'

    print(f'#{tc} {result}')