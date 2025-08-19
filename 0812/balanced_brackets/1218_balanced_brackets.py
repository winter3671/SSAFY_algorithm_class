import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    brackets = input()
    result = 1
    sample_open = ['{', '[', '(', '<']
    sample_close = ['}', ']', ')', '>']

    empty_list = []
    for i in range(N):
        if brackets[i] in sample_open:  # 괄호열기 기호를 만나면
            empty_list.append(brackets[i])  # 빈 리스트에 추가
        elif brackets[i] in sample_close:   # 괄호닫기 기호를 만나면
            if sample_open.index(empty_list[-1]) == sample_close.index(brackets[i]):
                                                # 그 기호가 빈 리스트의 마지막 기호와 한쌍이라면
                empty_list.pop()    # 빈 리스트의 그 괄호열기 기호를 제거
            else:   # 한쌍이 아니라면 문자열이 유효하지 않음
                result = 0
                break

    if empty_list != []:    # 검증이 끝났는데 리스트가 비워있지 않으면, 쌍이 아닌 문자가 있다는 것
        result = 0

    print(f'#{tc} {result}')