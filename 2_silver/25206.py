import sys

input = sys.stdin.readline

grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
grade_score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

grade_to_score = []

score_list = []

grade_score_list = []

for _ in range(20):
    subject, score, grade = map(str, input().rstrip().split(" "))

    if grade != "P":
        score = float(score)

        score_list.append(score)

        for i in grade_list:
            if i in grade:
                grade = grade.replace(str(i), str(grade_score[grade_list.index(i)]))

                # grade_to_score.append(grade)

        grade_score_list.append(score * float(grade))

print("{0:.6f}".format(sum(grade_score_list) / sum(score_list)))