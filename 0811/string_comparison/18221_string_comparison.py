import sys
sys.stdin = open('4864_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    first_num = 0

def boyermoore(word1, word2, num):
    while num < len(word2)-len(word1):
        for j in range(len(word1)):
            if word1[j] != word2[num+j]:
                break
        else:
            return 1

        if num + len(word1) < len(word2):
            for j in range(word1):
                if word2[num+len(word1)-1] == word1[j]:
                    num += len(word1) - (j+1)
                else:
                    num += len(word1)
        else:
            num = len(word2)-len(word1)

    if num == len(word2)-len(word1):
        for j in range(len(word1)):
            if word1[j] != word2[num+j]:
                break
        else:
            return 1

        return 0

    boyermoore(word1, word2, num)

    print(f'# {tc} {boyermoore(str1, str2, first_num)}')

