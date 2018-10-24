'''
Created on Jun 21, 2018

@author: ftd
'''

class Datagridfield(object):
    '''
    classdocs
    '''


    def __init__(self, fieldname=None, readonly=False):
        '''
        Constructor
        '''
        self.__fieldname = fieldname
        
        if isinstance(readonly, bool):
            self.__readonly = readonly
        else:
            self.__readonly = False
            

    def get_fieldname(self):
        return self.__fieldname


    def get_readonly(self):
        return self.__readonly


    def set_fieldname(self, value):
        self.__fieldname = value


    def set_readonly(self, value):
        self.__readonly = value


    def del_fieldname(self):
        del self.__fieldname


    def del_readonly(self):
        del self.__readonly

    