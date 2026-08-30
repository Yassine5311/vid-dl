# YouTube Downloader

A simple and user-friendly GTK 4 desktop application for downloading YouTube videos and audio in various qualities.

## Features

- 🎬 **Multiple Quality Options**: Download videos in 1080p, 720p, 480p (MP4) or audio only (MP3)
- 📹 **Video Information**: Display video title, uploader, and duration before download
- 📂 **Custom Download Folder**: Choose where to save your downloads
- 📋 **Playlist Support**: Download entire playlists with a single click
- 📊 **Progress Tracking**: Real-time download progress with percentage indicator
- 🎨 **Modern GUI**: Clean and intuitive GTK 4 interface
- 🔄 **Threaded Downloads**: Non-blocking UI during download operations

## Requirements

- **Python 3.8+**
- **GTK 4.0**
- **FFmpeg** (required for audio extraction and video processing)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

### 2. Install System Dependencies

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip libgtk-4-dev libglib2.0-dev ffmpeg
```

**On Fedora:**
```bash
sudo dnf install python3 python3-pip gtk4-devel glib2-devel ffmpeg
```

**On macOS:**
```bash
brew install python3 gtk4 ffmpeg
```

**On Arch Linux:**
```bash
sudo pacman -S python tk4-devel glib2 ffmpeg
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python3 vid-dl.py
```

Or make it executable:

```bash
chmod +x vid-dl.py
./vid-dl.py
```

### How to Use:

1. **Enter URL**: Paste a YouTube video or playlist URL in the "Video URL" field
2. **Select Quality**: Choose your preferred download quality from the dropdown
3. **Playlist Option**: Check "Download entire playlist" if downloading a playlist
4. **Choose Folder**: Click "Change Folder" to select where downloads will be saved
5. **Start Download**: Click "📥 Start Download" to begin
6. **Monitor Progress**: Watch the progress bar and status messages

## Project Structure

```
youtube-downloader/
├── vid-dl.py           # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Dependencies

- **yt-dlp**: YouTube downloader library
- **PyGObject**: Python bindings for GObject (used for GTK 4)

See `requirements.txt` for complete list with versions.

## Configuration

### Default Download Location

By default, videos are saved to `~/Videos/youtube`. This can be changed directly in the application through the "Change Folder" button.

### Download Quality Settings

The application supports the following quality options:
- **1080p (MP4)**: Best video quality available up to 1080p
- **720p (MP4)**: Standard quality
- **480p (MP4)**: Reduced bandwidth option
- **Audio only (MP3)**: Extract audio in MP3 format

## Troubleshooting

### GTK 4 Not Found

If you get an error about GTK 4 not being found:
- Ensure `libgtk-4-dev` (or equivalent) is installed
- Check that your system supports GTK 4 (some older systems may need GTK 3)

### FFmpeg Not Found

If you get an error about FFmpeg missing:
- Install FFmpeg using your system's package manager (see Installation section)
- Verify it's in your PATH: `ffmpeg -version`

### Download Fails

- Verify the URL is a valid YouTube link
- Check your internet connection
- Ensure the download folder has write permissions
- Try with a different video if the issue persists

## License

This project is open source and available under the MIT License. See LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Disclaimer

This tool is for personal use only. Please respect content creators' rights and YouTube's Terms of Service. Only download content you have permission to download.

## Support

If you encounter any issues, please open an issue on GitHub or check the Troubleshooting section above.

---

**Happy downloading!** 🎉
