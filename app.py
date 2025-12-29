from pathlib import Path
import argparse

# shutil is basic library for file operations
import shutil

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


# Function to categorize files based on their extensions(such as .jpg, .pdf, etc.)
def categorize_file(file_path):
    ext = file_path.suffix.lower()

    for category, extensions in CATEGORY_RULES.items():
        if ext in extensions:
            return category

    return DEFAULT_CATEGORY


def move_file_to_category(file_path: Path, target_dir: Path):
    category = categorize_file(file_path)
    dest_dir = target_dir / category
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_path = dest_dir / file_path.name

    # If there are name conflicts, it will overwrite the exisiting file, just for now
    shutil.move(str(file_path), str(dest_path))

    return category, dest_path


# Function to iterate through all files in the target directory and its subdirectories
def iter_files(target_dir: Path):
    for item in target_dir.rglob("*"):
        if item.is_file():
            yield item


# Main function to parse arguments and execute categorization
def main():
    parser = argparse.ArgumentParser(description="Automatically categorize files")
    parser.add_argument(
        "target_dir", type=str, help="Directory to scan and categorize files"
    )

    # Define the arguments
    args = parser.parse_args()
    target = Path(args.target_dir)

    if not target.exists() or not target.is_dir():
        print(f"Error: The directory '{target}' does not exist or is not a directory")
        return

    print("=== auto-file-sorter ===")
    print(f"Scanning directory: {target}")

    count = 0
    for file_path in iter_files(target):
        try:
            category, dest_path = move_file_to_category(file_path, target)

            rel_src = file_path.relative_to(target)
            rel_dest = dest_path.relative_to(target)

            print(f"Moved: {rel_src} --> {rel_dest} [{category}]")
            count += 1
        except Exception as e:
            print(f"Error moving file {file_path}: {e}")

    if count == 0:
        print("No files found to categorize")
    else:
        print(f"{count} files categorized successfully")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
