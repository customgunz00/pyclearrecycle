import subprocess

def clear_recycle_bin():
  try:
    command = ["powershell", "-Command", "Clear-RecycleBin -Force"]
    subprocess.run(command, check=False)
  except subprocess.CalledProcessError:
    pass

clear_recycle_bin()
print("Recycle Bin Cleared (if it had any contents)"