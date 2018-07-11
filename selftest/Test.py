'''
Created on Jun 20, 2018

course from: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

@author: ftd
'''
from selftest import MyDef
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.javabak.Java_processor import Java_processor

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
    entityuri_start, entityuri_end, value_start, value_end= -1, -1, -1, -1
    with open('C:\\Ftd-work\\beans-app-context.xml', "r", encoding="utf-8") as f:
        for cur_line_number, line in enumerate(f):
            linecontents.append(line)
            if 'name=\"entityUriMapString\"' in line:
                entityuri_start = cur_line_number
            if 'value=' in line and entityuri_start > -1 and value_start == -1 and cur_line_number >= entityuri_start:
                value_start = cur_line_number
            if '\"/>' in line and entityuri_start > -1 and entityuri_end == -1 and cur_line_number >= entityuri_start:
                entityuri_end = cur_line_number
    
    f.close()
    
    if entityuri_start == -1 or entityuri_end == -1:
        print('The file format of beans-app-context is incorrect, cannot find \'entityUriMapString\'')
        exit()
    
    # --- the node in a single line
    if entityuri_start == entityuri_end or value_start == entityuri_end:
        idxarr = linecontents[entityuri_end].index('\"/>')
        linecontents[entityuri_end] = linecontents[entityuri_end][:idxarr].rstrip(' ') + ';'+value + linecontents[entityuri_end][idxarr:]            
    else:
        strtrim = linecontents[entityuri_end].replace('\"/>', '').replace('\t', '').replace('\n', '').strip(' ')
        # --- the end flag in a single line
        if strtrim == '':
            # --- add ';' in previous line
            idxarr = linecontents[entityuri_end-1].index('\n')
            linecontents[entityuri_end-1] = linecontents[entityuri_end-1][:idxarr].rstrip(' ') + ';\n'
            # --- clone the tab format in previous line
            tabpre = ''
            if (entityuri_end-1 != value_start):
                tabpre = linecontents[entityuri_end-1][:linecontents[entityuri_end-1].index('urn')]
            # --- insert new line
            value = tabpre + value + '\n'
            linecontents.insert(entityuri_end, value)
        else:
            idxarr = linecontents[entityuri_end].index('\"/>')
            linesuf = linecontents[entityuri_end][idxarr:]
            # --- only one uri in the last line
            if len(linecontents[entityuri_end].split(';')) == 1:
                linecontents[entityuri_end] = linecontents[entityuri_end][:idxarr].rstrip(' ') + ';\n'
                # --- clone the tab format in current line
                tabpre = linecontents[entityuri_end][:linecontents[entityuri_end].index('urn')]
                # --- insert new line
                value = tabpre + value + linesuf
                linecontents.insert(entityuri_end+1, value)
            else:
                # --- add the new uri at the end of this line
                linecontents[entityuri_end] = linecontents[entityuri_end][:idxarr].rstrip(' ') + ';'+value+ linecontents[entityuri_end][idxarr:]
    
    newfile = ''.join(linecontents)
    f = open('C:\\beans-app-context.xml', "w", encoding="utf-8")
    f.write(newfile)
    f.close()
    
    del linecontents[:]
    
    
elif testType == 9:
    Java_processor.java_3rd_tester()
    