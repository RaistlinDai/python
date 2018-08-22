'''
Created on Jul 4, 2018

@author: ftd
'''

class ResourceMetadataDTO(object):
    '''
    classdocs
    '''

    def __init__(self, 
                 meta_uri=None, 
                 view_uri=None, 
                 name_string=None, 
                 is_eligible=None, 
                 is_secure=None, 
                 primary_secure_Uri=None,
                 entity_type=None
                 ):
        '''
        Constructor
        '''
        self.__meta_uri = meta_uri
        self.__view_uri = view_uri
        self.__name_string = name_string
        self.__is_eligible = is_eligible
        self.__is_secure = is_secure
        self.__primary_secure_Uri = primary_secure_Uri
        self.__entity_type = entity_type
        
        self.__viewParameters = None
        
        self.ENTITY_TYPE_BE = "urn:be:"
        self.ENTITY_TYPE_SERVICE = "urn:service:"


    def get_view_parameters(self):
        return self.__viewParameters


    def set_view_parameters(self, value):
        if isinstance(value, ViewParametersDTO):
            self.__viewParameters = value


    def del_view_parameters(self):
        del self.__viewParameters


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


    def get_entity_type(self):
        return self.__entity_type


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


    def set_entity_type(self, value):
        self.__entity_type = value


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
                      is_eligible=None, is_secure=None, primary_secure_Uri=None,
                      entity_type=None):
        '''
        Constructor
        '''
        self.__meta_uri = meta_uri
        self.__view_uri = view_uri
        self.__name_string = name_string
        self.__is_eligible = is_eligible
        self.__is_secure = is_secure
        self.__primary_secure_Uri = primary_secure_Uri
        self.__entity_type = entity_type
    viewParameters = property(get_view_parameters, set_view_parameters, del_view_parameters, "viewParameters's docstring")
        
        
        
class ViewParametersDTO(object):
    '''
    classdocs
    '''

    def __init__(self, 
                 entityModule=None, 
                 storedViewKey=None, 
                 usesDomain=None, 
                 resourceUrlPrefix=None, 
                 dataResource=None, 
                 table=None,
                 keyFields=[]
                 ):
        self.__entityModule=entityModule, 
        self.__storedViewKey=storedViewKey, 
        self.__usesDomain=usesDomain, 
        self.__resourceUrlPrefix=resourceUrlPrefix, 
        self.__dataResource=dataResource, 
        self.__table=table,
        self.__keyFields=keyFields
        

    def get_entity_module(self):
        return self.__entityModule


    def get_stored_view_key(self):
        return self.__storedViewKey


    def get_uses_domain(self):
        return self.__usesDomain


    def get_resource_url_prefix(self):
        return self.__resourceUrlPrefix


    def get_data_resource(self):
        return self.__dataResource


    def get_table(self):
        return self.__table


    def get_key_fields(self):
        return self.__keyFields


    def set_entity_module(self, value):
        self.__entityModule = value


    def set_stored_view_key(self, value):
        self.__storedViewKey = value


    def set_uses_domain(self, value):
        self.__usesDomain = value


    def set_resource_url_prefix(self, value):
        self.__resourceUrlPrefix = value


    def set_data_resource(self, value):
        self.__dataResource = value


    def set_table(self, value):
        self.__table = value


    def set_key_fields(self, value):
        self.__keyFields = value
        
    
    def push_key_field(self, value):
        if isinstance(value, KeyField):
            self.__keyFields.append(value)


    def del_entity_module(self):
        del self.__entityModule


    def del_stored_view_key(self):
        del self.__storedViewKey


    def del_uses_domain(self):
        del self.__usesDomain


    def del_resource_url_prefix(self):
        del self.__resourceUrlPrefix


    def del_data_resource(self):
        del self.__dataResource


    def del_table(self):
        del self.__table


    def del_key_fields(self):
        del self.__keyFields

    entityModule = property(get_entity_module, set_entity_module, del_entity_module, "entityModule's docstring")
    storedViewKey = property(get_stored_view_key, set_stored_view_key, del_stored_view_key, "storedViewKey's docstring")
    usesDomain = property(get_uses_domain, set_uses_domain, del_uses_domain, "usesDomain's docstring")
    resourceUrlPrefix = property(get_resource_url_prefix, set_resource_url_prefix, del_resource_url_prefix, "resourceUrlPrefix's docstring")
    dataResource = property(get_data_resource, set_data_resource, del_data_resource, "dataResource's docstring")
    table = property(get_table, set_table, del_table, "table's docstring")
    keyFields = property(get_key_fields, set_key_fields, del_key_fields, "keyFields's docstring")
        
    
class KeyField(object):
    '''
    classdocs
    '''

    def __init__(self, 
                 BrowseKeyField=None, 
                 EntityKeyField=None,
                 IsParentForeignKey=None
                 ):
        self.__BrowseKeyField=BrowseKeyField, 
        self.__EntityKeyField=EntityKeyField, 
        self.__IsParentForeignKey=IsParentForeignKey

    def get_browse_key_field(self):
        return self.__BrowseKeyField


    def get_entity_key_field(self):
        return self.__EntityKeyField


    def get_is_parent_foreign_key(self):
        return self.__IsParentForeignKey


    def set_browse_key_field(self, value):
        self.__BrowseKeyField = value


    def set_entity_key_field(self, value):
        self.__EntityKeyField = value


    def set_is_parent_foreign_key(self, value):
        self.__IsParentForeignKey = value


    def del_browse_key_field(self):
        del self.__BrowseKeyField


    def del_entity_key_field(self):
        del self.__EntityKeyField


    def del_is_parent_foreign_key(self):
        del self.__IsParentForeignKey

    BrowseKeyField = property(get_browse_key_field, set_browse_key_field, del_browse_key_field, "BrowseKeyField's docstring")
    EntityKeyField = property(get_entity_key_field, set_entity_key_field, del_entity_key_field, "EntityKeyField's docstring")
    IsParentForeignKey = property(get_is_parent_foreign_key, set_is_parent_foreign_key, del_is_parent_foreign_key, "IsParentForeignKey's docstring")
        
    