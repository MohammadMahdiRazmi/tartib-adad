num1= int(input("adad khod ra vared konid:"))
num2= int(input("adad khod ra vared konid:"))
num3= int(input("adad khod ra vared konid:"))
if (num1<num2<num3):
    big=num3
    meduim=num2
    small=num1
elif (num1<num3<num2):
    big=num2
    meduim=num3
    small=num1
elif (num2<num1<num3):
    big=num3
    meduim=num1
    small=num2
elif (num2<num3<num1):
    big=num1
    meduim=num3
    small=num2 
elif (num3<num2<num1):
    big=num1
    meduim=num2
    small=num3
elif (num3<num1<num2):
    big=num2
    meduim=num1
    small=num3
elif(num1==num2<num3):
    big=num3
    meduim=num2
    small=num1
elif(num2==num3<num1):
    big=num1
    meduim=num2
    small=num3
elif(num1==num3<num2):
    big=num2
    meduim=num3
    small=num1
elif(num1==num3>num2):
    big=num1
    meduim=num3
    small=num2
else:
    print("error not valid")
print(big,meduim,small)