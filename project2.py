choice= int(input("type 1 to peform sum, 2 for substraction, 3 for multiplication, 4 for division:"))
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if choice==1:
 print("The sum of",a,"and",b,"is", a+b)
elif choice==2:
 print("The substraction of",a,"and",b,"is", a-b)
elif choice==3:
 print("The multiplication of",a,"and",b,"is", a*b)
else:
 print("The division of",a,"and",b,"is", a/b)
      
