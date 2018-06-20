'''
Created on Jun 20, 2018

@author: ftd
'''
from builtins import range

def my_slice():
    sl = list(range(100))
    s2 = tuple(range(20))
    s3 = 'ABCDEFGHIJKLMN'
    print(sl[12:17]) #from 12 to 17 in list
    print(sl[::10]) #each 10 record
    print(sl[20:50:5]) #each 5 record from 20 to 50
    print(s2[5:9]) #from 5 to 9 in tuple
    print(s3[3:8]) #from 3 to 8 in string
    print(s3[::3]) #each 3 record in string
    

    
my_slice()