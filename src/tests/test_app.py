# import  pytest
# import os, sys, platform
# from PyQt5.QtGui import QIcon, QKeySequence, QPalette, QColor
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication
# from app.py import MainWindow, dark_mode, ligh_mode
#
# app = QApplication(sys.argv)
# app.setWindowIcon(QIcon(':/icons/pastaq.png'))
# if platform.system() == 'Windows':
#     import ctypes
#     ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('pastaq-gui')
# app.setStyle("Fusion")
#
# mainWindow = MainWindow()
# mainWindow.resize(QSize(600, 600))
# mainWindow.show()
#
# # Start the event loop.
# app.exec()
#
# def test_init_light_mode():
#     assert mainWindow.dark == False
#

#
# also optimize your imports, when you want to mock something, you have to mock it from the file that imports it and not here
import sys, os
import pytest
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMenuBar, QMenu
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # fixed this for importing app properly
import app

# this is the application stuff that i meant
application = QApplication(sys.argv)
mainWindow = app.MainWindow()

def test_init_light_mode():
    assert not mainWindow.dark

# def test_change_dark_mode():
#     mainWindow = MainWindow()
#     app = QApplication(sys.argv)
#     app.processEvents()
#     dark_mode()
#     pp = QApplication(sys.argv)
#     pp.processEvents()
#
#     # app.exec_()
#     assert mainWindow.dark == True
#
# def test_change_light_mode():
#     dark_mode()
#     light_mode()
#     assert mainWindow.dark == False

def test_icon():
    testIcon = mainWindow.init_logo()
    pixmap = QPixmap(':/icons/pastaq.png')
    pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
    icon = QLabel()
    icon.setPixmap(pixmap)
    assert icon.layout() == testIcon.layout()
    assert icon.font() == testIcon.font()
    assert icon.height() == testIcon.height()
    assert icon.picture() == testIcon.picture()

def test_menu_bar():
    menu_bar = mainWindow.findChildren(QMenuBar)
    assert len(menu_bar) == 1

def test_file_menu():
    file_menu = mainWindow.findChildren(QMenu)
    assert mainWindow.fileMenu in file_menu

def test_action_menu():
    action_menu = mainWindow.findChildren(QMenu)
    assert mainWindow.actionMenu in action_menu

def test_help_menu():
    help_menu = mainWindow.findChildren(QMenu)
    assert mainWindow.fileMenu in help_menu

def test_number_menu():
    menus = mainWindow.findChildren(QMenu)
    assert len(menus) == 3

# test_app is unnecessary because everything will be executed with pytest anyways, so i dont get why this is needed
# since no other test file has this, we should stay consistent
def test_app():
    test_init_light_mode()
    # test_change_dark_mode()
    # test_change_light_mode()
    test_icon()
    test_menu_bar()
    test_help_menu()
    test_file_menu()
    test_action_menu()
