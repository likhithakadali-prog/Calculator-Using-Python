print("select operations:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

choice=input("enter choice:")

n1=float(input("enter the first number:"))
n2=float(input("enter the second number:"))

if choice=='1':
   result=n1+n2
   print("result is:",result)
         
elif choice=='2':
   result=n1-n2
   print("result is:",result)
         
elif choice=='3':
   result=n1*n2
   print("result is:",result)
         
                  
elif choice=='4':
         if n2==0:
            print("error!cannot divide by zero")
         else:
             result=n1/n2
             print("result is:",result)
else:
    print("Invalid Input")

