'''
Created on Jun 27, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.ViewMetadataDTO import ViewMetadataDTO

class FileDTOSet(object):
    '''
    classdocs
    '''

    def __init__(self):
        #dtos
        viewDTO = ViewMetadataDTO()
        self.__dto = {'Entity':None,
                      'ViewFullPath':None,
                      'ResourceFullPath':None,
                      'ViewMetaData':viewDTO}
        
    
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