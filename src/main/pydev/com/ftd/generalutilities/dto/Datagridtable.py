'''
Created on Jun 21, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.dto.Datagridfield import Datagridfield


class Datagridtable(object):
    '''
    classdocs
    '''


    def __init__(self, name, datagridfields=[]):
        '''
        Constructor
        '''
        self.__name = name
        
        for f in datagridfields:
            if isinstance(f, Datagridfield):
                self.__datagridfields.append(f)