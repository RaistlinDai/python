'''
Created on Jul 10, 2018

@author: ftd
'''

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from src.main.pydev.com.ftd.generalutilities.metadata.dto.database.Database_parameters import Database_parameters
from src.main.pydev.com.ftd.generalutilities.metadata.service.database.api.IDatabase_driver import IDatabase_driver

class Cassandra_driver(IDatabase_driver):
    '''
    classdocs
    '''

    def __init__(self, connection_param):
        '''
        Constructor
        '''
        IDatabase_driver.__init__(self, connection_param)
        self.__database_parameters = connection_param
        self.__cluster = None
        self.__database_list = {}  # {A:{xxx}, B:{yyy}}
        
    
    def active_connection(self):
        '''
        Active the Cassandra connection
        '''
        portItr = int(self.__database_parameters.get_port())
        
        # Cassandra cluster IP
        self.__contact_points = [self.__database_parameters.get_contact_points()]
        # Cassandra port
        self.__port = portItr
        # Cassandra username and password
        self.__auth_provider = PlainTextAuthProvider(username=self.__database_parameters.get_username(), \
                                                     password=self.__database_parameters.get_password())
        
        # Create Cassandra cluster
        self.__cluster = Cluster(contact_points=self.__contact_points, port=self.__port, auth_provider=self.__auth_provider)
    
    
    def shutdown_connection(self):
        '''
        Shutdown the Cassandra connection
        '''
        # Shutdown the connection
        self.__cluster.shutdown()
        
    
    def test_connection(self):
        '''
        Test the Cassandra connection
        '''
        portItr = int(self.__database_parameters.get_port())
        
        # Cassandra cluster IP
        self.__contact_points = [self.__database_parameters.get_contact_points()]
        # Cassandra port
        self.__port = portItr
        # Cassandra username and password
        self.__auth_provider = PlainTextAuthProvider(username=self.__database_parameters.get_username(), \
                                                     password=self.__database_parameters.get_password())
        
        test_result = False
        # Create Cassandra cluster
        temp_cluster = Cluster(contact_points=self.__contact_points, port=self.__port, auth_provider=self.__auth_provider)
        session = temp_cluster.connect(wait_for_all_pools=True)
        if not session.is_shutdown:
            test_result = True
        # Shutdown the connection
        temp_cluster.shutdown()
        
        return test_result
    
    
    # overwrite super class
    def get_database_list(self):
        '''
        get the cassandra keyspace list
        '''
        keyspaces = []
        # Create Cassandra cluster
        self.active_connection()
        self.__cluster.connect(wait_for_all_pools=True)
        keyspace_items = self.__cluster.metadata.keyspaces
        
        for db_item in keyspace_items.items():
            tables = []
            table_items = self.__cluster.metadata.keyspaces[db_item[0]].tables
            for tb_item in table_items.items():
                tables.append(tb_item[0])
            
            self.__database_list[db_item[0]] = tables
        
        self.__cluster.shutdown()
        
        for db_item in self.__database_list.keys():
            keyspaces.append(db_item)
        
        return keyspaces
    
    
    def get_table_list(self, database_name):
        '''
        get the cassandra table by keyspace name
        @param database_name: keyspace name
        '''
        if not self.__database_list[database_name]:
            self.get_database_list()
            
        return self.__database_list[database_name]
    
    
    def get_records(self, database_name, table_name):
        '''
        get the records by table name
        '''
        # Create Cassandra cluster
        self.active_connection()
        session = self.__cluster.connect(database_name, wait_for_all_pools=True)
        query = 'SELECT * FROM %s' % table_name
        print(query)
        result = session.execute(query)
        
        self.__cluster.shutdown()
        return result.column_names, result.column_types, result.current_rows
    
    
    
        