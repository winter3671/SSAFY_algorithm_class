import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
for tc in range(1, T+1):
    tc_num, N = input().split()
    tc_num = int(tc_num.lstrip('#'))    # '#'을 빼고 tc_num만 받기 위해 lstrip 사용
    N = int(N)
    word_list = list(input().split())

    sample = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new_list = []

    for word in sample:
        for i in range(N):
            if word_list[i] == word:    # sample의 단어와 word_list[i]의 단어가 같을때만 더하기
                new_list.append(word_list[i])

    print(f'#{tc_num}')
    print(' '.join(new_list))