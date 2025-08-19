import sys
sys.stdin = open('4873_input.txt')

T = int(input())
for tc in range(1, T+1):
    words = input().strip()
    empty_list = []
    for i in range(len(words)):
        if empty_list == []:    # 리스트의 원소가 없으면 인덱스를 사용할 수 없음
            empty_list.append(words[i])     # 그때 words[i]를 empty_list에 추가하고, 아래를 건너뜀
            continue
        if words[i] != empty_list[-1]:  # empty_list의 마지막 원소와 words[i]가 다르면
            empty_list.append(words[i])     # empty_list에 추가
        else:   # 같으면
            empty_list.pop()    # empty_list의 마지막 원소를 삭제

    print(f'#{tc} {len(empty_list)}')