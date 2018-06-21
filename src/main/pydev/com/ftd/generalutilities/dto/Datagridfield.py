'''
Created on Jun 21, 2018

@author: ftd
'''

class Datagridfield(object):
    '''
    classdocs
    '''


    def __init__(self, fieldname, readonly):
        '''
        Constructor
        '''
        self.__fieldname = fieldname
        
        if isinstance(readonly, bool):
            self.__readonly = readonly
        else:
            self.__readonly = False