'''
Created on Jul 5, 2018

@author: ftd
'''

class TransactionDTO(object):
    '''
    classdocs
    '''


    def __init__(self, process_flow=None, proj_path=None):
        '''
        Constructor
        '''
        self.__dto = {'ProcessFlow':process_flow,
                      'ProjectPath':proj_path}
        
        
    def set_dtos(self, dtos):
        self.__dto = dtos
        
        
    def get_dtos(self):
        return self.__dto
    
    
    def set_processflow(self, processflow):
        if self.__dto:
            self.__dto['ProcessFlow'] = processflow
            
            
    def get_processflow(self):
        if self.__dto:
            return self.__dto['ProcessFlow']
        else:
            return None
        
        
    def set_projectpath(self, projpath):
        if self.__dto:
            self.__dto['ProjectPath'] = projpath
            
            
    def get_projectpath(self):
        if self.__dto:
            return self.__dto['ProjectPath']
        else:
            return None