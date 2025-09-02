import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    finish = []

    while len(arr) > len(finish):
        corr = [0] * 201
        save = []

        for lst in arr:
            if lst not in finish:
                check = True
                [a, b] = lst
                if a % 2 == 1:
                    a += 1
                if b % 2 == 1:
                    b += 1

                if a < b:
                    for i in range(a//2, (b//2)+1):
                        if corr[i] == 1:
                            check = False
                            break
                    if check is True:
                        save.append(lst)
                        for i in range(a//2, (b//2)+1):
                            corr[i] = 1
                else:
                    for i in range(b//2, (a//2)+1):
                        if corr[i] == 1:
                            check = False
                            break
                    if check is True:
                        save.append(lst)
                        for i in range(b//2, (a//2)+1):
                            corr[i] = 1

        for i in range(len(save)):
            finish.append(save[i])

        cnt += 1

    print(f'#{tc} {cnt}')