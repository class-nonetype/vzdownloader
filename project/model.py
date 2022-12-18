from PyQt5 import QtCore
from PyQt5 import Qt

import platform

class Model:


    def __init__(self) -> None:
        
        self.download_directory_path = str(None)
        self.download_file_path = str(None)

        self.download_file_name = str(None)
        self.downloads = []

        self.platform_system = platform.system()

        self.system = {
                'os' : platform.system(),
                'system' : platform.system(),
                'version' : platform.version(),
                'processor' : platform.processor(),
                'node' : platform.node(),
                'machine' : platform.machine(),
                'architecture' : platform.architecture(),
                'platform' : platform.platform()
            }


