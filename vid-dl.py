import gi

gi.require_version("Gtk", "4.0")

import os
import threading
from pathlib import Path

import yt_dlp  # Fixed: was yt-dlp
from gi.repository import GLib, Gtk


class YouTubeDownloader(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.gtkyt.downloader")
        self.window = None
        self.download_path = str(Path.home() / "Videos/youtube")
        # Ensure download directory exists
        Path(self.download_path).mkdir(parents=True, exist_ok=True)

    def do_activate(self):
        if not self.window:
            self.window = Gtk.ApplicationWindow(application=self)
            self.window.set_title("Vid-dl")
            self.window.set_default_size(600, 250)
            self.window.set_resizable(False)

            self.build_ui()

        self.window.present()

    def build_ui(self):
        # Header bar
        header = Gtk.HeaderBar()
        header.set_title_widget(Gtk.Label(label="Vid-dl"))
        header.set_show_title_buttons(True)
        self.window.set_titlebar(header)

        # Main layout
        main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10,
            margin_start=20,
            margin_end=20,
            margin_top=20,
            margin_bottom=20,
        )
        self.window.set_child(main_box)

        # URL Entry
        self.url_entry = Gtk.Entry()
        self.url_entry.set_placeholder_text("Paste YouTube video URL here")
        main_box.append(self._labelled_row("Video URL:", self.url_entry))

        # Quality selector
        quality_options = Gtk.StringList()
        quality_options.append("1080p (MP4)")
        quality_options.append("720p (MP4)")
        quality_options.append("480p (MP4)")
        quality_options.append("Audio only (MP3)")
        self.quality_combo = Gtk.DropDown(model=quality_options)
        self.quality_combo.set_selected(0)
        main_box.append(self._labelled_row("Download As:", self.quality_combo))

        # Playlist checkbox
        self.playlist_checkbox = Gtk.CheckButton(label="Download entire playlist")
        main_box.append(self.playlist_checkbox)

        # Folder selector
        self.folder_label = Gtk.Label(label=self.download_path, xalign=0)
        self.folder_label.set_ellipsize(3)  # Ellipsize at end
        self.folder_label.set_max_width_chars(40)
        folder_button = Gtk.Button(label="Change Folder")
        folder_button.connect("clicked", self.select_folder)
        folder_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        folder_row.append(folder_button)
        folder_row.append(self.folder_label)
        main_box.append(folder_row)

        # Video Info Display
        self.info_label = Gtk.Label(label="", xalign=0)
        self.info_label.set_selectable(True)
        self.info_label.set_wrap(True)
        main_box.append(self.info_label)

        # Download button
        self.download_button = Gtk.Button(label="Start Download")
        self.download_button.set_margin_top(10)
        self.download_button.connect("clicked", self.start_download)
        main_box.append(self.download_button)

        # Progress bar
        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_show_text(True)
        main_box.append(self.progress_bar)

        # Status message
        self.status_label = Gtk.Label(label="Ready to download", xalign=0.5)
        self.status_label.set_wrap(True)
        main_box.append(self.status_label)

    def _labelled_row(self, label_text, widget):
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        label = Gtk.Label(label=label_text, xalign=0)
        label.set_width_chars(14)
        row.append(label)
        widget.set_hexpand(True)
        row.append(widget)
        return row

    def select_folder(self, button):
        dialog = Gtk.FileDialog.new()
        dialog.set_title("Select Download Folder")

        def on_response(dialog, result):
            try:
                folder = dialog.select_folder_finish(result)  # Fixed: was open_finish
                if folder:
                    self.download_path = folder.get_path()
                    self.folder_label.set_label(self.download_path)
                    # Ensure directory exists
                    Path(self.download_path).mkdir(parents=True, exist_ok=True)
            except GLib.Error as e:
                if "dismissed" not in e.message.lower():
                    self.status_label.set_label(
                        f"Error selecting folder: {e.message}"
                    )

        dialog.select_folder(self.window, None, on_response)  # Fixed: was open

    def start_download(self, button):
        url = self.url_entry.get_text().strip()

        # Better URL validation
        if not url:
            self.status_label.set_label("Please enter a URL")
            return

        if not any(domain in url for domain in ["youtube.com", "youtu.be"]):
            self.status_label.set_label("Please enter a valid YouTube URL")
            return

        quality_index = self.quality_combo.get_selected()
        qualities = ["1080p (MP4)", "720p (MP4)", "480p (MP4)", "Audio only (MP3)"]
        quality = qualities[quality_index]
        self.playlist_enabled = self.playlist_checkbox.get_active()
        self.status_label.set_label("Fetching video info...")
        self.download_button.set_sensitive(False)
        self.progress_bar.set_fraction(0.0)
        self.progress_bar.set_text("0%")
        self.info_label.set_label("")

        threading.Thread(
            target=self.prepare_and_download, args=(url, quality), daemon=True
        ).start()

    def prepare_and_download(self, url, quality):
        # Fetch video info
        try:
            with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get("title", "Unknown Title")
                uploader = info.get("uploader", "Unknown Uploader")
                duration = info.get("duration", 0)
                minutes = duration // 60
                seconds = duration % 60

                info_text = (
                    f" Title: {title}\n"
                    f" Uploader: {uploader}\n"
                    f" Duration: {minutes}:{seconds:02d}"
                )
                GLib.idle_add(self.info_label.set_label, info_text)
                GLib.idle_add(self.status_label.set_label, " Downloading...")
        except Exception as e:
            GLib.idle_add(
                self.status_label.set_label, f" Could not fetch info: {str(e)}"
            )
            GLib.idle_add(self.download_button.set_sensitive, True)
            return

        # Proceed with download
        self.download_worker(url, quality)

    def download_worker(self, url, quality):
        try:
            # Map quality to yt_dlp format strings
            format_map = {
                "1080p (MP4)": "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]",
                "720p (MP4)": "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]",
                "480p (MP4)": "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]",
            }

            if quality == "Audio only (MP3)":
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": os.path.join(self.download_path, "%(title)s.%(ext)s"),
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3",
                            "preferredquality": "192",
                        }
                    ],
                    "progress_hooks": [self.progress_hook],
                    "quiet": True,
                    "no_warnings": True,
                    "noplaylist": not self.playlist_enabled,
                }
            else:
                ydl_opts = {
                    "format": format_map.get(quality, "best"),
                    "merge_output_format": "mp4",
                    "outtmpl": os.path.join(self.download_path, "%(title)s.%(ext)s"),
                    "progress_hooks": [self.progress_hook],
                    "quiet": True,
                    "no_warnings": True,
                    "noplaylist": not self.playlist_enabled,
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            GLib.idle_add(self.update_status, " Download completed!")
            GLib.idle_add(self.progress_bar.set_fraction, 1.0)
            GLib.idle_add(self.progress_bar.set_text, "Complete")
        except Exception as e:
            GLib.idle_add(self.update_status, f" Error: {str(e)}")
            GLib.idle_add(self.progress_bar.set_fraction, 0.0)
        finally:
            GLib.idle_add(self.download_button.set_sensitive, True)

    def progress_hook(self, d):
        if d.get("status") == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes")
            if total and downloaded:
                fraction = downloaded / total
                GLib.idle_add(self.progress_bar.set_fraction, fraction)
                GLib.idle_add(self.progress_bar.set_text, f"{int(fraction * 100)}%")
        elif d.get("status") == "finished":
            GLib.idle_add(self.status_label.set_label, " Processing...")

    def update_status(self, message):
        self.status_label.set_label(message)


if __name__ == "__main__":
    app = YouTubeDownloader()
    app.run()
