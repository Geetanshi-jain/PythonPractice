#list
list=[i for i in range(10)]
print(list)
list1=[i*i for i in range(19)]
list =[1,2,3,4,5]
list.append(7)
print(list)


country =["India","usa""goa"]

if "India" in country:
    print("India is country")
else:
    print("Germeny is atleast")

#Set methods
s={2,4,3,2,1,8,5,6,7}

s={}
print(s)
print(type(s))
s1={1,2,3,4}
s2={2,3,1,4}
print(s1.union(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.add(3))
s1.remove(2)#agar elm nhi mila to error milega
s1.discard(5)# mile na mile ye alag bat h baki error nhi deta
val= s1.pop()
#it return random value
print(val)

del(s1)# it like drop 
#pure list ko hi remove kar dega
#nhi kar sakte
s1.clear()

#if in keyword
if 1 in s1:
    print("yes")
else:
    print("no")
    #dictionary in python
    '''dictionary is a ordered collection'''

#dictionary method
dic={"name":"Geetanshi","age":18,"city":"mumbai"}

dic.clear()
dic.popitem()#last se ek item delete hoga

for i in range(9):
    print(i)
    if i==4:
        break
    else:
        print("sorry")


#Error class in python
a=input("Enter a number")
print(f"multiplication tble of {a} is :")
try:
    for i in range(1,11):
      print(f"{int(a)} X{i}={int(a)*i}")
except Exception as e:
    print("sorry some error occured")



try:
    num=int(input("Enter an interger"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number enterd is not an integer")
except IndexError:
    print("Index error")

print("Some lines of code")
print("End of program")
#if else shorthanded
a=330
b=220
print("A") if a>b else  print("=") if a==b else print("B")
 #try catch or finally
def func():
    try:
        l=[1,2,4,3]
        i=int(input("enter the index"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")


p = func()
print(p)

a=int(input("Enter "))

#Custom exception in python
a=int(input("Enter any value between 5 or 9"))
if(a>5 or a<9):
    raise ValueError("Value should be between 5 or 9")



