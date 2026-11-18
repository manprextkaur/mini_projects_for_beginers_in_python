name=[]
price=[]
for i in range(3):
    item_name=input("enter your name of item:")
    name.append(item_name)
    item_price=int(input("enter your price of the item:"))
    price.append(item_price)
total=0
for i in range(len(name)):
    print(i+1,name[i],price[i])
    total=total+price[i]
print("grand total",total)
