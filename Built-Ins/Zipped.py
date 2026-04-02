#https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true 

n_students, n_subjs = map(int,input().split())

scores = []
for _ in range(n_subjs):
    m = list(map(float, input().split()))
    scores.append(m)

#zip function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.
all_student_scores_list = zip(*scores)

for one_student_scores in all_student_scores_list:
    print(sum(score for score in one_student_scores)/n_subjs)
