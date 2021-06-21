##a = eval(input('Enter the value: '))

##if a%2:
##    print(a, 'is Odd Number')
##else:
##    print(a, 'is even number')

##b = eval(input('Enter the second value: '))
##c = eval(input('Enter the third value: '))

##if a>b:
##    print('a is bigger')
##    if a>c:
##        print('its largest')
##    else:
##        print('c is bigger than a')
##elif b>a:
##    print('b is bigger')
##else:
##    print('this is not desired')
        

##while a > b:
##    print('nice')
##    a -= 1

##for i in [a,b,c]:
##    print('good', i)


##k = [8,7,56,4,9,11,10]
###p = [4,28,2,5]
##m = []
##for i in k:
##    if i%2:
##        m.append(i)
##print(k)
##print(m)
##
##
##p = []
##for i in k:
##    if not i%2:
##        p.append(i//2)
##print(p)

##for i in range(1,11,1):
##    print(i*a)
##
##print('*'*20)
##for i in range(10,0,-1):
##    print(i*a)

# break: breaks from a loop
##for i in range(10):
##    print('hi'*i)
##    if i==4:
##        break

### continue: breaks from an iteration
##for i in range(10):
##    if i ==5 or i==8:
##        continue
##    print('*'*i)
##    
### pass: pass it further
##while cond:
##    pass
##print('hello')

#print(4,5,6, sep='$', end='%')
##print(4,5,6, sep='$')
##print('done')

'''

*****
****
***
**
*


*        *
**      **
***    ***
****  ****
**********

1
12
123
1234
12345

1
22
333
4444
55555

'''

######################################
# Comprehension
## 1. This is to create collections
## 2. They use for-loop
## 3. Its a one-liner
## 4. if-statement can be used
## 5. Nesting is possible
## 6. We can use ternary conditional statement


# List Comp..
a = [4,5,7,8,93,3]

##b = []
##for i in a:
##    b.append(i*2)

b = [i*2 for i in a]
print(a)
print(b)

odd = [i for i in a if i%2]
print(odd)

values = [i if i%2 else i//2 for i in a]
print(values)





