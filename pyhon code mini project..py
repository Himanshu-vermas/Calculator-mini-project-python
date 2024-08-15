first = input("enter first number:")
operator = input("enter operator(+,-,*,/,%):")
second = input("enter second number:")


first= int(first)
second=int(second)

if operator=="+":
    print(first + second)
if operator=="-":
    print(first - second)
if operator=="*":
    print(first * second)
if operator=="/":
    print(first / second)
if operator=="%":
    print(first % second)  
else:
    print("INvalid operation")
  