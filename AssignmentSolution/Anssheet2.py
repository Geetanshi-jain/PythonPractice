#1         *
#        * *
#      * * *
#    * * * *
#  * * * * *
for i in range(0,6):
    for j in range(6-i):
       print(" ",end=' ')
    for j in range(i+1):
        print("*",end='')
    print()

#2.
'''* 
   * *
   * * *
   * * * *
   * * * * * '''
for i in range(5):
     for j in  range(i+1):
          print("*",end='')
     print()
#3.* * * * * 
#    * * * *
#      * * * 
#        * *
#          *
for i in range(0,6):
    for j in range(i):
        print(" ",end=' ')

    for j in range(6-i):
        print("*",end=' ')

    print()

#3.* * * * * 
#  * * * *
#  * * * 
#  * *
#  *

for i in range(6,0,-1):
    for j in range(1,i):
        print("*",end=' ')
    print()


# Diamond  pattern
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end= " ")
    print()
# inverse Diamond
n=5
for i in range(n,-1):
    for j in range(2*n-1):
        print("*",end=" ")
    for k in range(j,-1):
        print(" ",end=" ")
    print()




    