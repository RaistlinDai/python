'''
Created on Jun 26, 2018

@author: ftd
'''

class ViewMetadataDTO(object):
    
    def __init__(self, datafields=None, datalabels=None, datagrids=None):
        '''
        Constructor
        '''
        if isinstance(datafields, dict):
            self.__datafields = datafields
            
        if isinstance(datalabels, dict):
            self.__datalabels = datalabels
        
        if isinstance(datagrids, dict):
            self.__datagrids = datagrids


    def get_datafields(self):
        return self.__datafields


    def get_datalabels(self):
        return self.__datalabels


    def get_datagrids(self):
        return self.__datagrids


    def set_datafields(self, value):
        self.__datafields = value


    def set_datalabels(self, value):
        self.__datalabels = value


    def set_datagrids(self, value):
        self.__datagrids = value


    def del_datafields(self):
        del self.__datafields


    def del_datalabels(self):
        del self.__datalabels


    def del_datagrids(self):
        del self.__datagrids

    
    def get_datafield(self, fieldname):
        if self.__datafields:
            return self.__datafields.get(fieldname)
        else:
            return None
    
    
    def get_datalabel(self, labelname):
        if self.__datalabels:
            return self.__datalabels.get(labelname)
        else:
            return None
        
        
    def get_datagrid(self, gridname):
        if self.__datagrids:
            return self.__datagrids.get(gridname)
        else:
            return None