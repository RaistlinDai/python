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
        self.dto = {'Entity':None,
                    'FullPath':None,
                    'ViewMetaData':viewDTO}
        
    
    def set_dtos(self, dtos):
        self.dto = dtos
        
        
    def get_dtos(self):
        return self.dto
    
    
    def set_entityname(self, entityname):
        if self.dto:
            self.dto['Entity'] = entityname


    def set_fullpath(self, fullpath):
        if self.dto:
            self.dto['FullPath'] = fullpath
        print(self.dto['FullPath'])