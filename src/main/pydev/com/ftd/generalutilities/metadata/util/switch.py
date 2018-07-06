'''
Created on Jul 6, 2018

@author: ftd
'''

class switch(object):
    '''
    classdocs
    '''
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        '''
        Iterator: return the match method once, then stop
        '''
        yield self.match
        raise StopIteration
    
    
    def match(self, *args):
        '''
        Generator: indicate whether or not to enter a case suite
        '''
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False