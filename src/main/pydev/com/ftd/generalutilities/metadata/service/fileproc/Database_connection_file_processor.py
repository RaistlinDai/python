'''
Created on Jul 11, 2019

@author: ftd
'''
from pathlib import Path

class Database_connection_file_processor(object):
    
    @staticmethod
    def create_connection_file(file_name, connection_params):
        '''
        create the default file
        @param file_name: the connection file full path
        @param connection_params: the new connection parameters (name:host=xxx,port=xxx,username=xxx,password=xxx)
        '''
        Path(file_name).touch()
        file = open(file_name, 'w')
        file.write(connection_params + '\n')
        file.close()
        
    
    @staticmethod
    def update_connection_file(file_name, connection_name, connection_params):
        '''
        update the connection file
        @param file_name: the connection file full path
        @param connection_name: the connection name
        @param connection_params: the connection parameters (name:host=xxx,port=xxx,username=xxx,password=xxx)
        '''
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        idx = 0
        isExisting = False
        for line in lines:
            if str.startswith(line, connection_name + ':'):
                #new value
                line = connection_params + '\n'
                lines[idx] = line
                isExisting = True
                break
            idx = idx + 1
            
        if not isExisting:
            line = connection_params + '\n'
            lines.append(line)
        
        with open(file_name, 'w') as newfile:
            newfile.writelines(lines)
                
        file.close()
        newfile.close()
        
    
    @staticmethod
    def verify_connection_name_exist(file_name, connection_name):
        '''
        verify if the connection name is saved in connection file
        @param file_name: the connection file full path
        @param connection_name: the connection name
        '''
        with open(file_name, 'r') as file:
            lines = file.readlines()
        
        idx = 0
        isExisting = False
        for line in lines:
            if str.startswith(line, connection_name + ':'):
                isExisting = True
                break
            idx = idx + 1

        file.close()
        
        return isExisting
    
    
    @staticmethod
    def read_connection_names(file_name):
        '''
        read the connection names
        @param file_name: the connection file full path
        @return: the default info
        '''
        names = []
        file = open(file_name, 'r')
        for eachline in file.readlines():
            if ':' in eachline:
                names.append(eachline[:eachline.index(':')])    
                
        file.close()
        return names
    
     
    @staticmethod
    def read_connection_params(file_name, connection_name):
        '''
        read the connection file
        @param file_name: the connection file full path
        @return: the default info
        '''
        info = {}
        file = open(file_name, 'r')
        for eachline in file.readlines():
            if str.startswith(eachline, connection_name + ':'):
                templine = eachline.replace('\n', '')[eachline.index(':')+1:]
                cells = templine.split(',')
                for eachcell in cells:
                    if str.startswith(eachcell, 'host='):
                        info['host'] = eachcell[eachcell.index('=')+1:]
                    elif str.startswith(eachcell, 'port='):
                        info['port'] = eachcell[eachcell.index('=')+1:]
                    elif str.startswith(eachcell, 'username='):
                        info['username'] = eachcell[eachcell.index('=')+1:]
                    elif str.startswith(eachcell, 'password='):
                        info['password'] = eachcell[eachcell.index('=')+1:]
                    
                break
            
        file.close()
        return info
    