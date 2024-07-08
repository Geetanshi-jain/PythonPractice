#posoitive negative Zero

a=int(input("enter a number"))
if a>0:
  print(" the no is positive")
elif a<0:
 print("the no is negative")
else:
 print("Zero")
 
 

a=2
b=330
print("A") if a>b else print("B")
#ternary way

a=220
b=22
print("A") if a>b else print("=") if a==b else print("b")


#
a=330
b=22
c=33
if a>b and c>a:
  print("Both conditional are true ")

  if a>b or a>c:
    print("At least one of the condition is true")

x=41
if x>10:
  print("Above ten")
if x>20:
  print("ans also above 20!")
else:
  print("but not above 20.")

  i=1
  while(i<6):
    print(i)
    i+=1

    i=1
    while i<6:
      print(i)
      if i==3:
        break
      i+=1

      i=0
      while  i<6:
        i+=1
        if i==3:
          continue
        print(i)








