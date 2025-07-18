from PySide6.QtWidgets import QWidget
from playerp6.skin_player import Ui_SkinPlayer


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SkinPlayer()
        self.ui.setupUi(self)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    player = Player()
    player.show()
    sys.exit(app.exec())