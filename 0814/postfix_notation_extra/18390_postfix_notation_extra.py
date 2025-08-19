import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    expression = input()

    top = -1
    stack = [0] * (len(expression)+1)
    postfix = ''

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    for i in expression:
        if i not in '(+-*/)':
            postfix += i
        else:   # i가 기호일 때
            if top == -1:   # 그 기호가 첫번째 기호일 때
                top += 1
                stack[top] = i
            else:
                if i != ')':
                    if isp[stack[top]] < icp[i]:   # i의 우선순위가 stack[top]보다 높으면
                        top += 1
                        stack[top] = i
                    else:
                        while top > -1 and isp[stack[top]] >= icp[i]:
                            postfix += stack[top]
                            stack[top] = 0
                            top -= 1
                        top += 1
                        stack[top] = i
                else:   # i가 ')'이면
                    while stack[top] != '(':
                        postfix += stack[top]
                        stack[top] = 0
                        top -= 1
                    stack[top] = 0
                    top -= 1
    while top > -1:
        postfix += stack[top]
        stack[top] = 0
        top -= 1

    print(f'#{tc} {postfix}')