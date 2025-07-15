# downloader/theme_toggle.py

import customtkinter as ctk

def apply_theme(choice: str):
    """
    Apply the selected appearance mode.
    """
    if choice in ["Light", "Dark", "System"]:
        ctk.set_appearance_mode(choice)
