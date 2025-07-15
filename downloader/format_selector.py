# downloader/format_selector.py

available_formats = ["mp4", "mkv", "mp3", "webm"]

_selected = "mp4"  # default

def set_format(fmt: str):
    global _selected
    _selected = fmt

def get_selected_format():
    return _selected

def is_audio_format():
    return _selected == "mp3"  # we postprocess MP3
