Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Simple
>>> # Ladder
>>> # Nested
>>> # Hybrid
>>> 
>>> a = input('Enter your name: ')
Enter your name: Peeyush Sanam
>>> a
'Peeyush Sanam'
>>> 
>>> b = input('Enter some number: ')
Enter some number: 45
>>> b
'45'
>>> type(b)
<class 'str'>
>>> type(a)
<class 'str'>
>>> int(b)
45
>>> float(b)
45.0
>>> b1 = input('Enter some number: ')
Enter some number: 45.3
>>> int(b1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int(b1)
ValueError: invalid literal for int() with base 10: '45.3'
>>> float(b1)
45.3
>>> b2 = eval(b1)
>>> b2
45.3
>>> type(b2)
<class 'float'>
>>> b3 = eval(b)
>>> b3
45
>>> b = eval(input('Enter some number: '))
Enter some number: 65.3
>>> b
65.3
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the first number: 67
Enter the second number: 8
a is bigger than b
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:15
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:14
It can be divided by 7
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:20
It is not possible to divide by 7
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:34
Enter the second number: 6
a is bigger than b
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:0
Enter the second number: 0
none of them is bigger
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:9
Enter the second number: 5
Very good
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:9
Enter the second number: 99
Very nice
>>> 
========== RESTART: E:/TN/SITP21/8thJune_B1_AI_ML/day6/editor_code.py ==========
Enter the number:-9
Enter the second number: 454
Tough luck
>>> 