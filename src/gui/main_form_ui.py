# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created: Fri Oct  7 23:08:25 2011
#      by: PySide UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = DragDropGraphicsView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuProcessing = QtGui.QMenu(self.menubar)
        self.menuProcessing.setObjectName("menuProcessing")
        MainWindow.setMenuBar(self.menubar)
        self.blockTreeDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blockTreeDock.sizePolicy().hasHeightForWidth())
        self.blockTreeDock.setSizePolicy(sizePolicy)
        self.blockTreeDock.setFloating(False)
        self.blockTreeDock.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.blockTreeDock.setObjectName("blockTreeDock")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.blocks_tree = QtGui.QTreeWidget(self.dockWidgetContents)
        self.blocks_tree.setDragEnabled(True)
        self.blocks_tree.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.blocks_tree.setObjectName("blocks_tree")
        self.blocks_tree.headerItem().setText(0, "1")
        self.blocks_tree.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.blocks_tree)
        self.blockTreeDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.blockTreeDock)
        self.previewDock = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewDock.sizePolicy().hasHeightForWidth())
        self.previewDock.setSizePolicy(sizePolicy)
        self.previewDock.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.previewDock.setObjectName("previewDock")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.keepPreview1 = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.keepPreview1.setObjectName("keepPreview1")
        self.verticalLayout_3.addWidget(self.keepPreview1)
        self.previewImage1 = QtGui.QLabel(self.dockWidgetContents_2)
        self.previewImage1.setFrameShape(QtGui.QFrame.Box)
        self.previewImage1.setFrameShadow(QtGui.QFrame.Sunken)
        self.previewImage1.setObjectName("previewImage1")
        self.verticalLayout_3.addWidget(self.previewImage1)
        self.line = QtGui.QFrame(self.dockWidgetContents_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.keepPreview2 = QtGui.QCheckBox(self.dockWidgetContents_2)
        self.keepPreview2.setObjectName("keepPreview2")
        self.verticalLayout_3.addWidget(self.keepPreview2)
        self.previewImage2 = QtGui.QLabel(self.dockWidgetContents_2)
        self.previewImage2.setFrameShape(QtGui.QFrame.Box)
        self.previewImage2.setFrameShadow(QtGui.QFrame.Sunken)
        self.previewImage2.setObjectName("previewImage2")
        self.verticalLayout_3.addWidget(self.previewImage2)
        self.previewDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.previewDock)
        self.propertiesDock = QtGui.QDockWidget(MainWindow)
        self.propertiesDock.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.propertiesDock.setObjectName("propertiesDock")
        self.propertiesContents = QtGui.QWidget()
        self.propertiesContents.setObjectName("propertiesContents")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.propertiesContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.propertyTable = QtGui.QTableView(self.propertiesContents)
        self.propertyTable.setObjectName("propertyTable")
        self.propertyTable.horizontalHeader().setVisible(False)
        self.propertyTable.horizontalHeader().setHighlightSections(False)
        self.propertyTable.verticalHeader().setDefaultSectionSize(100)
        self.verticalLayout_4.addWidget(self.propertyTable)
        self.propertiesDock.setWidget(self.propertiesContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.propertiesDock)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionHelp_contents = QtGui.QAction(MainWindow)
        self.actionHelp_contents.setObjectName("actionHelp_contents")
        self.actionAbout_Garland = QtGui.QAction(MainWindow)
        self.actionAbout_Garland.setObjectName("actionAbout_Garland")
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete = QtGui.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionArrange_scheme = QtGui.QAction(MainWindow)
        self.actionArrange_scheme.setObjectName("actionArrange_scheme")
        self.actionZoom_in = QtGui.QAction(MainWindow)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtGui.QAction(MainWindow)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionText_mode = QtGui.QAction(MainWindow)
        self.actionText_mode.setObjectName("actionText_mode")
        self.actionImage_mode = QtGui.QAction(MainWindow)
        self.actionImage_mode.setObjectName("actionImage_mode")
        self.actionIcon_mode = QtGui.QAction(MainWindow)
        self.actionIcon_mode.setObjectName("actionIcon_mode")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionArrange_scheme)
        self.menuView.addAction(self.actionZoom_in)
        self.menuView.addAction(self.actionZoom_out)
        self.menuView.addAction(self.actionText_mode)
        self.menuView.addAction(self.actionImage_mode)
        self.menuView.addAction(self.actionIcon_mode)
        self.menuHelp.addAction(self.actionHelp_contents)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Garland)
        self.menuProcessing.addAction(self.actionStart)
        self.menuProcessing.addAction(self.actionStop)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProcessing.setTitle(QtGui.QApplication.translate("MainWindow", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.blockTreeDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Processing blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.previewDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.keepPreview1.setText(QtGui.QApplication.translate("MainWindow", "Keep", None, QtGui.QApplication.UnicodeUTF8))
        self.previewImage1.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.keepPreview2.setText(QtGui.QApplication.translate("MainWindow", "Keep", None, QtGui.QApplication.UnicodeUTF8))
        self.previewImage2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.propertiesDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp_contents.setText(QtGui.QApplication.translate("MainWindow", "Help Contents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Garland.setText(QtGui.QApplication.translate("MainWindow", "About Garland", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrange_scheme.setText(QtGui.QApplication.translate("MainWindow", "Arrange scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_in.setText(QtGui.QApplication.translate("MainWindow", "Zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_out.setText(QtGui.QApplication.translate("MainWindow", "Zoom out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionText_mode.setText(QtGui.QApplication.translate("MainWindow", "Text mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImage_mode.setText(QtGui.QApplication.translate("MainWindow", "Image mode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIcon_mode.setText(QtGui.QApplication.translate("MainWindow", "Icon mode", None, QtGui.QApplication.UnicodeUTF8))

from dragdropgraphicsview import DragDropGraphicsView