Marks= int(input("Enter your marks here:"))
if(Marks>100 or Marks<0):
    print("invalid Marks")
else:
    if(Marks>=90):
        print("You are pass and Your grade is : A")
    elif(Marks>=80 and Marks<90):
        print("You are pass and Your grade is : B")
    elif(Marks>=70 and Marks<80):
        print("You are pass and Your grade is : C")
    elif(Marks>=60 and Marks<70):
        print("You are pass and Your grade is : D")
    else:
        print("You are Fail")
              
    
