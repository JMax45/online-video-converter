from __future__ import unicode_literals
from modules.pytube import *
from design import design
from PyQt5 import QtWidgets, QtTest, QtGui
from PyQt5.Qt import QApplication, QClipboard, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import urllib.request

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    closed = pyqtSignal()
    download_complete = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.hide()
        self.buttonBox.hide()
        self.label_2.hide()
        self.label_4.hide()
        self.pushButton.clicked.connect(self.convert_video_start)
        self.buttonBox.accepted.connect(self.convert_video_start_download)
        self.buttonBox.rejected.connect(self.convert_video_cancel)
        self.toolButton.hide()
    def convert_video(self):
        video_url = self.lineEdit.text()
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        self.label.hide()
        self.lineEdit.hide()
        self.pushButton.hide()
        self.label_4.hide()
    def video_found(self):
        self.pushButton.hide()
        self.lineEdit.setReadOnly(True)
        self.buttonBox.show()
        url = thumbnail_url_global
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)       
        self.label_4.setPixmap(QtGui.QPixmap(image))
        self.label_4.show()
        self.label_2.show()
    def video_download_complete(self):
        self.label_4.hide()
        self.label.setText("INSERISCI IL LINK")
        self.label.show()
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.pushButton.show()
        self.progressBar.setProperty("value", 0)
        self.progressBar.hide()
        self.label_2.hide()
    def convert_video_cancel(self):
        self.buttonBox.hide()
        self.pushButton.show()
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.label.setText("INSERISCI IL LINK")
        self.label.show()
        self.label_4.hide()
        self.label_2.hide()
    def convert_video_start_download(self):
        self.buttonBox.hide()
        self.label.setText("Downloading...")
        self.label.show()
        self.progressBar.show()
        class YourThreadName(QThread):
            def __init__(self2):
                QThread.__init__(self2)
                
            def __del__(self2):
                self2.wait()
            def percent(self2, tem, total):
                perc = (float(tem) / float(total)) * float(100)
                return perc    
            def progress_func(self2, stream, chunk, file_handle,bytes_remaining):
              size = self2.stream.filesize
              progress = (float(abs(bytes_remaining-size)/size))*float(100)
              self.progressBar.setValue(progress)
            def run(self2):
                yt = YouTube(self.lineEdit.text(), on_progress_callback=self2.progress_func)
                
                yt.streams.all()
                self2.stream = yt.streams.first()
                self2.stream.download()
                
                self.download_complete.connect(self.video_download_complete)
                self.download_complete.emit()
                
        self.myThread = YourThreadName()
        self.myThread.start()
    def convert_video_start(self):
        class YourThreadName(QThread):
            def __init__(self2):
                QThread.__init__(self2)
                
            def __del__(self2):
                self2.wait()
            
            def run(self2):
                self.label.setText("Stiamo verificando il link...")
                yt = YouTube(self.lineEdit.text())
                print(yt.title)
                self.label_2.setText(yt.title)
                self.label.hide()
                print(yt.thumbnail_url)
                global thumbnail_url_global
                thumbnail_url_global = yt.thumbnail_url

                print(yt.streams.filter(file_extension='mp4').all())
    
                self.closed.connect(self.video_found)
                self.closed.emit()
                
                
        self.myThread = YourThreadName()
        self.myThread.start()
        
def main():
    app = QtWidgets.QApplication(sys.argv)  
    window1 = ExampleApp()  
    window1.show()
    app.exec_()

if __name__ == '__main__':
    main()     
