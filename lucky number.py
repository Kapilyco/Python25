number = int(input("Enter the Number First : "))
if(number%3==0 and number%5==0):
     print("number is fizzbuzz")
else:
    if(number%3==0):
             print("number is Fizz")
    elif(number%5==0):
        print("number is Buzz")
    else:
        print(number)
    

 
