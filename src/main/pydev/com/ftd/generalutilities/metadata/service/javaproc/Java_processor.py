'''
Created on Jul 10, 2018

@author: ftd
'''
from jpype import *
import jpype

class Java_processor(object):
    '''
    classdocs
    '''


    @staticmethod
    def jar_reader():
        # jvmPath = jpype.getDefaultJVMPath() 
        jvmPath = ur'D:\jre-8u151-windows-i586\jre1.8.0_151\bin\client\jvm.dll'
        jpype.startJVM(jvmPath) 
        jpype.java.lang.System.out.println("hello world!")
        jpype.shutdownJVM()
