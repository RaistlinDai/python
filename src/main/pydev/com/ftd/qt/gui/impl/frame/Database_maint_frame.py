'''
Created on Jul 22, 2019

@author: ftd

pip install PyQt5
pip install PyQt5-tools

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Database_maint_frame(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI() #界面绘制交给InitUi方法
        
        
    def initUI(self):
        #设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)  
        #设置窗口的标题
        self.setWindowTitle('Database maintain')
        #设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.png'))        
        
        #显示窗口
        self.show()