'''
Created on Jul 14, 2019

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.database.Database_parameters import Database_parameters

class IDatabase_driver(object):
    '''
    classdocs
    '''
    
    def __init__(self, connection_param=None):
        self.verify_database_parameters(connection_param)
    
    
    def verify_database_parameters(self, params):
        if not isinstance(params, Database_parameters):
            raise TypeError('Incorrect connection parameters!')

        
    def active_connection(self):
        pass
    
    
    def shutdown_connection(self):
        pass
    
    
    def test_connection(self):
        pass
    
    
    def get_database_list(self):
        pass
    
    
    