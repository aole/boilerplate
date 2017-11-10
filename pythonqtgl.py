#!/usr/bin/env python3

from PyQt5.QtWidgets import QWidget, QApplication, QAction, qApp, QMainWindow, QMenu, QFileDialog, QHBoxLayout, QVBoxLayout, QOpenGLWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QRect, QSize, QPoint

import sys

__author__ = 'Bhupendra Aole'
__version__ = '0.1.0'

class Canvas( QOpenGLWidget ):
    def __init__( self, parent ):
        super().__init__( parent )
    
    def paintEvent( self, event ):
        qp = QPainter()
        qp.begin( self )
        qp.drawText( event.rect(), Qt.AlignCenter, 'Boilerplate Code' )
        qp.end()
    
# window class
class MainWindow( QMainWindow ):
    def __init__( self ):
        super().__init__()
        
        self.setWindowTitle( 'Window Title' )
        
        
        self.initUI()
        self.initMenu()
        self.initToolbar()
    
        self.statusBar().showMessage( 'Ready' )
        
    def initUI( self ):
        self.resize( 300, 200 )
        
        self.canvas = Canvas( self )
        self.setCentralWidget( self.canvas )
        
    def initMenu( self ):
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu( '&File' )
        
        self.openAction = QAction( '&Open', self )
        self.openAction.setShortcut( 'Ctrl+O' )
        self.openAction.setStatusTip( 'Open File' )
        self.openAction.triggered.connect( self.showOpenDialog )
        fileMenu.addAction( self.openAction )
        
        self.exitAction = QAction( 'E&xit', self )
        self.exitAction.setShortcut( 'Ctrl+Q' )
        self.exitAction.setStatusTip( 'Exit Application' )
        self.exitAction.triggered.connect( self.quit )
        fileMenu.addAction( self.exitAction )
    
    def initToolbar( self ):
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(self.exitAction)
        
    # context menu
    def contextMenuEvent( self, event ):
        cm = QMenu(self)
        cm.addAction('New')
        cm.addAction(self.exitAction)
        action = cm.exec_(self.mapToGlobal(event.pos()))
    
    def showOpenDialog(self):
        fname = QFileDialog.getOpenFileName( self, 'Open file', filter='Text Files(*.txt *.py)' )
        if fname[0]:
            f = open(fname[0], 'r')
            line = f.readline()
            print(line)
            
    def quit(self):
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

