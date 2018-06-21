'''
Created on Jun 20, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.dto.UiObject import UiObject
from src.main.pydev.com.ftd.generalutilities.metadata.dto.Field import Field


obj1 = UiObject(3,6)
print(obj1.get_row())

obj2 = Field(1,8, 'CustPayment', 'CustomerCode')
print(obj2.get_column())

