print("welcome to sbi atm")
pin=int(input("enter your atm pin:"))
if pin==123:
    print("proceeding")
    withdrawal_amount=int(input("enter your  withdrawal amount"))
    available_amout=20000
    if withdrawal_amount<=available_amout:
        print("wait for transaction")
        print("successfully withdrawal")
        check_balance=available_amout-withdrawal_amount
        print("your remaning  balance ",check_balance)
    else:
        print("insufficient balance")
      
else:
    print("wrong pin")