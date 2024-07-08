questions =[["which language was used to create fb?","python","java","c","cpp"],
           ["which language was used to create fb?","python","java","c","cpp"],
           ["which language was used to create fb?","python","java","c","cpp"],
           ["which language was used to create fb?","python","java","c","cpp"],
           ["which language was used to create fb?","python","java","c","cpp"],
]
levels=[1000,2000,3000,4000,5000,]
money=0
for i in range(0,len(questions)):
       
            question=questions[i]
            print(f"\n\nQuestion for Rs,{levels[i]}")
            print(f"a.{questions[1]}  b.{questions[2]}")

            print(f"c.{questions[3]}  d.{questions[4]}")

            reply =int(input("Enter your answer(1-4)"))
                    
            if(reply==question[-1]):
                    print(f"Correct ans","you have won Rs.{levels[i]}")
            if(i==4):
                    money =10000
            elif(i==9):
                    money =320000
            elif(i==14):
                    money=500000
            else:
                    print("Wrong answer")
                    break
               

print("your take home money is {money}")



              

