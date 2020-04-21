import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QApplication, QDialog, QVBoxLayout, QMessageBox
from fontTools import subset
import StreamlinedFont_rc

from fontTools.ttLib import TTFont
from xml.etree.ElementTree import ElementTree
from xpinyin import Pinyin
import os


def modFont():
    # 加载字体文件：
    font = TTFont('font.ttf')

    # 转为xml文件：
    font.saveXML('font.xml')

    def is_chinese(string):
        """
        检查整个字符串是否包含中文
        :param string: 需要检查的字符串
        :return: bool
        """
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True

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
    if is_chinese(newtext):
        p = Pinyin()
        newtext = p.get_pinyin(newtext, '')

    change_node_text(text_nodes, newtext)

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "4"})
    change_node_text(text_nodes, newtext)

    text_nodes = get_node_by_keyvalue(find_nodes(tree, "name/namerecord"), {"nameID": "6"})
    change_node_text(text_nodes, newtext)

    write_xml(tree, "font2.xml")

    font = TTFont()
    font.importXML('font2.xml')
    font.save('font.ttf')

    os.remove('font.xml')
    os.remove('font2.xml')
    os.startfile(os.getcwd())


def subSetFont(ff):
    options = subset.Options()  # dir(options)
    font = subset.load_font(ff, options)
    subsetter = subset.Subsetter(options)
    subsetter.populate(text='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-=[]{},./?><\'\\|')
    subsetter.subset(font)
    # options.flavor = 'woff'

    subset.save_font(font, 'font.ttf', options)
    modFont()
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