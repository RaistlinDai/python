'''
Created on Jul 04, 2018

@author: ftd
'''

class BeansAppContextDTO(object):
    '''
    classdocs
    '''


    def __init__(self, 
                 bean_id=None, 
                 bean_class=None, 
                 entity_uri_mapstring=None, 
                 label_service=None, 
                 entity_metadata_service=None,
                 view_metadata_service=None):
        '''
        Constructor
        '''
        self.__filename = 'beans-app-context.xml'
        self.__bean_id = bean_id
        self.__bean_class = bean_class
        self.__entity_uri_mapstring = entity_uri_mapstring
        self.__label_service = label_service
        self.__entity_metadata_service = entity_metadata_service
        self.__view_metadata_service = view_metadata_service


    def get_filename(self):
        return self.__filename


    def set_filename(self, value):
        self.__filename = value


    def get_bean_class(self):
        return self.__bean_class


    def set_bean_class(self, value):
        self.__bean_class = value


    def del_bean_class(self):
        del self.__bean_class


    def get_bean_id(self):
        return self.__bean_id


    def get_entity_uri_mapstring(self):
        return self.__entity_uri_mapstring


    def get_label_service(self):
        return self.__label_service


    def get_entity_metadata_service(self):
        return self.__entity_metadata_service


    def get_view_metadata_service(self):
        return self.__view_metadata_service


    def set_bean_id(self, value):
        self.__bean_id = value


    def set_entity_uri_mapstring(self, value):
        self.__entity_uri_mapstring = value


    def set_label_service(self, value):
        self.__label_service = value


    def set_entity_metadata_service(self, value):
        self.__entity_metadata_service = value


    def set_view_metadata_service(self, value):
        self.__view_metadata_service = value


    def del_bean_id(self):
        del self.__bean_id


    def del_entity_uri_mapstring(self):
        del self.__entity_uri_mapstring


    def del_label_service(self):
        del self.__label_service


    def del_entity_metadata_service(self):
        del self.__entity_metadata_service


    def del_view_metadata_service(self):
        del self.__view_metadata_service


    bean_id = property(get_bean_id, set_bean_id, del_bean_id, "bean_id's docstring")
    entity_uri_mapstring = property(get_entity_uri_mapstring, set_entity_uri_mapstring, del_entity_uri_mapstring, "entity_uri_mapstring's docstring")
    label_service = property(get_label_service, set_label_service, del_label_service, "label_service's docstring")
    entity_metadata_service = property(get_entity_metadata_service, set_entity_metadata_service, del_entity_metadata_service, "entity_metadata_service's docstring")
    view_metadata_service = property(get_view_metadata_service, set_view_metadata_service, del_view_metadata_service, "view_metadata_service's docstring")
    bean_class = property(get_bean_class, set_bean_class, del_bean_class, "bean_class's docstring")
        
         
        