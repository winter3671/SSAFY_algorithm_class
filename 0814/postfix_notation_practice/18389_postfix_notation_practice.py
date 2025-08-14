import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    expression = input().strip()

    top = -1
    stack = [0] * (len(expression)+1)
    postfix = ''

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 밖에 있을 때의 우선순위(클수록 높음)
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 안에 있을 때의 우선순위(클수록 높음)

    for i in expression:
        if i not in '(+-*/)':   # i가 숫자라면
            postfix += i     # postfix에 그 숫자를 추가
        else:   # i가 연산기호라면
            if top == -1:   # stack에 아무것도 없으면(맨 처음 만난 기호)
                top += 1
                stack[top] = i      # stack[0]에 그 기호를 넣음
            else:     # stack에 하나 이상의 기호가 있다면
                if i != ')':    # i가 ')'가 아닌 다른 기호일 때,
                    if isp[stack[top]] < icp[i]:    # i의 우선순위가 stack[top]의 우선순위보다 크면
                        top += 1
                        stack[top] = i      # stack의 맨 위에 i를 추가함
                    else:   # i의 우선순위가 stack[top]의 우선순위보다 작거나 같으면
                        while top > -1 and isp[stack[top]] >= icp[i]:    # 우선순위가 커질때 까지
                            postfix += stack[top]    # stack의 맨 위를 postfix에 추가하고 제거
                            stack[top] = 0
                            top -= 1
                        top += 1
                        stack[top] = i
                else:     # i가 ')'이면
                    while stack[top] != '(':    # '('를 만날 때 까지
                        postfix += stack[top]   # stack의 위를 postfix에 추가하고 제거
                        stack[top] = 0
                        top -= 1

    while top != -1:
        postfix += stack[top]
        top -= 1

    print(f'#{tc} {postfix}')

