'''
Created on Jul 23, 2018

@author: ftd
'''
from pathlib import Path

class User_default_file_processor(object):
    
    @staticmethod
    def create_default_file(filename):
        '''
        create the default file
        @param filename: the default file full path
        '''
        Path(filename).touch()
        file = open(filename, 'w')
        file.write('workspace=\n')
        file.write('project=\n')
        file.close()
        
    
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
    
    
    @staticmethod
    def update_default_file(filename, prop_name, prop_value):
        '''
        update the default file
        @param filename: the default file full path
        @param prop_name: the property name
        @param prop_value: the property value
        '''
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        idx = 0
        for line in lines:
            if (prop_name + '=') in line:
                #new value
                line = prop_name + '=' + prop_value + '\n'
                lines[idx] = line
                break
            idx = idx + 1
        
        with open(filename, 'w') as newfile:
            newfile.writelines(lines)
                
        file.close()
        newfile.close()