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


# Function to categorize files based on their extensions(such as .jpg, .pdf, etc.)
def categorize_file(file_path):
    ext = file_path.suffix.lower()

    for category, extensions in CATEGORY_RULES.items():
        if ext in extensions:
            return category

    return DEFAULT_CATEGORY


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
        print(f"Error: The directory '{target} does not exist or is not a directory")
        return

    print("=== auto-file-sorter ===")
    print(f"Scanning directory: {target}")
    print("Categorization results:")

    # Initialize category counts
    count = 0

    for file_path in iter_files(target):
        category = categorize_file(file_path)
        dest_dir = target / category
        # dest_path is the full path where the file will be moved, which is included dest_dir and the file name
        dest_path = dest_dir / file_path.name

        try:
            rel_src = file_path.relative_to(target)
        except ValueError:
            # Just in case(cause of unexpected errors)
            rel_src = file_path

        rel_dest = dest_path.relative_to(target)

        # Print the categorization result
        print(f"{rel_src} --> {rel_dest} ({category})")
        count += 1

    if count == 0:
        print("No files found to categorize")
    else:
        print(f"Total files categorized is: {count}")
        print("Categorization completed.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
