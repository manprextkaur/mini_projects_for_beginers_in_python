count_expenses=int(input("enter your expenses:"))
total_expenses=0
for i in range(1,count_expenses+1):
    expenses=float(input("enter your expenses you spend in a month:"))
    total_expenses=total_expenses+expenses
print("total expenses ",total_expenses)
average=total_expenses/count_expenses
print(average)

