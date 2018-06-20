'''
Created on Jun 20, 2018

@author: ftd
'''
import MyDef

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
    str1 = 'Value in dic: ' , dic.keys()
    inputKey = int(input(str1))
    if inputKey in dic:
        print(dic[inputKey])

elif testType == 5:
    str1 = 123 # input('input a value:') 
    data = MyDef.my_abs(str1)
    print(data)
    
