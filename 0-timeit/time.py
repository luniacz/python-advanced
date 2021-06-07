import timeit

setup = '''
def power_function(a):
    return a**2,

power_lambda = lambda a: a ** 2

my_list = [x for x in range(100000)]'''

code1 = '''
a = power_function(10)
'''

code2 = '''
a = power_lambda(10)
'''

code3 = '''
my_list.pop(3)
'''

code4 = '''
del my_list[3]
'''

# print(timeit.timeit(code1, setup, number=10000000))
# print(timeit.timeit(code2, setup, number=10000000))

time1 = timeit.timeit(code3, setup, number=10000)
time2 = timeit.timeit(code4, setup, number=10000)

print((time2-time1)/time2*100)

