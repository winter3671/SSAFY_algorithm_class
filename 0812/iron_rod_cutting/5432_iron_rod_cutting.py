import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    words = input()
    empty_list = []
    cnt = 0
    top = 0
    for i in range(len(words)):
        if words[i] == '(':    # '('이 있으면 1줄 올라가는것
            top += 1
        elif words[i] == ')':   # ')'이 있으면 1줄 내려가는것인데,
            top -= 1
            if words[i-1] == '(':   # 바로전에 '('이 있어서 '()'꼴이 된다면
                cnt += top   # 높이만큼의 갯수를 cnt에 더해준다 (그림 상 레이저의 왼쪽부분)
            else:   # '()'꼴이 아니라면,
                cnt += 1    # 한줄 내려가면서 cnt에 1개를 더해준다 (그림 상 레이저의 오른쪽 윗부분)

    print(f'#{tc} {cnt}')