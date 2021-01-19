Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ----------------------------------- SETS
>>> 
>>> 
>>> s1 = {'a', 'b', 'c', 'd', 'e', 'f'}
>>> type(s1)
<class 'set'>
>>> s1
{'f', 'b', 'a', 'd', 'c', 'e'}
>>> s1 = {'a', 'a', 'a','b', 'c', 'd', 'e', 'f'}
>>> s1
{'f', 'b', 'a', 'd', 'c', 'e'}
>>> 
>>> 
>>> s1.add('g')
>>> s1
{'f', 'b', 'a', 'd', 'c', 'g', 'e'}
>>> s1.remove('g')
>>> s1
{'f', 'b', 'a', 'd', 'c', 'e'}
>>> s1.remove('z')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s1.remove('z')
KeyError: 'z'
>>> 
>>> s = set("xyz")
>>> s
{'y', 'z', 'x'}
>>> s1.add(s)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s1.add(s)
TypeError: unhashable type: 'set'
>>> 
>>> 
>>> L = []
>>> L.append(s)
>>> L
[{'y', 'z', 'x'}]
>>> 
>>> 
>>> s
{'y', 'z', 'x'}
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> s1.update(s)
>>> s1
{'f', 'b', 'a', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> 
>>> s1.remove('a')
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> 
>>> s1.
SyntaxError: invalid syntax
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> 
>>> s2 = "defghijk"
>>> s2 = set(s2)
>>> 
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> s2
{'f', 'j', 'h', 'k', 'd', 'i', 'g', 'e'}
>>> s1.intersection(s2)
{'f', 'e', 'd'}
>>> s1.union(s2)
{'f', 'b', 'y', 'j', 'h', 'k', 'd', 'i', 'z', 'c', 'g', 'e', 'x'}
>>> 
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> 
>>> 
>>> 
>>> # ------------------------- Megha/Vishwanath
>>> 
>>> 
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> s2
{'f', 'j', 'h', 'k', 'd', 'i', 'g', 'e'}
>>> 
>>> 
>>> s
{'y', 'z', 'x'}
>>> s = {'m', 'n', 'o'}
>>> 
>>> s1.intersection(s2)
{'f', 'e', 'd'}
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> s2
{'f', 'j', 'h', 'k', 'd', 'i', 'g', 'e'}
>>> s3 = s1.intersection(s2)
>>> s3
{'f', 'e', 'd'}
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> s2
{'f', 'j', 'h', 'k', 'd', 'i', 'g', 'e'}
>>> 
>>> 
>>> 
>>> s
{'m', 'o', 'n'}
>>> s1.union(s)
{'f', 'b', 'y', 'o', 'd', 'z', 'n', 'c', 'm', 'e', 'x'}
>>> s1
{'f', 'b', 'y', 'd', 'z', 'c', 'e', 'x'}
>>> s
{'m', 'o', 'n'}
>>> 
>>> 
>>> s1.update(s)
>>> s1
{'f', 'b', 'o', 'y', 'd', 'z', 'n', 'c', 'm', 'e', 'x'}
>>> 
>>> s
{'m', 'o', 'n'}
>>> s.add('f')
>>> s1.update(s)
>>> s1
{'f', 'b', 'o', 'y', 'd', 'z', 'n', 'c', 'm', 'e', 'x'}
>>> 
>>> s3 = s1.update(s)
>>> s3
>>> s3 = s1.union(s)
>>> s3
{'f', 'b', 'o', 'y', 'd', 'z', 'n', 'c', 'm', 'e', 'x'}
>>> s1
{'f', 'b', 'o', 'y', 'd', 'z', 'n', 'c', 'm', 'e', 'x'}
>>> 
>>> 
>>> # --------------------------------- Operators
>>> 
>>> 
>>> s1
{'f', 'b', 'o', 'y', 'd', 'z', 'n', 'c', 'm', 'e', 'x'}
>>> s2
{'f', 'j', 'h', 'k', 'd', 'i', 'g', 'e'}
>>> 
>>> s1 | s2
{'f', 'b', 'o', 'h', 'k', 'z', 'n', 'm', 'e', 'j', 'y', 'd', 'i', 'c', 'g', 'x'}
>>> s1 & s2
{'f', 'e', 'd'}
>>> s1 ^ s2
{'o', 'j', 'h', 'k', 'b', 'y', 'i', 'z', 'n', 'c', 'm', 'g', 'x'}
>>> 
