
def app1(fx,value):
    return 6+fx(value)

double =lambda x:x*2
cube =lambda x: x*x*x
avg =lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(app1(lambda x:x*x*x,2))
print(app1(lambda X:X*X*X),3)


