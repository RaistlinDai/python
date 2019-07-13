'''
Created on 2018/12/24

@author: ftd
'''
import pymongo

class Mongodb_driver(object):
    '''
    class doc
    '''
    
    def __init__(self, connection_param):
        self.__mongodb_client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.__mongodb_database_connector = None
    
    
    def get_database_list(self):
        '''
        get the mongodb database list
        '''
        return self.__mongodb_client.list_database_names()
    
    
    def connect_database_by_name(self, db_name):
        '''
        get the mongodb database by name
        @param db_name: mongodb database name
        '''
        dblist = self.__mongodb_client.list_database_names()
        if db_name in dblist:
            self.__mongodb_database_connector = self.__mongodb_client[db_name]
            return True, None
        else:
            message = f"database %s is not existing{db_name}!"
            print(message)
            return False, message
            
    
    @staticmethod
    def create_collection(db_object, collection_name):
        if not db_object:
            return None
        else:
            collist = db_object.list_collection_names()
            if collection_name in collist:
                print("collection %s is existing" % collection_name)
                return db_object[collection_name]
            else:
                print("collection %s is not existing" % collection_name)
                new_collection = db_object.create_collection(collection_name)
                return new_collection
            

    @staticmethod
    def create_document(col_object, docs):
        if not col_object:
            return False
        else:
            if isinstance(docs, list):
                col_object.insert_many(docs)
                return None
            elif isinstance(docs, dict):
                col_object.insert_one(docs)
            else:
                return False
        
        return True
        