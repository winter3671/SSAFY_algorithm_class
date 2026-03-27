import sys
sys.stdin = open('sample_input.txt')

def restore(cnt, word, a, b, c, d):
    global result
    if result is not 'impossible':
        return

    if a > A or b > B or c > C or d > D:
        return

    if a == A and b == B and c == C and d == D:
        result = word
        return

    if cnt == 0:
        restore(cnt + 1, 'A', a+1, b, c, d)
        restore(cnt + 1, 'B', a, b+1, c, d)
        restore(cnt + 1, 'C', a, b, c+1, d)
        restore(cnt + 1, 'D', a, b, c, d+1)

    else:
        if word[-1] == 'A' or word[-1] == 'C':
            restore(cnt + 1, word + 'A', a+1, b, c, d)
            restore(cnt + 1, word + 'B', a, b+1, c, d)
        elif word[-1] == 'B' or word[-1] == 'D':
            restore(cnt + 1, word + 'C', a, b, c+1, d)
            restore(cnt + 1, word + 'D', a, b, c, d+1)


T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    word_dic = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}
    result = 'impossible'
    result_num = ""

    restore(0, '', 0, 0, 0, 0)

    if result is not 'impossible':
        result_num = word_dic[result[0]]
        for i in range(1, len(result)):
            result_num += word_dic[result[i]][1]
    else:
        result_num = result

    print(f'#{tc} {result_num}')

