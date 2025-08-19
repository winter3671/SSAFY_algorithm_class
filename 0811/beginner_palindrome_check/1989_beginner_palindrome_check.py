import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input().strip()
    len_word = len(word)
    result = 0

    for i in range(len_word//2):    # len_word의 절반만 탐색
        if word[i] != word[(len_word-1)-i]:     # 양 대칭점이 일치하지 않으면 break
            break
    else:   # 범위를 순회할동안 break 되지 않으면 result를 1로 바꿈
        result = 1

    print(f'#{tc} {result}')
