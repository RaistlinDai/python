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
        
        self.USER_DEFAULT = '\\ftdgen_default.txt'
        self.VIEW_METADATA_PATH = '\\src\\main\\resources\\com\\qad\\erp\\financials\\view\\'
        self.RESOURCE_METADATA_PATH = '\\src\\main\\resources\\com\\qad\\erp\\financials\\data\\meta\\'
        self.JAVA_CLASS_PATH = '\\src\\main\\java\\com\\qad\\erp\\financials\\'
        self.JAVA_DATACONTROLLER_PATH = '\\src\\main\\java\\com\\qad\\erp\\financials\\%s\\mvc\\controller\\data\\%s'
        self.JAVA_SERVICEIMPL_PATH = '\\src\\main\\java\\com\\qad\\erp\\financials\\%s\\service\\impl\\%s'
        self.ENTITY_MAP_PATH = '\\src\\main\\resources\\com\\qad\\erp\\financials\\data\\doc\\entityMap.xml'
        self.BEAN_APP_CONTEXT_PATH = '\\src\\main\\resources\\WEB-INF\\qad\\erp\\financials\\beans-app-context.xml'
        self.POM_PATH = '\\pom.xml'
        self.IMPL_JAR_LIB_PATH = '\\.m2\\repository\\com\\qad\\financials-impl\\'
        self.API_JAR_LIB_PATH = '\\.m2\\repository\\com\\qad\\financials-api\\'
        self.FIN_IMPL_JAR_PREFIX = 'financials-impl-'
        self.FIN_API_JAR_PREFIX = 'financials-api-'
        self.IMPL_FOLDER = 'impl\\'
        self.API_FOLDER = 'api\\'
        self.RESOURCE_TS_MAIN_PATH = '\\src\\main\\resources\\META-INF\\resources\\resources\\ts\\com\\qad\\erp\\financials\\'
        self.RESOURCE_TS_DTO_BL_FOLDER = 'DTO\\bl\\'
        self.RESOURCE_TS_DTO_UI_FOLDER = 'DTO\\ui\\'
        self.RESOURCE_TS_COMMON_FOLDER = 'common\\'
        self.RESOURCE_TS_UTIL_FOLDER = 'util\\'
        
        
        # ----------- The java service and interface -------
        self.JAVA_SERVICE_SUFFIX = 'Service'
        self.JAVA_FACTORY_SUFFIX = 'Factory'
        self.JAVA_CONTAINER_SUFFIX ='Container'
        self.JAVA_HOLDER_SUFFIX ='Holder'
        self.JAVA_QRA_PREFIX = 'Qra'
        self.SERVICEIMPL_SUFFIX = 'ServiceImpl'
        self.DATACONTROLLER_SUFFIX = 'DataController'
        self.TS_CONSTANT_SUFFIX ='Constants'
        self.TS_OBSERVABLE_OBJECT_SUFFIX = 'ObservableObject'
        
        self.UNZIP_JAR_FOLDER = 'uz\\'
        self.BACKUP_JAVA_FOLDER = 'bck\\'
        
        self.BACKUP_SUFFIX = '.bck'
        self.XML_SUFFIX = ".xml"
        self.JAR_SUFFIX = ".jar"
        self.JAVA_SUFFIX = ".java"
        self.TS_SUFFIX = ".ts"
        self.DEPOMPILE_JAVA_SUFFIX = "._java"
        self.RESOURCE_METADATA_SUFFIX = "-ViewResourceMeta.xml"
        
        self.FILE_TYPE = {'FFD8FF':'jpg', 
                          '89504E47':'png', 
                          '47494638':'gif', 
                          '424D':'bmp',
                          '3C3F786D6C':'xml', 
                          '68746D6C3E':'html', 
                          '52617221':'rar',
                          '504B0304':'jar', #the same as zip
                          '7061636b616765207765':'java',
                          '213C617263683E0A':'lib'}