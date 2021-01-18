Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------- LISTS
>>> 
>>> L = [12, 13.4, -34, "red", "green", "blue", True, False, [1, 2, 3]]
>>> 
>>> 
>>> L[0]
12
>>> L[1]
13.4
>>> L[-1]
[1, 2, 3]
>>> L[-1][1]
2
>>> L[3:6]
['red', 'green', 'blue']
>>> L[5]
'blue'
>>> L[5][1]
'l'
>>> L[::-1]
[[1, 2, 3], False, True, 'blue', 'green', 'red', -34, 13.4, 12]
>>> L[::2]
[12, -34, 'green', True, [1, 2, 3]]
>>> 
>>> # ???
>>> 
>>> L[4]
'green'
>>> L[4] = "yellow"
>>> L
[12, 13.4, -34, 'red', 'yellow', 'blue', True, False, [1, 2, 3]]
>>> L[3]
'red'
>>> L[3][1] = "y"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    L[3][1] = "y"
TypeError: 'str' object does not support item assignment
>>> L[-1]
[1, 2, 3]
>>> L[-1][2] = 5
>>> L
[12, 13.4, -34, 'red', 'yellow', 'blue', True, False, [1, 2, 5]]
>>> 

>>> # ------------------------------------ specific usage
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = ["black", "white", "grey"]
>>> L
['red', ['black', 'white', 'grey'], 'blue']
>>> 
>>> 
>>> 
>>> L = ["red", "green", "blue"]
>>> L1 = ["black", "white", "grey"]
>>> L[1:2]
['green']
>>> L[1:2] = L1
>>> L
['red', 'black', 'white', 'grey', 'blue']
>>> 
>>> 
>>> # ---------------------------- Operators
>>> 
>>> [1,2,3] + [3,4,5]
[1, 2, 3, 3, 4, 5]
>>> [1,2,3,4] * 3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> len(L)
5
>>> L
['red', 'black', 'white', 'grey', 'blue']
>>> "red" in L
True
>>> "cyan" in L
False
>>> del L
>>> L
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> 
>>> # ------------------------------------- Functions
>>> 
>>> L = ["red", "green", "blue"]
>>> 
>>> # ----------------- adding elements
>>> 
>>> L.append("maroon")
>>> L
['red', 'green', 'blue', 'maroon']
>>> L.append("cyan")
>>> L
['red', 'green', 'blue', 'maroon', 'cyan']
>>> L.insert(1, "yellow")
>>> L
['red', 'yellow', 'green', 'blue', 'maroon', 'cyan']
>>> L1 = ["black", "white", "grey"]
>>> L.append(L1)
>>> L
['red', 'yellow', 'green', 'blue', 'maroon', 'cyan', ['black', 'white', 'grey']]
>>> L.insert(1, L1)
>>> L
['red', ['black', 'white', 'grey'], 'yellow', 'green', 'blue', 'maroon', 'cyan', ['black', 'white', 'grey']]
>>> L = ["red", "green", "blue"]
>>> L.extend(L1)
>>> L
['red', 'green', 'blue', 'black', 'white', 'grey']
>>> L + ["maroon", "cyan"]
['red', 'green', 'blue', 'black', 'white', 'grey', 'maroon', 'cyan']
>>> L
['red', 'green', 'blue', 'black', 'white', 'grey']
>>> 
>>> 
>>> 
>>> # ------------------------ remove elements
>>> 
>>> L
['red', 'green', 'blue', 'black', 'white', 'grey']
>>> L.pop()
'grey'
>>> L
['red', 'green', 'blue', 'black', 'white']
>>> L.pop()
'white'
>>> L
['red', 'green', 'blue', 'black']
>>> L.pop(1)
'green'
>>> L
['red', 'blue', 'black']
>>> 'blue' in L
True
>>> L.remove('blue')
>>> L
['red', 'black']
>>> 
>>> # ----------------------- finding, searching, counting
>>> 
>>> 
>>> L
['red', 'black']
>>> L = ["red", "red", "green", "blue", "green", "red"]
>>> 'blue' in L
True
>>> L.index("blue")
3
>>> L[3]
'blue'
>>> L.index("red")
0
>>> L.count("red")
3
>>> L.index("black")
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    L.index("black")
ValueError: 'black' is not in list
>>> L.find("black")
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    L.find("black")
AttributeError: 'list' object has no attribute 'find'
>>> 
>>> 
>>> # --------------------------------- re-arranging elements
>>> 
>>> L = ["zebra", "banana", "cat", "ant"]
>>> sorted(L)
['ant', 'banana', 'cat', 'zebra']
>>> L
['zebra', 'banana', 'cat', 'ant']
>>> reversed(L)
<list_reverseiterator object at 0x00000209EFAC9F28>
>>> list(reversed(L))
['ant', 'cat', 'banana', 'zebra']
>>> L[::-1]
['ant', 'cat', 'banana', 'zebra']
>>> L
['zebra', 'banana', 'cat', 'ant']
>>> 
>>> 
>>> L.reverse()
>>> L
['ant', 'cat', 'banana', 'zebra']
>>> L.sort()
>>> L
['ant', 'banana', 'cat', 'zebra']
>>> 
>>> 
>>> L = [1, 3, 2, 5, 4]
>>> L.sort()
>>> L
[1, 2, 3, 4, 5]
>>> L.sort(reverse=True)
>>> L
[5, 4, 3, 2, 1]
>>> 
>>> L.sort().reverse()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    L.sort().reverse()
AttributeError: 'NoneType' object has no attribute 'reverse'
>>> L.sort()
>>> L.reverse()
>>> L
[5, 4, 3, 2, 1]
>>> 
>>> 
>>> # --------------------- iteration
>>> 
>>> L = ['red', 'green', 'blue', 'black', 'white', 'grey']
>>> 
>>> for item in L:
	print(item + ' ----> ' + str(len(item)))

	
red ----> 3
green ----> 5
blue ----> 4
black ----> 5
white ----> 5
grey ----> 4
>>> 
>>> 
>>> # -------------------------- Miscellaneous functions
>>> 
>>> 
>>> L = [1, 2, 4, 5]
>>> sum(L)
12
>>> any(L)
True
>>> all(L)
True
>>> L.append(0)
>>> L
[1, 2, 4, 5, 0]
>>> all(L)
False
>>> max(L)
5
>>> min(L)
0
>>> s = "python"
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n']
>>> 
>>> 
>>> L = [1, -2, 4, 5]
>>> all(L)
True
>>> any(L)
True
>>> L.append(0)
>>> L
[1, -2, 4, 5, 0]
>>> all(L)
False
>>> # Any non-zero is True, zero is False
>>> 
>>> # ------------------------------------------------
>>> 
>>> N = []
>>> for i in range(5):
	x = input("Enter a number: ")
	N.append(x)

	
Enter a number: 12
Enter a number: 23
Enter a number: 34
Enter a number: 45
Enter a number: 56
>>> N
['12', '23', '34', '45', '56']
>>> 
