'''
Created on Jul 27, 2018

@author: ftd
'''
from multiprocessing import Process
import os
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from tkinter.messagebox import askyesno

class Multiple_processor(object):
    '''
    classdocs
    '''

    @staticmethod
    def multiprocessing_service(transDTO):
        '''
        Multiple processing service
        '''
        fileconstant = File_constant()
        #jar full path
        jarfullpath = transDTO.get_finImplJarPath()
        #workspace full path
        unzip_path = transDTO.get_workspacepath() + fileconstant.UNZIP_JAR_FOLDER
        
        #remove the legacy folder
        if File_processor.verify_dir_existing(unzip_path):
            if askyesno('Confirm', 'The decompile folder existing, do you want to cover it?'):
                File_processor.remove_folder(unzip_path)
            else:
                return
        
        print('Parent process %s.' % os.getpid())
        #process the child processing
        p = Process(target=Multiple_processor.jar_decompile_proc, args=('JarDecompile',jarfullpath,unzip_path,))
        p.start()
        # p.join() join will be waiting for the child process
        print('Child process end.')
        
    
    @staticmethod
    def jar_decompile_proc(name, jarfullpath, unzip_path):
        '''
        Jar decompile process
        '''
        print('Run child process %s (%s) start.' % (name, os.getpid()))
        
        #jar unzip
        Java_processor.java_decomp_ftdJD(jarfullpath, unzip_path)
        print('Run child process %s (%s) end.' % (name, os.getpid()))
        
        