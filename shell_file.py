Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
4
Traceback (most recent call last):
  File "E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py", line 5, in <module>
    xyz(4,5)
TypeError: xyz() takes 1 positional argument but 2 were given
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
(4, 7, 8, 9)
([4, 76, 90],)
('good',)
Traceback (most recent call last):
  File "E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py", line 20, in <module>
    abc(e,a)
NameError: name 'a' is not defined
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
(4, 7, 8, 9)
([4, 76, 90],)
('good',)
('good', [4, 76, 90])
('good', [4, 76, 90], 80, 90, 4, 5, 78, 9, 4, 8, 4)
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
(4, 7, 8, 9)
([4, 76, 90],)
('good',)
('good', [4, 76, 90])
('good', [4, 76, 90], 80, 90, 4, 5, 78, 9, 4, 8, 4)
(4, 76, 90)
('g', 'o', 'o', 'd')
>>> k = (13,)
>>> k
(13,)
>>> type(k)
<class 'tuple'>
>>> k1 = (13)
>>> k1
13
>>> type(k1)
<class 'int'>
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
Traceback (most recent call last):
  File "E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py", line 36, in <module>
    pqr(b=30,a='hi', c=40,d=40)
TypeError: pqr() got an unexpected keyword argument 'c'
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
hi 30
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
{'a': 30, 'b': 40, 'age': 19, 'name': 'Rahul'}
>>> 
{'a': 30, 'b': 40, 'age': 19, 'name': 'Rahul'}===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
{'a': 30, 'b': 40, 'age': 19, 'name': 'Rahul'}
>>> 
>>> 
>>> every_type(4,5)
4 5 10 1 () {}
>>> every_type(4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    every_type(4)
TypeError: every_type() missing 1 required positional argument: 'b'
>>> every_type(4,5,e=9,d=20)
4 5 20 9 () {}
>>> every_type(4,5,e=9,d=20,5,6,7,4)
SyntaxError: positional argument follows keyword argument
>>> every_type(4,5,9,20,5,6,7,4)
4 5 9 20 (5, 6, 7, 4) {}
>>> every_type(4,5,9,20,5,6,7,4,hi=30)
4 5 9 20 (5, 6, 7, 4) {'hi': 30}
>>> 
>>> p = every_type
>>> p
<function every_type at 0x000002C190402AF0>
>>> p(6,6,)
6 6 10 1 () {}
>>> print
<built-in function print>
>>> q = 10
>>> 1
1
>>> q
10
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
>>> doubler(40)
80
>>> d = doubler(40)
>>> d
80
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
>>> d = doubler2(40)
>>> d
80
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
[6, 8, 10, 12, 14, 16, 46, 64, 1092]
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
[6, 8, 10, 12, 14, 16, 46, 64, 1092]
[6, 8, 10, 12, 14, 16, 46, 64, 1092]
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
[6, 8, 10, 12, 14, 16, 46, 64, 1092]
[3, 2, 5, 3, 7, 4, 23, 16, 273]
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
[6, 8, 10, 12, 14, 16, 46, 64, 1092]
[3, 2, 5, 3, 7, 4, 23, 16, 273]
[13, 14, 15, 16, 17, 18, 33, 42, 556]
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
[9, 16, 25, 36, 49, 64, 529, 1024, 298116]
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
[9, 16, 25, 36, 49, 64, 529, 1024, 298116]
[3, 5, 7, 23]
>>> a
[3, 4, 5, 6, 7, 8, 23, 32, 546]
>>> m = map(lambda x:x**2, a)
>>> m
<map object at 0x000001F8FF954CA0>
>>> list(m)
[9, 16, 25, 36, 49, 64, 529, 1024, 298116]
>>> list(m)
[]
>>> m
<map object at 0x000001F8FF954CA0>
>>> list(m)
[]
>>> m = map(lambda x:x**2, a)
>>> next(m)
9
>>> next(m)
16
>>> next(m)
25
>>> next(m)
36
>>> next(m)
49
>>> next(m)
64
>>> next(m)
529
>>> next(m)
1024
>>> next(m)
298116
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    next(m)
StopIteration
>>> list(m)
[]
>>> m = map(lambda x:x**2, a)
>>> next(m)
9
>>> list(m)
[16, 25, 36, 49, 64, 529, 1024, 298116]
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    next(m)
StopIteration
>>> m = map(lambda x:x**2, a)
>>> for i in m:
	print(i)

	
9
16
25
36
49
64
529
1024
298116
>>> list(m)
[]
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    next(m)
StopIteration
>>> b = [3,4,6,7]
>>> for i in range(len(b))
SyntaxError: invalid syntax
>>> for i in range(len(b)):
	print(b[i])

	
3
4
6
7
>>> for i in b:
	print(i)

	
3
4
6
7
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
>>> my_gen(3)
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
>>> my_gen(3)
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
>>> 
===== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day10/script_file.py =====
>>> my_gen(3)
<generator object my_gen at 0x00000199AFE1F0B0>
>>> g=my_gen(3)
>>> for i in g:
	print(i)

	
3
6
9
12
15
18
21
24
27
30
>>> 