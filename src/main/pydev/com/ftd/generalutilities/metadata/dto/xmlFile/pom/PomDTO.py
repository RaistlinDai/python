'''
Created on Jul 7, 2018

@author: ftd
'''

class PomDTO(object):
    
    def __init__(self, fin_api_ver=None):
        '''
        Constructor
        '''
        self.__filename = 'pom.xml'
        self.__financials_api_version = fin_api_ver

    def get_filename(self):
        return self.__filename


    def get_financials_api_version(self):
        return self.__financials_api_version


    def set_filename(self, value):
        self.__filename = value


    def set_financials_api_version(self, value):
        self.__financials_api_version = value


    def del_filename(self):
        del self.__filename


    def del_financials_api_version(self):
        del self.__financials_api_version

    filename = property(get_filename, set_filename, del_filename, "filename's docstring")
    financials_api_version = property(get_financials_api_version, set_financials_api_version, del_financials_api_version, "financials_api_version's docstring")
        
    
    