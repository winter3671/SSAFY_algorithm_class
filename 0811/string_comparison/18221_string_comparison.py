import sys
sys.stdin = open('4864_input.txt')


def boyermoore(word1, word2, num):  # num은 word1이 탐색을 시작하는 index
    while num <= len(word2) - len(word1):
        if num < len(word2) - len(word1):
            for j in range(len(word1)):
                if word1[j] != word2[num + j]:
                    break
            else:
                return 1
            for j in range(len(word1)):
                if word2[num + len(word1) - 1] == word1[j]:
                    num += len(word1) - (j + 1)
                    break
            else:
                num += len(word1)

        else:
            for j in range(len(word1)):
                if word1[j] != word2[num + j]:
                    break
            else:
                return 1

        return boyermoore(word1, word2, num)


    if num > len(word2) - len(word1):
        num = len(word2) - len(word1)
        return boyermoore(word1, word2, num)

    return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    num = 0

    result = boyermoore(str1, str2, num)

    print(f'# {tc} {result}')

