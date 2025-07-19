import os
import logging
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Qt, QTimer, QUrl, QStandardPaths
from playerp6.skin_player import Ui_SkinPlayer

# Configurar logger para el módulo
logger = logging.getLogger(__name__)

class PlayerP6(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SkinPlayer()
        self.ui.setupUi(self)
        self.__configPlayerP6()
        
        # Log de inicialización
        logger.info("PlayerP6 inicializado correctamente")
    
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

        # Configurar el slider de tiempo con máximo de 500
        self.ui.sld_tiempo.setMaximum(500)
        self.ui.sld_tiempo.setMinimum(0)
        
        # Conectar eventos
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
        
        self.set_vol(50)
        logger.debug("Configuración del reproductor completada")

    def set_vol(self, vol: int):
        """Establece el volumen inicial del reproductor"""
        self.ui.sld_vol.setValue(vol)
        self.set_volume(vol)
        self.ui.lb_vol.setText(str(vol))
        logger.debug(f"Volumen establecido a: {vol}")

    def update_ui(self):
        """Actualiza la interfaz de usuario con la posición actual"""
        if self.duration > 0:
            self.ui.sld_tiempo.blockSignals(True)
            # Calcular posición en escala de 500
            slider_position = int(self.position * 500 / self.duration)
            self.ui.sld_tiempo.setValue(slider_position)
            self.ui.sld_tiempo.blockSignals(False)

        self.ui.lb_time.setText(self.format_time(self.position))
        self.ui.lb_time_t.setText(self.format_time(self.position))
        time_rem = self.duration - self.position
        self.ui.lb_time_rem.setText(self.format_time(time_rem))

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
        """Alterna entre reproducir y pausar"""
        if self.media_player.playbackState() == QMediaPlayer.PlayingState:
            self.media_player.pause()
            logger.debug("Video pausado")
        else:
            self.media_player.play()
            logger.debug("Video reproduciendo")
            
    def stop(self):
        """Detiene la reproducción"""
        self.media_player.stop()
        logger.debug("Reproducción detenida")
        
    def set_position(self, position):
        """Establece la posición de reproducción basada en el slider (0-500)"""
        if self.duration > 0:
            # Convertir de escala 0-500 a milisegundos
            new_position = int(position * self.duration / 500)
            self.media_player.setPosition(new_position)
            logger.debug(f"Posición cambiada a: {self.format_time(new_position)}")
            
    def set_volume(self, volume):
        """Establece el volumen de audio"""
        self.audio_output.setVolume(volume / 100.0)
        self.ui.lb_vol.setText(str(volume))
        logger.debug(f"Volumen ajustado a: {volume}")
        
    def forward_5s(self):
        """Avanza 5 segundos en la reproducción"""
        current_position = self.media_player.position()
        new_position = min(current_position + 5000, self.duration)
        self.media_player.setPosition(new_position)
        logger.debug(f"Avance +5s: {self.format_time(new_position)}")
        
    def backward_5s(self):
        """Retrocede 5 segundos en la reproducción"""
        current_position = self.media_player.position()
        new_position = max(current_position - 5000, 0)
        self.media_player.setPosition(new_position)
        logger.debug(f"Retroceso -5s: {self.format_time(new_position)}")

    def next_frame(self):
        """Avanza aproximadamente un frame (asumiendo 30 fps)"""
        current_position = self.media_player.position()
        new_position = min(current_position + 33, self.duration)
        self.media_player.setPosition(new_position)
        logger.debug(f"Siguiente frame: {self.format_time(new_position)}")
        
    def previous_frame(self):
        """Retrocede aproximadamente un frame (asumiendo 30 fps)"""
        current_position = self.media_player.position()
        new_position = max(current_position - 33, 0)
        self.media_player.setPosition(new_position)
        logger.debug(f"Frame anterior: {self.format_time(new_position)}")

    def capture_frame(self):
        """Captura el frame actual del video"""
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
                    logger.info(f"Captura guardada exitosamente: {file_path}")
                    original_title = self.windowTitle()
                    self.setWindowTitle(f"{original_title} - ✓ Captura guardada!")
                    QTimer.singleShot(2000, lambda: self.setWindowTitle(original_title))
                else:
                    logger.error("Error al guardar la captura en disco")
            else:
                logger.warning("No se pudo capturar el frame - pixmap nulo")
                
        except Exception as e:
            logger.error(f"Error al capturar frame: {e}", exc_info=True)

    def position_changed(self, position):
        """Callback cuando cambia la posición de reproducción"""
        self.position = position
        
    def duration_changed(self, duration):
        """Callback cuando se obtiene la duración del video"""
        self.duration = duration
        logger.info(f"Duración del video: {self.format_time(duration)}")
        
    def state_changed(self, state):
        """Callback cuando cambia el estado de reproducción"""
        if state == QMediaPlayer.PlayingState:
            self.is_playing = True
            logger.debug("Estado cambiado a: Reproduciendo")
        elif state == QMediaPlayer.PausedState:
            self.is_playing = False
            logger.debug("Estado cambiado a: Pausado")
        elif state == QMediaPlayer.StoppedState:
            self.is_playing = False
            logger.debug("Estado cambiado a: Detenido")

    def set_videopath(self, file_path: str):
        """Establece la ruta del video a reproducir"""
        if file_path:
            try:
                if not os.path.exists(file_path):
                    logger.error(f"El archivo de video no existe: {file_path}")
                    return
                    
                self.media_player.setSource(QUrl.fromLocalFile(file_path))
                filename = os.path.basename(file_path)
                self.setWindowTitle(f"Reproductor de Video - {filename}")
                logger.info(f"Video cargado: {filename}")
                
            except Exception as e:
                logger.error(f"Error al cargar el video {file_path}: {e}", exc_info=True)

    def toggle_control(self):
        """Alterna entre diferentes vistas de control"""
        current_index = self.ui.sw.currentIndex()
        new_index = 1 if current_index == 0 else 0
        self.ui.sw.setCurrentIndex(new_index)
        logger.debug(f"Vista de control cambiada a índice: {new_index}")


def setup_logging(level=logging.INFO, log_file=None):
    """
    Configura el sistema de logging para el reproductor
    
    Args:
        level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Archivo opcional donde guardar los logs
    """
    # Configurar formato de logging
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Configurar logger principal
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    
    # Handler para archivo si se especifica
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


if __name__ == "__main__":
    import sys
    
    # Configurar logging para desarrollo
    setup_logging(level=logging.DEBUG, log_file="player_debug.log")
    
    app = QApplication(sys.argv)
    player = PlayerP6()
    v1 = "/run/media/tomy/sis/temp-test/aile.mp4"
    player.set_videopath(v1)
    player.show()
    sys.exit(app.exec())