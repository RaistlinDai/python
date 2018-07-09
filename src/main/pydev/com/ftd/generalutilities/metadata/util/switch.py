'''
Created on Jul 6, 2018

@author: ftd
'''

class switch(object):
    '''
    classdocs
    '''
    def __init__(self, value):
        self.__value = value
        self.__fall = False

    def __iter__(self):
        '''
        Iterator: return the match method once, then stop
        '''
        yield self.__match
        raise StopIteration
    
    
    def __match(self, *args):
        '''
        Generator: indicate whether or not to enter a case suite
        '''
        if self.__fall or not args:
            return True
        elif self.__value in args: # changed for v1.5, see below
            self.__fall = True
            return True
        else:
            return False