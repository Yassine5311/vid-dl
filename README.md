# YouTube Downloader

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GTK 4.0](https://img.shields.io/badge/GTK-4.0-green.svg)](https://www.gtk.org/)

A professional-grade GTK 4 desktop application for downloading and converting YouTube videos and audio content. Built with Python, designed for efficiency and ease of use.

## Features

- **Multiple Quality Options** - Download videos in 1080p, 720p, 480p (MP4) or audio only (MP3)
- **Metadata Preview** - Display video title, uploader, and duration before initiating downloads
- **Flexible Output Location** - Custom download folder selection with automatic directory creation
- **Batch Processing** - Download entire playlists efficiently
- **Real-time Progress Tracking** - Live progress updates with percentage indicators
- **Modern User Interface** - Clean GTK 4 native interface with responsive design
- **Asynchronous Operations** - Non-blocking UI with threaded download operations
- **Robust Error Handling** - Comprehensive error messages and recovery options

## System Requirements

| Component | Version | Purpose |
|-----------|---------|----------|
| Python | 3.8+ | Runtime environment |
| GTK | 4.0+ | UI framework |
| FFmpeg | Latest | Audio/video processing |
| libgtk-4 | Dev headers | GTK development libraries |
| libglib2.0 | Dev headers | GLib development libraries |

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

### Step 2: Install System Dependencies

**Ubuntu / Debian**
```bash
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-dev libgtk-4-dev libglib2.0-dev ffmpeg
```

**Fedora / RHEL**
```bash
sudo dnf install -y python3 python3-pip gtk4-devel glib2-devel ffmpeg
```

**macOS**
```bash
brew install python3 gtk4 ffmpeg
```

**Arch Linux**
```bash
sudo pacman -S python python-pip gtk4 glib2 ffmpeg
```

### Step 3: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### Quick Start

```bash
python3 vid-dl.py
```

Or make the script executable:

```bash
chmod +x vid-dl.py
./vid-dl.py
```

### User Guide

1. **Input URL** - Paste a YouTube video or playlist URL into the "Video URL" field
2. **Select Format** - Choose your preferred output quality:
   - 1080p (MP4) - Maximum video quality
   - 720p (MP4) - Balanced quality and file size
   - 480p (MP4) - Reduced bandwidth consumption
   - Audio only (MP3) - Audio extraction
3. **Playlist Mode** - Enable the "Download entire playlist" checkbox for batch operations
4. **Set Output Location** - Click "Change Folder" to specify the download directory
5. **Initiate Download** - Click "Start Download" to begin the operation
6. **Monitor Progress** - Observe real-time progress updates via the progress bar and status indicators

## Project Structure

```
youtube-downloader/
├── vid-dl.py              # Main application entry point
├── requirements.txt       # Python package dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history and updates
└── .gitignore             # Git repository exclusions
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| yt-dlp | ≥2024.1.1 | YouTube content extraction and downloading |
| PyGObject | ≥3.48.0 | Python bindings for GTK 4 and GObject |

For complete dependency specifications, refer to [requirements.txt](requirements.txt).

## Configuration

### Default Output Directory

The application saves content to `~/Videos/youtube` by default. This location can be modified at runtime using the "Change Folder" interface button.

### Output Formats

| Format | Codec | Bitrate | Use Case |
|--------|-------|---------|----------|
| 1080p (MP4) | H.264 + AAC | Adaptive | Maximum video fidelity |
| 720p (MP4) | H.264 + AAC | Adaptive | Balanced quality/size |
| 480p (MP4) | H.264 + AAC | Adaptive | Low bandwidth environments |
| Audio (MP3) | MP3 | 192 kbps | Audio-only content |

### Advanced Options

- **Playlist Mode**: Enable to download entire playlists as a batch operation
- **Custom Output Path**: Dynamically change the save location per download session

## Troubleshooting

### GTK 4 Not Found

**Issue**: "GTK 4 not found" error on startup

**Solution**:
- Install GTK 4 development headers: `sudo apt-get install libgtk-4-dev` (Debian/Ubuntu)
- Verify GTK 4 availability: `pkg-config --modversion gtk4`
- Note: GTK 4 is required; GTK 3 is not compatible

### FFmpeg Not Found

**Issue**: "FFmpeg not found" error during audio extraction

**Solution**:
- Install FFmpeg using your system package manager
- Verify installation: `ffmpeg -version`
- Ensure the executable is in your system PATH

### Download Failures

**Issue**: Downloads fail or produce errors

**Diagnostic Steps**:
1. Validate the YouTube URL format
2. Test network connectivity: `ping youtube.com`
3. Verify write permissions on the output directory: `touch ~/Videos/youtube/test.txt`
4. Attempt download with a different video to isolate the issue
5. Check system logs for detailed error messages

### UI Freezing

**Issue**: Application interface becomes unresponsive during downloads

**Solution**: This is likely due to system resource constraints. The application uses threading, so this should not occur. If it does:
- Check system memory and disk space availability
- Restart the application and try again
- Report the issue with system specifications

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for complete details.

## Contributing

Contributions are highly encouraged and appreciated. For detailed guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

### Ways to Contribute

- **Report Bugs** - Submit detailed issues with reproducible steps
- **Suggest Features** - Propose enhancements with use cases
- **Submit Pull Requests** - Contribute code improvements
- **Improve Documentation** - Enhance README, comments, or guides
- **Test & Validate** - Help identify edge cases and compatibility issues

## Legal Notice

**Disclaimer**: This tool is provided for legitimate, personal use only. Users are responsible for ensuring compliance with:
- YouTube's Terms of Service
- Applicable copyright and intellectual property laws
- Local regulations regarding content download
- Individual content creators' licensing agreements

Unauthorized reproduction or distribution of copyrighted content is prohibited.

## Support & Issues

- **Bug Reports** - Open an issue on GitHub with detailed reproduction steps
- **Feature Requests** - Create an issue with the `enhancement` label
- **Troubleshooting** - Consult the [Troubleshooting](#troubleshooting) section or existing issues
- **Security Issues** - Report privately to project maintainers

## Changelog

For version history and upcoming features, see [CHANGELOG.md](CHANGELOG.md).

---

**Project Status**: Active Development | **Last Updated**: 2024

Made with Python and GTK 4
