# input marks for 5 subjects
marks= []
for i in range(1,6):
    mark = float(input(f"Enter marks for subject {i}:"))
    marks.append(mark)

# Calculate total and percentage
total_marks = sum(marks)
percentage = (total_marks /500) * 100 # assuming each subject is out of 100

# Determine grade
if percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'E'

# Display results
print("\n------ Result-----")
print(f"total marks: {total_marks}/500")
print(f"percentage: {percentage:.2f}%")
print(f"grade:{grade}")
