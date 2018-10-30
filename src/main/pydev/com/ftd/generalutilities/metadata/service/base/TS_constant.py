'''
Created on Sep 6, 2018

@author: ftd
'''

class TS_constant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        # TS end flag
        self.TS_END_MARK = ';'
        self.TS_SEPERATOR = ','
        self.TS_DOT_MARK = '.'
        self.TS_UNDERLINE = '_'
        self.TS_RIGHT_BRACKET = ')'
        self.TS_LEFT_BRACKET = '('
        self.TS_RIGHT_BRACE = '}'
        self.TS_LEFT_BRACE = '{'
        self.TS_LEFT_COMMENT = '/*'
        self.TS_RIGHT_COMMENT = '*/'
        self.TS_LEFT_DASH = '<'
        self.TS_RIGHT_DASH = '>'
        self.TS_TAB = '    '
        self.TS_COLON = ':'
        self.TS_QUESTION_MARK = '?'
        self.TS_SQUARE_BRACKETS = '[]'
        
        # ----------------- types ------------------
        self.TS_TYPE_STRING = 'string'
        self.TS_TYPE_BOOLEAN = 'boolean'
        self.TS_TYPE_NUMBER = 'number'
        self.TS_TYPE_DATE = 'Date'
        
        # ----------------- function prefix ------------------
        self.TS_HTTPRESPONSE_PREFIX = 'HttpResponse'
        self.TS_EXPORT_INTERFACE_PREFIX = 'export interface '
        
        # ----------------- TS module key word ---------------
        self.TS_KEYWORD_MODULE = 'module'
        
        # common references
        self.TS_REFERENCE_COMMON_ANGULAR = '/// <reference path="../../../../../../Lib/DefinitelyTyped/angular/angular.d.ts" />'
        self.TS_REFERENCE_COMMON_JQUERY = '/// <reference path="../../../../../../Lib/DefinitelyTyped/jquery/jquery.d.ts" />'
        self.TS_REFERENCE_COMMON_KENDO = '/// <reference path="../../../../../../Lib/kendo/kendo.all.d.ts" />'
        self.TS_REFERENCE_COMMON_UTILS = '/// <reference path="../../../../../../Lib/Qad/utils.d.ts" />'
        self.TS_REFERENCE_COMMON_QADTS = '/// <reference path="../../../../../../qad-ts.d.ts" />'
        
        self.TS_REFERENCE_COMMON_REFERENCES = [self.TS_REFERENCE_COMMON_ANGULAR,
                                               self.TS_REFERENCE_COMMON_JQUERY,
                                               self.TS_REFERENCE_COMMON_KENDO,
                                               self.TS_REFERENCE_COMMON_UTILS,
                                               self.TS_REFERENCE_COMMON_QADTS]
        
        # util references
        self.TS_REFERENCE_UTIL_GENERAL = '/// <reference path="../../util/services/GeneralUtilities.ts" />'
        self.TS_REFERENCE_UTIL_FIN_WEB = '/// <reference path="../../util/services/FinancialsWebUIService.ts" />'
        self.TS_REFERENCE_UTIL_VALIDATOR = '/// <reference path="../../util/services/Validator.ts" />'
        
        self.TS_REFERENCE_UTIL_REFERENCES = [self.TS_REFERENCE_UTIL_GENERAL,
                                             self.TS_REFERENCE_UTIL_FIN_WEB,
                                             self.TS_REFERENCE_UTIL_VALIDATOR]
        
        # observable object header
        self.TS_OBSERVABLE_OBJ_HEADER = 'namespace com.qad.financials.%s.%s.TSHandler.%s.DTO.UI {\n' + self.TS_TAB + '\"use strict\";\n'
        
        # observable object template
        self.TS_OBSERVABLE_OBJ_RESPONSE_TEMPLATE = 'export interface HttpResponse%s {\n%s \n    }\n'
        
        # observable object import template
        self.TS_OBSERVABLE_OBJ_NAMESPACE_TEMP = 'import %s = %sTSHandler.%s.DTO.%s;'
        
        # observable object reference template
        self.TS_OBSERVABLE_OBJ_REFERENCE_TEMP = '/// <reference path="../%s/ds%s.ts" />'
        
        # ts module suffix
        self.TS_DTO_MODULE = '.DTO'
        self.TS_DTO_UI_MODULE = '.DTO.UI'
        
        # constant file header
        self.TS_CONSTANT_HEADER = 'namespace com.qad.erp.financials.%s.%s {\n' + self.TS_TAB + '\"use strict\";\n'
        
        # constant file field template
        self.TS_CONSTANT_FIELD_LINE_TEMP = self.TS_TAB + self.TS_TAB + '%s: "%s",\n'
        
        # constant field interface template
        self.TS_CONSTANT_FIELDS_TEMP = self.TS_TAB + 'export const %sControls = {\n%s\n' + self.TS_TAB + '};\n\n'
        
        # constant grid interface template
        self.TS_CONSTANT_GRIDS_TEMP = self.TS_TAB + 'export const %sDataGrids = {\n%s\n' + self.TS_TAB + '};\n\n'
        
        # constant grid field interface template
        self.TS_CONSTANT_GRIDFIELD_TEMP = self.TS_TAB + 'export const %sFields = {\n%s\n' + self.TS_TAB + '};\n\n'
        
        
        # TS CommonService header
        self.TS_COMMONSERVICE_HEADER = 'namespace com.qad.erp.financials.%s.%s {\n' + self.TS_TAB + '\"use strict\";\n'
        
        # TS CommonService import
        self.TS_FIN_COMMONSERVICE_IMPORT = 'import FinancialsCommonService = com.qad.erp.financials.common.services.FinancialsWebUIService;'
        self.TS_DTO_IMPORT_TEMP = 'import %s = com.qad.financials.%s.%s.TSHandler.%s.DTO.%s;'
        