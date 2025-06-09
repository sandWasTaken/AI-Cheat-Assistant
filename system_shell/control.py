import os
import subprocess

def open_application(name):
    subprocess.Popen(name, shell=True)

def move_file(src, dest):
    if not os.path.exists(src):
        print("FRAIL - file not found:", src)
        return
    os.rename(src, dest)

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        return True
    return False

def list_dir(dir_path="."):
    return os.listdir(dir_path)