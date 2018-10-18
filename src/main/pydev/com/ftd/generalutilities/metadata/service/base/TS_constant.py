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
        
        # ----------------- types ------------------
        self.TS_TYPE_STRING = 'string'
        self.TS_TYPE_BOOLEAN = 'boolean'
        self.TS_TYPE_NUMBER = 'number'
        self.TS_TYPE_DATE = 'Date'
        
        # ----------------- function prefix ------------------
        self.TS_HTTPRESPONSE_PREFIX = 'HttpResponse'
        
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
        
        # observable object header
        self.TS_OBSERVABLE_OBJ_HEADER = 'namespace com.qad.financials.%s.%s.TSHandler.%s.DTO.UI {\n' + self.TS_TAB + '\'use strict\';\n'
        
        
        # observable object template
        self.TS_OBSERVABLE_OBJ_RESPONSE_TEMPLATE = 'export interface HttpResponse%s {\n%s \n    }\n'
        
        # observable object import template
        self.TS_OBSERVABLE_OBJ_NAMESPACE_TEMP = 'import %s = %sTSHandler.%s.DTO.%s;'
        
        # observable object reference template
        self.TS_OBSERVABLE_OBJ_REFERENCE_TEMP = '/// <reference path="../%s/ds%s.ts" />'
        