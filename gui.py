import sys

from PyQt5.QtWidgets import QAction, QDesktopWidget, QMenu, QMenuBar, QMessageBox, QWidget, QApplication, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image, ImageQt
from detect import detect


class ObjDetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ObjDetApp")
        self.resize(1000, 700)
        self.center()

        layout = QVBoxLayout()

        self.lbl = QLabel(self)
        self.lbl.setVisible(False)

        self.btn = QPushButton("Upload Image", self)
        self.btn.clicked.connect(self.upload)

        layout.addWidget(self.btn, 0, Qt.AlignCenter)
        layout.addWidget(self.lbl, 0, Qt.AlignCenter)
        self.setLayout(layout)

        self.createActions()
        self.createMenus()

    def center(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

    def upload(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Select an image", "", "Images (*.png *.jpeg *.jpg)", options=options)

        if filename:
            orig_image = Image.open(filename)
            orig_image = orig_image.convert('RGB')
            new_image = detect(orig_image, min_score=0.2,
                               max_overlap=0.5, top_k=200)
            pix = QPixmap.fromImage(ImageQt.ImageQt(new_image))
            self.lbl.setPixmap(pix)
            self.lbl.setVisible(True)

    def about(self):
        QMessageBox.about(self, "About ObjDetApp", "This is a side project (or not qualified as a project) derived from a school assignment, which focuses on the deployment of a pytorch model for object detection, hence the name.")

    def createActions(self):
        self.uploadAct = QAction("Upload", self, triggered=self.upload)
        self.aboutAct = QAction("About", self, triggered=self.about)

    def createMenus(self):
        self.fileMenu = QMenu("File", self)
        self.fileMenu.addAction(self.uploadAct)

        self.helpMenu = QMenu("Help", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menubar = QMenuBar(self)
        self.menubar.addMenu(self.fileMenu)
        self.menubar.addMenu(self.helpMenu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ObjDetApp()
    win.show()
    sys.exit(app.exec_())
