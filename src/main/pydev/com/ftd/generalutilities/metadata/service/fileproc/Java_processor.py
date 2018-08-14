'''
Created on Jul 11, 2018

@author: ftd
'''
import jpype
import os
import zipfile
from jpype._jexception import JavaException
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base import Java_constant
from src.main.pydev.com.ftd.generalutilities.metadata.dto.javaFile.JavaDTO import JavaDTO

class Java_processor(File_processor):
    '''
    This class is used to process the Java and Jar files
    Note: before compiling this class, you have to install jpype and numpy in Python
    '''
    
    @staticmethod
    def verify_jar_type(dir_path):
        '''
        verify the jar file type
        @param dir_path: file directory
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_file(dir_path):
            return False, "The jar file is not exist, please check."
        
        ftype = Java_processor.get_file_type(dir_path)
                
        if ftype == 'unknown':
            return False, 'The file type is unknown!'
        
        if ftype != 'jar':
            return False, 'The file type(%s) is not (jar) !' % ftype
        
        return True, None
        

    @staticmethod
    def java__tester():
        '''
        tester function for reading java
        '''
        jvmPath = jpype.getDefaultJVMPath() 
        jpype.startJVM(jvmPath) 
        jpype.java.lang.System.out.println('hello world!')
        jpype.shutdownJVM()
        
    
    @staticmethod
    def java_decomp_ftdJD(srcfile, dcpfile):
        '''
        decompile the jar to the target directory
        @param srcfile: the jar file
        @param dcpfile: the decompiled directory
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!"
        
        fileconstant = File_constant()
        #--- get the 3rd lib jar path
        root_path = os.path.dirname(os.path.abspath(__file__))
        proj_path = root_path[:root_path.index(fileconstant.MY_PROJECT_PACKAGE)]
        #--- java class path
        jarpath = proj_path + fileconstant.FTD_JD_JAR + ';' + proj_path + fileconstant.THIRD_JDCORE_JAR
        
        #--- start JVM and point out the jar path
        if not jpype.isJVMStarted():  
            jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % jarpath)
            
        try:
            #--- import the jar class
            javaclass = jpype.JClass('main.java.com.jd.FtdDecompiler')
            #--- run java method
            javaclass.jarDecompiler(srcfile, dcpfile)
            
            return True, None
        except JavaException as ex: 
            print("Caught exception : ", ex.message())
            return False, ex.message()
        finally:
            #--- close JVM
            jpype.shutdownJVM()
            
    
    @staticmethod
    def unzip_jar(srcfile, outdir, deep_unzip=False):
        '''
        unzip the jar to the target directory
        @param srcfile: the jar file
        @param outdir: the output directory
        @param deep_unzip: if unzip the inner jar also
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!"
        
        if not File_processor.verify_dir_existing(outdir):
            os.makedirs(outdir)
        
        fileconstant = File_constant()
        
        if fileconstant.JAR_SUFFIX in srcfile:
            zfile = zipfile.ZipFile(srcfile, 'r')  
            zfile.extractall(outdir)  
            zfile.close
        else:
            return False, "The source file is not jar!"
        
        #--- unzip all inner jars
        if deep_unzip:
            for fullname in File_processor.dir_iterbrowse(outdir):
                #get the inner jar files
                if (fileconstant.JAR_SUFFIX in fullname):
                    inner_jar_outdir = fullname[:fullname.index(fileconstant.JAR_SUFFIX)]
                    result, message = Java_processor.unzip_jar(fullname, inner_jar_outdir, deep_unzip)
                    if not result:
                        return False, "Deep unzip failed!"

        return True, None
    
    
    @staticmethod
    def read_java_file(srcfile):
        '''
        read and analysis the java file, output the information in JavaDTO
        NOTE: this is a light weight reador for java file. Generally we should use java reflection
        @param srcfile: the java file
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!", None
        
        javaconstant = Java_constant()
        javaDTO = JavaDTO()
        
        file = open(srcfile, 'r')
        # read java file line by line
        for eachline in file.readlines():
            # split the line by blank
            cells = eachline.split(' ')
            
            if javaconstant.JAVA_KEY_PACKAGE in cells:
                javaDTO.set_class_package(cells[cells.index(javaconstant.JAVA_KEY_PACKAGE)+1])
        
        file.close()
        return True, None, javaDTO
        
        
    @staticmethod
    def read_java_keyword(cells):
        
        pass
        