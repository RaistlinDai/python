'''
Created on Jul 14, 2019

@author: ftd
'''

class IDatabase_driver(object):
    '''
    classdocs
    '''
    
    def __init__(self, connection_param=None):
        print('IDATABASE_DRIVER')
        self.__database_driver = self.setup_connection(connection_param)
    
    
    def set_database_driver(self, db_driver):
        self.__database_driver = db_driver
        
        
    def get_database_driver(self):
        return self.__database_driver
    
    
    def setup_connection(self, connection_param=None):
        pass
        
    
    def get_database_list(self):
        pass
