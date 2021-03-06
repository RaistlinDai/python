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
        impljarfullpath = transDTO.get_finImplJarPath()
        apijarfullpath = transDTO.get_finApiJarPath()
        #workspace full path
        unzip_path = transDTO.get_workspacepath() + fileconstant.UNZIP_JAR_FOLDER
        
        #remove the legacy folder
        if File_processor.verify_dir_existing(unzip_path):
            if not askyesno('Confirm', 'The decompile folder existing, do you want to skip decompile?'):
                File_processor.remove_folder(unzip_path)
            else:
                return
        
        print('Parent process %s.' % os.getpid())
        #process the child processing
        p1 = Process(target=Multiple_processor.jar_decompile_proc, args=('JarDecompile',impljarfullpath, unzip_path+fileconstant.IMPL_FOLDER,))
        p1.start()
        
        p2 = Process(target=Multiple_processor.jar_decompile_proc, args=('JarDecompile',apijarfullpath, unzip_path+fileconstant.API_FOLDER,))
        p2.start()
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
        
        