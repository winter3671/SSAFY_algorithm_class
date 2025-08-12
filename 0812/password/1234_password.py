import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, words  = input().split()
    N = int(N)
    new_words = []
    for i in range(N):
        if new_words == []:     # new_words가 빈 리스트이면 번호를 추가
            new_words.append(words[i])
        else:
            if new_words[-1] == words[i]:   # new_words의 마지막 숫자와 번호를 비교
                new_words.pop()     # 같으면, new_words의 마지막 숫자를 제거
            else:
                new_words.append(words[i])      # 다르면, 번호를 추가

    print(f'#{tc} {"".join(new_words)}')


