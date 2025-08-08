import sys
sys.stdin = open('sample_input.txt')

def search(p, page):
    l = 1    # 탐색 범위의 첫 페이지
    r = p    # 탐색 범위의 마지막 페이지

    count = 0
    while True:
        c = int((l + r) / 2)    # 탐색 범위의 중간

        count += 1
        if abs(r-l) == 1:
            break

        if c == page:
            break

        elif c < page:
            l = c

        elif c > page:
            r = c

    return count

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    if search(P, Pa) < search(P, Pb):
        result = 'A'
    elif search(P, Pa) > search(P, Pb):
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')

