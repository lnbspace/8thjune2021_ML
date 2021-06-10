Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Integer
>>> ##############################################
>>> a = 10
>>> type(a)
<class 'int'>
>>> 
>>> # Float
>>> ##############################################
>>> b = 10.0
>>> type(b)
<class 'float'>
>>> a
10
>>> print(a)
10
>>> float(a)
10.0
>>> c = float(a)
>>> c
10.0
>>> type(c)
<class 'float'>
>>> d = int(b)
>>> d
10
>>> # Complex
>>> ###############################################
>>> e = 10+0j
>>> type(e)
<class 'complex'>
>>> e
(10+0j)
>>> 
>>> 
>>> ###############################################
>>> # String
>>> ###############################################
>>> s = 'Hello this is a string'
>>> type(s)
<class 'str'>
>>> s1 = "Hello this is a string"
>>> type(s1)
<class 'str'>
>>> s
'Hello this is a string'
>>> s1
'Hello this is a string'
>>> print(s)
Hello this is a string
>>> 
>>> s2 = 'I\'ve a python string'
>>> s2
"I've a python string"
>>> print(s2)
I've a python string
>>> s3 = 'this is first line\nAnd this is second line'
>>> s3
'this is first line\nAnd this is second line'
>>> print(s3)
this is first line
And this is second line
>>> a
10
>>> s4 = str(a)
>>> s4
'10'
>>> type(s4)
<class 'str'>
>>> print(s4)
10
>>> s5 = '''this is the first line
and here we have second line as well
lastly we have one more stuff'''
>>> s5
'this is the first line\nand here we have second line as well\nlastly we have one more stuff'
>>> print(s5)
this is the first line
and here we have second line as well
lastly we have one more stuff
>>> s6 = """this is the first line
and here we have second line as well
lastly we have one more stuff"""
>>> print(s6)
this is the first line
and here we have second line as well
lastly we have one more stuff
>>> type(s5)
<class 'str'>
>>> type(s6)
<class 'str'>
>>> '''this is the first line
and here we have second line as well
more line









kjdshgkjfd

lastly we have one more stuff'''
'this is the first line\nand here we have second line as well\nmore line\n\n\n\n\n\n\n\n\n\nkjdshgkjfd\n\nlastly we have one more stuff'
>>> s = 'Hello World!'
>>> type(s)
<class 'str'>
>>> len(s)
12
>>> s[0]
'H'
>>> s[-1]
'!'
>>> s[-4]
'r'
>>> s[3]
'l'
>>> s[11]
'!'
>>> s[12]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s[12]
IndexError: string index out of range
>>> 
>>> #### Slicing
>>> s[0:5:1]
'Hello'
>>> s[6:11:1]
'World'
>>> s[6:11:2]
'Wrd'
>>> s[6:11:3]
'Wl'
>>> s[-6:12:1]
'World!'
>>> s[-6:-1:1]
'World'
>>> 
>>> s[6:-1]
'World'
>>> s[6:-1:]
'World'
>>> s[0:5]
'Hello'
>>> s[:5]
'Hello'
>>> s[-6:]
'World!'
>>> 
>>> s
'Hello World!'
>>> s[6:-1]
'World'
>>> s[-2:-6]
''
>>> s[-2:-6:-1]
'dlro'
>>> s[-2:-7:-1]
'dlroW'
>>> s[4::-1]
'olleH'
>>> s[::-1]
'!dlroW olleH'
>>> 
>>> 
>>> 3 * 3
9
>>> 'go'*4
'gogogogo'
>>> print('#'*20)
####################
>>> 
>>> 'wow'+'nice'
'wownice'
>>> s
'Hello World!'
>>> s1
'Hello this is a string'
>>> s+s1
'Hello World!Hello this is a string'
>>> 
>>> 
>>> s
'Hello World!'
>>> s = s[:6] + 'New ' + s[6:]
>>> s
'Hello New World!'
>>> s += '!'
>>> s
'Hello New World!!'
>>> s[0]
'H'
>>> s[0] = 'K'
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s[0] = 'K'
TypeError: 'str' object does not support item assignment
>>> del s[0]
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    del s[0]
TypeError: 'str' object doesn't support item deletion
>>> 
>>> b
10.0
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> 
>>> 
>>> s
'Hello New World!!'
>>> s.capitalize()
'Hello new world!!'
>>> s
'Hello New World!!'
>>> ss = s.capitalize()
>>> ss
'Hello new world!!'
>>> 
>>> s.count('e')
2
>>> s.find('W')
10
>>> s.upper()
'HELLO NEW WORLD!!'
>>> s.split()
['Hello', 'New', 'World!!']
>>> 
>>> help(s.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> s
'Hello New World!!'
>>> s = s[:6]+s[-7:]
>>> s
'Hello World!!'
>>> s[:-2]
'Hello World'
>>> sss = s[:-2]
>>> sss
'Hello World'
>>> 