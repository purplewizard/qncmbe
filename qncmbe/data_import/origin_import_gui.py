# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'origin_import_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.intro_message = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intro_message.sizePolicy().hasHeightForWidth())
        self.intro_message.setSizePolicy(sizePolicy)
        self.intro_message.setMinimumSize(QtCore.QSize(0, 80))
        self.intro_message.setMaximumSize(QtCore.QSize(16777215, 150))
        self.intro_message.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.intro_message.setFrameShadow(QtWidgets.QFrame.Plain)
        self.intro_message.setReadOnly(True)
        self.intro_message.setBackgroundVisible(False)
        self.intro_message.setObjectName("intro_message")
        self.verticalLayout.addWidget(self.intro_message)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.end_button = QtWidgets.QPushButton(self.centralwidget)
        self.end_button.setObjectName("end_button")
        self.gridLayout.addWidget(self.end_button, 1, 0, 1, 1)
        self.t_step_button = QtWidgets.QPushButton(self.centralwidget)
        self.t_step_button.setObjectName("t_step_button")
        self.gridLayout.addWidget(self.t_step_button, 2, 0, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 0, 0, 1, 1)
        self.end = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.end.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end.setObjectName("end")
        self.gridLayout.addWidget(self.end, 1, 2, 1, 1)
        self.start = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.start.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 2, 1, 1)
        self.path_button = QtWidgets.QPushButton(self.centralwidget)
        self.path_button.setObjectName("path_button")
        self.gridLayout.addWidget(self.path_button, 3, 0, 1, 1)
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 3, 2, 1, 1)
        self.start_label = QtWidgets.QLabel(self.centralwidget)
        self.start_label.setObjectName("start_label")
        self.gridLayout.addWidget(self.start_label, 0, 1, 1, 1)
        self.end_label = QtWidgets.QLabel(self.centralwidget)
        self.end_label.setObjectName("end_label")
        self.gridLayout.addWidget(self.end_label, 1, 1, 1, 1)
        self.file_button = QtWidgets.QPushButton(self.centralwidget)
        self.file_button.setObjectName("file_button")
        self.gridLayout.addWidget(self.file_button, 4, 0, 1, 1)
        self.t_step_label = QtWidgets.QLabel(self.centralwidget)
        self.t_step_label.setObjectName("t_step_label")
        self.gridLayout.addWidget(self.t_step_label, 2, 1, 1, 1)
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setObjectName("path_label")
        self.gridLayout.addWidget(self.path_label, 3, 1, 1, 1)
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setObjectName("file_label")
        self.gridLayout.addWidget(self.file_label, 4, 1, 1, 1)
        self.file = QtWidgets.QLineEdit(self.centralwidget)
        self.file.setObjectName("file")
        self.gridLayout.addWidget(self.file, 4, 2, 1, 1)
        self.t_step = QtWidgets.QLineEdit(self.centralwidget)
        self.t_step.setText("")
        self.t_step.setObjectName("t_step")
        self.gridLayout.addWidget(self.t_step, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_button.sizePolicy().hasHeightForWidth())
        self.import_button.setSizePolicy(sizePolicy)
        self.import_button.setMinimumSize(QtCore.QSize(0, 30))
        self.import_button.setMaximumSize(QtCore.QSize(16777215, 30))
        self.import_button.setFlat(False)
        self.import_button.setObjectName("import_button")
        self.verticalLayout.addWidget(self.import_button)
        self.runtime_messages = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runtime_messages.sizePolicy().hasHeightForWidth())
        self.runtime_messages.setSizePolicy(sizePolicy)
        self.runtime_messages.setMinimumSize(QtCore.QSize(0, 40))
        self.runtime_messages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.runtime_messages.setFrameShadow(QtWidgets.QFrame.Plain)
        self.runtime_messages.setReadOnly(True)
        self.runtime_messages.setTabStopWidth(85)
        self.runtime_messages.setBackgroundVisible(False)
        self.runtime_messages.setObjectName("runtime_messages")
        self.verticalLayout.addWidget(self.runtime_messages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.start_button, self.start)
        MainWindow.setTabOrder(self.start, self.end_button)
        MainWindow.setTabOrder(self.end_button, self.end)
        MainWindow.setTabOrder(self.end, self.t_step_button)
        MainWindow.setTabOrder(self.t_step_button, self.t_step)
        MainWindow.setTabOrder(self.t_step, self.path_button)
        MainWindow.setTabOrder(self.path_button, self.path)
        MainWindow.setTabOrder(self.path, self.file_button)
        MainWindow.setTabOrder(self.file_button, self.file)
        MainWindow.setTabOrder(self.file, self.import_button)
        MainWindow.setTabOrder(self.import_button, self.runtime_messages)
        MainWindow.setTabOrder(self.runtime_messages, self.intro_message)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Origin data import wizard"))
        self.intro_message.setPlainText(_translate("MainWindow", "This tool imports Molly, LabView, and SVT data into Origin for plotting. This will be saved as a new Origin file under \"Path\\Filename\"\n"
"\n"
"Note:\n"
"Make sure insitu has up-to-date data before running this script! (Molly binaries and SVT data may need to be synced.)"))
        self.end_button.setText(_translate("MainWindow", "Set default"))
        self.t_step_button.setText(_translate("MainWindow", "Set default"))
        self.start_button.setText(_translate("MainWindow", "Set default"))
        self.end.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.start.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd HH:mm:ss"))
        self.path_button.setText(_translate("MainWindow", "Set default"))
        self.start_label.setText(_translate("MainWindow", "Start time"))
        self.end_label.setText(_translate("MainWindow", "End time"))
        self.file_button.setText(_translate("MainWindow", "Set default"))
        self.t_step_label.setText(_translate("MainWindow", "Time step (s)"))
        self.path_label.setText(_translate("MainWindow", "Path"))
        self.file_label.setText(_translate("MainWindow", "Filename"))
        self.import_button.setText(_translate("MainWindow", "Import data!"))
        self.runtime_messages.setPlainText(_translate("MainWindow", "(Runtime messages will appear here.)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

