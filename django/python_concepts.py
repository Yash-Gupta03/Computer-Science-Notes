# print('Hello')

my_num = [1,2,3,4,5,5]
# print(sum(my_num))


# s = 'Yash'
# print(s[::-1])

# s = 'abba'
# print('True' if s == s[::-1] else 'False')

# x = set(my_num)
# print(x)
# x = []
# [x.append(i) for i in my_num if i not in x]
# print(x)

# try:
#     x = 1/0
# except Exception as e:
#     print(e)

# total = lambda my_num: my_num if 1<0 else 0
# print(total(my_num))

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(10))

# Decorators
# def Hello(greet):
#     def x():
#         print('Hello', end=' ')
#         greet()
#     return x


# @Hello
# def greet():
#     print('Yash')

# greet()


# deep copy

# import copy
# newlist = copy.deepcopy(my_num)
# newlist.append([6,7,8])
# print(newlist, my_num)


# square = [i*10 for i in range(5,10) ]
# print(square)


# x = [1,2,3,4]
# y = x
# print('yes') if newlist is my_num else print('No')

#*args and **kargs
# def keywords(*args, **kargs):
#     for i in args:
#         print(i)
#     for k,v in kargs.items():
#         print(k, v)

# keywords(1,2,3,4,a=10,b=20)

# Generators and list
# def gen(n):
#     for i in range(n):
#         yield i

# x = gen(50)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))




