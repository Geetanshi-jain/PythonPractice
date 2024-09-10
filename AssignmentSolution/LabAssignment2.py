for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


#2. 
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
        j=j+1
    print()


#3.
a='A'
for i in range(1,6):
    for  j in range(1,i+1):
        print(a,end= " ")
       
    print()
    a=chr(ord(a)+1)
    
#4. 
for i in range(5,0,-1):
    for j in range(i):
        print("*",end= " ") 
    print()

#5.
ctn=1
for i in range(5,0,-1):
    for j in range(i):
        print(ctn,end= " ") 
        ctn=ctn+1
    print()
    ctn=1


#7.
#        * 
#      * * *
#    * * * * *
#  * * * * * * * 

for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

# 7. * * * * * 
#      * * *
#        *

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")

    for j in  range(2*i-1):
        print("*",end=" ")
    print()


#        * 
#      * * *
#    * * * * *
#  * * * * * * * 
#    * * * * *  
#      * * *
#        *


for i in range(5):
    for j in range(5-1-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")

    for j in  range(2*i-1):
        print("*",end=" ")
    print()
"""
 8  * * * * 
    * * * *
    * * * *
    * * * * 
 """

for i in range(4):
    for j in range(4):
        print(" *" ,end=" ")
    print()


"""
 *
 * * *
 * * * *
 * * * * *
 * * * * * *
 * * * * * 
 * * *
 *
"""
for i in range(6):
    for  j in range(i+1):
         print("*",end= " ")
    print()
for  k in range(3,0,-1):
    for l in range(2*k-1):
        print("*",end=" ")
    print()

"""
 1 1 1 1 1 
 2 2 2 2 2 
 3 3 3 3 3
 4 4 4 4 4
 5 5 5 5 5
 """
for i in range(1,6):
    for j in range(6):
        print(i,end=" ")
    print()

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()


"""
13.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(i):
        print(i)
    print()


#14




