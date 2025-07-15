# downloader/core.py

from yt_dlp import YoutubeDL
from downloader.save_location import get_download_path
from downloader.quality import get_format_selector
from downloader.format_selector import get_selected_format, is_audio_format
import os

def download_video(url, progress_callback, done_callback):
    def hook(d):
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate')

            if total:
                percent_complete = (downloaded / total) * 100
                progress_callback(percent_complete / 100, f"{int(percent_complete)}%")

        elif d['status'] == 'finished':
            progress_callback(1.0, "100%")
            done_callback("✅ Download Complete")

    output_ext = get_selected_format()
    output_path = os.path.join(get_download_path(), '%(title)s.%(ext)s')

    postprocessors = []

    # If MP3, use audio extractor
    if is_audio_format():
        output_ext = "mp3"
        postprocessors.append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        })
    else:
        postprocessors.append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': output_ext,
        })

    ydl_opts = {
        'format': get_format_selector(),
        'outtmpl': output_path,
        'progress_hooks': [hook],
        'quiet': True,
        'merge_output_format': output_ext,
        'postprocessors': postprocessors,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        done_callback(f"❌ Error: {str(e)}")
