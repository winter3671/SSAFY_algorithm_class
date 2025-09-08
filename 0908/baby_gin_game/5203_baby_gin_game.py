import sys
sys.stdin = open('5203_input.txt')

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    first_cards = []
    second_cards = []
    first_idx = 0
    second_idx = 0
    result = 0

    for i in range(12):
        if i % 2 == 0:
            first_cards.append(nums[i])
            first_idx += 1
            if first_idx >= 3:
                run_cnt = 0
                for num in first_cards:     # 마지막 카드와 같은 카드가 2장 더 있을 때
                    if first_cards[first_idx-1] == num:
                       run_cnt += 1
                if run_cnt >= 3:
                    result = 1
                    break
                if first_cards[first_idx-1] - 1 in first_cards and first_cards[first_idx-1] - 2 in first_cards:
                    result = 1  # 마지막 카드 -1, 마지막 카드 -2가 first_cards 에 있을 때
                    break
                if first_cards[first_idx - 1] + 1 in first_cards and first_cards[first_idx - 1] + 2 in first_cards:
                    result = 1  # 마지막 카드 +1, 마지막 카드 +2가 first_cards 에 있을 때
                    break
                if first_cards[first_idx - 1] + 1 in first_cards and first_cards[first_idx - 1] - 1 in first_cards:
                    result = 1  # 마지막 카드 +1, 마지막 카드 -1가 first_cards 에 있을 때
                    break
        else:
            second_cards.append(nums[i])
            second_idx += 1
            if second_idx >= 3:
                run_cnt = 0
                for num in second_cards:
                    if second_cards[second_idx - 1] == num:
                        run_cnt += 1
                if run_cnt >= 3:
                    result = 2
                    break
                if second_cards[second_idx - 1] - 1 in second_cards and second_cards[
                    second_idx - 1] - 2 in second_cards:
                    result = 2
                    break
                if second_cards[second_idx - 1] + 1 in second_cards and second_cards[
                    second_idx - 1] + 2 in second_cards:
                    result = 2
                    break
                if second_cards[second_idx - 1] + 1 in second_cards and second_cards[second_idx - 1] - 1 in second_cards:
                    result = 2
                    break



    print(f'#{tc} {result}')
