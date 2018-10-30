'''
Created on Oct 30, 2018

@author: ftd
'''

class TSDtoDTO(object):
    
    def __init__(self, fin_api_ver=None):
        '''
        Constructor
        '''
        self.__filename = None
        self.__dsname = None
        self.__fullpath = None
        self.__maintable = None


    def get_filename(self):
        return self.__filename


    def get_dsname(self):
        return self.__dsname


    def get_fullpath(self):
        return self.__fullpath


    def get_maintable(self):
        return self.__maintable


    def set_filename(self, value):
        self.__filename = value


    def set_dsname(self, value):
        self.__dsname = value


    def set_fullpath(self, value):
        self.__fullpath = value


    def set_maintable(self, value):
        self.__maintable = value


    def del_filename(self):
        del self.__filename


    def del_dsname(self):
        del self.__dsname


    def del_fullpath(self):
        del self.__fullpath


    def del_maintable(self):
        del self.__maintable
        

    filename = property(get_filename, set_filename, del_filename, "filename's docstring")
    dsname = property(get_dsname, set_dsname, del_dsname, "dsname's docstring")
    fullpath = property(get_fullpath, set_fullpath, del_fullpath, "fullpath's docstring")
    tables = property(get_maintable, set_maintable, del_maintable, "maintable's docstring")
        

class TSDtoTable(object):
    
    def __init__(self, fin_api_ver=None):
        '''
        Constructor
        '''
        self.__tablename = None
        self.__subtables = []
        
    
    def get_tablename(self):
        return self.__tablename


    def set_tablename(self, value):
        self.__tablename = value
        
        
    def push_subtable(self, value):
        self.__subtables.append(value)
        
    
    def get_subtables(self):
        return self.__subtables