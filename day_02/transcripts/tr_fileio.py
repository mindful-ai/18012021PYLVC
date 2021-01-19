Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # FILE IO
>>> # open(filename/path, mode)
>>> # r -> read, w -> write, a -> write/append b -> binary
>>> # close()
>>> # read(), readline(), readlines()
>>> # write(), writelines()
>>> # seek(), tell()
>>> 
>>> f = open("C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data.txt", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> path = "c:\text\next\read\sec\data.txt"
>>> print(path)
c:	ext
extead\sec\data.txt
>>> path = r"c:\text\next\read\sec\data.txt"
>>> print(path)
c:\text\next\read\sec\data.txt
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data.txt", "r")
>>> type(f)
<class '_io.TextIOWrapper'>
>>> f.read()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    f.read()
  File "C:\Users\Purushotham\AppData\Local\Programs\Python\Python37\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 333: character maps to <undefined>
>>> f.close()
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\data.txt", "r")
>>> f.read()
"Imagine there's no heaven\nIt's easy if you try\nNo hell below us\nAbove us only sky\nImagine all the people living for today\nImagine there's no countries\nIt isn't hard to do\nNothing to kill or die for\nAnd no religion too\nImagine all the people living life in peace, you\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one\nImagine no possessions\nI wonder if you can\nNo need for greed or hunger\nA brotherhood of man\nImagine all the people sharing all the world, you\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one"
>>> print(f.read())

>>> f.tell()
652
>>> f.seek(0)
0
\
>>> print(f.read())
Imagine there's no heaven
It's easy if you try
No hell below us
Above us only sky
Imagine all the people living for today
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people living life in peace, you
You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
Imagine no possessions
I wonder if you can
No need for greed or hunger
A brotherhood of man
Imagine all the people sharing all the world, you
You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
>>> f.readline()
''
>>> f.seek(100)
100
>>> f.readline()
'e people living for today\n'
>>> f.readline()
"Imagine there's no countries\n"
>>> f.readline()
"It isn't hard to do\n"
>>> f.readlines()
['Nothing to kill or die for\n', 'And no religion too\n', 'Imagine all the people living life in peace, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one\n', 'Imagine no possessions\n', 'I wonder if you can\n', 'No need for greed or hunger\n', 'A brotherhood of man\n', 'Imagine all the people sharing all the world, you\n', "You may say I'm a dreamer\n", "But I'm not the only one\n", "I hope some day you'll join us\n", 'And the world will be as one']
>>> f.seek(0)
0
>>> content = f.read()
>>> content
"Imagine there's no heaven\nIt's easy if you try\nNo hell below us\nAbove us only sky\nImagine all the people living for today\nImagine there's no countries\nIt isn't hard to do\nNothing to kill or die for\nAnd no religion too\nImagine all the people living life in peace, you\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one\nImagine no possessions\nI wonder if you can\nNo need for greed or hunger\nA brotherhood of man\nImagine all the people sharing all the world, you\nYou may say I'm a dreamer\nBut I'm not the only one\nI hope some day you'll join us\nAnd the world will be as one"
>>> f.close()
>>> 
>>> 
>>> 
>>> # ---------------------------- Writing to a file
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\histogram.txt", "w")
>>> f.write("HISTOGRAM for IMAGINE\n\n")
23
>>> f.close()


>>> for word in set(words):
	print(word, ' --> ', words.count(word))

	
not  -->  2
only  -->  3
It  -->  1
in  -->  1
world  -->  2
countries  -->  1
you'll  -->  2
people  -->  3
say  -->  2
try  -->  1
if  -->  2
sky  -->  1
hell  -->  1
do  -->  1
Nothing  -->  1
And  -->  3
of  -->  1
today  -->  1
or  -->  2
possessions  -->  1
join  -->  2
Imagine  -->  6
wonder  -->  1
will  -->  2
need  -->  1
you  -->  4
heaven  -->  1
sharing  -->  1
the  -->  8
easy  -->  1
for  -->  3
world,  -->  1
all  -->  4
I'm  -->  4
I  -->  3
You  -->  2
brotherhood  -->  1
hope  -->  2
living  -->  2
as  -->  2
die  -->  1
too  -->  1
life  -->  1
some  -->  2
religion  -->  1
A  -->  1
Above  -->  1
day  -->  2
one  -->  4
hunger  -->  1
But  -->  2
peace,  -->  1
kill  -->  1
No  -->  2
a  -->  2
dreamer  -->  2
may  -->  2
man  -->  1
there's  -->  2
below  -->  1
can  -->  1
greed  -->  1
no  -->  4
It's  -->  1
hard  -->  1
isn't  -->  1
be  -->  2
to  -->  2
us  -->  4
>>> 
>>> 
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\histogram.txt", "a")
>>> for word in set(words):
	f.write(str(word) + ' --> ' + str(words.count(word)) + "\n")

	
10
11
9
9
12
16
13
13
10
10
9
10
11
9
14
10
9
12
9
18
11
14
13
11
11
10
13
14
10
11
10
13
10
10
8
10
18
11
13
9
10
10
11
11
15
8
12
10
10
13
10
13
11
9
8
14
10
10
14
12
10
12
9
11
11
12
9
9
9
>>> f.close()
>>>

>>> f.close()
>>> f = open(r"C:\Users\Purushotham\Desktop\oracle\day_02\livedemo\histogram.txt", "a")
>>> f.writelines(["\n\n", "---------------------\n", "Thankyou!"])
>>> f.close()

