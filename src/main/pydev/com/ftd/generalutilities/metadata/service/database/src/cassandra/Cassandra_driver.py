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
        self.__is_connected = False
        
    
    # overwrite super class
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
        
        try:
            # Create Cassandra cluster
            self.__cluster = Cluster(contact_points=self.__contact_points, port=self.__port, auth_provider=self.__auth_provider)
        except Exception as e:
            raise e
        
        self.__is_connected = True
    
    
    # overwrite super class
    def shutdown_connection(self):
        '''
        Shutdown the Cassandra connection
        '''
        # Shutdown the connection
        self.__cluster.shutdown()
        
    
    # overwrite super class
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
        
        try:
            # Create Cassandra cluster
            if not self.__is_connected:
                self.active_connection()
                
            self.__cluster.connect(wait_for_all_pools=True)
            keyspace_items = self.__cluster.metadata.keyspaces
            
            for db_item in keyspace_items.items():
                tables = []
                table_items = self.__cluster.metadata.keyspaces[db_item[0]].tables
                for tb_item in table_items.items():
                    tables.append(tb_item[0])
                
                self.__database_list[db_item[0]] = tables
            
            for db_item in self.__database_list.keys():
                keyspaces.append(db_item)
                
        except Exception as e:
            raise e
        
        return keyspaces
    
    
    # overwrite super class
    def get_table_list(self, database_name):
        '''
        get the cassandra table by keyspace name
        @param database_name: keyspace name
        '''
        if not self.__database_list[database_name]:
            self.get_database_list()
            
        return self.__database_list[database_name]
    
    
    # overwrite super class
    def get_records(self, database_name, table_name):
        '''
        get the records by table name
        '''
        column_names = []
        column_types = []
        analysis_rows = []
        
        # Create Cassandra cluster
        try:
            self.active_connection()
            session = self.__cluster.connect(database_name, wait_for_all_pools=True)
            query = 'SELECT * FROM %s LIMIT 50' % table_name
            print(query)
            
            result = session.execute(query)
            column_names = result.column_names
            column_types = result.column_types
            
            # analysis records
            analysis_rows = []
            if len(result.column_names) > 0 and len(result.current_rows) > 0:
                for i in range(0, len(result.current_rows)):
                    temp_row = result.current_rows[i]
                    analysis_row = []
                    for j in range(0, len(result.column_names)):
                        analysis_row.append(temp_row[j])
                    analysis_rows.append(analysis_row)
        except Exception as e:
            raise e
        
        return column_names, column_types, analysis_rows
    
    