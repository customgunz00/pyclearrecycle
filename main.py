import subprocess
import platform

osname = platform.system()
command = None

if osname == 'Windows':
    command = ["powershell", "-ExecutionPolicy", "Bypass", "-File"]
    command = ["powershell", "./win.ps1"]
    subprocess.run(command, check=False)