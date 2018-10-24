'''
Created on Jun 21, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.Datagridfield import Datagridfield

class Datagridtable(object):
    '''
    classdocs
    '''


    def __init__(self, name=None, datagridfields=[]):
        '''
        Constructor
        '''
        self.__name = name
        self.__datagridfields = []
        
        for f in datagridfields:
            if isinstance(f, Datagridfield):
                self.__datagridfields.append(f)
                

    def get_name(self):
        return self.__name


    def set_name(self, value):
        self.__name = value
        
        
    def push_datagridfield(self, field):
        self.__datagridfields.append(field)


    def del_name(self):
        del self.__name

    