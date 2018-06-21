'''
Created on Jun 20, 2018

@author: ftd
'''
from builtins import range
from _collections_abc import Iterable
import os 
import MyDef

def my_slice():
    sl = list(range(50, 100))
    s2 = tuple(range(20))
    s3 = 'ABCDEFGHIJKLMN'
    print(sl[12:17]) #from 12 to 17 in list
    print(sl[::10]) #each 10 record
    print(sl[20:50:5]) #each 5 record from 20 to 50
    print(s2[5:9]) #from 5 to 9 in tuple
    print(s3[3:8]) #from 3 to 8 in string
    print(s3[::3]) #each 3 record in string
    
def my_interator():
    s1 = {'a':'ftd', 'b':'pdj', 'c':'zal', 'd':'ynh'} #iterator for dict
    if isinstance(s1, Iterable):
        for sx1 in s1: #loop the keys
            print(sx1)
        for sx2 in s1.values(): #loop the values
            print(sx2)
        for sx3 in s1.items():
            print(sx3)
        for i, x in enumerate(s1): #loop with subscript
            print(i, x)

def my_listComp():
    l1 = [n*5 for n in range(11)] #list generate comprehension
    print(l1)
    
    l2 = [n*n for n in range(1, 10) if n % 2 == 0]
    print(l2)
    
    l3 = [n+m for n in 'ABCD' for m in 'XYZ']
    print(l3)
    
    l4 = [d for d in os.listdir('.')] #list all the files in current folder
    print(l4)
    
    s1 = {'a':'ftd', 'b':'pdj', 'c':'zal', 'd':'ynh'} 
    l5 = [n + '=' + m for n, m in s1.items()]
    print(l5)

def my_generator():
    l1 = [n*5 for n in range(11)]
    print(l1)
    
    l2 = (n*5 for n in range(11))
    for n in l2:
        print(n)











#Main block
tp = int(input('Test type (1 - 9): '))
print(tp)

if tp == 1:
    my_slice()
elif tp == 2:
    my_interator()
elif tp == 3:
    my_listComp()
elif tp == 4:
    my_generator()
elif tp == 5:
    fir = int(input('Fibonacci start from: '))
    maxC = int(input('Fibonacci loop for: '))
    result = MyDef.my_Fibonacci(fir = fir, maxC = maxC)
    while True:
        try:
            x = next(result)
            print(x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break

