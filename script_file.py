# Variable Arguments

##def xyz(x=0):
##    print(x)
##
##xyz()
##xyz(4)
##xyz(4,5)


##def abc(*a):
##    print(a)
##
##abc(4,7,8,9)
##
##d = [4,76,90]
##abc(d)
##
##e = 'good'
##abc(e)
##
##abc(e,d)
##
##abc(e,d,80,90,4,5,78,9,4,8,4)
##
##abc(*d)
##abc(*e)


# Variable Keyword Arguments
##def pqr(a,b):
##    print(a,b)
##
##pqr(b=30,a='hi')#, c=40,d=40)

##def pqrs(**a):
##    print(a)
##
##pqrs(a=30, b=40, age = 19, name='Rahul')
##
##def every_type(a,b,d=10,e=1,*f,**g):
##    print(a,b,d,e,f,g)

### not allowed
##def ekor(*a = (4,5)):
##    print(a)
##ekor()


# Lambda Expressions (Annonymous Functions)
# - One liner
# - Always return a value
# - we can input args
# - we can use ternary conditions or nested ones
#
#  lambda input_arg : output_arg

##def doubler(n):
##    return n*2

##doubler2 = lambda n : n*2


##def operate(f,n):
##    c = []
##    for i in n:        
##        c.append(f(i))
##    return c
##
##a = [3,4,5,6,7,8,23,32,546]
##
##g = operate(lambda x:x*2, a)
##print(g)
##
##g1 = operate(lambda x: x if x%2 else x//2, a)
##print(g1)
##
##def something(k):
##    return k+10
##
##g2 = operate(something, a)
##print(g2)


# Generator
############
##a = [3,4,5,6,7,8,23,32,546]
##m = list(map(lambda x:x**2, a))
##print(m)
##
##f = list(filter(lambda x:x%2==1, a))
##print(f)


def my_gen(n):
    for i in range(1,11):
        yield n*i

##    c = []
##    for i in range(1,11):
##         c.append(n*i)
##    return c












































