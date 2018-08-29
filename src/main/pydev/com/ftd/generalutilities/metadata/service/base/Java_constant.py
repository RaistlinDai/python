'''
Created on Aug 14, 2018

@author: ftd
'''

class Java_constant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.JAVA_KEY_PACKAGE = 'package'
        self.JAVA_KEY_IMPORT = 'import'
        self.JAVA_KEY_CLASS = 'class'
        self.JAVA_KEY_INTERFACE = 'interface'
        self.JAVA_KEY_ABSTRACT = 'abstract'
        self.JAVA_KEY_EXTENDS = 'extends'
        self.JAVA_KEY_IMPLEMENTS = 'implements'
        
        self.JAVA_KEY_PUBLIC = 'public'
        self.JAVA_KEY_PROTECTED = 'protected'
        self.JAVA_KEY_PRIVATE = 'private'
        
        # java end flag
        self.JAVA_END_MARK = ';'
        self.JAVA_SEPERATOR = ','
        self.JAVA_DOT_MARK = '.'
        self.JAVA_RIGHT_BRACKET = ')'
        self.JAVA_LEFT_BRACKET = '('
        self.JAVA_RIGHT_BRACE = '}'
        self.JAVA_LEFT_BRACE = '{'
        self.JAVA_LEFT_COMMENT = '/*'
        self.JAVA_RIGHT_COMMENT = '*/'
        self.JAVA_LEFT_DASH = '<'
        self.JAVA_RIGHT_DASH = '>'
        self.JAVA_TAB = '\t'
        
        # java keywords
        self.JAVA_PRIMITIVE_TYPE_ARRAY = ["boolean", "char", "byte", "short", "int",
                                          "long", "float", "double", "void"]
        
        self.JAVA_KEY_ARRAY = ["abstract", "break", "case", "catch", "class",
            "const", "continue", "default", "do", "else", "extends", "final",
            "finally", "for", "goto", "if", "implements", "import",
            "instanceof", "interface", "native", "new", "package", "private",
            "protected", "public", "return", "static", "strictfp", "super",
            "switch", "synchronized", "this", "throw", "throws", "transient",
            "try", "volatile", "while"]
        
        self.JAVA_LITERAL_ARRAY = [ "null", "true", "false" ]
        
        # ----------------- standard functions --------------
        self.JAVA_FUNCTION_CREATE = 'create'
        self.JAVA_FUNCTION_UPDATE = 'update'
        self.JAVA_FUNCTION_DELETE = 'delete'
        self.JAVA_FUNCTION_FETCH = 'fetch'
        self.JAVA_FUNCTION_CLEARINST = 'clearInstance'
        self.JAVA_FUNCTION_GET = 'get'
        self.JAVA_FUNCTION_ADD = 'add'
        self.JAVA_FUNCTION_INITIALIZE = 'initialize'
        
        # ----------------- collections ----------------
        self.JAVA_COLLECTION_HOLDER = 'Holder'
        
        
        # ---------------------------------------------------------------- #
        #                  annotation                                      #
        # ---------------------------------------------------------------- #
        self.JAVA_ANNOTATION_SERVICE = '@Service(\"%s\")'
        self.JAVA_ANNOTATION_OVERRIDE = '@Override'
        
        # ---------------------------------------------------------------- #
        #                  serviceImpl.java                                #
        # ---------------------------------------------------------------- #
        # ------------------ impl jar service
        self.JAVA_IMPL_PACKAGE_PREFIX = 'com.qad.financials.'
        
        # ----------------- serviceImpl title comments ------------------ #
        self.JAVA_ENTITY_TITLE = '/*******************************************************************************\n * Copyright 2015 QAD Inc. All rights reserved.\n ******************************************************************************/\n'
        
        # ----------------- serviceImpl package ------------------ #
        self.JAVA_ENTITY_SERVICEIMPL_PACKAGE = 'com.qad.erp.financials.%s.service.impl'
        self.JAVA_ENTITY_DATACONTROLLER_PACKAGE = 'com.qad.erp.financials.%s.mvc.controller.data'
        
        # ----------------- serviceImpl header ------------------ #
        self.JAVA_SERVICE_HEADER = 'public class %s extends FinQraEntityService<%s, %s> {'
        
        # ----------------- standard imports ------------------ #
        self.JAVA_SERVICE_IMPORT_SPRING_FRAME = 'import org.springframework.stereotype.Service;'
        self.JAVA_SERVICE_IMPORT_PRO_DATAGRAPH = 'import com.progress.open4gl.ProDataGraph;'
        self.JAVA_SERVICE_IMPORT_FIN_QRA_ENTITYSERVICE = 'import com.qad.erp.financials.mvc.service.impl.FinQraEntityService;'
        self.JAVA_SERVICE_IMPORT_API_EXCEPTION = 'import com.qad.qra.ApiException;'
        self.JAVA_SERVICE_IMPORT_CONNECTION_MANAGER = 'import com.qad.qra.ConnectionManager;'
        self.JAVA_SERVICE_IMPORT_CONTEXT = 'import com.qad.qra.Context;'
        self.JAVA_SERVICE_IMPORT_HOLDER = 'import com.qad.qra.Holder;'
        self.JAVA_SERVICE_IMPORT_EXCEPTION_UTIL = 'import com.qad.qracore.util.ExceptionUtil;'
        self.JAVA_SERVICE_IMPORT_QRA_WORKSPACE_UTIL = 'import com.qad.qracore.util.QraWorkspaceUtil;'
        self.JAVA_SERVICE_IMPORT_SUBMIT_RESULTANDDATA = 'import com.qad.qraview.dto.SubmitResultAndData;'
        self.JAVA_SERVICE_IMPORT_API_DATAGRAPH = 'import commonj.sdo.DataGraph;'
        
        
        # ----------------- Code format ----------------#
        self.JAVA_ENTITY_CONST_CONTAINER_INTER = '%CONTAINER_INTERFACE%'
        self.JAVA_ENTITY_CONST_FACTORY_INTER = '%FACTORY_INTERFACE%'
        self.JAVA_ENTITY_CONST_CONTAINER_QRA = '%CONTAINER_QRA%'
        self.JAVA_ENTITY_CONST_FACTORY_QRA = '%FACTORY_QRA%'
        self.JAVA_ENTITY_CONST_HOLDER = '%ENTITYHOLDER%'
        self.JAVA_ENTITY_CONST_ENTITY_DATASET = '%ENTITY_DATASET%'
        
        self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER = '%MTD_CREATE_CONTAINER_INTERFACE%'
        self.JAVA_MTD_CONST_GET_SERVICE_INTER = '%MTD_GET_SERVICE_INTERFACE%'
        self.JAVA_MTD_CONST_INITIAL_ENTITY_DATASET = '%MTD_INITIAL_ENTITY_DATASET%'
        self.JAVA_MTD_CONST_GET_ENTITY_DATASET_LIST = '%MTD_GET_ENTITY_DATASET_LIST%'
        
        self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_VALUE = '%FETCH_MTD_PARAMETERS_VALUE%'
        self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_INPUT = '%FETCH_MTD_PARAMETERS%_INPUT'
        self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_CALL = '%FETCH_MTD_PARAMETERS%_CALL'
        self.JAVA_MTD_CONST_ADD_ENTITY_DATASET = '%MTD_ADD_ENTITY_DATASET%'
        self.JAVA_MTD_CONST_ADD_METHOD_PARAMS_INPUT = '%ADD_MTD_PARAMETERS%_INPUT'
        self.JAVA_MTD_CONST_ADD_METHOD_PARAMS_CALL = '%ADD_MTD_PARAMETERS%_CALL'
        self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME = '%COMMON_METHOD_NAME%'
        self.JAVA_MTD_CONST_COMMON_METHOD_PARAM_INPUT = '%COMMON_METHOD_PARAM_INPUT%'
        self.JAVA_MTD_CONST_COMMON_METHOD_PARAM_CALL = '%COMMON_METHOD_PARAM_CALL%'
        self.JAVA_MTD_CONST_COMMON_METHOD_COMMENT = '%COMMON_METHOD_COMMENT%'
        
        
        # ------------------- Standard methods -------------------------- #
        # initialize()
        self.JAVA_SERVICE_OVERRIDE_INITIALIZE = [self.JAVA_ANNOTATION_OVERRIDE,
                                                 'public ' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' initialize() {',
                                                 self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER +' factory = this.getEntityFactory();',
                                                 self.JAVA_TAB + 'String str1 = QraWorkspaceUtil.getFinancialEntityCode(sessionDataHolder.getCurrentWorkspace());',
                                                 '\n',
                                                 self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ' container = (' + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ') factory.' + self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER + '();',
                                                 '\n',
                                                 self.JAVA_TAB + 'Holder<DataGraph> holder = new Holder<DataGraph>((DataGraph) container.getProDataGraph());',
                                                 self.JAVA_TAB + 'Holder<String> ' + self.JAVA_ENTITY_CONST_HOLDER + ' = new com.qad.qra.Holder<String>();',
                                                 '\n',
                                                 self.JAVA_TAB + 'factory.' + self.JAVA_MTD_CONST_GET_SERVICE_INTER + '().' + self.JAVA_MTD_CONST_INITIAL_ENTITY_DATASET + '(str1, holder, ' + self.JAVA_ENTITY_CONST_HOLDER + ');',
                                                 self.JAVA_TAB + 'container.setProDataGraph((ProDataGraph) holder.getValue());',
                                                 self.JAVA_TAB + 'return container;',
                                                 self.JAVA_RIGHT_BRACE]
        
        # getEntityFactory()
        self.JAVA_SERVICE_OVERRIDE_GETENTITYFACTORY = [self.JAVA_ANNOTATION_OVERRIDE,
                                                       'protected ' + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' getEntityFactory(ConnectionManager connectionManager, Context context) {',
                                                       self.JAVA_TAB + 'return new ' + self.JAVA_ENTITY_CONST_FACTORY_QRA + '(connectionManager, context);',
                                                       self.JAVA_RIGHT_BRACE]
        
        # getEntityListFromContainer()
        self.JAVA_SERVICE_OVERRIDE_GETENTITYLIST = [self.JAVA_ANNOTATION_OVERRIDE,
                                                    'public List<' + self.JAVA_ENTITY_CONST_ENTITY_DATASET + '> getEntityListFromContainer(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container) {',
                                                    self.JAVA_TAB + 'List<' + self.JAVA_ENTITY_CONST_ENTITY_DATASET + '> entityList = new ArrayList<' + self.JAVA_ENTITY_CONST_ENTITY_DATASET + '>();',
                                                    self.JAVA_TAB + 'for (' + self.JAVA_ENTITY_CONST_ENTITY_DATASET + ' entity : container.' + self.JAVA_MTD_CONST_GET_ENTITY_DATASET_LIST + '()) {',
                                                    self.JAVA_TAB + self.JAVA_TAB + 'entityList.add(entity);',
                                                    self.JAVA_TAB + self.JAVA_RIGHT_BRACE,
                                                    '\n',
                                                    self.JAVA_TAB + 'return entityList;',
                                                    self.JAVA_RIGHT_BRACE]
        
        # createEntity()
        self.JAVA_SERVICE_OVERRIDE_CREATEENTITY = [self.JAVA_ANNOTATION_OVERRIDE,
                                                   'protected ' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' createEntity(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container) {',
                                                   self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' factory = getEntityFactory();',
                                                   self.JAVA_TAB + 'factory.' + self.JAVA_MTD_CONST_GET_SERVICE_INTER + '().create(((' + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ') container).getProDataGraph());',
                                                   self.JAVA_TAB + 'return container;',
                                                   self.JAVA_RIGHT_BRACE]
        
        # updateEntity()
        self.JAVA_SERVICE_OVERRIDE_UPDATEENTITY = [self.JAVA_ANNOTATION_OVERRIDE,
                                                   'public ' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' updateEntity(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container) {',
                                                   self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' factory = getEntityFactory();',
                                                   self.JAVA_TAB + 'factory.' + self.JAVA_MTD_CONST_GET_SERVICE_INTER + '().update(((' + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ') container).getProDataGraph());',
                                                   self.JAVA_TAB + 'return container;',
                                                   self.JAVA_RIGHT_BRACE]
        
        # readEntity()
        self.JAVA_SERVICE_OVERRIDE_READENTITY = [self.JAVA_ANNOTATION_OVERRIDE,
                                                 'protected ' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' readEntity(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container) {',
                                                 self.JAVA_TAB + self.JAVA_ENTITY_CONST_ENTITY_DATASET + ' entity = getEntityListFromContainer(container).get(0);',
                                                 self.JAVA_TAB + 'return read(' + self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_VALUE + ');',
                                                 self.JAVA_RIGHT_BRACE]
        
        # getJsonFromEntity()
        self.JAVA_SERVICE_OVERRIDE_GETJSONFROMENTITY = [self.JAVA_ANNOTATION_OVERRIDE,
                                                        'protected String getJsonFromEntity(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' entity) {',
                                                        self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' factory = getEntityFactory();',
                                                        self.JAVA_TAB + 'return factory.containerToJson(entity);',
                                                        self.JAVA_RIGHT_BRACE]
        
        # override methods list    
        self.JAVA_SERVICEIMPL_OVERRIDE_METHODS = [self.JAVA_SERVICE_OVERRIDE_INITIALIZE,
                                                  self.JAVA_SERVICE_OVERRIDE_GETENTITYFACTORY,
                                                  self.JAVA_SERVICE_OVERRIDE_GETENTITYLIST,
                                                  self.JAVA_SERVICE_OVERRIDE_CREATEENTITY,
                                                  self.JAVA_SERVICE_OVERRIDE_UPDATEENTITY,
                                                  self.JAVA_SERVICE_OVERRIDE_READENTITY,
                                                  self.JAVA_SERVICE_OVERRIDE_GETJSONFROMENTITY]
        
        # read()
        self.JAVA_SERVICE_READ = ['public ' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' read(' + self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_INPUT +') {',
                                  self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ' container = null;',
                                  self.JAVA_TAB + 'try {',
                                  self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_QRA + ' factory = (' + self.JAVA_ENTITY_CONST_FACTORY_QRA + ') getEntityFactory();',
                                  self.JAVA_TAB + self.JAVA_TAB + 'container = factory.' + self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER + '();',
                                  '\n',
                                  self.JAVA_TAB + self.JAVA_TAB + 'Holder<DataGraph> holder = new Holder<DataGraph>();',
                                  self.JAVA_TAB + self.JAVA_TAB + 'factory.' + self.JAVA_MTD_CONST_GET_SERVICE_INTER + '().fetch(' + self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_CALL + ', holder);',
                                  self.JAVA_TAB + self.JAVA_TAB + 'container.setProDataGraph((ProDataGraph) holder.getValue());',
                                  '\n',
                                  self.JAVA_TAB + '} catch (ApiException apie) {',
                                  self.JAVA_TAB + self.JAVA_TAB + 'if (ExceptionUtil.isMessageNumber(apie, 5)) // Not found',
                                  self.JAVA_TAB + self.JAVA_TAB + self.JAVA_TAB + 'container = null;',
                                  self.JAVA_TAB + self.JAVA_TAB + 'else',
                                  self.JAVA_TAB + self.JAVA_TAB + self.JAVA_TAB + 'throw apie;',
                                  self.JAVA_TAB + self.JAVA_RIGHT_BRACE,
                                  '\n',
                                  self.JAVA_TAB + 'return container;',
                                  self.JAVA_RIGHT_BRACE]
        
        # delete()
        self.JAVA_SERVICE_DELETE = ['public SubmitResultAndData<' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + '> delete(' + self.JAVA_MTD_CONST_ADD_METHOD_PARAMS_INPUT + ') {',
                                    self.JAVA_TAB + 'SubmitResultAndData<' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + '> submitResultAndData = new SubmitResultAndData<' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + '>();',
                                    self.JAVA_TAB + '' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' resultContainer = null;',
                                    '\n',
                                    self.JAVA_TAB + 'try {',
                                    self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' factory = getEntityFactory();',
                                    self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ' container = (' + self.JAVA_ENTITY_CONST_CONTAINER_QRA + ') factory.'+ self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER + '();',
                                    self.JAVA_TAB + self.JAVA_TAB + 'container.' + self.JAVA_MTD_CONST_ADD_ENTITY_DATASET + '(' + self.JAVA_MTD_CONST_ADD_METHOD_PARAMS_CALL + ');',
                                    self.JAVA_TAB + self.JAVA_TAB + 'factory.' + self.JAVA_MTD_CONST_GET_SERVICE_INTER + '().delete(container.getProDataGraph());',
                                    self.JAVA_TAB + self.JAVA_TAB + 'resultContainer = factory.'+ self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER + '();',
                                    self.JAVA_TAB + '} catch (ApiException apie) {',
                                    self.JAVA_TAB + self.JAVA_TAB + 'ExceptionUtil.convertException(apie, submitResultAndData);',
                                    self.JAVA_TAB + self.JAVA_RIGHT_BRACE,
                                    '\n',
                                    self.JAVA_TAB + 'submitResultAndData.setData(resultContainer);',
                                    self.JAVA_TAB + 'return submitResultAndData;',
                                    self.JAVA_RIGHT_BRACE]
        
        # CRUD methods list    
        self.JAVA_SERVICEIMPL_CRUD_METHODS = [self.JAVA_SERVICE_READ,
                                              self.JAVA_SERVICE_DELETE]
        
        
        # general methods format
        self.JAVA_SERVICEIMPL_COMMON_FORAMT = ['public void ' + self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME + '(' + self.JAVA_MTD_CONST_COMMON_METHOD_PARAM_INPUT + ') {\n',
                                               '\n',
                                               self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_QRA + ' factory = (' + self.JAVA_ENTITY_CONST_FACTORY_QRA + ') getEntityFactory();',
                                               '\n',
                                               self.JAVA_TAB + 'factory.' + self.JAVA_MTD_CONST_GET_SERVICE_INTER + '().' + self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME + '(' + self.JAVA_MTD_CONST_COMMON_METHOD_PARAM_CALL + ');\n',
                                               self.JAVA_RIGHT_BRACE]
        
        # general methods comment
        self.JAVA_SERVICEIMPL_COMMON_COMMENT = ['/**',
                                                ' *',
                                                self.JAVA_MTD_CONST_COMMON_METHOD_COMMENT,
                                                ' */']
        
        
        # ---------------------------------------------------------------- #
        #                  dataController.java                             #
        # ---------------------------------------------------------------- #
        
        
        
        
        
        