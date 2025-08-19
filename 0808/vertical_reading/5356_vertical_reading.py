import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    empty_list = []

    for i in range(5):
        empty_list.append(input())

    max_len_word = 0      # 단어들의 최댓값
    for word in empty_list:
        if max_len_word < len(word):
            max_len_word = len(word)

    new_list = []
    for i in range(max_len_word):  # 최댓값만큼 순회
        for word in empty_list:     # 단어들에 대해
            if i < len(word):
                new_list.append(word[i])    # 단어들의 i번째를 더한다
                                    # 단어의 인덱스를 초과하면 더하지않고 넘어감
    print(f'#{tc} {"".join(new_list)}')

