from PyQt4 import QtCore

class Node(object):
    def __init__(self):
        self.__sprite = ""
        self.__pos = QtCore.QPointF(0,0)
        self.__scale = QtCore.QPointF(1,1)
        self.__angle = 0
