username= "deepanshu garg"

def func():
    username = "chai"
    print(username)


print(username)
func()

x = 99

# def func2(y):
#     z=x+y
#     return z
# print(func2(10))

# def func3():
#     global x
#     x=880
# func3()
# print(x)

def f1():
    x=88
    def f2():
        print(x)
    return f2
# this what we call closure def se related jitne bhi variable ha uske refernce bhi jate ha 
# f2() this will execute the function return f2 this will return the reference 
myresult = f1()
myresult()

def chaicoder(N):
    def actual(x):
        return  x**N
    return actual 

# def chaicoder(2):

#     # below place has been gone and backback also
#     def actual(x):
#         return  x**2
#     return actual 
# actual we are returnig the defination not running it for running we have to do this actual() 

f = chaicoder(2)
g=chaicoder(3)
#  f and g memory has a function so we can execute this ,f and g has actual method
print(f(3))
print(g(3))