'''
Created on Jun 20, 2018

course from: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

@author: ftd
'''
from selftest import MyDef

print('hello,world')

testType = int(input('Test type (1 - 9): '))
print(testType)

if testType == 1:
    xyz = ('E', 'T', 'RT')
    print(xyz[1])
    print(xyz[-1])
    
elif testType == 2:
    abc = ['M', 'S', 'WQ']
    for abcd in abc:
        print(abcd)
        
elif testType == 3:
    sumx = 0
    for i in range(100):
        sumx = sumx + i
    print(sumx)
    
elif testType == 4:
    dic = {111: 'FTD', 222: 'PDJ', 333: 'ZAL'}
    str1 = print('Value in dic: ' , dic.keys())
    for ii in dic.items():
        if ii[0] == 111:
            print(ii)

elif testType == 5:
    str1 = 123 # input('input a value:') 
    data = MyDef.my_abs(str1)
    print(data)
    
elif testType == 6:
    MyDef.my_keyword01('Dai', 36, 'USA', 'a', job='SE', test='aaa')
    MyDef.my_keyword02('Dai', 36, 'England', city='Qingdao', job='QA')
    
elif testType == 7:
    data = MyDef.my_fact(7)
    print(data)