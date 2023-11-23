# class Calculator:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname
#     def add(self,a,b,c):
#         return a+b+c
#     def add(self,a,b):
#         return a+b


# class Calculator1:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c


# cal = Calculator("Pratik","Mane")
# print(cal.add(2,3))
# print(cal.add(3,4))

# cal2 = Calculator1()

# # Calling the add method with two arguments
# result1 = cal2.add(5, 10,1)
# print("Result with two arguments:", result1)  # Output: Result with two arguments: 15

# # Calling the add method with three arguments
# result2 = cal2.add(5, 10, 15)
# print("Result with three arguments:", result2) 

def add(*args):
    sum = 0
    for i in args:
        sum += i

    return sum 

print(add(2,3))
print(add(3,2,1,5))

def calc(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        print("key-->",key)
        print("value -->",value)

print(calc(name="Pratik",surname="Mane"))

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')