'''
Created on Jul 27, 2018

@author: ftd
'''
from multiprocessing import Process
import os
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor

class Multiple_processor(object):
    '''
    classdocs
    '''

    @staticmethod
    def multiprocessing_service(transDTO):
        '''
        Multiple processing service
        '''
        print('Parent process %s.' % os.getpid())
        #jar full path
        jarfullpath = transDTO.get_finImplJarPath()
        #workspace full path
        workfullpath = transDTO.get_workspacepath()
        #process the child processing
        p = Process(target=Multiple_processor.jar_decompile_proc, args=('JarDecompile',jarfullpath,workfullpath,))
        p.start()
        # p.join() join will be waiting for the child process
        print('Child process end.')
        
    
    @staticmethod
    def jar_decompile_proc(name, jarfullpath, workfullpath):
        '''
        Jar decompile process
        '''
        print('Run child process %s (%s)...' % (name, os.getpid()))
        fileconstant = File_constant()
        unzip_path = workfullpath + fileconstant.UNZIP_JAR_FOLDER
        
        #remove the legacy folder
        if File_processor.verify_dir_existing(unzip_path):
            File_processor.remove_folder(unzip_path)
        
        #jar unzip
        Java_processor.java_decomp_ftdJD(jarfullpath, unzip_path)
        
        
        