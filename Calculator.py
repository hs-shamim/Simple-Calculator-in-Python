print("Calculator\n")
num1=float(input("Enter your first number:"))
oper=input("Enter operator (+, -, *, /):")
num2=float(input("Enter second number:"))
if oper=="+":
  su=num1+num2
  re=str(su)
  print("Result:"+re)
elif oper=="*":
  su=num1*num2
  re=str(su)
  print("Result:"+re)
elif oper=="/":
  su=num1/num2
  re=str(su)
  print("Result:"+re)
elif oper=="-":
  su=num1-num2
  re=str(su)
  print("Result:"+re)
else :
  print("Invalid operator!")
