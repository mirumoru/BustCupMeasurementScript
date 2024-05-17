# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication

#.measureがファイル名でMeasureWindowがクラス名
from .measure import MeasureWindow

def distance():
    qap = QApplication.instance()
    if(qap==None):
        qap = QApplication(sys.argv)
    measure = MeasureWindow()
    measure.show()
    return measure

'''
定形 ファイル名
import measure
ファイル名 def名
measure.measure()
'''
