Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------------ TUPLES
>>> 
>>> 
>>> L = ['red', 'green', 'blue']
>>> type(L)
<class 'list'>
>>> T = ('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> 
>>> 
>>> T[0]
'red'
>>> T[0:2]
('red', 'green')
>>> T[::-1]
('blue', 'green', 'red')
>>> 
>>> 
>>> # -------------------------- immutability
>>> 
>>> L[1]
'green'
>>> L[1] = 'lightgreen'
>>> L
['red', 'lightgreen', 'blue']
>>> T[1]
'green'
>>> T[1] = 'lightgreen'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    T[1] = 'lightgreen'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # -------------------------------- searching, counting
>>> 
>>> T.count('red')
1
>>> T.index('red')
0
>>> 'red' in T
True
>>> T.find('red')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    T.find('red')
AttributeError: 'tuple' object has no attribute 'find'
>>> 
>>> # ------------------------------- Re-arranging elements
>>> 
>>> T
('red', 'green', 'blue')
>>> reversed(T)
<reversed object at 0x0000025B4AE84710>
>>> tuple(reversed(T))
('blue', 'green', 'red')
>>> T
('red', 'green', 'blue')
>>> T.reverse()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    T.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> L.reverse()
>>> L
['blue', 'lightgreen', 'red']
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> 
>>> # ------------------------ process to make changes to tuple
>>> 
>>> T
('red', 'green', 'blue')
>>> T = list(T)
>>> type(T)
<class 'list'>
>>> T.append('golden')
>>> T
['red', 'green', 'blue', 'golden']
>>> T = tuple(T)
>>> type(T)
<class 'tuple'>
>>> T
('red', 'green', 'blue', 'golden')
>>> 
>>> 
>>> # -------------------------- unpacking list/tuple elements
>>> 
>>> T
('red', 'green', 'blue', 'golden')
>>> L
['blue', 'lightgreen', 'red']
>>> r, g, b = L
>>> r
'blue'
>>> g
'lightgreen'
>>> b
'red'
>>> 
>>> 
>>> r, g, b = T
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    r, g, b = T
ValueError: too many values to unpack (expected 3)
>>> r, g, *x = T
>>> r
'red'
>>> g
'green'
>>> x
['blue', 'golden']
>>> 
>>> 
>>> # ------------------------  Megha
>>> 
>>> L
['blue', 'lightgreen', 'red']
>>> L.append(5)
>>> L.append([1,2,3])
>>> L
['blue', 'lightgreen', 'red', 5, [1, 2, 3]]
>>> a,b,c,d,e = L
>>> type(a)
<class 'str'>
>>> type(d)
<class 'int'>
>>> type(e)
<class 'list'>
>>> L.append(('a','e','i'))
>>> L
['blue', 'lightgreen', 'red', 5, [1, 2, 3], ('a', 'e', 'i')]
>>> 

>>> # -------------------- Prajaktha
>>> 
>>> L
['blue', 'lightgreen', 'red', 5, [1, 2, 3], ('a', 'e', 'i')]
>>> a, b, c = L
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a, b, c = L
ValueError: too many values to unpack (expected 3)
>>> a, b, c, *x = L
>>> a
'blue'
>>> b
'lightgreen'
>>> c
'red'
>>> x
[5, [1, 2, 3], ('a', 'e', 'i')]
>>> 
>>> 
>>> # ----------------------------- Hrishi
>>> 
>>> a, b, c = L[:3]
>>> a
'blue'
>>> b
'lightgreen'
>>> c
'red'
>>> 
>>> 
>>> # --------------------------- Megha
>>> 
>>> L
['blue', 'lightgreen', 'red', 5, [1, 2, 3], ('a', 'e', 'i')]
>>> L = [1, 2, 3, 4, 5, 6]
>>> L[1:3]
[2, 3]
>>> L[1:4]
[2, 3, 4]
>>> [-5:-2]
SyntaxError: invalid syntax
>>> L[-5:-2]
[2, 3, 4]
>>> L[:3]
[1, 2, 3]
>>> L[3:]
[4, 5, 6]
>>> 
>>> 
>>> # ---------------------------- duplicating lists/tuples
>>> 
>>> 
>>> L
[1, 2, 3, 4, 5, 6]
>>> L1 = L
>>> L
[1, 2, 3, 4, 5, 6]
>>> L1
[1, 2, 3, 4, 5, 6]
>>> L[3] = L[3] * 10
>>> L
[1, 2, 3, 40, 5, 6]
>>> L1
[1, 2, 3, 40, 5, 6]
>>> 
>>> L1[2] = 20
>>> L
[1, 2, 20, 40, 5, 6]
>>> L1
[1, 2, 20, 40, 5, 6]
>>> 
>>> 
>>> import copy
>>> L
[1, 2, 20, 40, 5, 6]
>>> L = [1, 2, 3, 4, 5, 6]
>>> L
[1, 2, 3, 4, 5, 6]
>>> L1 = copy.deepcopy(L)
>>> L
[1, 2, 3, 4, 5, 6]
>>> L1
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> L[3] = L[3] * 10
>>> L
[1, 2, 3, 40, 5, 6]
>>> L1
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> 
>>> T
('red', 'green', 'blue', 'golden')
>>> L = T
>>> L
('red', 'green', 'blue', 'golden')
>>> T
('red', 'green', 'blue', 'golden')
>>> 
>>> L
('red', 'green', 'blue', 'golden')
>>> T
('red', 'green', 'blue', 'golden')
>>> 
>>> T = list(T)
>>> T
['red', 'green', 'blue', 'golden']
>>> L
('red', 'green', 'blue', 'golden')
>>> T.append("golden")
>>> T
['red', 'green', 'blue', 'golden', 'golden']
>>> L
('red', 'green', 'blue', 'golden')
>>> 
>>> 
>>> # -------------------------- Vishwanath
>>> 
>>> L
('red', 'green', 'blue', 'golden')
>>> L = list(L)
>>> L
['red', 'green', 'blue', 'golden']
>>> T = ("black", "white")
>>> T = L
>>> T
['red', 'green', 'blue', 'golden']
>>> L
['red', 'green', 'blue', 'golden']
>>> 
>>> 
>>> a =10
>>> a
10
>>> a = "string"
>>> a
'string'
>>> T
['red', 'green', 'blue', 'golden']
>>> L
['red', 'green', 'blue', 'golden']
>>> L.sppend("white")
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    L.sppend("white")
AttributeError: 'list' object has no attribute 'sppend'
>>> L.append("white")
>>> L
['red', 'green', 'blue', 'golden', 'white']
>>> T
['red', 'green', 'blue', 'golden', 'white']
>>> 
>>> 
>>> # ------------------------------ Megha
>>> 
>>> L
['red', 'green', 'blue', 'golden', 'white']
>>> T = tuple(L)
>>> T
('red', 'green', 'blue', 'golden', 'white')
>>> L
['red', 'green', 'blue', 'golden', 'white']
>>> L.append("black")
>>> L
['red', 'green', 'blue', 'golden', 'white', 'black']
>>> T
('red', 'green', 'blue', 'golden', 'white')
>>> ('red', 'green', 'blue', 'golden', 'white')
('red', 'green', 'blue', 'golden', 'white')
>>> 
>>> 
>>> # ------------------------------------- Hrishi
>>> 
>>> # The above effects are predominently seeen in tuples and lists
>>> # doesn't apply numbers and strings
>>> 
>>> 
