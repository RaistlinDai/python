'''
Created on Jul 13, 2019

@author: ftd
'''
import pymongo
from src.main.pydev.com.ftd.generalutilities.metadata.service.database.api.IDatabase_driver import IDatabase_driver
from urllib.parse import quote_plus

class Mongodb_driver(IDatabase_driver):
    '''
    class doc
    '''
    
    def __init__(self, connection_param=None):
        '''
        Constructor
        '''
        IDatabase_driver.__init__(self, connection_param)
        self.__database_parameters = connection_param
        self.__client = None
        self.__database_list = {}  # {A:{xxx}, B:{yyy}}
    
    
    # overwrite super class
    def active_connection(self):
        '''
        Active the Mongodb connection
        '''
        # Mongodb cluster IP
        self.__contact_points = self.__database_parameters.get_contact_points()
        # Mongodb port
        self.__port = self.__database_parameters.get_port()
        self.__username = self.__database_parameters.get_username()
        self.__password = self.__database_parameters.get_password()
        
        maxSevSelDelay = 1
        self.__client = pymongo.MongoClient("mongodb://%s:%s@%s:%s" % (quote_plus(self.__username), \
                                                                       quote_plus(self.__password), \
                                                                       quote_plus(self.__contact_points), \
                                                                       quote_plus(self.__port)), \
                                            serverSelectionTimeoutMS=maxSevSelDelay)
    
    
    def shutdown_connection(self):
        '''
        Shutdown the Mongodb connection
        '''
        # Shutdown the connection
        self.__client.close()
        
        
    def test_connection(self):
        '''
        Test the Mongodb connection
        '''        
        # Mongodb cluster IP
        self.__contact_points = self.__database_parameters.get_contact_points()
        # Mongodb port
        self.__port = self.__database_parameters.get_port()
        self.__username = None
        self.__password = None
        
        maxSevSelDelay = 3
        self.__client = pymongo.MongoClient('mongodb://%s:%s/' % (self.__contact_points,self.__port), \
                                            serverSelectionTimeoutMS=maxSevSelDelay)
        
        self.__client.server_info()
        
        # Shutdown the connection
        self.__client.close()
        
    
    # overwrite super class
    def get_database_list(self):
        '''
        get the mongodb database list
        '''
        db_list = []
        # Create Mongodb client
        self.active_connection()
        db_list = self.__client.list_database_names()
        self.shutdown_connection()
        
        return db_list
    
    
    # overwrite super class
    def get_table_list(self, database_name):
        '''
        get the mongodb table by database name
        @param database_name: database name
        '''
        return []
    
    
    # overwrite super class
    def get_records(self, database_name, table_name):
        '''
        get the records by table name
        '''
        return []
        