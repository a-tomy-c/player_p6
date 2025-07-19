import sys
from PySide6.QtWidgets import QApplication
from playerp6 import PlayerP6
# from otros.dos import PlayerP6

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = PlayerP6()
    v1 = "/run/media/tomy/sis/temp-test/aile.mp4"
    player.set_videopath(v1)
    player.show()
    sys.exit(app.exec())