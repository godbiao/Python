import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QApplication, QDialog, QVBoxLayout, QMessageBox
from fontTools import subset
import StreamlinedFont_rc


def subSetFont(ff):


    options = subset.Options()  # dir(options)
    font = subset.load_font(ff, options)
    subsetter = subset.Subsetter(options)
    subsetter.populate(text='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-=[]{},./?><\'\\|')
    subsetter.subset(font)
    # options.flavor = 'woff'

    subset.save_font(font, 'font.ttf', options)
    msg('字体精简完成\n请在程序目录下找到font.ttf文件')


def msg(text):
    messageBox = QMessageBox(1, '', '')
    messageBox.setWindowIcon(QIcon(':/windowIcon.png'))
    messageBox.setWindowTitle('提示')
    messageBox.setText(text)
    messageBox.addButton(QPushButton('知道了'), QMessageBox.YesRole)
    messageBox.exec_()


class SelectFontButton(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith('.ttf'):
            e.accept()
        else:
            msg('你拖入了不支持的文件类型')
            e.ignore()

    def dropEvent(self, e):  # 放下文件后的动作
        path = e.mimeData().text().replace('file:///', '')  # 删除多余开头
        subSetFont(path)


class StreamlinedFont(QDialog):
    def __init__(self, parent=None):
        super(StreamlinedFont, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("字体精简")
        self.resize(300, 100)
        self.setFixedSize(300, 100)
        self.setWindowIcon(QIcon(':/windowIcon.png'))
        layout = QVBoxLayout()
        self.button1 = SelectFontButton("选择或拖拽字体文件", self)
        self.button1.clicked.connect(self.clickedButton)
        self.button1.setFixedHeight(60)
        layout.addWidget(self.button1)
        self.setLayout(layout)

    def clickedButton(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选择需要精简的字体", '', "字体文件(*.ttf)")
        subSetFont(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StreamlinedFont()
    main.show()
    sys.exit(app.exec_())