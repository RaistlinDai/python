'''
Created on Jun 20, 2018

course from: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

@author: ftd
'''
from selftest import MyDef
import xml.dom.minidom

print('hello,world')

testType = int(input('Test type (1 - 9): '))

if testType == 1:
    xyz = ('E', 'T', 'RT')
    print(xyz[1])
    print(xyz[-1])
    
elif testType == 2:
    abc = ['M', 'S', 'WQ']
    print(abc.index('S'))
    print(len(abc))
        
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
    
elif testType == 8:
    value = 'xxxxx'
    linecontents = []
    with open('C:\\beans-app-context.xml', "r", encoding="utf-8") as f:
        entityuri_start, entityuri_end = -1, -1
        for cur_line_number, line in enumerate(f):
            linecontents.append(line)
            if 'name=\"entityUriMapString\"' in line: 
                entityuri_start = cur_line_number
            elif '/>' in line and entityuri_start > -1 and entityuri_end == -1 and cur_line_number >= entityuri_start:
                entityuri_end = cur_line_number
    
    f.close()
    print(str(entityuri_start) + ',' + str(entityuri_end))
    
    # --- the node in a single line
    if entityuri_start == entityuri_end:
        
        print(linecontents[entityuri_end])
    else:
        print(linecontents[entityuri_end])
        strtrim = linecontents[entityuri_end].replace('/>', '').replace('\t', '').replace('\n', '').rstrip(' ')
        if strtrim == '' or strtrim == '\"':
            linecontents.insert(entityuri_end, value+'\n')
        else:
            linecontents[entityuri_end] = linecontents[entityuri_end].replace('\"', ';'+value+'\"')
            print(linecontents[entityuri_end])
    
    newfile = ''.join(linecontents)
    f = open('C:\\beans-app-context.xml', "w", encoding="utf-8")
    f.write(newfile)
    f.close()
    
    del linecontents[:] 
    