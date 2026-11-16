# inputs we need from user
#  rent
#electricity units spends
#charger per unit
#water bill
# maintenance charges

rent=int(input("enter your rent"))
roomates=int(input("enter the numbers of rommates"))
electricity_units=float(input("enter the number of units spend"))
electricity_rate=float(input("enter the rate of elecricity"))
water_bill=int(input("enter the water bill"))
maintenance_charges=int(input("enter the maintenance charges"))
electricity_bill=electricity_rate*electricity_units
total_monthly_rent=rent+electricity_bill+ water_bill+ maintenance_charges
each_among_rommates_rent=(total_monthly_rent / roomates) 
print(total_monthly_rent)
print("each roomates rent=",each_among_rommates_rent)
