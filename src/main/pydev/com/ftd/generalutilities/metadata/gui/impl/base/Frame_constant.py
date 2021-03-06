'''
Created on Jul 05, 2018

@author: ftd
'''

class Frame_constant:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.%s" % name)

        if not name.isupper():
            raise self.ConstCaseError(
                "const name '%s' is not all uppercase" % name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("can't unbind const(%s)" % name)
        raise NameError(name)
    
    def __init__(self):
        self.DATA_CONTROLLER = 'DataController'
        self.ENTITY_MAP_AND_BEAN_APP = 'EntityMap & BeanAppContext'
        self.SERVICE_IMPL = 'ServiceImpl'
        self.GENERATOR_SELECTION = 'GeneratorSelection'
        self.LOAD_FROM_DIRECTORY = 'LoadFromDirectory'
        self.TS_CONSTANTS = 'TSConstants'
        self.TS_HANDLER = 'TSHandler'
        self.MOCK_DTO = 'MockDTO'
        self.OBSERVABLE_OBJ = 'ObservableObj'
        self.TS_HANDLER_MAINT = 'TSMaint'
        self.TS_HANDLER_VIEWFORM = 'TSViewForm'
        self.TS_HANDLER_GRID = 'TSGrid'
        self.TS_HANDLER_BROWSE = 'TSBrowse'
        self.TS_HANDLER_COMMON = 'TSCommonService'
        
        #----------------- action ------------
        self.ACTION_UPDATE = 'update'
        self.ACTION_DELETE = 'delete'
