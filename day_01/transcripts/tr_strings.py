Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -------------------------------- STRINGS
>>> 
>>> s = "python"
>>> 
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[2]
't'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> s[-3]
'h'
>>> s[4]
'o'
>>> s[3]
'h'
>>> # ----------------- immutability
>>> 
>>> s[0]
'p'
>>> s[0] = "j"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[0] = "j"
TypeError: 'str' object does not support item assignment
>>> 
>>> s
'python'
>>> s = 'jython'
>>> s
'jython'
>>> 
>>> # --------------------- subscripting
>>> # [index]
>>> # [start:end]
>>> # [start:end:interval]
>>> 
>>> 
>>> s = "computer"
>>> s[0]
'c'
>>> s[2]
'm'
>>> s[-1]
'r'
>>> s[3:5]
'pu'
>>> s[3:6]
'put'
>>> s[0:3]
'com'
>>> s[:3]
'com'
>>> s[5:8]
'ter'
>>> s[5:]
'ter'
>>> s[:]
'computer'
>>> s[-5:-2]
'put'
>>> ## HRISHI
>>> s[-1:-4]
''
>>> 
>>> s[0:6]
'comput'
>>> s[0:6:2]
'cmu'
>>> s[::3]
'cpe'
>>> s[::1]
'computer'
>>> s[::-1]
'retupmoc'
>>> 
>>> 
>>> a = "madam"
>>> a == a[::-1]
True
>>> s[::-2]
'rtpo'
>>> s[3:7]
'pute'
>>> s[3:7:-1]
''
>>> s[3:7][::-1]
'etup'
>>> 
>>> s[2:-2]
'mput'
>>> s
'computer'
>>> s[-2:2]
''
>>> # Vishwanath
>>> 
>>> 
>>> # ----------------------------- operators
>>> 
>>> 
>>> "py" + "thon"
'python'
>>> 
>>> "Hi" * 5
'HiHiHiHiHi'
>>> len(s)
8
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> s = "python"
>>> "o" in s
True
>>> "A" in s
False
>>> 
>>> # ----------------------------- in built functions
>>> 
>>> # -- Case
>>> 
>>> s
'python'
>>> s.upper()
'PYTHON'
>>> s.lower()
'python'
>>> s.capitalize()
'Python'
>>> 
>>> 
>>> # --- Querying
>>> 
>>> a = '1234'
>>> a.isdigit()
True
>>> b = "123er5
SyntaxError: EOL while scanning string literal
>>> b = "123er4"
>>> b.isdigit()
False
>>> b.isalpha()
False
>>> b.isalnum()
True
>>> c = '  '
>>> c.isalnum()
False
>>> c.isspace()
True
>>> 
>>> # --------------- searching
>>> 
>>> s
'python'
>>> s.find('t')
2
>>> 'o' in s
True
>>> 
>>> s.index('t')
2
>>> s.index('a')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    s.index('a')
ValueError: substring not found
>>> s.find('a')
-1
>>> 
>>> 
>>> # ------------------------ modifying strings
>>> 
>>> ip = "192-168-1-1"
>>> ip.replace("-",".")
'192.168.1.1'
>>> ip
'192-168-1-1'
>>> 
>>> 
>>> 
>>> s = '      python   '
>>> s
'      python   '
>>> s.strip()
'python'
>>> s
'      python   '
>>> 
>>> 
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = "python"
>>> a
'python'
>>> s
'      python   '
>>> s.lstrip()
'python   '
>>> s.rstrip()
'      python'
>>> 
>>> 
>>> 
>>> 
>>> s = "python"
>>> s.ljust(20)
'python              '
>>> s.rjust(20, '>')
'>>>>>>>>>>>>>>python'
>>> s.center(20)
'       python       '
>>> 
>>> 
>>> text = "mary had a little lamb"
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text
'mary had a little lamb'
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> L = text.split('a')
>>> L
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 'A'.join(L)
'mAry hAd A little lAmb'
>>> 
>>> 
>>> #--------------------------------------------
>>> 
>>> a = "13,45,657.00 INR"
>>> a = "13,45,657.00"
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '13,45,657.00'
>>> a.replace(",","")
'1345657.00'
>>> int(a.replace(",",""))
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    int(a.replace(",",""))
ValueError: invalid literal for int() with base 10: '1345657.00'
>>> float(a.replace(",",""))
1345657.0
>>> float(a.replace(",","")) * 12 * 0.065
1049612.46
>>> 
