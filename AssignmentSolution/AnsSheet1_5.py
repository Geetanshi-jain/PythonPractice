'''num1= int(input("enter first  number"))
num2= int(input("enter secand number"))
num3= int(input("enter third number"))
if(num1>num2 and num1>num3 ):
    print(" num1 is greatest number")
elif(num2>num1 and num2>num3):
    print("num2 is greates number")
else:
    print("num3 is gratest number")
"""
# 2.	Write a python program whether a number is positive negative or zero. 

num=int(input("enter number"))
if(num>0):
    print("numbber is positive")
elif(num<0):
    print("number is negative")
else:
    print("number is Zero")

    #3.	Write a python program to check whether a number is divisible by 11 or not. 
    num =int(input("enter a number"))
    if(num%11==0):
        print("number is divisible by 11")
    else:
        print("number is not divisible by 11")

        #4 4.	Write a python program to check whether a number is even or odd using conditional statement and using for and while loop. 

num=int(input("enter a number"))
if(num%2==0):
    print("number is  even")
else:
    print("number is odd")
    #5.	Write a python program to check whether a year is a leap year or not. 
    num =int(input("enter a number"))
if((num%4==0 and num%100==0) or (num%400==0)):
    print("number is leap year")
else:
    print("number is not leap year ")
#6.	Write a python program to calculate profit or loss. 
    sp =int(input("enter selling price"))
    cp=int(input("enter cost price"))
    if(sp-cp>0):
        print("you are in profit your profit is"+(sp-cp))
    elif(sp-cp<0):
        print("you are in loss"+(cp-sp))
    else:
        print("you are in ideal condition no profit and loss")'''
    #7.	Write a python program to calculate grades of a student. 
marks =int (input("enter marks"))
if marks>90:
    print(" O grade")
elif(marks>=80 and marks<90):
    print("A+ grade")
elif(marks>=70 and marks<80):
    print("A grade")
elif(marks>=60 and marks<70):
    print(" B+ grade")
elif(marks>=50 and marks<60):
    print(" B grade")
elif(marks>=40 and marks<50):
    print(" c grade")
else:
    print("fail")
#8.	Write a python program to check whether a person is eligible for loan or not if he is having salary more than 50k and 3 years of experience. 
salary= int(input("enter a salary "))
experience = int(input("enter experience"))

if (salary>50000 and experience >3 ):
    print("you are eligible for   loan ")
else:
    print("not eligible for loan ")

    #9.	Write a python program to find the area and volume of sphere. 
r =int(input("enter radius"))
v=4/3*22/7*r**3
print("volume of sphere "+v)
#10.	Write a python program to display the data type.
a =12
b =1.2
c='str'
d=3+4
e = [1,2,3]
f=(1,2,3)
g= {"a":1}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


