'''
Created on Jul 4, 2018

@author: ftd
'''

class ResourceMetadataDTO(object):
    '''
    classdocs
    '''

    def __init__(self, meta_uri=None, view_uri=None, name_string=None, 
                is_eligible=None, is_secure=None, primary_secure_Uri=None):
        '''
        Constructor
        '''
        self.__meta_uri = meta_uri
        self.__view_uri = view_uri
        self.__name_string = name_string
        self.__is_eligible = is_eligible
        self.__is_secure = is_secure
        self.__primary_secure_Uri = primary_secure_Uri
    

    def get_meta_uri(self):
        return self.__meta_uri


    def get_view_uri(self):
        return self.__view_uri


    def get_name_string(self):
        return self.__name_string


    def get_is_eligible(self):
        return self.__is_eligible


    def get_is_secure(self):
        return self.__is_secure


    def get_primary_secure_uri(self):
        return self.__primary_secure_Uri


    def set_meta_uri(self, value):
        self.__meta_uri = value


    def set_view_uri(self, value):
        self.__view_uri = value


    def set_name_string(self, value):
        self.__name_string = value


    def set_is_eligible(self, value):
        self.__is_eligible = value


    def set_is_secure(self, value):
        self.__is_secure = value


    def set_primary_secure_uri(self, value):
        self.__primary_secure_Uri = value


    def del_meta_uri(self):
        del self.__meta_uri


    def del_view_uri(self):
        del self.__view_uri


    def del_name_string(self):
        del self.__name_string


    def del_is_eligible(self):
        del self.__is_eligible


    def del_is_secure(self):
        del self.__is_secure


    def del_primary_secure_uri(self):
        del self.__primary_secure_Uri

    meta_uri = property(get_meta_uri, set_meta_uri, del_meta_uri, "meta_uri's docstring")
    view_uri = property(get_view_uri, set_view_uri, del_view_uri, "view_uri's docstring")
    name_string = property(get_name_string, set_name_string, del_name_string, "name_string's docstring")
    is_eligible = property(get_is_eligible, set_is_eligible, del_is_eligible, "is_eligible's docstring")
    is_secure = property(get_is_secure, set_is_secure, del_is_secure, "is_secure's docstring")
    primary_secure_Uri = property(get_primary_secure_uri, set_primary_secure_uri, del_primary_secure_uri, "primary_secure_Uri's docstring")

    
    def update_header(self, meta_uri=None, view_uri=None, name_string=None, 
                      is_eligible=None, is_secure=None, primary_secure_Uri=None):
        '''
        Constructor
        '''
        self.__meta_uri = meta_uri
        self.__view_uri = view_uri
        self.__name_string = name_string
        self.__is_eligible = is_eligible
        self.__is_secure = is_secure
        self.__primary_secure_Uri = primary_secure_Uri