# downloader/quality.py

available_options = [
    "Best",
    "1080p",
    "720p",
    "480p",
    "360p",
    "Audio only"
]

selected_quality = "Best"

def set_quality(q: str):
    global selected_quality
    selected_quality = q

def get_format_selector():
    quality_map = {
        "Best": "bestvideo+bestaudio",
        "1080p": "bestvideo[height=1080]+bestaudio",
        "720p": "bestvideo[height=720]+bestaudio",
        "480p": "bestvideo[height=480]+bestaudio",
        "360p": "bestvideo[height=360]+bestaudio",
        "Audio only": "bestaudio"
    }
    return quality_map.get(selected_quality, "bestvideo+bestaudio")
