'''
Created on Jul 7, 2018

@author: ftd
'''

class EntityMaps(object):
    
    def __init__(self, dtos=None):
        '''
        Constructor
        '''
        self.__filename = 'entityMap.xml'
        if not dtos:
            self.__dtos = dtos
        else:
            self.__dtos = []
            

    def get_filename(self):
        return self.__filename


    def get_dtos(self):
        return self.__dtos


    def set_filename(self, value):
        self.__filename = value


    def set_dtos(self, value):
        self.__dtos = value


    def del_filename(self):
        del self.__filename


    def del_dtos(self):
        del self.__dtos

        
    def add_entitymap(self, entitymap):
        '''
        add a entityMap dto into the dto list
        @param entitymap: entityMap dto
        '''
        if isinstance(entitymap, EntityMap):
            if self.__dtos:
                self.__dtos.append(entitymap)
            else:
                self.__dtos = [entitymap]
            
    
    def get_entitymap_uris(self):
        results = []
        for dto in self.__dtos:
            results.append(dto.get_urn())
        return results
        
    
    filename = property(get_filename, set_filename, del_filename, "filename's docstring")
    dtos = property(get_dtos, set_dtos, del_dtos, "dtos's docstring")
        

class EntityMap(object):
    
    def __init__(self, 
                 urn=None, 
                 ent_type=None, 
                 object_name=None, 
                 pan_domain=None):
        '''
        Constructor
        '''
        self.__urn = urn
        self.__type = ent_type
        self.__object_name = object_name
        self.__pan_domain = pan_domain


    def get_urn(self):
        return self.__urn


    def get_type(self):
        return self.__type


    def get_object_name(self):
        return self.__object_name


    def get_pan_domain(self):
        return self.__pan_domain


    def set_urn(self, value):
        self.__urn = value


    def set_type(self, value):
        self.__type = value


    def set_object_name(self, value):
        self.__object_name = value


    def set_pan_domain(self, value):
        self.__pan_domain = value


    def del_urn(self):
        del self.__urn


    def del_type(self):
        del self.__type


    def del_object_name(self):
        del self.__object_name


    def del_pan_domain(self):
        del self.__pan_domain

    urn = property(get_urn, set_urn, del_urn, "urn's docstring")
    type = property(get_type, set_type, del_type, "type's docstring")
    object_name = property(get_object_name, set_object_name, del_object_name, "object_name's docstring")
    pan_domain = property(get_pan_domain, set_pan_domain, del_pan_domain, "pan_domain's docstring")
        
        
    