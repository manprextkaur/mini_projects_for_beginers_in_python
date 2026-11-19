pass_count=0
fail_count=0
toper_total=0
topper_name=" "
student_strength=int(input("enter class strength:"))
for i in range(1,student_strength+1):
    student_name=input("enter your name:")
    marks=[]
    for j in range(5):
        student_marks=int(input("enter your marks:"))
        marks.append(student_marks)
    print("student name is :",student_name)
    total=sum(marks)
    print("total marks obtained is:",total)
    percentage=total/500*100
    print("percentage is:",percentage)
    if percentage>=90:
            print("grade A")
    elif percentage>=75:
            print("grade B")
    elif percentage>=60:
            print("grade C")
    elif percentage>=40:
            print("grade D")
    else:
          print("fail")

    if percentage>=40:
        print("pass")
        pass_count=pass_count+1
  
    else:
        print("fail")
        fail_count=fail_count+1
    if total>toper_total:
        toper_total=total
        topper_name=student_name
       

print("pass number of student in class is:",pass_count)
print("fail number of student in class is:",fail_count)
print("the topper is:",topper_name,toper_total)

    
