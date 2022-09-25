import sys
import filter


from PIL import Image
from gui import Window
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from threading import Thread


class App(Window):
    def __init__(self):
        super().__init__()
        self.button_file.clicked.connect(self.select_image)
        self.slider_blur.valueChanged[int].connect(self.bluring)
        self.button_sobel.clicked.connect(self.sobel)
        self.button_prewitt.clicked.connect(self.prewitt)
        self.button_binary.clicked.connect(self.binary)
        self.button_save.clicked.connect(self.save_image)
        
        self.image = None
        self.current_image = None
        self.sobel_image = None


    def set_pixmap(self, image):
        qim = ImageQt(image)
        pix = QPixmap.fromImage(qim)
        self.label_image.setPixmap(pix)

    def select_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self,
        "QFileDialog.getOpenFileName()", "",
        "Image Files (*.jpg *.png *.jpeg *.svg *.jfif);", options=options)

        if filename:
            self.image = Image.open(filename).convert('L')
            self.set_pixmap(self.image)
    
    def bluring(self):
        value = self.slider_blur.value()
        self.label_blur.setText(f"Set Blur [{value}]")

        if self.image:
            image = self.image
            image = filter.gaussian(self.image, mask_size=value)
            self.blur_image = image
            self.current_image = image
            self.set_pixmap(image)
            
    def sobel(self):
        image = self.image
        if self.image:
            if self.sobel_image != image:

                image = filter.sobel(image)
                self.sobel_image = image
                self.current_image = image
                self.set_pixmap(image)
            else:
                self.set_pixmap(self.image)
    
    def prewitt(self):
        if self.image:
            image = filter.prewitt(self.image)
            self.current_image = image
            self.set_pixmap(image)


    def binary(self):
        if self.image:
            image = self.image
            value = self.slider_threshold.value()
            image = filter.binary(filter.sobel(image), k=value)
            self.current_image = image
            self.set_pixmap(image)

    
    def save_image(self):
        if self.current_image:
            options = QFileDialog.Options()

            fileName, _ = QFileDialog.getSaveFileName(self,
            "QFileDialog.getSaveFileName()", "",
            "All Files (*);", options=options)
            
            if fileName:
                self.current_image.save(fileName)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())