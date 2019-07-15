'''
Created on Jul 11, 2018

@author: ftd
'''

class Database_parameters(object):
    '''
    classdocs
    '''

    def __init__(self, contact_points='0.0.0.0', port=0, username='qad', password='qad'):
        '''
        Constructor
        '''
        self.__contact_points = contact_points
        self.__port = port
        self.__username = username
        self.__password = password
        

    def get_contact_points(self):
        return self.__contact_points


    def get_port(self):
        return self.__port


    def get_username(self):
        return self.__username


    def get_password(self):
        return self.__password


    def set_contact_points(self, value):
        self.__contact_points = value


    def set_port(self, value):
        self.__port = value


    def set_username(self, value):
        self.__username = value


    def set_password(self, value):
        self.__password = value


    def del_contact_points(self):
        del self.__contact_points


    def del_port(self):
        del self.__port


    def del_username(self):
        del self.__username


    def del_password(self):
        del self.__password

    contact_points = property(get_contact_points, set_contact_points, del_contact_points, "contact_points's docstring")
    port = property(get_port, set_port, del_port, "port's docstring")
    username = property(get_username, set_username, del_username, "username's docstring")
    password = property(get_password, set_password, del_password, "password's docstring")
        
    
    