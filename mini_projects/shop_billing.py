item_bought=int(input("enter the number of item bought:"))
total_items=0
for i in range(1,item_bought+1):
    item_name=input("enter the name of item:")
    item_price=int(input("enter your item price:"))
    qty=int(input("enter your quantity bought:"))
    bill=item_price*qty
    total_items=total_items+bill
print("total bill:",total_items)
if total_items>=2000:
    discount=total_items*20/100
    print("discount is given:",discount)
elif total_items>=1000:
    discount=total_items*10/100
    print("discount is given:",discount)
elif total_items>=500:
    discount=total_items*5/100
    print("discount is given:",discount)
else:
    discount=0
    print("discount is given:",discount)
final_amount=total_items-discount
print("final amount is:",final_amount)

