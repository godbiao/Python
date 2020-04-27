#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import SkinInstaller_UI
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
Ui_MainWindow = SkinInstaller_UI.Ui_MainWindow

path = ""
install = ""

"""
创建安装类，继承Ui_MainWindow类，以在执行的时候绘制界面
"""


class InstallApk(QtWidgets.QMainWindow, Ui_MainWindow):
    trigger = pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_MainWindow.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        # 连接QPushButton的点击信号到槽函数getDevicesName等
        self.pushButton.clicked.connect(self.getDevicesAttachment)
        self.pushButton_2.clicked.connect(self.filePathMsg)
        self.pushButton_3.clicked.connect(self.install)

    # 获取设备连接信息函数
    def getDevicesAttachment(self):
        devices = []
        devicesname = []
        try:
            for dAttachment in os.popen("adb devices"):  # 打开adb连接设备指令,连接设备
                if "\t" in dAttachment:
                    if dAttachment.find("emulator") < 0:
                        devices.append(dAttachment.split("\t")[0]);
            devices.sort(cmp=None, key=None, reverse=False);
        except:
            pass
        for name in devices:
            # 获取设备类型
            deviceName = os.popen('adb -s ' + name + ' shell getprop ro.product.brand').read()
            # 获取设备型号
            device = os.popen('adb -s ' + name + ' shell getprop ro.product.name ').read()
            deviceName = str(deviceName).replace("\n", "")
            deviceName1 = deviceName + ": " + device
            print(deviceName1)
            devicesname.append(deviceName1)
        print(u"\n设备名称: %s \n总数量:%s台" % (devices, len(devices)));

        if devices == []:
            self.label_8.setText("设备未连接")
        else:
            self.label_8.setText(str(devicesname))
        return devices, devicesname
    # 获取所有手机数量
    x = 0;
    isinstall = False;

    # 选取Apk文件路径函数
    def filePathMsg(self):
        global path  # 定义path（路径）全局变量
        fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
        print(fileName)  # 打印文件全部路径（包括文件名和后缀名）
        path = fileName
        self.label_3.setText(fileName)  # 把路径的名称写进文本框中
    # 获取所有手机数量
    x = 0
    isinstall = False

    def install(self):
        """
        a = InstallApk.getDevicesAttachment(devices)
        if a == []:
            self.label_6.setText("设备未连接")
        else:
            self.label_6.setText("")
        """
        # 每次点击安装按钮，把界面安装日志清空
        self.label_5.setText("")
        self.label_6.setText("")
        # 清空事件
        QApplication.processEvents()
        # 开始安装提示。。。
        self.label_5.setText("安装中...请查看设备")
        # 创建线程对象
        self.workThread = WorkThread()
        # 启动子线程，开始安装操作
        self.workThread.start()
        # 获得子线程执行结束信号，进行安装结果判断，输出结果到界面
        self.workThread.trigger.connect(self.installOut)

    # 子线程执行安装，安装结束之后根据安装结果进行处理
    def installOut(self):
        if "Success" in install:
            self.label_6.setText("安装成功")
        else:
            self.label_6.setText("安装失败")


"""
创建一个线程类，通过重写线程里面的run方法，实现Ui和安装业务逻辑分离，
解决在安装的时候会出现界面会出现“未响应”、“鼠标转圈”的情况
"""


class WorkThread(QThread):
    # 定义一个子线程执行结束，给主线程发送结束信号
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        # 重写run方法
        WorkThread.insatallNow(self)
        # 安装完成后发出信号给主线程
        self.trigger.emit()

    def insatallNow(self):
        devices = self.getAllDevices()
        self.installApk(devices);

    def getAllDevices(self):
        devices = [];
        try:
            for dName_ in os.popen("adb devices"):
                if "\t" in dName_:
                    if dName_.find("emulator") < 0:
                        devices.append(dName_.split("\t")[0]);
            devices.sort(cmp=None, key=None, reverse=False);
        except:
            pass
        print(u"\n设备名称: %s \n总数量:%s台" % (devices, len(devices)));
        return devices

    def installApk(self, devices):
        global x, isinstall, path, install

        for dname in devices:
            try:
                print('Installing...')
                print("adb  -s " + dname + " install -r" + r" C:\Users\Administrator\Desktop\platform-tools\target.apk")
                print("安装文件路径："+path)
                # ADb开始安装
                install = os.popen("adb  -s " + dname + " install -r" + r" " + path).read()
                # install = subprocess.popen("adb  -s "+ dname + " install -r"+ r" "+path)
                if "Success" in install:
                    print(os.popen("adb -s " + dname + " install -r" + r" " + path).read())
                    print("安装成功")
                else:
                    print("安装失败")
                print("处理后的path:" + path)
                # 如果安装出现异常
            except TypeError as e:
                print(e)
                self.label_5.setText(str(e))
    x = 0
    isinstall = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstallApk()
    window.show()  # QT对象显示
    window.getDevicesAttachment()  # 但启动程序的时候就会执行这个函数，自动检测设备连接情况
    sys.exit(app.exec_())
