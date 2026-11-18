subtotal=0
item_price=float(input("enter your item price(0 to finish):"))
while item_price!=0:
    item_qty=int(input("enter your qty"))
    total= item_price*item_qty
    subtotal=subtotal+total
    print("the item price is:",item_price,"\n""item bought:",item_qty,"\n""total price*qty is :",total)
    item_price=float(input("enter your item price(0 to finish):"))
print("subtotal is:",subtotal)
if subtotal>=2000:
    discount=subtotal*20/100
   
    print("discountis given:",discount)
elif subtotal>=1000:
    discount=subtotal*10/100
    print("discountis given:",discount)
elif subtotal>=500:
    discount=subtotal*5/100
    print("discountis given:",discount)
else:
    discount=0
    print("discountis given:",discount)
after_discount=subtotal-discount
print("after_discount is:",after_discount)
gst=after_discount*18/100
print("gst is given:",gst)
final_amount=after_discount+gst
print("final amount",final_amount)

   



