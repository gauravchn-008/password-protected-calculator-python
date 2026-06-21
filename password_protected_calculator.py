username=input("USERNAME : ")
password=input("PASSWORD : ")
if username=="Admin" and password=="1234" :
    num=int(input("ENTER NUMBER 1 : "))
    num2=int(input("ENTER NUMBER 2 : "))
    print("SELECT OPERATOR : \n 1. SUM \n 2. SUBTRACT \n 3. MULTIPLY \n 4. DIVIDE \n 5. REMAINDER", "\n note : enter number of operator you want to perform")
    operator=int(input("enter operator number : "))
    if operator==1 :
        print(num+num2)
    elif operator==2:
        print(num-num2)
    elif operator==3:
        print(num*num2)
    elif operator==4:
        if num2!=0:
            print(num/num2)
        else:
            print ("incorrect value in denominator")
    elif operator==5:
        if num2!=0:
            print(num%num2)
        else:
            print ("incorrect value in denominator")
    else :
        print("choose correct operation number")
        
else :
    print("Invalid Username or Password")
    
            
        

    

