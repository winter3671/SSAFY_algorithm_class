import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()

    result = []
    for i in range(len(word)-1, -1, -1):    # 뒤에서부터 체크하면서 하나씩 문자를 뒤집어서 추가
        if word[i] == 'b':
            result.append('d')
        elif word[i] == 'd':
            result.append('b')
        elif word[i] == 'p':
            result.append('q')
        elif word[i] == 'q':
            result.append('p')

    print(f'#{tc} {"".join(result)}')