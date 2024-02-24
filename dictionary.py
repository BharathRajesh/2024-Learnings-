student_marks={
    'bharath':23,
    'niharika':34,
    'shylaja':45,
    'poornima':56
}
for student in student_marks:
    marks=student_marks[student]
    if marks>50:
        student_marks[student]='Outstanding'
    elif marks>40:
        student_marks[student]='pass'
    elif marks>30:
        student_marks[student]='just pass'
    elif marks<30 :
        student_marks[student]='fail'

print(student_marks)