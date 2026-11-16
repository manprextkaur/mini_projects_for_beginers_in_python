employee_name=input("enter your name:")
employee_salary=int(input("enter your salary amount:"))
employee_experience=float(input("enter your experience:"))
HRA= employee_salary*20/100
print(HRA)
if employee_experience>=6:
    bonus=employee_salary*30/100
    print(bonus)
elif employee_experience>=2:
    bonus=employee_salary*20/100
    print(bonus)
else:
    bonus=0
    print("bonus:",bonus)
gross=employee_salary+HRA+bonus
print("gross",gross)
tax=gross*10/100
if gross >=50000:
    print("tax applied",tax)
else:
    tax=0
    print("tax",tax)
net_salary=gross-tax
print("net salary",net_salary)
