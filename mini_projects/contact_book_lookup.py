contact_book={
    "contact1":{"name":"Aman","Phone_no":9023502189},
    "contact2":{"name":"Lin","Phone_no":9023502019},
    "contact3":{"name":"kam","Phone_no":9023550609}

}
find_name=input("enter the name you want to see in contact:")
found=0
for contact in contact_book:
    if contact_book[contact]["name"] == find_name:
        print(contact_book[contact]["name"],":",contact_book[contact]["Phone_no"])
        found=1
if found==0:
    print("not found")
    new_name=input("enter your name:")
    new_number=int(input("enter your number:"))
    new_contact="contact"+str(len(contact_book)+1)
    contact_book[new_contact]={"name":new_name,"Phone_no":new_number}
    print("contact added sucessfully")
for contact in contact_book:
    print(contact_book[contact]["name"],":",contact_book[contact]["Phone_no"])
print("total contact:",len(contact_book))

