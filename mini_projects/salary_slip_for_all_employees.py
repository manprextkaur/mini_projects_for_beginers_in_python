count_employees=int(input("enter no of employees in company:"))
for i in range(1,count_employees+1):
    employee_name=input("enter your name:")
    employee_salary=int(input("enter your salary:"))
    employee_experience=float(input("enter your experience:"))
    Hra=employee_salary*20/100
    if employee_experience>=5:
       bonus=employee_salary*20/100
       print("bonus is given to employee is:",bonus)
    elif employee_experience>=3:
        bonus=employee_salary*10/100
        print("bonus is given to employee is:",bonus)
    elif employee_experience>=1:
        bonus=employee_salary*5/100
        print("bonus is given to employee is:",bonus)
    else:
        bonus=0
        print("bonus is given to employee is:",bonus)
    gross=employee_salary+Hra+bonus
    if gross>50000:
        tax=gross*10/100
        print("tax is applied:",tax)
    else:
        tax=0
        print("tax is applied:",tax)
    net_salary=gross-tax
    print("net salary for ",employee_name,"employee is:",net_salary)



     


        

