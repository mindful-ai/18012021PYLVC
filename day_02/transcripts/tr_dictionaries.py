Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # --------------- Dictionary
>>> 
>>> D = {'name':'Anil', 'age', :35, 'company':'oracle'}
SyntaxError: invalid syntax
>>> D = {'name':'Anil', 'age' :35, 'company':'oracle'}
>>> type(D)
<class 'dict'>
>>> D['name']
'Anil'
>>> D['age']
35
>>> D['company']
'oracle'
>>> 
>>> 
>>> D['dob'] = '12-12-1999'
>>> D
{'name': 'Anil', 'age': 35, 'company': 'oracle', 'dob': '12-12-1999'}
>>> D['country']
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    D['country']
KeyError: 'country'
>>> D['country'] = 'India'
>>> D
{'name': 'Anil', 'age': 35, 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> D['age'] = 36
>>> D
{'name': 'Anil', 'age': 36, 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> D.pop('age')
36
>>> D
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> 
>>> D1 = {"addr" : "bangalore", "phone":"9817273445" }
>>> D1
{'addr': 'bangalore', 'phone': '9817273445'}
>>> D.update(D1)
>>> D
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India', 'addr': 'bangalore', 'phone': '9817273445'}
>>> 
>>> D.setdefault('hobbies', ['cricket', 'music', 'movies'])
['cricket', 'music', 'movies']
>>> D
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India', 'addr': 'bangalore', 'phone': '9817273445', 'hobbies': ['cricket', 'music', 'movies']}
>>> D['hobbies']
['cricket', 'music', 'movies']
>>> D['hobbies'][1]
'music'
>>> D['hobbies'][1] = "walking"
>>> D
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India', 'addr': 'bangalore', 'phone': '9817273445', 'hobbies': ['cricket', 'walking', 'movies']}
>>> D['health']
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    D['health']
KeyError: 'health'
>>> D.setdefault('name')
'Anil'
>>> D['health']
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    D['health']
KeyError: 'health'
>>> D.setdefault('health')
>>> D
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India', 'addr': 'bangalore', 'phone': '9817273445', 'hobbies': ['cricket', 'walking', 'movies'], 'health': None}
>>> 'name' in D
True
>>> 
>>> 
>>> # --------------------------------------
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'dob', 'country', 'addr', 'phone', 'hobbies', 'health'])
>>> D.values()
dict_values(['Anil', 'oracle', '12-12-1999', 'India', 'bangalore', '9817273445', ['cricket', 'walking', 'movies'], None])
>>> 
>>> 
>>> x = D.keys()
>>> type(x)
<class 'dict_keys'>
>>> 
>>> 
>>> D.items()
dict_items([('name', 'Anil'), ('company', 'oracle'), ('dob', '12-12-1999'), ('country', 'India'), ('addr', 'bangalore'), ('phone', '9817273445'), ('hobbies', ['cricket', 'walking', 'movies']), ('health', None)])
>>> 
>>> 
>>> x
dict_keys(['name', 'company', 'dob', 'country', 'addr', 'phone', 'hobbies', 'health'])
>>> x.append('wealth')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x.append('wealth')
AttributeError: 'dict_keys' object has no attribute 'append'
>>> 
>>> 
>>> y = D.items()
>>> type(y)
<class 'dict_items'>
>>> 
>>> 
>>> dir(y)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'isdisjoint']
>>> 
>>> 
>>> 
>>> # ------------------------- Karthika
>>> 
>>> 
>>> a = 10
>>> isinstance(a, 'int')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    isinstance(a, 'int')
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(a, int)
True
>>> isinstance(a, str)
False
>>> 
>>> 
>>> 
>>> # --------------------------------- Jayaprakash
>>> 
>>> 
>>> D
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India', 'addr': 'bangalore', 'phone': '9817273445', 'hobbies': ['cricket', 'walking', 'movies'], 'health': None}
>>> 
>>> 
>>> r1 = {'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> r2 = {'name': 'Sunil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> 
>>> 
>>> t = { 1: r1, 2: r2 }
>>> t[1]
{'name': 'Anil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> t[2]
{'name': 'Sunil', 'company': 'oracle', 'dob': '12-12-1999', 'country': 'India'}
>>> t[1]['name']
'Anil'
>>> t[1].values()
dict_values(['Anil', 'oracle', '12-12-1999', 'India'])
>>> 
