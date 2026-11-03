import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from principal import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save)

    def save(self):
        fields = [
            (self.ui.nameLabel, self.ui.nameEdit),
            (self.ui.lastNameLabel, self.ui.lastNameEdit),
            (self.ui.idLabel, self.ui.lineEdit),
            (self.ui.phoneLabel, self.ui.phoneEdit),
        ]
        with open("data.txt", "w", encoding="utf-8") as archivo:
            for label, edit in fields:
                archivo.write(f"{label.text()} {edit.text()}\n")
        QMessageBox.information(self, "Saved", "Data saved to datos.txt")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
