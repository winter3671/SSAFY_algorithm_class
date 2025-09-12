import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))

    scores_set = {0}

    for i in scores:
        new_scores = set()
        for j in scores_set:
            new_scores.add(i+j)
        scores_set |= new_scores

    print(f'#{tc} {len(scores_set)}')