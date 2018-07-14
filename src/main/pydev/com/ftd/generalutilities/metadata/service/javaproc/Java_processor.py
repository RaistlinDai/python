'''
Created on Jul 11, 2018

@author: ftd
'''
import jpype
import os
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from jpype._jexception import JavaException
from jpype._jpackage import JPackage

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
    def java_load_ftdJD():
        fileconstant = File_constant()
        #--- get the 3rd lib jar path
        root_path = os.path.dirname(os.path.abspath(__file__))
        proj_path = root_path[:root_path.index(fileconstant.MY_PROJECT_PACKAGE)]
        jarpath = proj_path + fileconstant.FTD_JD_JAR + ';' + proj_path + fileconstant.THIRD_JDCORE_JAR
        
        #--- start JVM and point out the jar path
        if not jpype.isJVMStarted():  
            jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % jarpath)
            
        try:
           #--- import the jar class
            javaclass = jpype.JClass('main.java.com.jd.FtdDecompiler')
            
            print(javaclass)
            #--- run java method
            class_pth = 'C:\\Users\\Raistlin\\Desktop\\PyWorkspace\\ftdjd\\test\\reader\\ftdTest.class'
            output_path = 'C:\\Users\\Raistlin\\Desktop\\PyWorkspace\\output\\test.txt'
            javaclass.decompiler(class_pth, output_path)
            
            
        except JavaException as ex: 
            print("Caught exception : ", ex.message())
        
        finally:
            #--- close JVM
            jpype.shutdownJVM()
            
            
            