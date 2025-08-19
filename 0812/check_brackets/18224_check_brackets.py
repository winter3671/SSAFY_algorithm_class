import sys
sys.stdin = open('4866_input.txt')

T = int(input())
for tc in range(1, T+1):
    code = input()

    sample_open = ['{', '[', '(']
    sample_close = ['}', ']', ')']
    empty_list = []
    result = 1

    for i in range(len(code)):
        if code[i] in sample_open:
            empty_list.append(code[i])
        elif code[i] in sample_close:
            if sample_open.index(empty_list[-1]) == sample_close.index(code[i]):
                empty_list.pop()
            else:
                result = 0
                break

    if empty_list != []:
        result = 0


    print(f'#{tc} {result}')