'''
Created on Jun 27, 2018

@author: ftd
'''

class File_constant(object):
    '''
    classdocs
    '''
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
        '''
        Constructor
        '''
        
        '''
        @todo: the project is incorrect after package, should be correct later
        '''
        self.MY_PROJECT_PACKAGE = '\\src\\main\\pydev'
        self.FTD_JD_JAR = '\\3rd\\lib\\jar\\FtdJD.jar'
        self.THIRD_JDCORE_JAR = '\\3rd\\lib\\jar\\jd-core-0.7.1.jar'
        
        self.VIEW_METADATA_PATH = '\\src\\main\\resources\\com\\qad\\erp\\financials\\view\\'
        self.RESOURCE_METADATA_PATH = '\\src\\main\\resources\\com\\qad\\erp\\financials\\data\\meta\\'
        self.JAVA_CONTROLLER_PATH = '\\src\\main\\java\\com\\qad\\erp\\financials\\'
        self.ENTITY_MAP_PATH = '\\src\\main\\resources\\com\\qad\\erp\\financials\\data\\doc\\entityMap.xml'
        self.BEAN_APP_CONTEXT_PATH = '\\src\\main\\resources\\WEB-INF\\qad\\erp\\financials\\beans-app-context.xml'
        self.POM_PATH = '\\pom.xml'
        self.JAR_LIB_PATH = '\\.m2\\repository\\com\\qad\\financials-impl\\'
        self.FIN_IMPL_JAR_PREFIX = 'financials-impl-'
        
        self.BACKUP_SUFFIX = '.bck'
        self.XML_SUFFIX = ".xml"
        self.JAR_SUFFIX = ".jar"
        self.RESOURCE_METADATA_SUFFIX = "-ViewResourceMeta.xml"
        
    