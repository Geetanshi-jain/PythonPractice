import time
timestamp =time.strftime('%H:%M:%S')
print(timestamp)
timestamp=time.strftime('%H')
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)


# match case
x=int(input("Enter the value of x"))
match x:
    case 0:
        print("x is Zero")
    case 1:
        print("case 1")
    case  2:
        print("case 2")
    case _ if x!=50:
        print("other case")
    case _ if x!=23:
        print("x,is not 23")
    case _:
        print(x)

        
colors= ["red","Green","yellow","blue","purple"]
for x in colors:
    print(x)

#iterate each word in list
colors=["Red","blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
#range function
for k in range(10):
    print(k)
for k in range(10):
    print(k+ 1)

for k in range(1,5):
    print(k+ 1)
#while loop
i=int(input("enter the number"))


for i in range(19):
    print(" 5 X",i+1,"=",5*i+1)
    if(i==10):
        break
#continue
for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X",i,"=",5*i)

i==0
while True:
    if(i%100==0):
        break


    def calculatorGemean(a,b):
        mean=(a*b)/(a+b)
        print(mean)

        a=9
        b=1
        calculatorGemean(9,1)
        c=3
        d=4
        calculatorGemean(c,d)

def isgreater(a,b):
    if(a>b):
        print("a is greater no")
    else:
        print("b is greater no")


    a=2
    b=3
    if(a>b):
        print("first number is ")
    else:
        print("ssecond number is greater or equal to secand num")


isgreater(2,1)

def islesser(a,b):
    pass

#Arguments in python 
#function
def average(a,b):
    print(a+b/2)
    #default arg
    average(2,3)
#keyword argument
average(b=2,a=3)


#variable length args
#in list
numbers=(1,2,3,2,1,1)
def average(*numbers):
    for i in numbers:
        sum=sum+i
print("avg = ",sum/len (numbers) )
average(*numbers)

#in dictonaries
def name(**names):
    print("Hello,",names["fname"],names["mname"],names["lname"])
name(mname="van" ,lname="rosum", fname="Guido")


