import os
import sys
from pathlib import Path
from yt_dlp import YoutubeDL
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from mutagen.easyid3 import EasyID3

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

OUTPUT_DIR = Path("Downloads")
OUTPUT_DIR.mkdir(exist_ok=True)

sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii():
    spotify_green = "\033[38;5;46m"
    reset = "\033[0m"
    ascii_art = f"""
{spotify_green}
░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░  
       ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
     ░▒▓██▓▒░       ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓██▓▒░         ░▒▓█▓▒░ ░▒▓██████▓▒░ ░▒▓████████▓▒░ 
 ░▒▓██▓▒░    ░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░░▒▓██████▓▒░    ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░ 
{reset}
"""
    print(ascii_art)

def format_size(bytes_value):
    return f"{round(bytes_value / 1024 / 1024, 1)}MiB"

def edit_metadata(filepath, title=None, artist=None, album=None):
    """Edit ID3 tags of downloaded files"""
    audio = EasyID3(filepath)
    if title: audio['title'] = title
    if artist: audio['artist'] = artist
    if album: audio['album'] = album
    audio.save()    

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        downloaded = d.get('downloaded_bytes', 0)
        percent = downloaded / total_bytes if total_bytes else 0
        percent_str = f"{percent * 100:5.1f}%"
        size_str = format_size(downloaded)
        filename = os.path.basename(d.get('filename', 'unknown'))

        bar_len = 20
        filled_len = int(bar_len * percent)
        bar = '█' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write(f"\r[{bar}] {percent_str} | {size_str} | {filename}")
        sys.stdout.flush()

    elif d['status'] == 'finished':
        print("\nTrack downloaded successfully.")

def download_spotify(url: str) -> None:
    try:
        track_id = url.split('/track/')[1].split('?')[0]
        track = sp.track(track_id)

        title = track['name']
        artist = ', '.join([a['name'] for a in track['artists']])
        query = f"{title} {artist}"

        print(f"{title} - {artist}")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(OUTPUT_DIR / f"{title} - {artist}.%(ext)s"),
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegMetadata'}
            ],
            'writethumbnail': True,
            'embed_thumbnail': True,
            'quiet': True,
            'no_warnings': True,
            'progress_hooks': [progress_hook],
            'logtostderr': False,
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'ytsearch1:{query}'])
    except Exception as e:
        print(f"\nError: {e}")

def download_high_quality_audio(url: str, platform: str) -> None:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(OUTPUT_DIR / '%(title)s.%(ext)s'),
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata'}
        ],
        'writethumbnail': True,
        'embed_thumbnail': True,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [progress_hook],
        'logtostderr': False,
    }

    if platform == 'SoundCloud':
        ydl_opts['extractor_args'] = {'soundcloud': {'format': 'original'}}

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Title')
            print(title)
            ydl.download([url])
    except Exception as e:
        print(f"\nError: {e}")

def download_youtube_video(url: str) -> None:
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': str(OUTPUT_DIR / '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [progress_hook],
        'logtostderr': False,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(info.get('title', 'Unknown Title'))
            ydl.download([url])
    except Exception as e:
        print(f"\nError: {e}")

# MAIN
if __name__ == "__main__":
    clear_console()
    print_ascii()

    print("⚡ MEDIA DOWNLOADER ⚡")
    choice = input("Choose target:\n1. YouTube (Video)\n2. YouTube (Audio)\n3. SoundCloud\n4. Spotify\n> ").strip()
    url = input("Enter URL: ").strip()

    platforms = {
        '1': 'YouTube Video',
        '2': 'YouTube',
        '3': 'SoundCloud',
        '4': 'Spotify'
    }

    if choice == '1':
        download_youtube_video(url)
    elif choice == '4':
        download_spotify(url)
    elif choice in platforms:
        download_high_quality_audio(url, platforms[choice])
    else:
        print("Invalid choice.")
