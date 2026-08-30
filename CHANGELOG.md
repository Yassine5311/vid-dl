# Changelog

All notable changes to this project are documented in this file.

**Format**: Based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
**Versioning**: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [1.0.0] - 2024-08-30

### Added
- Initial stable release of YouTube Downloader
- GTK 4.0 native graphical user interface
- Multi-quality video download (1080p, 720p, 480p MP4)
- Audio extraction to MP3 format with configurable bitrate
- Batch playlist download support
- Real-time download progress tracking with percentage display
- Pre-download metadata display (title, uploader, duration)
- Custom output directory selection with automatic creation
- Asynchronous download operations with non-blocking UI
- Comprehensive error handling and user feedback
- Cross-platform support (Linux, macOS, BSD)
- Full project documentation and contribution guidelines

### Core Features
✓ YouTube video download in multiple formats
✓ MP3 audio extraction
✓ Playlist batch processing
✓ Modern, responsive GTK 4 interface
✓ Live progress monitoring
✓ Metadata preview before download
✓ Folder browsing and selection
✓ Thread-based download management

---

## [Unreleased] - Development

### Planned Features (Next Release)

- [ ] Video thumbnail preview in metadata display
- [ ] Download queue management and prioritization
- [ ] Subtitle/caption download support
- [ ] Additional audio format export (AAC, FLAC, OGG)
- [ ] Preferences/settings dialog with persistent configuration
- [ ] Batch download from text file or URL list
- [ ] Application theme support (light/dark mode)
- [ ] Download history and management
- [ ] Keyboard shortcuts for common operations
- [ ] Integration with system download manager

### Improvements
- Performance optimization for large playlist processing
- Enhanced error recovery mechanisms
- Expanded platform compatibility testing
- Comprehensive automated test suite
- API documentation for potential extension framework

### Known Issues
- FFmpeg must be installed separately on all platforms (no bundled binary)
- Some YouTube age-gated content may require additional authentication
- Large playlist downloads (1000+ videos) may require extended timeouts

---

## Version Legend

- **Added** - New features and capabilities
- **Changed** - Modifications to existing functionality
- **Fixed** - Bug fixes and corrections
- **Deprecated** - Features scheduled for removal
- **Removed** - Previously deprecated features
- **Security** - Vulnerability patches and security updates

---

## Support & Contributing

- 🐛 **Report Bugs**: [GitHub Issues](https://github.com/yassine5311/vid-dl/issues)
- 💡 **Request Features**: [GitHub Discussions](https://github.com/yassine5311/vid-dl/discussions)
- 🤝 **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)
- 📖 **Documentation**: [README.md](README.md)

**Project Status**: ✅ Active Development | **Maintained**: Yes
