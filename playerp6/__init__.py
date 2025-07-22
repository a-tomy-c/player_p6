import os
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Qt, QTimer, QUrl, QStandardPaths
from playerp6.skin_player import Ui_SkinPlayer


class PlayerP6(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SkinPlayer()
        self.ui.setupUi(self)
        self.__configPlayerP6()
    
    def __configPlayerP6(self):
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)

        self.is_playing = False
        self.duration = 0
        self.position = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(100)

        vly = QVBoxLayout(self.ui.fm_video)
        vly.addWidget(self.video_widget)
        vly.setContentsMargins(0,0,0,0)

        self.ui.bt_prev.clicked.connect(self.previous_frame)
        self.ui.bt_next.clicked.connect(self.next_frame)
        self.ui.bt_rewind.clicked.connect(self.backward_5s)
        self.ui.bt_forward.clicked.connect(self.forward_5s)
        self.ui.bt_play.clicked.connect(self.toggle_play_pause)
        self.ui.bt_cap.clicked.connect(self.capture_frame)
        self.ui.bt_toggle.clicked.connect(self.toggle_control)
        self.ui.bt_stop.clicked.connect(self.stop)
        self.ui.sld_tiempo.valueChanged.connect(self.set_position)
        self.ui.sld_vol.valueChanged.connect(self.set_volume)
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.playbackStateChanged.connect(self.state_changed)
        self.set_vol(5)
        self.ui.sld_tiempo.setMaximum(500)
        self.ui.sld_tiempo.setMinimum(0)

    def set_vol(self, vol:int):
        self.ui.sld_vol.setValue(vol)
        self.set_volume(vol)
        self.ui.lb_vol.setText(str(vol))

    def update_ui(self):
        if self.duration <= 0 or not self.media_player.hasVideo():
            return
        
        if self.media_player.playbackState() == QMediaPlayer.PlayingState:
            self.ui.sld_tiempo.blockSignals(True)
            self.ui.sld_tiempo.setValue(int(self.position*500/self.duration))
            self.ui.sld_tiempo.blockSignals(False)
            # print(int(self.position*100/self.duration), self.ui.sld_tiempo.maximum())

        self.ui.lb_time.setText(self.format_time(self.position))
        self.ui.lb_time_t.setText(self.format_time(self.position))
        time_rem = self.duration - self.position
        self.ui.lb_time_rem.setText(self.format_time(time_rem))

    def get_current_time(self) -> str:
        return self.format_time(self.position)

    def format_time(self, milliseconds):
        """Convierte milisegundos a formato HH:MM:SS.mmm"""
        seconds = milliseconds // 1000
        ms = milliseconds % 1000
        minutes = seconds // 60
        seconds = seconds % 60
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{ms:03d}"
    
    def toggle_play_pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()
            
    def stop(self):
        self.media_player.stop()
        
    def set_position(self, position):
        if self.duration > 0:
            self.media_player.setPosition(int(position * self.duration / 500))
            
    def set_volume(self, volume):
        self.audio_output.setVolume(volume / 100.0)
        self.ui.lb_vol.setText(f'{volume}')
        
    def forward_5s(self):
        current_position = self.media_player.position()
        new_position = min(current_position + 5000, self.duration)
        self.media_player.setPosition(new_position)
        
    def backward_5s(self):
        current_position = self.media_player.position()
        new_position = max(current_position - 5000, 0)
        self.media_player.setPosition(new_position)

    def next_frame(self):
        # Avanzar aproximadamente un frame (asumiendo 30 fps)
        current_position = self.media_player.position()
        new_position = min(current_position + 33, self.duration)
        self.media_player.setPosition(new_position)
        
    def previous_frame(self):
        # Retroceder aproximadamente un frame (asumiendo 30 fps)
        current_position = self.media_player.position()
        new_position = max(current_position - 33, 0)
        self.media_player.setPosition(new_position)

    def capture_frame(self):
        # Capturar solo el área del widget de video (sin botones)
        try:
            # Obtener la pantalla actual
            screen = QApplication.primaryScreen()
            
            # Obtener la posición global del widget de video
            global_pos = self.video_widget.mapToGlobal(self.video_widget.rect().topLeft())
            
            # Capturar solo el área del widget de video
            pixmap = screen.grabWindow(0, 
                                     global_pos.x(), 
                                     global_pos.y(),
                                     self.video_widget.width(), 
                                     self.video_widget.height())
            
            if not pixmap.isNull():
                # Crear nombre de archivo basado en la posición actual
                timestamp = self.format_time(self.position)
                filename = f"captura_{timestamp.replace(':', '-').replace('.', '-')}.png"
                
                # Obtener directorio de escritorio
                desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
                file_path = os.path.join(desktop_path, filename)
                
                if pixmap.save(file_path, "PNG"):
                    original_title = self.windowTitle()
                    self.setWindowTitle(f"{original_title} - ✓ Captura guardada!")
                    QTimer.singleShot(2000, lambda: self.setWindowTitle(original_title))
                else:
                    print("Error al guardar la captura")
            else:
                print("No se pudo capturar el frame")
                
        except Exception as e:
            print(f"Error al capturar frame: {e}")

    def position_changed(self, position):
        self.position = position
        
    def duration_changed(self, duration):
        self.duration = duration
        
    def state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            self.is_playing = True
            if not self.timer.isActive():
                self.timer.start(100)
        else:
            self.is_playing = False
            self.timer.stop()

    def set_videopath(self, file_path:str):
        if file_path:
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.setWindowTitle(f"Reproductor de Video - {os.path.basename(file_path)}")
            # if not self.timer.isActive():
            if self.is_playing:
                self.timer.start(100)

    def toggle_control(self):
        index = 1 if self.ui.sw.currentIndex()==0 else 0
        self.ui.sw.setCurrentIndex(index)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    player = PlayerP6()
    v1 = "/run/media/tomy/sis/temp-test/aile.mp4"
    player.set_videopath(v1)
    player.show()
    sys.exit(app.exec())