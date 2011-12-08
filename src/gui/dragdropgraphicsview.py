#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v2.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
from PySide import QtGui, QtCore

import graphblock


class DragDropGraphicsView(QtGui.QGraphicsView):
    """ Graphics view with drag and drop capabilities 

    """
    
    def __init__(self, parent):
        super(DragDropGraphicsView, self).__init__(parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.acceptProposedAction()
    
    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.accept()
            main_form = self.parent().parent()
            grid = main_form.scheme._grid
            grid.enable_dummy_block()
            pos = self.mapToScene(event.pos())
            row, column = grid.get_cell_in_point( (pos.x(), pos.y()) )
            grid.set_dummy_block_cell(row, column)
    
    def dragLeaveEvent(self, event):
        main_form = self.parent().parent()
        main_form.scheme._grid.disable_dummy_block()
    
    def dropEvent(self, event):
        # Decode treewidget item mime data
        main_form = self.parent().parent()
        grid = main_form.scheme._grid
        model = QtGui.QStandardItemModel()
        model.dropMimeData(event.mimeData(), QtCore.Qt.CopyAction, 0,0, QtCore.QModelIndex())
        block_type = model.item(0).text()
        grid.disable_dummy_block()
        pos = self.mapToScene(event.pos())
        row, column = grid.get_cell_in_point( (pos.x(), pos.y()) )
        if block_type in main_form.block_classes:
            main_form.scheme.add_block(block_type, row, column)
        event.acceptProposedAction()

    
    
    
