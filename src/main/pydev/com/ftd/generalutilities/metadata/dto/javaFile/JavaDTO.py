'''
Created on Aug 14, 2018

@author: ftd
'''

class JavaDTO(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__class_name = None
        self.__class_type = None
        self.__class_range = None
        self.__class_methods = None
        self.__class_extends = None
        self.__class_implements = None
        self.__class_properties = None
        self.__class_package = None
    
    
    def get_class_package(self):
        return self.__class_package


    def set_class_package(self, value):
        self.__class_package = value


    def get_class_extends(self):
        return self.__class_extends


    def get_class_implements(self):
        return self.__class_implements


    def set_class_extends(self, value):
        self.__class_extends = value


    def set_class_implements(self, value):
        self.__class_implements = value


    def del_class_extends(self):
        del self.__class_extends


    def del_class_implements(self):
        del self.__class_implements
        

    def get_class_name(self):
        return self.__class_name


    def get_class_type(self):
        return self.__class_type


    def get_class_range(self):
        return self.__class_range


    def get_class_methods(self):
        return self.__class_methods


    def get_class_properties(self):
        return self.__class_properties


    def set_class_name(self, value):
        self.__class_name = value


    def set_class_type(self, value):
        self.__class_type = value


    def set_class_range(self, value):
        self.__class_range = value


    def set_class_methods(self, value):
        self.__class_methods = value


    def set_class_properties(self, value):
        self.__class_properties = value


    def del_class_name(self):
        del self.__class_name


    def del_class_type(self):
        del self.__class_type


    def del_class_range(self):
        del self.__class_range


    def del_class_methods(self):
        del self.__class_methods


    def del_class_properties(self):
        del self.__class_properties

    class_name = property(get_class_name, set_class_name, del_class_name, "class_name's docstring")
    class_type = property(get_class_type, set_class_type, del_class_type, "class_type's docstring")
    class_range = property(get_class_range, set_class_range, del_class_range, "class_range's docstring")
    class_methods = property(get_class_methods, set_class_methods, del_class_methods, "class_methods's docstring")
    class_properties = property(get_class_properties, set_class_properties, del_class_properties, "class_properties's docstring")
    class_extends = property(get_class_extends, set_class_extends, del_class_extends, "class_extends's docstring")
    class_implements = property(get_class_implements, set_class_implements, del_class_implements, "class_implements's docstring")
        
        
class JavaMethodDTO(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, methodname, methodrange, methodparams, methodreturn):
        '''
        Constructor
        '''
        self.__method_name = methodname
        self.__method_range = methodrange
        self.__method_params = methodparams
        self.__method_return = methodreturn

    def get_method_name(self):
        return self.__method_name


    def get_method_range(self):
        return self.__method_range


    def get_method_params(self):
        return self.__method_params


    def get_method_return(self):
        return self.__method_return


    def set_method_name(self, value):
        self.__method_name = value


    def set_method_range(self, value):
        self.__method_range = value


    def set_method_params(self, value):
        self.__method_params = value


    def set_method_return(self, value):
        self.__method_return = value


    def del_method_name(self):
        del self.__method_name


    def del_method_range(self):
        del self.__method_range


    def del_method_params(self):
        del self.__method_params


    def del_method_return(self):
        del self.__method_return

    method_name = property(get_method_name, set_method_name, del_method_name, "method_name's docstring")
    method_range = property(get_method_range, set_method_range, del_method_range, "method_range's docstring")
    method_params = property(get_method_params, set_method_params, del_method_params, "method_params's docstring")
    method_return = property(get_method_return, set_method_return, del_method_return, "method_return's docstring")
        
        