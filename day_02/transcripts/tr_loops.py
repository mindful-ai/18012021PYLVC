Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "python"
>>> for c in s:
	print("Oracle")

	
Oracle
Oracle
Oracle
Oracle
Oracle
Oracle
>>> for c in s:
	print(s + " ----> " + "Oracle")

	
python ----> Oracle
python ----> Oracle
python ----> Oracle
python ----> Oracle
python ----> Oracle
python ----> Oracle
>>> for c in s:
	print(c + " ----> " + "Oracle")

	
p ----> Oracle
y ----> Oracle
t ----> Oracle
h ----> Oracle
o ----> Oracle
n ----> Oracle
>>> 
>>> for item in ["red", "green", "blue"]:
	print(item, ' ', len(item))

	
red   3
green   5
blue   4
>>> for item in ("red", "green", "blue"):
	print(item, ' ', len(item))

	
red   3
green   5
blue   4
>>> 
>>> D = {"name":'Anil', "age":35, "company": "Oracle" }
>>> D
{'name': 'Anil', 'age': 35, 'company': 'Oracle'}
>>> for i in D:
	print(i)

	
name
age
company
>>> for i in D.keys():
	print(i)

	
name
age
company
>>> for i in D.values():
	print(i)

	
Anil
35
Oracle
>>> for i in D.keys():
	print(i + ' ------> ' + str(D[i]))

	
name ------> Anil
age ------> 35
company ------> Oracle
>>> 
>>> for i in D.keys():
	print(i , ' ------> ' , D[i])

	
name  ------>  Anil
age  ------>  35
company  ------>  Oracle
>>> for i in D.keys():
	print(i + ' ------> ' + D[i])

	
name ------> Anil
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    print(i + ' ------> ' + D[i])
TypeError: can only concatenate str (not "int") to str
>>> 
>>> for item in D.items():
	print(item)

	
('name', 'Anil')
('age', 35)
('company', 'Oracle')
>>> 
>>> for key, value in D.items():
	print(key, value)

	
name Anil
age 35
company Oracle
>>> 
>>> D1 = {}
>>> for key, value in D.items():
	D1.setdefault(value, key)

	
'name'
'age'
'company'
>>> D1
{'Anil': 'name', 35: 'age', 'Oracle': 'company'}
>>> 
>>> for s in set("mississippi"):
	print(s)

	
i
p
m
s
>>> 
>>> # ----------------------------------------
>>> 
>>> N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for n in N:
	print(5, ' X ', n, ' = ', 5 * n)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(30, 40))
[30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
>>> list(range(10, 100, 2))
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> list(range(100, 90, -1))
[100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
>>> for n in range(11):
	print(5, ' X ', n, ' = ', 5 * n)

	
5  X  0  =  0
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> for n in range(1,11):
	print(5, ' X ', n, ' = ', 5 * n)

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> 
>>> 
>>> i = 1
>>> while i <= 10:
	print(5, ' X ', i, ' = ', 5 * i)
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> # ----------------------------- Loop controls
>>> 
>>> 
>>> for c in "computer":
	print(c, end=' ')

	
c o m p u t e r 
>>> for c in "computer":
	print(c, end='|')

	
c|o|m|p|u|t|e|r|
>>> 
>>> 
>>> ['u', 'i', 'x']
['u', 'i', 'x']
>>> 
>>> for c in "computer":
	if c in ['u', 'i', 'x']:
		break
	print(c, end='|')

	
c|o|m|p|
>>> for c in "computer":
	if c in ['u', 'i', 'x']:
		continue
	print(c, end='|')

	
c|o|m|p|t|e|r|
>>> 
