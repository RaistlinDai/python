'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.dto.UiObject import UiObject
from src.main.pydev.com.ftd.generalutilities.dto.Field import Field


obj1 = UiObject('a', 3)
print(obj1.get_row())

obj2 = Field(1,8, 'CustPayment', 'CustomerCode')
print(obj2.get_column())

