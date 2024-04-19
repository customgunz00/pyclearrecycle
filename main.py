import subprocess
import platform

osname = platform.system()
command = None

if osname == 'Windows':
    command = ["powershell", "-ExecutionPolicy", "Bypass", "-File"]
    subprocess.run(command, check=False)
    command = ["powershell", "./win.ps1"]
elif osname == 'Linux':
    command = ["sh", "./ubuntu.sh"]
elif osname == 'Darwin':
    command = ["sh", "./mac.sh"]