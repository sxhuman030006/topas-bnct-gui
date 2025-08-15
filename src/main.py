import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TOPAS-BNCT Configurator(W1-D2)")
        self.setFixedSize(400, 300)
        label = QLabel("Hello BNCT World!",alignment=Qt.AlignCenter)
        self.setCentralWidget(label)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())