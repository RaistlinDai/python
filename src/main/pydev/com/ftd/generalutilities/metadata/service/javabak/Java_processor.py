'''
Created on Jul 11, 2018

@author: ftd
'''
import jpype

class Java_processor(object):
    '''
    before compiling this class, you have to install jpype and numpy in Python
    '''

    @staticmethod
    def java__tester():
        jvmPath = jpype.getDefaultJVMPath() 
        jpype.startJVM(jvmPath) 
        jpype.java.lang.System.out.println('hello world!')
        jpype.shutdownJVM()
        
    
    @staticmethod
    def java_3rd_tester():
        #jarpath = '/3rd/lib/jar/FTD.jar'
        jarpath = 'C:\\Users\\ftd\\Desktop\\PyWorkspace\\FTD.jar'
        #--- start JVM and point out the jar path
        jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % jarpath)
        #--- import the jar class
        javaclass = jpype.JClass('test.reader.ftdTest')
        #--- create instance
        javaInstance = javaclass('test in python')
        #--- run java method
        result = javaInstance.getFtdTest('FTD', jpype.java.lang.Integer(45))
        print('java result: %s' % result)
        
        jpype.shutdownJVM()