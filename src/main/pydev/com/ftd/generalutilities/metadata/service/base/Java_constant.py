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
        self.JAVA_EQUALS = '='
        self.JAVA_TAB = '\t'
        self.JAVA_COMMA = '\"'
        
        # java processing flag
        self.JAVA_AND_MARK = '&&'
        self.JAVA_OR_MARK = '||'
        
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
        self.JAVA_FUNCTION_SET = 'set'
        self.JAVA_FUNCTION_ADD = 'add'
        self.JAVA_FUNCTION_INITIALIZE = 'initialize'
        
        #------------------ entity/domain --------------
        self.JAVA_KEY_FIELD_ENTITY = 'entityCode'
        self.JAVA_KEY_FIELD_DOMAIN = 'domainCode'
        
        # ----------------- collections ----------------
        self.JAVA_COLLECTION_HOLDER = 'Holder'
        self.JAVA_COLLECTION_HOLDER_DATAGRAPH = 'Holder<DataGraph>'
        
        # ----------------- types ------------------
        self.JAVA_TYPE_STRING = 'String'
        self.JAVA_TYPE_INTEGER = 'Integer'
        self.JAVA_TYPE_BIGDECIMAL = 'BigDecimal'
        self.JAVA_TYPE_BOOLEAN = 'Boolean'
        self.JAVA_TYPE_LONG = 'Long'
        self.JAVA_TYPE_GREGORIANCALENDAR = 'GregorianCalendar'
        self.JAVA_PROGRESS_TYPE_PREFIX = ['ii','it','ic','il','id','ig']
        
        # ---------------------------------------------------------------- #
        #                  annotation                                      #
        # ---------------------------------------------------------------- #
        self.JAVA_ANNOTATION_SERVICE = '@Service(\"%s\")'
        self.JAVA_ANNOTATION_OVERRIDE = '@Override'
        self.JAVA_ANNOTATION_CONTROLLER = '@Controller(\"%s\")'
        self.JAVA_ANNOTATION_AUTOWIRED = '@Autowired'
        self.JAVA_ANNOTATION_REQUESTMAPPING = '@RequestMapping'
        self.JAVA_ANNOTATION_REQUESTPARAM = '@RequestParam'
        
        # ---------------------------------------------------------------- #
        #                  ajax request                                    #
        # ---------------------------------------------------------------- #
        self.JAVA_AJAX_REQUEST_TYPE_GET = 'RequestMethod.GET'
        self.JAVA_AJAX_REQUEST_TYPE_POST = 'RequestMethod.POST'
        self.JAVA_AJAX_REQUEST_TYPE_DELETE = 'RequestMethod.DELETE'
        
        # ---------------------------------------------------------------- #
        #                  serviceImpl.java                                #
        # ---------------------------------------------------------------- #
        # ------------------ impl jar service
        self.JAVA_JAR_IMPL_PACKAGE_PREFIX = 'com.qad.financials.'
        
        # ----------------- serviceImpl title comments ------------------ #
        self.JAVA_ENTITY_TITLE = '/*******************************************************************************\n * Copyright 2015 QAD Inc. All rights reserved.\n ******************************************************************************/\n'
        
        # ----------------- serviceImpl package ------------------ #
        self.JAVA_ENTITY_SERVICEIMPL_PACKAGE = 'com.qad.erp.financials.%s.service.impl'
        self.JAVA_SERVICEIMPL_PACKAGE_PREFIX = 'com.qad.erp.financials.'
        
        # ----------------- serviceImpl header ------------------ #
        self.JAVA_SERVICE_HEADER = 'public class %s extends FinQraEntityService<%s, %s> {'
        
        # ----------------- standard imports ------------------ #
        self.JAVA_SERVICE_IMPORT_UTIL_ARRAYLIST = 'import java.util.ArrayList;'
        self.JAVA_SERVICE_IMPORT_UTIL_LIST = 'import java.util.List;'
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
        self.JAVA_ENTITY_CONST_DATARESOURCE = '%ENTITY_DATARESOURCE%'
        self.JAVA_ENTITY_CONST_ENTITY_NAME = '%ENTITY_NAME%'
        self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME = '%SERVICEIMPL_NAME%'
        self.JAVA_ENTITY_CONST_CONTROLLER_NAME = '%CONTROLLER_NAME%'
        
        self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER = '%MTD_CREATE_CONTAINER_INTERFACE%'
        self.JAVA_MTD_CONST_GET_SERVICE_INTER = '%MTD_GET_SERVICE_INTERFACE%'
        self.JAVA_MTD_CONST_INITIAL_ENTITY_DATASET = '%MTD_INITIAL_ENTITY_DATASET%'
        self.JAVA_MTD_CONST_GET_ENTITY_DATASET_LIST = '%MTD_GET_ENTITY_DATASET_LIST%'
        self.JAVA_MTD_CONST_SET_SERVICEIMPL = '%MTD_SET_SERVICEIMPL%'
        self.JAVA_MTD_CONST_ENTITY_DATASET = '%MTD_ENTITY_DATASET%'
        
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
        
        self.JAVA_MTD_CONST_CONTROLLER_STANDARD_DESCRIPTION = '%CONTROLLER_STANDARD_DESCRIPTION%'
        self.JAVA_MTD_CONST_CONTROLLER_AJAX_PARAM = '%CONTROLLER_AJAX_PARAM%'
        self.JAVA_MTD_CONST_PARAM_VERIFY = '%PARAM_VERIFY%'
        self.JAVA_MTD_CONST_PARAM_VERIFY_NON = '%PARAM_VERIFY_NON%'
        self.JAVA_MTD_CONST_PARAM_COMPARATION = '%PARAM_COMPARATION%'
        self.JAVA_MTD_CONST_CURRENT_ENTITY_DOMAIN = '%CURRENT_ENTITY_DOMAIN%'
        self.JAVA_MTD_CONST_HOLDER_CREATE = '%HOLDER_CREATE%'
        self.JAVA_MTD_CONST_REQUEST_CONVERSION = '%REQUEST_CONVERSION%'
        self.JAVA_MTD_CONST_REQUEST_BIGDEC_INIT = '%REQUEST_BIGDEC_INIT%'
        self.JAVA_MTD_CONST_ADD_HASHSET = '%ADD_HASHSET%'
        self.JAVA_MTD_CONST_ADD_ATTRIBUTE = '%ADD_ATTRIBUTE%'
        self.JAVA_MTD_CONST_CONTAINER_CREATE = '%CONTAINER_CREATE%'
        self.JAVA_MTD_CONST_CONTAINER_ASSIGN = '%CONTAINER_ASSIGN%'
        
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
        # ----------------- dataController ajax method ------------------ #
        self.JAVA_CONTROLLER_AJAX_METHOD_PREFIX = 'public View '
        self.JAVA_CONTROLLER_AJAX_CELL_VALUE = 'value'
        self.JAVA_CONTROLLER_AJAX_CELL_METHOD = 'method'
        
        # ----------------- dataController package ------------------ #
        self.JAVA_ENTITY_DATACONTROLLER_PACKAGE = 'com.qad.erp.financials.%s.mvc.controller.data'
        
        # ----------------- dataController header ------------------ #
        self.JAVA_CONTROLLER_HEADER = 'public class %s extends FinQraDataController<%s> %s{'
        
        # ----------------- standard imports ------------------ #
        self.JAVA_CONTROLLER_IMPORTS = ['import java.util.HashSet;',
                                        'import java.util.List;',
                                        'import java.util.Set;',
                                        'import org.slf4j.Logger;',
                                        'import org.slf4j.LoggerFactory;',
                                        'import org.springframework.beans.factory.annotation.Autowired;',
                                        'import org.springframework.http.MediaType;',
                                        'import org.springframework.stereotype.Controller;',
                                        'import org.springframework.ui.Model;',
                                        'import org.springframework.web.bind.annotation.ModelAttribute;',
                                        'import org.springframework.web.bind.annotation.RequestBody;',
                                        'import org.springframework.web.bind.annotation.RequestMapping;',
                                        'import org.springframework.web.bind.annotation.RequestMethod;',
                                        'import org.springframework.web.bind.annotation.RequestParam;',
                                        'import org.springframework.web.bind.annotation.ResponseBody;',
                                        'import org.springframework.web.servlet.View;',
                                        'import com.progress.open4gl.ProDataGraph;',
                                        'import com.qad.erp.financials.mvc.controller.data.FinQraDataController;',
                                        'import com.qad.erp.financials.util.service.impl.FinancialsDataSetUtil;',
                                        'import com.qad.qra.Holder;',
                                        'import com.qad.qracore.util.QraWorkspaceUtil;',
                                        'import com.qad.qraview.dto.QueryParameters;',
                                        'import com.qad.qraview.dto.SubmitResultAndData;',
                                        'import com.qad.qraview.util.StringUtil;']
        
        self.JAVA_CONTROLLER_CROSS_WORKSPACE_CONTROLLER = 'import com.qad.webshell.security.authorization.CrossWorkspaceController;'
        
        # ----------------- static final properties ------------------ #
        self.JAVA_CONTROLLER_STATIC_FINAL_PROP_SUFFIX = 'private static final String %s = "%s";'
        self.JAVA_CONTROLLER_STATIC_FINAL_PROP_LOGGER = 'private static final Logger logger = LoggerFactory.getLogger(%s.class);'
        
        
        # ------------------- Standard methods -------------------------- #
        # setServiceImpl()
        self.JAVA_CONTROLLER_OVERRIDE_INITIALIZE = [self.JAVA_ANNOTATION_AUTOWIRED,
                                                    'public void ' + self.JAVA_MTD_CONST_SET_SERVICEIMPL + '(' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ' service) {',
                                                    self.JAVA_TAB + 'crudProviderService = service;',
                                                    self.JAVA_RIGHT_BRACE]
        
        # getServiceProviderName()
        self.JAVA_CONTROLLER_OVERRIDE_GET_SERVICE_PROVIDER_NAME = [self.JAVA_ANNOTATION_OVERRIDE,
                                                                   'public String getServiceProviderName() {',
                                                                   self.JAVA_TAB + 'return com.qad.erp.financials.Plugin.PLUGIN_NAME;',
                                                                   self.JAVA_RIGHT_BRACE]
        
        # getEntityFromJson()
        self.JAVA_CONTROLLER_OVERRIDE_GET_ENTITY_FROM_JSON = [self.JAVA_ANNOTATION_OVERRIDE,
                                                              'protected ' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' getEntityFromJson(String json) {',
                                                              self.JAVA_TAB + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ' service = (' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ')crudProviderService;',
                                                              self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' factory = service.getEntityFactory();',
                                                              self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container = null;',
                                                              self.JAVA_TAB + 'try {',
                                                              self.JAVA_TAB + self.JAVA_TAB + 'container = factory.' + self.JAVA_MTD_CONST_CRAET_CONTAINER_INTER + '(json);',
                                                              self.JAVA_TAB + '} catch (Exception e) {',
                                                              self.JAVA_TAB + self.JAVA_TAB + 'e.printStackTrace();',
                                                              self.JAVA_TAB + self.JAVA_TAB + 'throw(new RuntimeException(e));',
                                                              self.JAVA_TAB + self.JAVA_RIGHT_BRACE,
                                                              '\n',
                                                              self.JAVA_TAB + 'return container;',
                                                              self.JAVA_RIGHT_BRACE]
        
        # getJsonFromEntity()
        self.JAVA_CONTROLLER_OVERRIDE_GET_JSON_FROM_ENTITY = [self.JAVA_ANNOTATION_OVERRIDE,
                                                              'protected String getJsonFromEntity(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' entity) {',
                                                              self.JAVA_TAB + self.JAVA_ENTITY_CONST_FACTORY_INTER + ' factory = ((' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ')crudProviderService).getEntityFactory();',
                                                              self.JAVA_TAB + 'return factory.containerToJson(entity);',
                                                              self.JAVA_RIGHT_BRACE]
        
        # getEntityCount()
        self.JAVA_CONTROLLER_OVERRIDE_GET_ENTITY_COUNT = [self.JAVA_ANNOTATION_OVERRIDE,
                                                          'protected int getEntityCount(' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container) {',
                                                          self.JAVA_TAB + 'return container.' + self.JAVA_MTD_CONST_ENTITY_DATASET + '().size();',
                                                          self.JAVA_RIGHT_BRACE]
        
        # override methods list    
        self.JAVA_CONTROLLER_OVERRIDE_METHODS = [self.JAVA_CONTROLLER_OVERRIDE_INITIALIZE,
                                                 self.JAVA_CONTROLLER_OVERRIDE_GET_SERVICE_PROVIDER_NAME,
                                                 self.JAVA_CONTROLLER_OVERRIDE_GET_ENTITY_FROM_JSON,
                                                 self.JAVA_CONTROLLER_OVERRIDE_GET_JSON_FROM_ENTITY,
                                                 self.JAVA_CONTROLLER_OVERRIDE_GET_ENTITY_COUNT]
        
        
        # createAndUpdateApi()
        self.JAVA_CONTROLLER_CRAETE_AND_UPDATE = ['/**',
                                                  ' * Handle API submit request for Update and Create actions.',
                                                  ' *',
                                                  ' * @param model',
                                                  ' * @param json',
                                                  self.JAVA_MTD_CONST_COMMON_METHOD_COMMENT,
                                                  ' * @return View - Springs representation of the view using the model provided',
                                                  ' */',
                                                  '@RequestMapping(value = "/api/erp/' + self.JAVA_ENTITY_CONST_DATARESOURCE + '", method = RequestMethod.POST, consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)',
                                                  'public @ResponseBody View ' + self.JAVA_ENTITY_CONST_ENTITY_NAME + 'CreateaAndUpdateApi(Model model, @RequestBody String json,',
                                                  self.JAVA_TAB + self.JAVA_TAB + self.JAVA_MTD_CONST_CONTROLLER_AJAX_PARAM + ') {',
                                                  '\n',
                                                  self.JAVA_TAB + 'if (logger.isDebugEnabled())',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'logger.debug("' + self.JAVA_ENTITY_CONST_CONTROLLER_NAME + '.' + self.JAVA_ENTITY_CONST_ENTITY_NAME + 'CreateaAndUpdateApi() invoked");',
                                                  self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' container = getEntityFromJson(json);',
                                                  '\n',
                                                  self.JAVA_TAB + 'if (' + self.JAVA_MTD_CONST_PARAM_VERIFY + ') {',
                                                  '\n',
                                                  self.JAVA_TAB + self.JAVA_TAB + '// Create',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'View view = getEntityCreateView(model, container);',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'return view;',
                                                  self.JAVA_TAB + '} else if (' + self.JAVA_MTD_CONST_PARAM_VERIFY_NON + ') {',
                                                  '\n',
                                                  self.JAVA_TAB + self.JAVA_TAB + '// Update',
                                                  self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ' service = ((' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ') crudProviderService);',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'List<' + self.JAVA_ENTITY_CONST_ENTITY_DATASET + '> entityList = service.getEntityListFromContainer(container);',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'if (entityList.size() == 0)',
                                                  self.JAVA_TAB + self.JAVA_TAB +self.JAVA_TAB + 'throw new IllegalArgumentException("No entity data submitted in update request.");',
                                                  '\n',
                                                  self.JAVA_TAB + self.JAVA_TAB + '// domainCode validation against the entity data now takes place in the service base classes.',
                                                  self.JAVA_TAB + self.JAVA_TAB + '// Do not validate domainCode in specific data controller implementations.',
                                                  self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_ENTITY_DATASET + ' entity = entityList.get(0);',
                                                  '\n',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'if (' + self.JAVA_MTD_CONST_PARAM_COMPARATION + ')',
                                                  '\n',
                                                  self.JAVA_TAB + self.JAVA_TAB +self.JAVA_TAB + 'throw new IllegalArgumentException("Key field parameter(s) must match the corresponding value in the submitted entity data.");',
                                                  '\n',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'return getEntityUpdateView(model, container);',
                                                  self.JAVA_TAB + '} else {',
                                                  self.JAVA_TAB + self.JAVA_TAB + 'throw new IllegalArgumentException("Key field parameter(s) must all be null or all non-null.");',
                                                  self.JAVA_TAB + self.JAVA_RIGHT_BRACE,
                                                  self.JAVA_RIGHT_BRACE]
        
        # readApi()
        self.JAVA_CONTROLLER_READ = ['/**',
                                     ' * Handle API request for List and Read actions.',
                                     ' *',
                                     ' * @param model',
                                     ' * @param queryParameters',
                                     self.JAVA_MTD_CONST_COMMON_METHOD_COMMENT,
                                     ' * @param initialize'
                                     ' * @return View - Springs representation of the view using the model provided',
                                     ' */',
                                     '@RequestMapping(value = "/api/erp/' + self.JAVA_ENTITY_CONST_DATARESOURCE + '", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)',
                                     'public View ' + self.JAVA_ENTITY_CONST_ENTITY_NAME + 'ReadApi(Model model, @ModelAttribute("QueryParameters") QueryParameters queryParameters,',
                                     self.JAVA_TAB + self.JAVA_TAB + self.JAVA_MTD_CONST_CONTROLLER_AJAX_PARAM + ',\n\t\t\t@RequestParam(value = "initialize", required = false) boolean initialize) {',
                                     '\n',
                                     self.JAVA_TAB + 'if (logger.isDebugEnabled())',
                                     self.JAVA_TAB + self.JAVA_TAB + 'logger.debug("' + self.JAVA_ENTITY_CONST_CONTROLLER_NAME + '.' + self.JAVA_ENTITY_CONST_ENTITY_NAME + 'ReadApi() invoked");',
                                     '\n',
                                     self.JAVA_MTD_CONST_CURRENT_ENTITY_DOMAIN,
                                     self.JAVA_TAB + 'if (initialize) {',
                                     self.JAVA_TAB + self.JAVA_TAB + '// Initialize',
                                     self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' entity = ((' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ') crudProviderService).initialize();',
                                     self.JAVA_TAB + self.JAVA_TAB + 'return getEntityReadView(model, entity);',
                                     self.JAVA_TAB + '} else if (' + self.JAVA_MTD_CONST_PARAM_VERIFY + ') {',
                                     '\n',
                                     self.JAVA_TAB + self.JAVA_TAB + '//List',
                                     self.JAVA_TAB + self.JAVA_TAB + 'return getEntityListView(model, queryParameters);',
                                     self.JAVA_TAB + '} else if (' + self.JAVA_MTD_CONST_PARAM_VERIFY_NON + ') {',
                                     '\n',
                                     self.JAVA_TAB + self.JAVA_TAB + '//Read',
                                     self.JAVA_TAB + self.JAVA_TAB + self.JAVA_ENTITY_CONST_CONTAINER_INTER + ' entity = ',
                                     self.JAVA_TAB + self.JAVA_TAB + self.JAVA_TAB + self.JAVA_TAB + '((' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ') crudProviderService).read(' + self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_VALUE + ');',
                                     '\n',
                                     self.JAVA_TAB + self.JAVA_TAB + 'return getEntityReadView(model, entity);',
                                     self.JAVA_TAB + '} else',
                                     self.JAVA_TAB + self.JAVA_TAB + 'throw new IllegalArgumentException("Key field parameters must all be null or all non-null.");',
                                     self.JAVA_RIGHT_BRACE]
        
        # deleteApi()
        self.JAVA_CONTROLLER_DELETE = ['/**',
                                       ' * Handle API request for Delete action.',
                                       ' *',
                                       ' * @param model',
                                       self.JAVA_MTD_CONST_COMMON_METHOD_COMMENT,
                                       ' @return View - Springs representation of the view using the model provided',
                                       ' */',
                                       '@RequestMapping(value = "/api/erp/' + self.JAVA_ENTITY_CONST_DATARESOURCE + '", method = RequestMethod.DELETE, produces = MediaType.APPLICATION_JSON_VALUE)',
                                       'public @ResponseBody View ' + self.JAVA_ENTITY_CONST_ENTITY_NAME + 'DeleteApi(Model model,',
                                       self.JAVA_TAB + self.JAVA_TAB + self.JAVA_MTD_CONST_CONTROLLER_AJAX_PARAM + ') {',
                                       '\n',
                                       self.JAVA_TAB + 'if (logger.isDebugEnabled())',
                                       self.JAVA_TAB + self.JAVA_TAB + 'logger.debug("' + self.JAVA_ENTITY_CONST_CONTROLLER_NAME + '.' + self.JAVA_ENTITY_CONST_ENTITY_NAME + 'DeleteApi() invoked");',
                                       '\n',
                                       self.JAVA_MTD_CONST_CURRENT_ENTITY_DOMAIN,
                                       self.JAVA_TAB + 'SubmitResultAndData<' + self.JAVA_ENTITY_CONST_CONTAINER_INTER + '> result = ',
                                       self.JAVA_TAB + self.JAVA_TAB + self.JAVA_TAB + '((' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ') crudProviderService).delete(' + self.JAVA_MTD_CONST_FETCH_METHOD_PARAMS_VALUE + ');',
                                       self.JAVA_TAB + 'return getEntityDeleteView(model, result);',
                                       self.JAVA_RIGHT_BRACE]
        
        # standard methods list
        self.JAVA_CONTROLLER_STANDARD_METHODS = [self.JAVA_CONTROLLER_CRAETE_AND_UPDATE,
                                                 self.JAVA_CONTROLLER_READ,
                                                 self.JAVA_CONTROLLER_DELETE]
        
        # serviceImpl import template
        self.JAVA_SERVICEIMPL_IMPORT_TEMP = 'com.qad.erp.financials.%s.service.impl.%s'
        # ajax parameters template
        self.JAVA_MTD_CONST_CONTROLLER_AJAX_PARAM_TEMP = '@RequestParam(value = "%s", required = false) %s %s'
        # holder creater template
        self.JAVA_MTD_CONST_HOLDER_CREATE_TEMP = '%s %s = new %s();'
        # data conversion template
        self.JAVA_MTD_CONST_DATE_CONVERT_TEMP = self.JAVA_TAB + self.JAVA_TAB + 'GregorianCalendar trans%s = new GregorianCalendar();\n\t\tif (%s == null || %s.isEmpty())\n\t\t\ttrans%s = null;\n\t\telse\n\t\t\tFinancialsDataSetUtil.convertDateFromStringToDate(%s, trans%s);\n'
        # BigDecimal initial template
        self.JAVA_MTD_CONST_BIGDECIMAL_INIT_TEMP = self.JAVA_TAB + self.JAVA_TAB + '%s = %s == null? new BigDecimal(0):%s;\n'
        # hashset add template
        self.JAVA_MTD_ADD_HASHSET_TEMP = 'set.add(%s);'
        # create container template
        self.JAVA_MTD_CONST_CONTAINER_CREATE_TEMP = '\t\t%s %sEntity = factory.create%s();\n'
        # assign container template
        self.JAVA_MTD_CONST_CONTAINER_ASSIGN_TEMP = '\t\t((%s) %sEntity)\n\t\t\t\t.setProDataGraph((ProDataGraph) %s.getValue());\n\n'
        # add attribute template
        self.JAVA_MTD_ADD_ATTRIBUTE_TEMP = 'model.addAttribute(%s, %s);'
        # ajax url template
        self.JAVA_CONTROLLER_AJAX_TEMP = '/api/erp/%s/%s'
        
        # datacontroller common function template
        self.JAVA_CONTROLLER_COMMON_FORMAT = ['@RequestMapping(value = "/api/erp/' + self.JAVA_ENTITY_CONST_DATARESOURCE + '/' + self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME + '", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)',
                                              'public View ' + self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME + '(Model model,',
                                              self.JAVA_TAB + self.JAVA_TAB + self.JAVA_MTD_CONST_CONTROLLER_AJAX_PARAM + ') {',
                                              '\n',
                                              self.JAVA_TAB + 'if (logger.isDebugEnabled())',
                                              self.JAVA_TAB + self.JAVA_TAB + 'logger.debug("' + self.JAVA_ENTITY_CONST_CONTROLLER_NAME + '.' + self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME + '() invoked");',
                                              '\n',
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_HOLDER_CREATE,
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_REQUEST_CONVERSION,
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_REQUEST_BIGDEC_INIT,
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_CONTAINER_CREATE,
                                              '\n',
                                              self.JAVA_TAB + '((' + self.JAVA_ENTITY_CONST_SERVICEIMPL_NAME + ') crudProviderService).' + self.JAVA_MTD_CONST_COMMON_MEHTOD_NAME + '(' + self.JAVA_MTD_CONST_COMMON_METHOD_PARAM_CALL + ');\n',
                                              '\n',
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_CONTAINER_ASSIGN,
                                              self.JAVA_TAB + 'Set<String> set = new HashSet<String>();',
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_ADD_HASHSET,
                                              '\n',
                                              self.JAVA_TAB + self.JAVA_MTD_CONST_ADD_ATTRIBUTE,
                                              '\n',
                                              self.JAVA_TAB + 'return createJsonView(set);',
                                              self.JAVA_RIGHT_BRACE]
        
        # general methods comment
        self.JAVA_CONTROLLER_COMMON_COMMENT = ['/**',
                                               ' *',
                                               self.JAVA_MTD_CONST_COMMON_METHOD_COMMENT,
                                               ' * @return View - HttpResponse',
                                               ' */']