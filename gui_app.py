import sys
import cv2
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QFileDialog, QHBoxLayout, QVBoxLayout
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO


class YOLOGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Object Detection - Kutu & Sise")
        self.setGeometry(100, 100, 1000, 600)

        self.model = YOLO("best.pt")
        self.image_path = None
        self.result_image = None

        # Image panels
        self.original_label = QLabel("Original Image")
        self.original_label.setAlignment(Qt.AlignCenter)

        self.result_label = QLabel("Tagged Image")
        self.result_label.setAlignment(Qt.AlignCenter)

        # Buttons
        self.btn_select = QPushButton("Select Image")
        self.btn_test = QPushButton("Test Image")
        self.btn_save = QPushButton("Save Image")

        self.btn_select.clicked.connect(self.select_image)
        self.btn_test.clicked.connect(self.test_image)
        self.btn_save.clicked.connect(self.save_image)

        # Layouts
        image_layout = QHBoxLayout()
        image_layout.addWidget(self.original_label)
        image_layout.addWidget(self.result_label)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_select)
        button_layout.addWidget(self.btn_test)
        button_layout.addWidget(self.btn_save)

        main_layout = QVBoxLayout()
        main_layout.addLayout(image_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.jpg *.png)"
        )
        if file_path:
            self.image_path = file_path
            self.show_image(file_path, self.original_label)

    def test_image(self):
        if not self.image_path:
            return

        results = self.model(self.image_path)
        annotated = results[0].plot()
        self.result_image = annotated

        self.show_cv_image(annotated, self.result_label)

    def save_image(self):
        if self.result_image is None:
            return

        save_path, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "Images (*.jpg *.png)"
        )
        if save_path:
            cv2.imwrite(save_path, self.result_image)

    def show_image(self, path, label):
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(
            label.width(), label.height(),
            Qt.KeepAspectRatio
        )
        label.setPixmap(pixmap)

    def show_cv_image(self, img, label):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qt_img = QImage(
            rgb.data, w, h, bytes_per_line, QImage.Format_RGB888
        )
        pixmap = QPixmap.fromImage(qt_img)
        pixmap = pixmap.scaled(
            label.width(), label.height(),
            Qt.KeepAspectRatio
        )
        label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YOLOGui()
    window.show()
    sys.exit(app.exec_())
