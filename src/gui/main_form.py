# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui
from main_form_ui import Ui_MainWindow
import os
import sys
import cv
import weakref

cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from ipf.ipfgraphloader import get_ipfblock_classes
import graphscheme
import propertiesmodel
import image_convert
import propertyeditor

class MainForm(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_blocks_widget()
        self.scheme = graphscheme.GraphScheme(self)
        self.ui.graphicsView.setScene(self.scheme)
        self.ui.graphicsView.setAlignment( QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.ui.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        # Block preview objects 
        self.previewPixmapItem1 = QtGui.QGraphicsPixmapItem()
        self.previewPixmapItem2 = QtGui.QGraphicsPixmapItem()
        self.previewScene1 = QtGui.QGraphicsScene()
        self.previewScene2 = QtGui.QGraphicsScene()
        self.previewScene1.addItem(self.previewPixmapItem1)
        self.previewScene2.addItem(self.previewPixmapItem2)
        self.ui.previewView1.setScene(self.previewScene1)
        self.ui.previewView2.setScene(self.previewScene2)
        self.properties_model = None
        self.init_actions()
        
        # Set property editor item delegate
        self.editor_delegate = propertyeditor.PropertyEditorDelegate()
        self.ui.propertyTable.setItemDelegate(self.editor_delegate)
        self.editor_delegate.closeEditor.connect(self.update_window)
        
        # Preview block
        self.previewBlock1 = None
        self.previewBlock2 = None
    
        
    def _init_blocks_widget(self):
        self.block_classes = get_ipfblock_classes()
        categories = set()
        for block in self.block_classes.values():
                categories.add(block.category)
        category_items = dict()
        for category in categories:
            category_items[category] = QtGui.QTreeWidgetItem(None)
            category_items[category].setText(0, category)
        for block in self.block_classes.values():
            block_item = QtGui.QTreeWidgetItem(category_items[block.category])
            block_item.setText(0, block.type)
        
        self.ui.blocks_tree.insertTopLevelItems(0, category_items.values())
        
        
    def block_selected(self, ipf_block):
        self.show_block_properties(ipf_block)
        if not self.ui.keepPreview1.isChecked():
            self.previewBlock1 = weakref.ref(ipf_block)
        if not self.ui.keepPreview2.isChecked():
            self.previewBlock2 = weakref.ref(ipf_block)
        self.update_window()
        
        
    def show_block_properties(self, block):
        self.properties_model = propertiesmodel.PropertiesModel(block)
        self.ui.propertyTable.setModel(self.properties_model)


    def init_actions(self):
        self.ui.actionAbout_Garland.triggered.connect(self.about)
        self.ui.actionArrange_scheme.triggered.connect(self.arrange_scheme)
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionCut.triggered.connect(self.cut)
        self.ui.actionDelete.triggered.connect(self.delete)
        self.ui.actionExit.triggered.connect(QtGui.QApplication.exit)
        self.ui.actionFind.triggered.connect(self.find)
        self.ui.actionHelp_contents.triggered.connect(self.help_contents)
        self.ui.actionIcon_mode.triggered.connect(self.icon_mode)
        self.ui.actionImage_mode.triggered.connect(self.image_mode)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionPaste.triggered.connect(self.paste)
        self.ui.actionText_mode.triggered.connect(self.text_mode)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_As.triggered.connect(self.save_file_as)
        self.ui.actionStart.triggered.connect(self.processing_start)
        self.ui.actionStop.triggered.connect(self.processing_stop)
        self.ui.actionZoom_in.triggered.connect(self.zoom_in)
        self.ui.actionZoom_out.triggered.connect(self.zoom_out)
        
    
    def open_file(self):
        pass
    
    
    def save_file(self):
        pass
    
    
    def save_file_as(self):
        pass
    
    
    def cut(self):
        pass
    
    
    def copy(self):
        pass
    
    
    def paste(self):
        pass
    
    
    def arrange_scheme(self):
        pass
    
    
    def find(self):
        pass
    
    
    def delete(self):
        selected_block = self.scheme.get_selected_block()
        if self.previewBlock1 is not None and \
           self.previewBlock1() == selected_block:
            self.previewBlock1 = None
        if self.previewBlock2 is not None and \
           self.previewBlock2() == selected_block:
            self.previewBlock2 = None
        self.properties_model = propertiesmodel.PropertiesModel()
        self.ui.propertyTable.setModel(self.properties_model)
        self.scheme.delete_selected()
        self.update_window()
    
    
    def processing_start(self):
        self.scheme.ipf_graph.process()
        self.update_window()
    
    
    def processing_stop(self):
        pass
    
    
    def zoom_in(self):
        pass
    
    
    def zoom_out(self):
        pass
    
    
    def text_mode(self):
        pass
    
    
    def image_mode(self):
        pass
    
    
    def icon_mode(self):
        pass
    
    
    def help_contents(self):
        pass
    
    
    def about(self):
        pass
    
    
    def update_window(self):
        """ Update all window GUI elements
        
        """
        # Perform image processing 
        self.scheme.ipf_graph.process()
        
        if self.previewBlock1 is not None:
            self._update_preview(self.previewBlock1(), 
                                 self.previewPixmapItem1, 
                                 self.ui.previewView1)
        if self.previewBlock2 is not None:
            self._update_preview(self.previewBlock2(), 
                                 self.previewPixmapItem2, 
                                 self.ui.previewView2)
        
        
    
    def _update_preview(self, ipf_block, previewPixmapItem, previewView):
        """ Update preview image for block in previewPixmapItem
        
        """
        if ipf_block is None:
            previewPixmapItem.setPixmap(QtGui.QPixmap())
        else:
            ipl_image = ipf_block.get_preview_image()
            if ipl_image is not None:
                qimage = image_convert.iplimage_to_qimage(ipl_image)
                qpixmap = QtGui.QPixmap.fromImage(qimage)
                previewPixmapItem.setPixmap(qpixmap)
                previewView.fitInView(previewPixmapItem, \
                                               QtCore.Qt.KeepAspectRatio)
        
    def graph_changed(self):
        """ Notify function, called when image processing graph is changed
        
        """
        self.update_window()