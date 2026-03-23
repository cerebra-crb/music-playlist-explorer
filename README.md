# 🎵 Netease Cloud Playlist Exporter

A Python tool to export songs from a **Netease Cloud Music playlist** into a clean text file, filtering out songs with Chinese characters. Perfect for creating curated, international song lists for personal use or migration to other platforms.  

## Features ✨

- **Fetch any public playlist** by ID from Netease Cloud Music.
- **Automatically filters out Chinese songs**, keeping only non-Chinese tracks.
- **Batch processing** to handle large playlists efficiently.
- **Outputs a clean text file** with song titles and artists.
- Simple and easy-to-use Python script.

## How It Works ⚙️

1. The script fetches all track IDs from the specified playlist.
2. It retrieves detailed song information in batches.
3. It checks each song’s title for Chinese characters and skips them.
4. Remaining songs are written to a text file with numbering and artist names.

## Usage 📝

1. Make sure you have Python installed (tested with Python 3.10+).  
2. Install dependencies:
   ```bash
   pip install requests
