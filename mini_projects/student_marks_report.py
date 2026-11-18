student_name=input("enter your name:")
marks=[]
for i in range(5):
    student_marks=int(input("enter your marks :"))
    marks.append(student_marks)
total=sum(marks)
print("total marks is:",total)
percentage=total/500*100
print("percentage is:",percentage,"%")
average=total/len(marks)
print("average is:",average)
print("highest marks is :",max(marks))
print("lowest marks is :",min(marks))
print(sorted(marks))
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

