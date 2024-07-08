s1={1,2,3,4}
s2={4,5,7}
print(s1.union(s2))
s1.update(s2)
#s2 ke sare element ko add kar dega
print(s1,s2)

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","seuol","kabul"}
cities3= cities.union(cities2)
print(cities3)
cities.intersection_update(cities2)
print(cities)

#remove ke case me agar nhi hoga to error milega
print(cities)
cities.discard("Tokyo")
#agar hoga to remove kar dega nhi hoga to error nhi dega
e = cities2.pop()
print(e)
#del cities delete all content
print(cities)
info ={"Carla",19,False,3.9}
if "carla" in info:
    print("Carla is present")
else:
    print("Carla is absent"
          )
    #Dictionary method
    info ={'name':'Karan','age':19,'eligible':True}
    print(info)
    info.update({'age':20})
    info.update({'Dob':2005})

#Dictionary method 2nd way to update dictionary value
    ep1={1:2,2:3,3:4,4:5,5:6}
    ep2={22:1,43:2,21:54}
    #ep1.update(ep2)
    ep1.clear()
    print(ep1)
    empt={}
    print(empt)
    
   
    #ep1.popitem()
    ep1.update(ep2)
    ep1.clear()
    em = ep2.popitem()#its like a peek of stack 
    print(em)
#Enumerate function in python
fruits=['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(index,fruit)


marks=[12,56,23,43,21,4,5]
#index=0
#for mark in marks:
 #       print(mark)
  #      if(index==3):
   #       print("Harry")  
    #    index+=1
for index ,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("harry")





















