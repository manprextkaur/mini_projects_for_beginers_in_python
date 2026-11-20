def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b


while True:
    print("press 2 for subtract operation")
    print("press 1 for addition operation")
    print("press 3 for multiplication operation")
    print("press 4 for division operation")
    print("press 5 for modulus operation")
    print("press 6 Exit")
    
    choice=int(input("enter the choice you want to perform operation"))
    if choice==6:
        print("goodbye")
        break
    a=int(input("enter your number:"))
    b=int(input("enter your number:"))
    if choice==1:
        print("addition operation is perform:")
        result=addition(a,b) 
        print("result is:",result)                 

    elif choice ==2:
        print(" subtract operation is perform:")
        result=subtract(a,b) 
        print("result is:",result) 


    elif choice ==3:
        print(" multiplication operation is perform:")
        result=multiplication(a,b) 
        print("result is:",result) 
                               
                            
    elif choice ==4:
        print(" division operation is perform:")
        if b!=0:
            result=division(a,b) 
            print("result is:",result) 
        else:
            print("cannot divide by 0")
                               
                            
    elif choice ==5:
        print(" modulus operation is perform:")
        if b!=0:
            result=modulus(a,b) 
            print("result is:",result) 
        else:
            print("cannot perform modulus by 0")
                                
    else:
        print("invalid choice")

                        

                        


