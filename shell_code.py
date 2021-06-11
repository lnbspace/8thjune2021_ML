Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## List
>>> ######################################
>>> a = [7, 'hi', 90, 93.2, 'go', 4+5j, [8,9,'nice']]
>>> type(a)
<class 'list'>
>>> len(a)
7
>>> print(a)
[7, 'hi', 90, 93.2, 'go', (4+5j), [8, 9, 'nice']]
>>> a
[7, 'hi', 90, 93.2, 'go', (4+5j), [8, 9, 'nice']]
>>> 
>>> # indexing
>>> a[0]
7
>>> a[1]
'hi'
>>> a[-1]
[8, 9, 'nice']
>>> a[-1][1]
9
>>> a[-1][-1]
'nice'
>>> a[-1][-1][-1]
'e'
>>> a[-1][-1][-2]
'c'
>>> # Slicing
>>> a[:3]
[7, 'hi', 90]
>>> a[-3:]
['go', (4+5j), [8, 9, 'nice']]
>>> 
>>> # List is mutable so.....
>>> a[0]
7
>>> a[0] = 77
>>> a
[77, 'hi', 90, 93.2, 'go', (4+5j), [8, 9, 'nice']]
>>> 
>>> del a[-2]
>>> a
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice']]
>>> 
>>> 
>>> a * 2
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice'], 77, 'hi', 90, 93.2, 'go', [8, 9, 'nice']]
>>> a + [99, 999]
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice'], 99, 999]
>>> 
>>> a += [1000, 10]
>>> a
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10]
>>> 
>>> a += ['Hello']
>>> a
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello']
>>> a += 'Hello'
>>> a
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o']
>>> a
[77, 'hi', 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o']
>>> a = a[:2] + [900] + a[2:]
>>> a
[77, 'hi', 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o']
>>> a = a[:2] + [['New list', 'data']] + a[2:]
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o']
>>> 
>>> a.append('bye')
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye']
>>> b = a
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye']
>>> b
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye']
>>> b.append('New')
>>> b
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New']
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New']
>>> a.append('old')
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> b
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> 
>>> c =a.copy()
>>> c
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> del c[6:12]
>>> c
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> help(a.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> a.count(7)
0
>>> a.count(10)
1
>>> a.extend(10,100,1000)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.extend(10,100,1000)
TypeError: list.extend() takes exactly one argument (3 given)
>>> a.extend([10,100,1000])
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old', 10, 100, 1000]
>>> a.index('bye')
16
>>> a.insert(10, 'wow')
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 1000, 10, 'wow', 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old', 10, 100, 1000]
>>> k = a.pop(8)
>>> k
1000
>>> a
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 10, 'wow', 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old', 10, 100, 1000]
>>> a.remove('hi')
>>> a
[77, ['New list', 'data'], 900, 90, 93.2, 'go', [8, 9, 'nice'], 10, 'wow', 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old', 10, 100, 1000]
>>> a.remove(['New list', 'data'])
>>> a
[77, 900, 90, 93.2, 'go', [8, 9, 'nice'], 10, 'wow', 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old', 10, 100, 1000]
>>> a.remove(4444)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.remove(4444)
ValueError: list.remove(x): x not in list
>>> a.reverse()
>>> a
[1000, 100, 10, 'old', 'New', 'bye', 'o', 'l', 'l', 'e', 'H', 'Hello', 'wow', 10, [8, 9, 'nice'], 'go', 93.2, 90, 900, 77]
>>> a[::-1]
[77, 900, 90, 93.2, 'go', [8, 9, 'nice'], 10, 'wow', 'Hello', 'H', 'e', 'l', 'l', 'o', 'bye', 'New', 'old', 10, 100, 1000]
>>> a
[1000, 100, 10, 'old', 'New', 'bye', 'o', 'l', 'l', 'e', 'H', 'Hello', 'wow', 10, [8, 9, 'nice'], 'go', 93.2, 90, 900, 77]
>>> 
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> b = [45,86,24,67,34]
>>> b.sort()
>>> b
[24, 34, 45, 67, 86]
>>> b.sort(reverse=True)
>>> b
[86, 67, 45, 34, 24]
>>> 
>>> 
>>> max(b)
86
>>> min(b)
24
>>> 
>>> ## Tuple
>>> ################################
>>> t = (45,75,34,8,'hi','nice',7.4)
>>> type(t)
<class 'tuple'>
>>> print(t)
(45, 75, 34, 8, 'hi', 'nice', 7.4)
>>> len(t)
7
>>> t1 = 5,75,34,8,'hi','nice',7.4
>>> t1
(5, 75, 34, 8, 'hi', 'nice', 7.4)
>>> t2 = 45,5
>>> t3 = 'hi'
>>> type(t2)
<class 'tuple'>
>>> type(t3)
<class 'str'>
>>> t3 = 'hi',
>>> type(t3)
<class 'tuple'>
>>> t3
('hi',)
>>> 
>>> t[0]
45
>>> t[-3]
'hi'
>>> t[4:]
('hi', 'nice', 7.4)
>>> 
>>> t[0] = 55
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    t[0] = 55
TypeError: 'tuple' object does not support item assignment
>>> del t[0]
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> t*3
(45, 75, 34, 8, 'hi', 'nice', 7.4, 45, 75, 34, 8, 'hi', 'nice', 7.4, 45, 75, 34, 8, 'hi', 'nice', 7.4)
>>> t+t
(45, 75, 34, 8, 'hi', 'nice', 7.4, 45, 75, 34, 8, 'hi', 'nice', 7.4)
>>> 
>>> t += 78,'hiii'
>>> t
(45, 75, 34, 8, 'hi', 'nice', 7.4, 78, 'hiii')
>>> t += 78,['hiii','go',555555]
>>> t
(45, 75, 34, 8, 'hi', 'nice', 7.4, 78, 'hiii', 78, ['hiii', 'go', 555555])
>>> t[-1]
['hiii', 'go', 555555]
>>> t[-1][-2]
'go'
>>> t.count(45)
1
>>> t.index(45)
0
>>> 
>>> 
>>> ## Dictionary
>>> ####################################
>>> students = {'age':[20,19,21,20,22],'course':['python','data science','ml','python','ml']}
>>> type(students)
<class 'dict'>
>>> print(students)
{'age': [20, 19, 21, 20, 22], 'course': ['python', 'data science', 'ml', 'python', 'ml']}
>>> len(students)
2
>>> d= {1:2,3:'nice',44:[3,4,5,7]}
>>> type(d)
<class 'dict'>
>>> d
{1: 2, 3: 'nice', 44: [3, 4, 5, 7]}
>>> students[0]
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    students[0]
KeyError: 0
>>> students['age']
[20, 19, 21, 20, 22]
>>> d[3]
'nice'
>>> d[44]
[3, 4, 5, 7]
>>> 
>>> d.get(44)
[3, 4, 5, 7]
>>> d.get(45)
>>> d[45]
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    d[45]
KeyError: 45
>>> 
>>> d.keys()
dict_keys([1, 3, 44])
>>> d.values()
dict_values([2, 'nice', [3, 4, 5, 7]])
>>> students.keys()
dict_keys(['age', 'course'])
>>> 
>>> d*2
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    d*2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> d+d
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    d+d
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d['new'] = 45
>>> d
{1: 2, 3: 'nice', 44: [3, 4, 5, 7], 'new': 45}
>>> del d[1]
>>> d
{3: 'nice', 44: [3, 4, 5, 7], 'new': 45}
>>> d['new'] = 450
>>> d
{3: 'nice', 44: [3, 4, 5, 7], 'new': 450}
>>> d[6666] = 450
>>> d
{3: 'nice', 44: [3, 4, 5, 7], 'new': 450, 6666: 450}
>>> d[66] = d[6666]
>>> del d[6666]
>>> d
{3: 'nice', 44: [3, 4, 5, 7], 'new': 450, 66: 450}
>>> d[606] = d.pop(66)
>>> d
{3: 'nice', 44: [3, 4, 5, 7], 'new': 450, 606: 450}
>>> 
>>> # concatenation of dictionaries
>>> d
{3: 'nice', 44: [3, 4, 5, 7], 'new': 450, 606: 450}
>>> students
{'age': [20, 19, 21, 20, 22], 'course': ['python', 'data science', 'ml', 'python', 'ml']}
>>> {d, students}
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    {d, students}
TypeError: unhashable type: 'dict'
>>> {**d, **students}
{3: 'nice', 44: [3, 4, 5, 7], 'new': 450, 606: 450, 'age': [20, 19, 21, 20, 22], 'course': ['python', 'data science', 'ml', 'python', 'ml']}
>>> 
>>> 
>>> a
[1000, 100, 10, 'old', 'New', 'bye', 'o', 'l', 'l', 'e', 'H', 'Hello', 'wow', 10, [8, 9, 'nice'], 'go', 93.2, 90, 900, 77]
>>> b
[86, 67, 45, 34, 24]
>>> c
[77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> (b,c)
([86, 67, 45, 34, 24], [77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'e', 'l', 'l', 'o', 'bye', 'New', 'old'])
>>> (*b,*c)
(86, 67, 45, 34, 24, 77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'e', 'l', 'l', 'o', 'bye', 'New', 'old')
>>> [*b,*c]
[86, 67, 45, 34, 24, 77, 'hi', ['New list', 'data'], 900, 90, 93.2, 'e', 'l', 'l', 'o', 'bye', 'New', 'old']
>>> 
>>> 
>>> ### Set
>>> s = {4,5,67,5,5,5,5,5,7,'hi'}
>>> s
{67, 4, 5, 7, 'hi'}
>>> len(s)
5
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> a = None
>>> a
>>> print(a)
None
>>> len(a)
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    len(a)
TypeError: object of type 'NoneType' has no len()
>>> 
>>> s1 = ''
>>> len(s1)
0
>>> k = []
>>> m = ()
>>> n = {}
>>> 