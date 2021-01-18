Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ----------------------------- NUMBERS
>>> 
>>> 
>>> # ------- Operators
>>> 
>>> # Arithmetic Operators
>>> 
>>> a = 5
>>> b = 2
>>> a + b
7
>>> c = a + b
>>> a
5
>>> b
2
>>> c
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a ** b
25
>>> 
>>> # Relational OPerators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a <= b
False
>>> a >= b
True
>>> a != b
True
>>> a == b
False
>>> 
>>> # Logical Operators
>>> 
>>> a > b
True
>>> a < 10
True
>>> a > b and a < 10
True
>>> a > b and a != 5
False
>>> a > b or a != 5
True
>>> a > b and not(a != 5)
True
>>> 
>>> # ------------------ in-built functions
>>> 
>>> 
>>> a
5
>>> b
2
>>> a - b
3
>>> b - a
-3
>>> abs(a - b)
3
>>> abs(b - a)
3
>>> 
>>> i = input("Enter a number: ")
Enter a number: 45
>>> i + 45
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    i + 45
TypeError: can only concatenate str (not "int") to str
>>> int(i) + 45
90
>>> float(i) * 5
225.0
>>> 
>>> x = 100
>>> hex(x)
'0x64'
>>> oct(100)
'0o144'
>>> bin(x)
'0b1100100'
>>> 
>>> 
>>> y = '0x64'
>>> int(y)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(y)
ValueError: invalid literal for int() with base 10: '0x64'
>>> y = '64'
>>> int(y)
64
>>> int('0x64', 16)
100
>>> y = 0x64
>>> y
100
>>> b = '1001'
>>> int(b)
1001
>>> int(b, 2)
9
>>> b = 0b1001
>>> b
9
>>> b = input("Enter a binary number: ")
Enter a binary number: 0b1001
>>> b
'0b1001'
>>> int(b)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '0b1001'
>>> int(b, 2)
9
>>> pow(5, 2)
25
>>> # ------------------------- in - built modules
>>> 
>>> a = 90
>>> sin(a)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    sin(a)
NameError: name 'sin' is not defined
>>> import math
>>> sin(a)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    sin(a)
NameError: name 'sin' is not defined
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * 3.14159/180)
0.9999999999991198
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> import random
>>> random.randint(1, 100)
99
>>> random.randint(1, 100)
20
>>> random.randint(1, 100)
21
>>> random.randint(1, 100)
54
>>> random.randint(1, 100)
12
>>> random.randint(1, 100)
12
>>> random.randint(1, 100)
10
>>> random.randint(1, 100)
73
>>> 
>>> # ----------------------------------------------------
>>> 
>>> a = 10
>>> b = math.sqrt(a)
>>> a
10
>>> b
3.1622776601683795
>>> 
>>> a == b * b
False
>>> a
10
>>> b * b
10.000000000000002
>>> 
