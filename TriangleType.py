side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1 == side2 == side3:
    print("All sides are equal. It's an Equilateral Triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Two sides are equal. It's an Isosceles Triangle.")
elif (((side1**2)==((side2**2)+(side3**2))) or ((side2**2)==((side1**2)+(side3**2))) or ((side3**2)==((side2**2)+(side1**2)))):
    if(side1 != side2 !=side3):
       print("This triangle  is Right angle Triangle and Scalene Triangle")
    else:
        print("This triangle  is Right angle Triangle")
else:
    print("All sides are different. It's a Scalene Triangle.")
    
