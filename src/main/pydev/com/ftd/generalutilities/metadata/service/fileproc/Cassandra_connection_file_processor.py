'''
Created on Jul 11, 2019

@author: ftd
'''
from pathlib import Path

class Cassandra_connection_file_processor(object):
    
    @staticmethod
    def create_connection_file(filename, connection):
        '''
        create the default file
        @param filename: the connection file full path
        @param connection: the new connection parameters (name:host=xxx,port=xxx,username=xxx,password=xxx)
        '''
        Path(filename).touch()
        file = open(filename, 'w')
        file.write(connection + '\n')
        file.close()
        
    
    @staticmethod
    def update_default_file(filename, connection_name, connection_params):
        '''
        update the connection file
        @param filename: the connection file full path
        @param connection_name: the connection name
        @param connection_params: the connection parameters (host=xxx,port=xxx,username=xxx,password=xxx)
        '''
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        idx = 0
        isExisting = False
        for line in lines:
            if (connection_name + ':') in line:
                #new value
                line = connection_name + ':' + connection_params + '\n'
                lines[idx] = line
                isExisting = True
                break
            idx = idx + 1
            
        if not isExisting:
            line = connection_name + ':' + connection_params + '\n'
            lines.append(line)
        
        with open(filename, 'w') as newfile:
            newfile.writelines(lines)
                
        file.close()
        newfile.close()
        
        
    @staticmethod
    def read_default_file(filename):
        '''
        read the default file
        @param filename: the default file full path
        @return: the default info
        '''
        info = {}
        file = open(filename, 'r')
        for eachline in file.readlines():
            if 'workspace=' in eachline:
                info['workspace'] = eachline.replace('\n', '')[eachline.index('=')+1:]
            if 'project=' in eachline:
                info['project'] = eachline.replace('\n', '')[eachline.index('=')+1:]
        
        file.close()
        return info
    