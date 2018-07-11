'''
Created on Jul 11, 2018

@author: ftd
'''
import jpype
import os
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from jpype._jexception import JavaException

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
        fileconstant = File_constant()
        #--- get the 3rd lib jar path
        curr_path = os.path.dirname(os.path.abspath(__file__))
        proj_path = curr_path[:curr_path.index(fileconstant.MY_PROJECT_PACKAGE)]
        jarpath = proj_path + fileconstant.MY_PROJECT_3RD_LIB_PATH
        
        #--- start JVM and point out the jar path
        if not jpype.isJVMStarted():  
            jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % jarpath)
            
        try:
            #--- import the jar class
            javaclass = jpype.JClass('test.reader.ftdTest')
            #--- create instance
            javaInstance = javaclass('test in python')
            #--- run java method
            result = javaInstance.getFtdTest('FTD', jpype.java.lang.Integer(45))
            print('java result: %s' % result)
        except JavaException as ex: 
            print("Caught exception : ", ex.message())
        except:
            print('Unkonw Error')
        finally:
            #--- close JVM
            jpype.shutdownJVM()
        
    
    
    