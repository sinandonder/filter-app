import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QFrame,
    QVBoxLayout,
    QSlider,
    QLabel,
    QSizePolicy
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Filter")
        self.frame_left = QFrame()
        self.frame_left.setObjectName("frame_left")
        self.frame_right = QFrame()

        layout = QHBoxLayout()
        layout.addWidget(self.frame_left, 6)
        layout.addWidget(self.frame_right, 1)
        self.setLayout(layout)

        self.button_file = QPushButton("Select Image")
        self.icon_file = QtGui.QIcon()
        self.icon_file.addPixmap(QtGui.QPixmap("icons/add.png"),
                                 QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_file.setIcon(self.icon_file)

        self.label_blur = QLabel()
        self.label_blur.setAlignment(Qt.AlignCenter)
        self.label_blur.setText("Set Blur [0]")

        self.slider_blur = QSlider(Qt.Horizontal)
        self.slider_blur.valueChanged[int].connect(self.slider_event)
        self.slider_blur.setMinimum(2)
        self.slider_blur.setMaximum(10)

        self.button_sobel = QPushButton("Sobel")
        self.button_prewitt = QPushButton("Prewitt")
        self.button_binary = QPushButton("Binary Image")

        self.label_threshold = QLabel(text="Threshold for Binary [0]")
        self.label_threshold.setAlignment(Qt.AlignCenter)

        self.slider_threshold = QSlider(Qt.Horizontal)
        self.slider_threshold.valueChanged[int].connect(
            self.slider_threshold_event)
        self.slider_threshold.setMinimum(1)

        self.button_save = QPushButton("Save Image")

        self.pixmap_image = QPixmap()
        self.label_image = QLabel(objectName="label_image")
        self.label_image.setPixmap(self.pixmap_image)
        self.label_image.setAlignment(Qt.AlignCenter)
        self.label_image.setScaledContents(True)

        layout_right = QVBoxLayout()
        layout_blur = QHBoxLayout()
        layout_blur.addWidget(self.label_blur)
        layout_blur.addWidget(self.slider_blur)

        layout_right.addWidget(self.button_file)
        layout_right.addWidget(self.label_blur)
        layout_right.addWidget(self.slider_blur)
        layout_right.addWidget(self.button_sobel)
        layout_right.addWidget(self.button_prewitt)
        layout_right.addWidget(self.label_threshold)
        layout_right.addWidget(self.slider_threshold)
        layout_right.addWidget(self.button_binary)
        layout_right.addWidget(self.button_save)

        layout_right.setAlignment(Qt.AlignTop)

        self.frame_right.setLayout(layout_right)

        layout_left = QHBoxLayout()

        layout_left.addWidget(self.label_image)

        layout_left.setAlignment(Qt.AlignCenter)

        self.frame_left.setLayout(layout_left)


        stylefile = open("style.css", "r")
        style = stylefile

        self.setStyleSheet(stylefile)

    def slider_event(self):
        value = self.slider_blur.value()
        self.label_blur.setText(f"Set Blur [{value}]")

    def slider_threshold_event(self):
        value = self.slider_threshold.value()
        self.label_threshold.setText(f"Threshold for Binary [{value}]")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
