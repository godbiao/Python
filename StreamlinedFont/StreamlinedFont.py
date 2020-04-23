import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFontDatabase, QFont
from PyQt5.QtWidgets import QPushButton, QApplication, QDialog, QVBoxLayout, QMessageBox, QPlainTextEdit, QLabel, \
    QHBoxLayout, QComboBox
from fontTools import subset
import StreamlinedFont_rc

from fontTools.ttLib import TTFont
from xml.etree.ElementTree import ElementTree
import os


def modFont():
    # 加载字体文件：
    font = TTFont('font.ttf')

    # 转为xml文件：
    font.saveXML('font.xml')

    del font

    def is_contain_chinese(check_str):
        """
        判断字符串中是否包含中文
        :param check_str: {str} 需要检测的字符串
        :return: {bool} 包含返回True， 不包含返回False
        """
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    def is_chinese(string):
        """
        检查整个字符串是否为中文
        Args:
            string (str): 需要检查的字符串,包含空格也是False
        Return
            bool
        """
        for chart in string:
            if chart < u'\u4e00' or chart > u'\u9fff':
                return False

        return True

    def read_xml(in_path):
        '''''读取并解析xml文件
           in_path: xml路径
           return: ElementTree'''
        tree = ElementTree()
        tree.parse(in_path)
        return tree

    def write_xml(tree, out_path):
        '''''将xml文件写出
           tree: xml树
           out_path: 写出路径'''
        tree.write(out_path, encoding="utf-8", xml_declaration=True)

    def if_match(node, kv_map):
        '''''判断某个节点是否包含所有传入参数属性
           node: 节点
           kv_map: 属性及属性值组成的map'''
        for key in kv_map:
            if node.get(key) != kv_map.get(key):
                return False
        return True

    # ----------------search -----------------
    def find_nodes(tree, path):
        '''''查找某个路径匹配的所有节点
           tree: xml树
           path: 节点路径'''
        return tree.findall(path)

    def get_node_by_keyvalue(nodelist, kv_map):
        '''''根据属性及属性值定位符合的节点，返回节点
           nodelist: 节点列表
           kv_map: 匹配属性及属性值map'''
        result_nodes = []
        for node in nodelist:
            if if_match(node, kv_map):
                result_nodes.append(node)
        return result_nodes

    def change_node_text(nodelist, text, is_add=False, is_delete=False):
        '''''改变/增加/删除一个节点的文本
           nodelist:节点列表
           text : 更新后的文本'''
        for node in nodelist:
            if is_add:
                node.text += text
            elif is_delete:
                node.text = ""
            else:
                node.text = text

    tree = read_xml("font.xml")

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "0"})
    change_node_text(text_nodes, "")

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "16"})
    change_node_text(text_nodes, "")

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "17"})
    change_node_text(text_nodes, "")

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "1"})
    newtext = text_nodes[0].text.replace(" ", "")

    if is_contain_chinese(newtext):
        newtext = 'myFont'

    change_node_text(text_nodes, newtext)

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "4"})
    change_node_text(text_nodes, newtext)

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "6"})
    change_node_text(text_nodes, newtext)

    write_xml(tree, "font2.xml")

    font = TTFont()
    font.importXML('font2.xml')
    font.save('font.ttf')

    del font

    os.remove('font.xml')
    os.remove('font2.xml')

    os.startfile(os.getcwd(), 'explore')


def msg(text):
    messageBox = QMessageBox(1, '', '')
    messageBox.setWindowIcon(QIcon(':/windowIcon.png'))
    messageBox.setWindowTitle('提示')
    messageBox.setText(text)
    messageBox.addButton(QPushButton('知道了'), QMessageBox.YesRole)
    messageBox.exec_()


class StreamlinedFont(QDialog):
    def __init__(self, parent=None):
        super(StreamlinedFont, self).__init__(parent)
        self.initUI()
        self.setAcceptDrops(True)

    def initUI(self):
        self.defaultText = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-=[]{},./?><\'\\|'
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle("字体精简小工具")
        self.resize(300, 170)
        self.setFixedSize(300, 170)
        self.setWindowIcon(QIcon(':/windowIcon.png'))

        # self.fontID = QFontDatabase.addApplicationFont('./font.ttf')
        # self.fontName = QFontDatabase.applicationFontFamilies(self.fontID)[0]

        hwg = QtWidgets.QWidget()
        vwg = QtWidgets.QWidget()
        layout = QVBoxLayout()
        layoutH = QHBoxLayout()

        self.label = QLabel("保留的字符:")
        self.label.setFixedHeight(20)
        layoutH.addWidget(self.label)
        self.list = QComboBox()
        self.list.setFixedHeight(20)
        self.list.setFixedWidth(90)
        self.list.addItem('常用')
        self.list.addItem('无符号')
        self.list.addItem('含中文标点')
        self.list.currentIndexChanged.connect(self.listChange)

        layoutH.addWidget(self.list)
        self.textEdit1 = QPlainTextEdit()
        self.textEdit1.setFixedHeight(50)
        self.textEdit1.setPlainText(self.defaultText)

        # self.button1 = SelectFontButton("选择或拖拽字体文件到这里", self)
        self.button1 = QPushButton("选择或拖拽字体文件到这里")
        self.button1.clicked.connect(self.clickedButton)
        self.button1.setFixedHeight(50)
        # self.button1.setFont(QFont(self.fontName, 12))

        hwg.setLayout(layoutH)

        layout.addWidget(hwg)
        layout.addWidget(self.textEdit1)
        layout.addWidget(self.button1)

        self.setLayout(layout)

    def listChange(self, i):
        if i == 0:
            self.textEdit1.setPlainText(self.defaultText)
        elif i == 1:
            self.textEdit1.setPlainText('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        elif i == 2:
            self.textEdit1.setPlainText(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-=[]{},./?><\'\\|，。？；：‘“【】！￥…（）—')
        else:
            pass

    def subSetFont(self, ff):
        options = subset.Options()  # dir(options)
        font = subset.load_font(ff, options)
        subsetter = subset.Subsetter(options)
        t = self.textEdit1.toPlainText()
        subsetter.populate(text=t)
        subsetter.subset(font)
        # options.flavor = 'woff'

        subset.save_font(font, 'font.ttf', options)
        modFont()
        # msg('字体精简完成\n请在程序目录下找到font.ttf文件')

    def clickedButton(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选择需要精简的字体", '', "字体文件(*.ttf)")
        if fileName:
            # subSetFont(fileName)
            self.subSetFont(fileName)

    def dragEnterEvent(self, e):
        text = e.mimeData().text().lower()
        if text.endswith('.ttf'):
            e.accept()
        else:
            msg('暂时不支持的文件类型')
            e.ignore()

    def dropEvent(self, e):  # 放下文件后的动作
        path = e.mimeData().text().replace('file:///', '')  # 删除多余开头
        self.subSetFont(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StreamlinedFont()
    main.show()
    sys.exit(app.exec_())
