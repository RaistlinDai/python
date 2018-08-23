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
        
        self.JAVA_FUNCTION_CREATE = 'create'
        self.JAVA_FUNCTION_UPDATE = 'update'
        self.JAVA_FUNCTION_DELETE = 'delete'
        self.JAVA_FUNCTION_FETCH = 'fetch'
        self.JAVA_FUNCTION_CLEARINST = 'clearInstance'
        
        # --- impl jar service
        self.JAVA_IMPL_PACKAGE_PREFIX = 'com.qad.financials.'
        
        
        # ---------------------------------------------------------------- #
        #                  annotation                                      #
        # ---------------------------------------------------------------- #
        self.JAVA_ANNOTATION_SERVICE = '@Service(\"%s\")'
        self.JAVA_ANNOTATION_OVERRIDE = '@Override'
        
        # ---------------------------------------------------------------- #
        #                  serviceImpl.java                                #
        # ---------------------------------------------------------------- #
        self.JAVA_ENTITY_TITLE = '/*******************************************************************************\n * Copyright 2015 QAD Inc. All rights reserved.\n ******************************************************************************/\n'
        
        self.JAVA_ENTITY_SERVICEIMPL_PACKAGE = 'com.qad.erp.financials.%s.service.impl'
        self.JAVA_ENTITY_DATACONTROLLER_PACKAGE = 'com.qad.erp.financials.%s.mvc.controller.data'
        
        self.JAVA_SERVICE_HEADER = 'public class %s extends FinQraEntityService<%s, %s> {'
        
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
        # initialize()
        self.JAVA_SERVICE_OVERRIDE_INITIALIZE = [self.JAVA_ANNOTATION_OVERRIDE,
                                                 'public %s initialize() {',
                                                 self.JAVA_TAB + 'String str1 = QraWorkspaceUtil.getFinancialEntityCode(sessionDataHolder.getCurrentWorkspace());',
                                                 '\n',
                                                 self.JAVA_TAB + '%s container = (%s) factory.%s();',
                                                 '\n',
                                                 self.JAVA_TAB + 'Holder<DataGraph> holder = new Holder<DataGraph>((DataGraph) container.getProDataGraph());',
                                                 '\n',
                                                 self.JAVA_TAB + 'Holder<String> %sHolder = new com.qad.qra.Holder<String>();',
                                                 '\n',
                                                 self.JAVA_TAB + 'factory.get%s().%s(str1, holder, %sHolder);',
                                                 self.JAVA_TAB + 'container.setProDataGraph((ProDataGraph) holder.getValue());',
                                                 self.JAVA_TAB + 'return container;',
                                                 self.JAVA_RIGHT_BRACE]
        
        self.JAVA_SERVICE_OVERRIDE_getEntityFactory = [self.JAVA_ANNOTATION_OVERRIDE,
                                                       'protected %s getEntityFactory(ConnectionManager connectionManager, Context context) {',
                                                       self.JAVA_TAB + 'return new %s(connectionManager, context);',
                                                       self.JAVA_RIGHT_BRACE]
        
        