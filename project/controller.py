from PyQt5 import QtCore
from PyQt5 import QtWidgets

from project.model import (
    Model
)
from project.views import View


import time
import os
try:
    import youtube_dl

except:
    os.system('pip install youtube_dl')


class Controller:


    def __init__(self):
        self.Model = Model()
        self.View = View(self)

    def main_window_title(self):
        self.View.MainView.labelWindowTitle.setText(
            f'''{time.asctime()} - {os.getlogin()}'''
        )
    
    def get_main_window_view(self):
        return self.View.get_main_window_view()


    def swipe_sidebar(self):
        if True:
            width = self.View.MainView.frameSidebar.width()
            normal = 46

            if width == 46:
                extend = 250
            else:
                extend = normal

            self.animation_menu_panel = QtCore.QPropertyAnimation(self.View.MainView.frameSidebar, b'minimumWidth')
            self.animation_menu_panel.setDuration(350)
            self.animation_menu_panel.setStartValue(width)
            self.animation_menu_panel.setEndValue(extend)
            self.animation_menu_panel.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation_menu_panel.start()


    def download(self):
        url = self.View.MainView.lineEditURL.text()

        if self.View.MainView.radioButtonAudioOption.isChecked():
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                self.View.MainView, 
                "Selecciona el destino", 
                QtCore.QDir.currentPath()
            )

            if directory:
                #self.View.MainView.lineEditDownloadPath.setText(directory)

                self.Model.download_directory_path = directory

                try:
                    video = youtube_dl.YoutubeDL().extract_info(
                        url = url, download = False
                    )

                    self.Model.download_file_name = video['title'] + '.mp3'
            
                    file_path = self.Model.download_directory_path + '\\' + self.Model.download_file_name
                    file_path = str(file_path).replace('/', '\\')

                    self.Model.download_file_path = file_path


                    options = {
                        'format'    : 'bestaudio/best',
                        'keepvideo' : False,
                        'postprocessors': [
                            {
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '320',
                            }
                        ],
                        'progress_hooks': [self.download_percent],
                        'outtmpl'   : f'{file_path}'
                    }

                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([video['webpage_url']])

                    self.View.MainView.lineEditURL.clear()
                    
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Information,
                        title = 'Descarga finalizada',
                        message = f'Se ha descargado correctamente el archivo en la ruta:\n{file_path}\n'
                    )
                
                except Exception as exc:
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Critical,
                        title = 'Descarga interrumpida',
                        message = f'Se ha interrumpido la descarga\n{exc}\n'
                    )


        if self.View.MainView.radioButtonVideoOption.isChecked():
            directory = QtWidgets.QFileDialog.getExistingDirectory(
                self.View.MainView, 
                "Selecciona el destino", 
                QtCore.QDir.currentPath()
            )

            if directory:
                #self.View.MainView.lineEditDownloadPath.setText(directory)

                self.Model.download_directory_path = directory

                try:
                    video = youtube_dl.YoutubeDL().extract_info(
                        url = url, download = False
                    )

                    self.Model.download_file_name = video['title'] + '.mp4'

                    file_path = str(directory + '\\' + self.Model.download_file_name)

                    self.Model.download_file_path = file_path

                    options = {
                        'format' : 'bestvideo+bestaudio',
                        'progress_hooks': [self.download_percent],
                        'outtmpl'   : f'{file_path}',
                        'quiet' : True,
                        'external_downloader_args': ['-loglevel', 'panic']

                    }

                    with youtube_dl.YoutubeDL(options) as ydl:
                        ydl.download([video['webpage_url']])

                    self.View.MainView.lineEditURL.clear()
                    
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Information,
                        title = 'Descarga finalizada',
                        message = f'Se ha descargado correctamente el archivo en la ruta:\n{file_path}\n'
                    )
                
                except Exception as exc:
                    return self.View.get_message_view(
                        status = QtWidgets.QMessageBox.Critical,
                        title = 'Descarga interrumpida',
                        message = f'Se ha interrumpido la descarga\n{exc}\n'
                    )



    def download_percent(self, download):
        

        if download['status'] == 'downloading':
            percent = download['_percent_str']
            percent = percent.replace('%', '')


            
            try:

                self.View.MainView.labelDownload.setText(
                    f'''{download['_speed_str']} de {download['_total_bytes_str']}'''
                )

                download_percent = int(float(percent))
                self.View.MainView.progressBarDownload.setValue(int(download_percent))
                self.View.MainView.progressBarDownload.setFormat('%.02f%%' % (float(percent)))
            except:
                pass
            
            QtWidgets.QApplication.processEvents()
        
        
        if download['status'] == 'finished':

            self.View.MainView.labelDownload.setText('')
            self.View.MainView.progressBarDownload.setValue(0)
            self.View.MainView.progressBarDownload.setFormat('%.02f%%' % (float(0)))


            self.Model.download_directory_path = str(self.Model.download_directory_path).replace('/', '\\')


            self.Model.downloads.append(
                [
                    time.ctime(os.path.getmtime(self.Model.download_file_path)),
                    self.Model.download_directory_path,
                    self.Model.download_file_name,
                    self.Model.download_file_path,
                    f'{int(float(os.path.getsize(self.Model.download_file_path) / 1024))}MB'
                ]
            )

            

            header = [
                'Fecha de creacion',
                'Ubicacion de la descarga',
                'Nombre del archivo',
                'Ubicacion del archivo',
                'Tamaño del archivo'
            ]

            self.View.MainView.tableWidgetDownloads.setColumnCount(len(header))
            self.View.MainView.tableWidgetDownloads.setHorizontalHeaderLabels(header)

            self.View.MainView.tableWidgetDownloads.setRowCount(len(self.Model.downloads))

            for row in range(len(self.Model.downloads)):
                for column in range(len(header)):
                    self.View.MainView.tableWidgetDownloads.setItem(row, column, QtWidgets.QTableWidgetItem(str(self.Model.downloads[row][column])))
                    self.View.MainView.tableWidgetDownloads.horizontalHeader().setSectionResizeMode(column, QtWidgets.QHeaderView.ResizeToContents)
            self.View.MainView.tableWidgetDownloads.cellClicked.connect(self.clicked_cell)
            self.View.MainView.tableWidgetDownloads.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            

    def clicked_cell(self, row, column):
        item = ''
        item = self.View.MainView.tableWidgetDownloads.item(row, column)

        try:
            if column == 1 or column == 3:
                os.startfile(f'''{item.text()}''')
        
        except:
            pass