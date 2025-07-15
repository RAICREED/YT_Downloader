# main.py

import tkinter as tk
import customtkinter as ctk
from downloader.core import download_video
from downloader import save_location, playlist
from downloader.format_selector import get_selected_format
from downloader import quality
from downloader import playlist
from downloader import theme_toggle
from tkinter import messagebox
import threading


def start_download():
    url = url_var.get().strip()

    # 🚨 Check for download folder
    if not save_location.get_download_path() or save_location.get_download_path() == ".":
        messagebox.showwarning("Folder Required", "Please choose a download folder before starting.")
        return

    # 🚨 Check for format selection
    fmt = get_selected_format()
    if not fmt:
        messagebox.showwarning("Format Required", "Please select a format (e.g., mp4, mp3) before downloading.")
        return

    download_btn.configure(state="disabled")
    finish_label.configure(text="Downloading...")

    def is_playlist(url):
        return "list=" in url

    if is_playlist(url):
        threading.Thread(target=playlist.download_playlist, args=(url, update_progress, on_finish)).start()
    else:
        threading.Thread(target=download_video, args=(url, update_progress, on_finish)).start()


def update_progress(percent_value: float, label_text: str):
    percent.configure(text=label_text)
    progressbar.set(percent_value)

def on_finish(message: str):
    finish_label.configure(text=message)
    download_btn.configure(state="normal")

# UI Setup
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI Elements
title = ctk.CTkLabel(app, text="Enter a YouTube Link")
title.pack(pady=10)

url_var = tk.StringVar()
link_entry = ctk.CTkEntry(app, width=400, height=40, textvariable=url_var)
link_entry.pack(pady=5)

finish_label = ctk.CTkLabel(app, text="")
finish_label.pack(pady=5)

percent = ctk.CTkLabel(app, text="0%")
percent.pack()

progressbar = ctk.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(pady=10)

download_btn = ctk.CTkButton(app, text="Download", command=start_download)
download_btn.pack(pady=20)

#select folder
folder_btn = ctk.CTkButton(app, text="Choose Folder", command=save_location.choose_folder)
folder_btn.pack(pady=5)

#quality selector

quality_option = ctk.CTkOptionMenu(
    app,
    values=quality.available_options,
    command=quality.set_quality
)
quality_option.set("Best")
quality_option.pack(pady=5)

#platlist support

def start_download():
    url = url_var.get().strip()
    download_btn.configure(state="disabled")
    finish_label.configure(text="Downloading...")

    def is_playlist(url):
        return "list=" in url

    if is_playlist(url):
        threading.Thread(target=playlist.download_playlist, args=(url, update_progress, on_finish)).start()
    else:
        threading.Thread(target=download_video, args=(url, update_progress, on_finish)).start()


#theme
theme_selector = ctk.CTkOptionMenu(
    app,
    values=["System", "Light", "Dark"],
    command=theme_toggle.apply_theme
)
theme_selector.set("System")
theme_selector.pack(pady=5)

#format 
from downloader import format_selector

format_menu = ctk.CTkOptionMenu(
    app,
    values=format_selector.available_formats,
    command=format_selector.set_format
)
format_menu.set("mp4")
format_menu.pack(pady=5)




app.mainloop()
