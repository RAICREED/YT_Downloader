# downloader/save_location.py

import tkinter.filedialog as fd

selected_path = None  # Global module-level variable

def choose_folder():
    global selected_path
    path = fd.askdirectory(title="Select Download Folder")
    if path:
        selected_path = path
    return selected_path

def get_download_path():
    return selected_path or '.'  # fallback to current directory
