user_age=int(input("enter your age:"))
user_salary=int(input("enter your salary"))
if user_age>=25 and user_salary>=30000:
    print("eligible for 5 lakh loan")
elif user_age>=25 and user_salary>=15000:
    print("eligible for 50 thousand loan") 
else:
    print("not eligible for loan")