from pathlib import Path
import argparse

# Define the sorting rules
CATEGORY_RULES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".md"},
    "archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "audio": {".mp3", ".wav", ".flac"},
    "video": {".mp4", ".mov", ".avi", ".mkv"},
}

# Other
DEFAULT_CATEGORY = "others"
