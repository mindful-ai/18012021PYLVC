Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input()
mobile
'mobile'
>>> s = input()
mobile
>>> s
'mobile'
>>> s
'mobile'
>>> s
'mobile'
>>> s.upper()
'MOBILE'
>>> s = input("Enter your name: ")
Enter your name: Purushotham
>>> s
'Purushotham'
>>> type(s)
<class 'str'>
>>> s = input("Enter your age: ")
Enter your age: 36
>>> type(s)
<class 'str'>
>>> s
'36'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
46
>>> print("My age is: ", age)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print("My age is: ", age)
NameError: name 'age' is not defined
>>> print("My age is: ", s)
My age is:  36
>>> type(s)
<class 'str'>
>>> p = int(S)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    p = int(S)
NameError: name 'S' is not defined
>>> p = int(s)
>>> type(p)
<class 'int'>
>>> 
