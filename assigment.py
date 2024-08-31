name=str(input("enter your name:"))
n1=int(input("what is your first favorite number:"))
n2=int(input("what is your second favorite number:"))
n3=int(input("what is your third favorite number"))
print(f"{name} ! hi how are you")
list=[n1,n2,n3]
a:list = []
for x in list:
    if(x % 2 == 0):
        print(f"The number {x} is even.")
        a.append(("even",x))
    else:
        print(f"The number {x} is odd.")
        a.append(("odd",x))
b:list = []
for x in list:
    b.append((x, x**2))
    print(f"the number {x} and its square: ({x}, {x**2})")
sum=(n1+n2+n3)
print(f"The sum of three number is {sum}")


i = 1
count = 0
while   i <= sum:
    if sum % i == 0:
        count += 1
    i += 1


if count == 2:
    print(" the  number is Prime")
else:
    print(" the number is not not prime")
    print ("hurrah! you have succeeded your task \n good job sir .")
