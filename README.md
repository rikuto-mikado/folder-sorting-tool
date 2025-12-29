# Folder Sorting Tool

Automatically categorize and organize files in a directory based on their file extensions.

## Features

- Recursively scans directories and subdirectories
- Automatically categorizes files by extension
- Moves files into organized category folders
- Handles file conflicts (overwrites by default)

## Installation

No external dependencies required. Uses Python standard library only.

## Usage

```bash
python app.py <target_directory>
```

### Example

```bash
python app.py ~/Downloads
```

This will scan `~/Downloads` and organize all files into category folders.

## Category Rules

| Category   | Extensions                          |
|------------|-------------------------------------|
| images     | .jpg, .jpeg, .png, .gif, .webp     |
| documents  | .pdf, .doc, .docx, .txt, .md       |
| archives   | .zip, .tar, .gz, .rar, .7z         |
| audio      | .mp3, .wav, .flac                  |
| video      | .mp4, .mov, .avi, .mkv             |
| others     | All other file types               |

## Output Structure

Before:
```
Downloads/
├── photo.jpg
├── document.pdf
├── song.mp3
└── video.mp4
```

After:
```
Downloads/
├── images/
│   └── photo.jpg
├── documents/
│   └── document.pdf
├── audio/
│   └── song.mp3
└── video/
    └── video.mp4
```