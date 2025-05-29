# 🎵 Media Downloader

A simple and powerful command-line tool to download audio and video from **YouTube**, **SoundCloud**, and **Spotify**.  
Supports high-quality downloads, embedded thumbnails, and automatic metadata tagging.

---

## ✨ Features

- 🎬 Download **YouTube** videos or audio in best quality
- 🎧 Download **SoundCloud** tracks in original quality
- 🔍 Download **Spotify** tracks by matching and downloading from YouTube
- 📈 Live **progress bar**
- 🖼️ Automatically embeds **thumbnails** and **metadata** (title, artist, album) in MP3 files

---

## 📦 Requirements

- Python 3.7+
- [FFmpeg](https://ffmpeg.org/) installed and added to your system `PATH`

---

## 🚀 Installation

### 1. Clone the repository
```
git clone https://github.com/guapguap/Loseless-Downloader.git
cd Loseless-Downloader
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Configure Spotify API credentials
```
⚠️ The `.env` file is already included, but **you should replace the credentials with your own** for better reliability.

Example `.env` content:


SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

Get your own credentials at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).


```
### 4. Make sure FFmpeg is installed and accessible from your system terminal
```
▶️ Usage

Run the script:
Double click on launch.py or py launch.py in cmd.

You'll be prompted to choose a platform and paste the media URL.
```
### 🧭 Options
```
1: Download YouTube video (MP4)
2: Download YouTube audio (MP3)
3: Download SoundCloud audio (MP3)
4: Download Spotify track (via YouTube, with metadata)
📁 Output
Downloaded files will be saved in a Downloads/ folder created in the project directory.
```
📄 License
MIT License — see the LICENSE file for details.
