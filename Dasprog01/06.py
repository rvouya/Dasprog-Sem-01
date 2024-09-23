#grading
needed_score = input("Enter desired grade : ")
minimum_score = float(input("Enter minimum average required : "))

#in decimal
grade = float(input("Enter current average in course : "))

#score weighting (in decimal)
score_weight_exam = float(input("Enter how much the final counts as a percentage of the course grade : "))
score_weight_assign = 100-score_weight_exam

#formula
final_exam = abs((minimum_score - (score_weight_assign / 100 * grade)) / (score_weight_exam / 100))
rounded_score = format(final_exam, ".2f")

#output
print(f"You need a score of {rounded_score} on the final to get a {needed_score}")