# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uninstall_pifu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

""" 安卓装包器界面绘制，使用Qt designer设计界面，把ui文件转换成py文件就可生成一下代码 """


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 380)
        MainWindow.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 170, 48, 21))
        self.label.setStyleSheet("color: rgb(232, 232, 232);\n" "background-color: rgb(35, 35, 35);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 220, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(232, 232, 232);\n" "background-color: rgb(57, 57, 57);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 170, 201, 21))
        self.label_3.setStyleSheet("color: rgb(232, 232, 232);\n" "background-color: rgb(156, 156, 156);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 0, 161, 31))
        self.label_2.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 220, 75, 23))
        self.pushButton_3.setStyleSheet("color: rgb(232, 232, 232);\n" "background-color: rgb(57,57, 57);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 170, 75, 23))
        self.pushButton_2.setStyleSheet("color: rgb(232, 232, 232);\n" "background-color: rgb(57, 57, 57);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 361, 121))
        self.textEdit.setStyleSheet("color: rgb(232, 232, 232);\n" "background-color: rgb(50, 50, 50);")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 111, 21))
        self.label_4.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 120, 20))
        self.label_5.setStyleSheet("background-color: rgb(35, 35, 35);\n" "color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 111, 20))
        self.label_6.setStyleSheet("background-color: rgb(35, 35, 35);\n" "color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 111, 21))
        self.label_7.setStyleSheet("background-color: rgb(35, 35, 35);\n" "color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 40, 161, 16))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 60, 161, 20))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 80, 161, 20))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(370, 100, 161, 20))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(370, 300, 61, 20))
        self.label_12.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 320, 161, 16))
        self.label_13.setStyleSheet("color: rgb(232, 232, 232);")
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "安卓装包器"))
        self.label.setText(_translate("MainWindow", "请选择："))
        self.pushButton.setText(_translate("MainWindow", "连接检测"))
        self.label_3.setText(_translate("MainWindow", "未选择"))
        self.label_2.setText(_translate("MainWindow", "已连接设备："))
        self.pushButton_3.setText(_translate("MainWindow", "安装"))
        self.pushButton_2.setText(_translate("MainWindow", "选择路径"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" 
                                                       "<html><head><meta   name=\"qrichtext\" content=\"1\" /><style "
                                                       "type=\"text/css\">\n" "p,   li { white-space: pre-wrap; }\n" 
                                                       "</style></head><body style=\" font-family:\'SimSun\'; "
                                                       "font-size:9pt; font-weight:400; font-style:normal;\">\n" "<p "
                                                       "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                       "margin-right:0px;-qt-block-indent:0; text-indent:0px;\"><span "
                                                       "style=\" font-size:10pt;\">使用说明</span></p>\n" "<p style=\" "
                                                       "margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                       "margin-right:0px;-qt-block-indent:0; text-indent:0px;\"><span "
                                                       "style=\" font-size:10pt;\">1、手动操作</span></p>\n" "<p style=\" "
                                                       "margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                       "margin-right:0px; -qt-block-indent:0; "
                                                       "text-indent:0px;\"><span style=\" "
                                                       "font-size:10pt;\">（1）在真机上手动打开[开发者模式-打开USB调试模式]  "
                                                       "</span></p>\n" "<p style=\" margin-top:0px; "
                                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                       "-qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                                       "font-size:10pt;\">（2）使用UBS线连接手机到电脑</span></p>\n" "<p style=\" "
                                                       "margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                       "margin-right:0px; -qt-block-indent:0; "
                                                       "text-indent:0px;\"><span  style=\" "
                                                       "font-size:10pt;\">（3）部分机型连接电脑后弹出几种连接模式，默认选择[仅充电]，需要手动选择["
                                                       "文件传输]</span></p>\n"  "<p style=\" margin-top:0px; "
                                                       "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                       "-qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                                       "font-size:10pt;\">2、装包操作</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "安装日志："))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt;\">版本 2.0.0</span></p></body></html>"))