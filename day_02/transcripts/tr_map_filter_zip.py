Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def c2f(t):
	return t * 1.8 + 32

>>> c2f(100)
212.0
>>> 
>>> T = [100, 99, 43, 67, 0]
>>> F = []
>>> for t in T:
	F.append(c2f(t))

	
>>> F
[212.0, 210.20000000000002, 109.4, 152.60000000000002, 32.0]
>>> 
>>> F1 = map(c2f, T)
>>> F1
<map object at 0x000001C26BA2CD30>
>>> list(F1)
[212.0, 210.20000000000002, 109.4, 152.60000000000002, 32.0]
>>> 
>>> F1
<map object at 0x000001C26BA2CD30>
>>> print(F1)
<map object at 0x000001C26BA2CD30>
>>> list(F1)
[]
>>> F1 = map(c2f, T)
>>> F1
<map object at 0x000001C26B9C5780>
>>> for t in F1:
	print(t)

	
212.0
210.20000000000002
109.4
152.60000000000002
32.0
>>> 
>>> 
>>> # -------------------------------------------
>>> 
>>> 
>>> 
>>> N = list(range(1, 100))
>>> N
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> X = []
>>> for n in N:
	if(n % 3 == 0):
		X.append(n)

		
>>> X
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> 
>>> def div3(n):
	if(n % 3 == 0):
		return True
	else:
		return False

	
>>> F1 = filter(div3, N)
>>> F1
<filter object at 0x000001C26BA42CF8>
>>> list(F1)
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> 
>>> 
>>> # -----------------------------------------------------
>>> 
>>> 
>>> t1 = ("Anil", "Raj", "Ram")
>>> t2 = ("Bangalore", "Hyderabad", "Chennai")
>>> zip(t1, t2)
<zip object at 0x000001C26B79FE88>
>>> list(zip(t1, t2))
[('Anil', 'Bangalore'), ('Raj', 'Hyderabad'), ('Ram', 'Chennai')]
>>> 
>>> dict(zip(t1, t2))
{'Anil': 'Bangalore', 'Raj': 'Hyderabad', 'Ram': 'Chennai'}
>>> t1 = ("Anil", "Raj", "Ram", "Sunil")
>>> list(zip(t1, t2))
[('Anil', 'Bangalore'), ('Raj', 'Hyderabad'), ('Ram', 'Chennai')]
>>> dict(zip(t1, t2))
{'Anil': 'Bangalore', 'Raj': 'Hyderabad', 'Ram': 'Chennai'}
>>> 
