'''
Created on Jun 27, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.ViewMetadataDTO import ViewMetadataDTO
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.resourcemetadata.ResourceMetadataDTO import ResourceMetadataDTO
from src.main.pydev.com.ftd.generalutilities.metadata.dto.javaFile.JavaDTO import JavaDTO

class EntityDTO(object):
    '''
    classdocs
    '''

    def __init__(self):
        #dtos
        viewDTO = ViewMetadataDTO()
        resourceDTO = ResourceMetadataDTO()
        serviceInterDTO = JavaDTO()
        entContInterDTO = JavaDTO()
        factoryInterDTO = JavaDTO()
        
        self.__dto = {'Entity':None,                      # entity name
                      'ViewFullPath':None,                # view metadata path
                      'ResourceFullPath':None,            # resource metadata path
                      'ViewMetaData':viewDTO,             # view metadata DTO
                      'ResourceMetaData':resourceDTO,     # resource metadata DTO
                      'ServiceInterDTO':serviceInterDTO,  # service interface DTO
                      'FactoryInterDTO':factoryInterDTO,  # factory interface DTO
                      'EntContInterDTO':entContInterDTO,  # entity container interface DTO
                      }
        
    
    def set_dtos(self, dtos):
        self.__dto = dtos
        
        
    def get_dtos(self):
        return self.__dto
    
    
    def set_entityname(self, entityname):
        if self.__dto:
            self.__dto['Entity'] = entityname
            
            
    def get_entityname(self):
        if self.__dto:
            return self.__dto['Entity']
        else:
            return None


    def set_viewfullpath(self, fullpath):
        if self.__dto:
            self.__dto['ViewFullPath'] = fullpath
            
        
    def get_viewfullpath(self):
        if self.__dto:
            return self.__dto['ViewFullPath']
        else:
            return None
        
        
    def set_resourcefullpath(self, fullpath):
        if self.__dto:
            self.__dto['ResourceFullPath'] = fullpath
        
        
    def get_resourcefullpath(self):
        if self.__dto:
            return self.__dto['ResourceFullPath']
        else:
            return None
        
        
    def set_serviceInterDTO(self, value):
        if self.__dto:
            self.__dto['ServiceInterDTO'] = value
        
        
    def get_serviceInterDTO(self):
        if self.__dto:
            return self.__dto['ServiceInterDTO']
        else:
            return None
        
        
    def set_entContInterDTO(self, value):
        if self.__dto:
            self.__dto['EntContInterDTO'] = value
        
        
    def get_entContInterDTO(self):
        if self.__dto:
            return self.__dto['EntContInterDTO']
        else:
            return None
        
        
    def set_factoryInterDTO(self, value):
        if self.__dto:
            self.__dto['FactoryInterDTO'] = value
        
        
    def get_factoryInterDTO(self):
        if self.__dto:
            return self.__dto['FactoryInterDTO']
        else:
            return None
        
#-------------------- resource metadata dto ---------
    def get_resourceDTO(self):
        if self.__dto:
            return self.__dto['ResourceMetaData']
        else:
            return None
    
    
    def set_resourceDTO(self, resDto):
        self.__dto['ResourceMetaData'] = resDto
    
    

    def set_resource_meta_uri(self, meta_uri):
        if self.__dto:
            if self.__dto['ResourceMetaData']:
                res = self.__dto['ResourceMetaData']
                res.set_meta_uri(meta_uri)
                
    
    def set_resource_view_uri(self, view_uri):
        if self.__dto:
            if self.__dto['ResourceMetaData']:
                res = self.__dto['ResourceMetaData']
                res.set_view_uri(view_uri)
                
                
    def set_resource_name_string(self, name_string):
        if self.__dto:
            if self.__dto['ResourceMetaData']:
                res = self.__dto['ResourceMetaData']
                res.set_name_string(name_string)
                
                
    def set_resource_is_eligible(self, is_eligible):
        if self.__dto:
            if self.__dto['ResourceMetaData']:
                res = self.__dto['ResourceMetaData']
                res.set_is_eligible(is_eligible)
                
                
    def set_resource_is_secure(self, is_secure):
        if self.__dto:
            if self.__dto['ResourceMetaData']:
                res = self.__dto['ResourceMetaData']
                res.set_is_secure(is_secure)
                
    
    def set_resource_primary_secure_Uri(self, primary_secure_Uri):
        if self.__dto:
            if self.__dto['ResourceMetaData']:
                res = self.__dto['ResourceMetaData']
                res.set_primary_secure_Uri(primary_secure_Uri)
                            