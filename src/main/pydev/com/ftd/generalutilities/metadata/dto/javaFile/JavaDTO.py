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
        self.__class_methods = []
        self.__class_extends = None
        self.__class_implements = None
        self.__class_properties = None
        self.__class_package = None
        self.__class_imports = []
    
    
    def get_class_imports(self):
        return self.__class_imports


    def set_class_imports(self, value):
        self.__class_imports = value
        
        
    def push_class_imports(self, import_value):
        self.__class_imports.append(import_value)
        

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


    def push_class_implements(self, value):
        self.__class_implements.append(value)
        

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
        
        
    def push_class_properties(self, value):
        if isinstance(value, JavaMethodDTO):
            self.__class_methods.append(value)
            
            
    def push_class_methods(self, value):
        if isinstance(value, JavaMethodDTO):
            self.__class_methods.append(value)


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
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__method_name = None
        self.__method_range = None
        self.__method_inputs = []
        self.__method_output = None
        self.__method_related_imports = []
        self.__method_annotations = []
        self.__method_ajax_type = None
        self.__method_ajax_url = None
        self.__method_ajax_resp = []

    def get_method_ajax_type(self):
        return self.__method_ajax_type


    def get_method_ajax_url(self):
        return self.__method_ajax_url


    def set_method_ajax_type(self, value):
        self.__method_ajax_type = value


    def set_method_ajax_url(self, value):
        self.__method_ajax_url = value


    def get_method_ajax_resp(self):
        return self.__method_ajax_resp


    def set_method_ajax_resp(self, value):
        self.__method_ajax_resp = value


    def push_method_ajax_resp(self, value):
        self.__method_ajax_resp.append(value)
        

    def del_method_ajax_type(self):
        del self.__method_ajax_type


    def del_method_ajax_url(self):
        del self.__method_ajax_url


    def get_method_annotations(self):
        return self.__method_annotations


    def set_method_annotations(self, value):
        self.__method_annotations = value


    def push_method_annotations(self, value):
        self.__method_annotations.append(value)
        

    def del_method_annotations(self):
        del self.__method_annotations


    def get_method_related_imports(self):
        return self.__method_related_imports


    def set_method_related_imports(self, value):
        self.__method_related_imports = value
        
    
    def push_method_related_imports(self, value):
        self.__method_related_imports.append(value)


    def del_method_related_imports(self):
        del self.__method_related_imports
        

    def get_method_name(self):
        return self.__method_name


    def get_method_range(self):
        return self.__method_range


    def get_method_inputs(self):
        return self.__method_inputs


    def get_method_output(self):
        return self.__method_output


    def set_method_name(self, value):
        self.__method_name = value


    def set_method_range(self, value):
        self.__method_range = value


    def set_method_inputs(self, value):
        self.__method_inputs = value


    def push_method_inputs(self, value):
        self.__method_inputs.append(value)


    def set_method_output(self, value):
        self.__method_output = value


    def del_method_name(self):
        del self.__method_name


    def del_method_range(self):
        del self.__method_range


    def del_method_inputs(self):
        del self.__method_inputs


    def del_method_output(self):
        del self.__method_output

    method_name = property(get_method_name, set_method_name, del_method_name, "method_name's docstring")
    method_range = property(get_method_range, set_method_range, del_method_range, "method_range's docstring")
    method_inputs = property(get_method_inputs, set_method_inputs, del_method_inputs, "method_inputs's docstring")
    method_output = property(get_method_output, set_method_output, del_method_output, "method_output's docstring")
    method_related_imports = property(get_method_related_imports, set_method_related_imports, del_method_related_imports, "method_related_imports's docstring")
    method_annotations = property(get_method_annotations, set_method_annotations, del_method_annotations, "method_annotations's docstring")
    method_ajax_type = property(get_method_ajax_type, set_method_ajax_type, del_method_ajax_type, "method_ajax_type's docstring")
    method_ajax_url = property(get_method_ajax_url, set_method_ajax_url, del_method_ajax_url, "method_ajax_url's docstring")
        

class JavaParameterDTO(object):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__parameter_name = None
        self.__parameter_type = None

    def get_parameter_name(self):
        return self.__parameter_name


    def get_parameter_type(self):
        return self.__parameter_type


    def set_parameter_name(self, value):
        self.__parameter_name = value


    def set_parameter_type(self, value):
        self.__parameter_type = value


    def del_parameter_name(self):
        del self.__parameter_name


    def del_parameter_type(self):
        del self.__parameter_type

    parameter_name = property(get_parameter_name, set_parameter_name, del_parameter_name, "parameter_name's docstring")
    parameter_type = property(get_parameter_type, set_parameter_type, del_parameter_type, "parameter_type's docstring")
        
        
class JavaPropertyDTO(object):
    '''
    classdocs
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__property_name = None
        self.__property_type = None


    def get_property_name(self):
        return self.__property_name


    def get_property_type(self):
        return self.__property_type


    def set_property_name(self, value):
        self.__property_name = value


    def set_property_type(self, value):
        self.__property_type = value


    def del_property_name(self):
        del self.__property_name


    def del_property_type(self):
        del self.__property_type

    property_name = property(get_property_name, set_property_name, del_property_name, "property_name's docstring")
    property_type = property(get_property_type, set_property_type, del_property_type, "property_type's docstring")
        