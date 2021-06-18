### Dictionary Comprehension
##a = ['name','age']
##b = ['Rahul',23]
##
##d = {a[i]:b[i] for i in range(2)}
##print(d)


# zip, enumerate, map, filter, *, **

##a = [3,5,7,2,8,3,9]
##for i in a:
##    print(i)

##for i in enumerate(a):
##    print(i)

##for a,b in enumerate(a):
##    print(b, 'is located at',a,'index')

##a = ['name','age']
##b = [['Rahul','Vijay','Vishesh'],[23,22,23]]
##c = {v:b[i] for i,v in enumerate(a)}
##print(c)

#file = open('data.txt','r')

##with open('data.txt','r') as file:
##    content = file.read()
##    file.close()
##
####print(content)
##c_list = content.split('\n')
####print(c_list)
##heading = c_list[0].split(',')
####print(heading)
##rows = [i.split(',') for i in c_list[1:]]
####print(rows)
##data = dict(zip(heading, zip(*rows)))
####print(data)
##
##import json
##with open('my_json_data.json','w') as file:
##    json.dump(data, file)
##print('saved')


##def gen_dict():
##    print('hi')
##
##def xyz(a):
##    print(a)
##
##def abc(a,b):
##    print(a+b)
##
##def pqr(a=1,b=0):
##    print(a+b)
##
##def new(n=2,k=0):
##    return (n**4)+k

##gen_dict()
##xyz(45)
##xyz(a=60)
##xyz(a='hello')
##abc(4,5)

def gen_dict(fileName = ''):
    with open(fileName,'r') as file:
        content = file.read()
        file.close()
    c_list = content.split('\n')
    heading = c_list[0].split(',')
    rows = [i.split(',') for i in c_list[1:]]
    return dict(zip(heading, zip(*rows)))

d1 = gen_dict('data.txt')
d2 = gen_dict('new_data.txt')
print(d1)
print(d2)


















