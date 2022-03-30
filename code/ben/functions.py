# def my_function(param1=;'default'):
#     print('my first function')

def my_function(x,y):
    if type(x)==type(y)==type(10):
        return x+y
    else:
        return "Sorry, I need integers!"

result = my_function(5,3)
print(result)

def hello():
    print('hello')

hello()

problem = my_function("5", 2)
print(problem)

mylist = [1,2,3,4,5,6,7,8]

# def even_bool(num):
#     return num%2 == 0

# evens = filter(even_bool,mylist)
# print(list(evens))

evens = filter(lambda num:num%2 == 0,mylist)
print(list(evens))