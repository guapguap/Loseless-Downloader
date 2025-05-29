# Media Downloader

A simple command-line tool to download audio and video from YouTube, SoundCloud, and Spotify tracks.  
Supports high-quality audio downloads, embedding thumbnails, and metadata tagging.

## Features

- Download YouTube videos or audio in best quality  
- Download SoundCloud tracks with original quality  
- Download Spotify tracks by searching on YouTube and tagging metadata  
- Progress bar for downloads  
- Automatically embeds thumbnails and metadata (title, artist, album) in MP3 files

## Requirements

- Python 3.7+  
- [FFmpeg](https://ffmpeg.org/) installed and added to your system PATH

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   
   
2. Install dependencies:

pip install -r requirements.txt


3. Prepare your .env file with Spotify credentials.
The .env file is already set up for you, but it is recommended to replace the Spotify Client ID and Client Secret with your own for better reliability and to avoid usage limits.

Example .env content:

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
You can get your own credentials at the Spotify Developer Dashboard.

4. Make sure FFmpeg is installed and accessible from your system's command line.

Usage
Run the script:

python launch.py
You will be prompted to choose a platform and enter the media URL.

Options
1: Download YouTube video (MP4)

2: Download YouTube audio (MP3)

3: Download SoundCloud audio (MP3)

4: Download Spotify track (finds best matching YouTube audio and downloads with metadata)

Output
Downloaded files will be saved in the Downloads folder created in the script directory.






MIT License — see the LICENSE file for details.