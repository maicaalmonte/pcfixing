import os
import shutil

# Define the path to your Downloads folder
downloads_folder = os.path.join(os.getenv("USERPROFILE"), "Downloads")

# Define file categories and their extensions
file_types = {
    "GIF": ["gif"],
    "Videos": ["mp4", "mkv", "avi", "mov", "wmv", "m4v"],
    "Photos": ["jpg", "jpeg", "png", "bmp", "tiff", "webp"],
    "PDF": ["pdf", "fdf"],
    "Excel": ["xls", "xlsx", "xlsm"],
    "Audio": ["mp3", "wav", "flac", "aac", "ogg", "m4a"],
    "Documents": ["txt", "doc", "docx", "odt", "rtf"],
    "PowerPoint": ["ppt", "pptx", "pps", "ppsx"],
    "Applications": ["exe", "apk"],
    "Archives": ["zip", "rar", "7z", "tar", "gz"]
}

# Create folders and move files
for category, extensions in file_types.items():
    # Create category folder if it doesn't exist
    category_folder = os.path.join(downloads_folder, category)
    os.makedirs(category_folder, exist_ok=True)

    # Move files to the respective folder
    for file_name in os.listdir(downloads_folder):
        source = os.path.join(downloads_folder, file_name)

        # Skip directories
        if os.path.isdir(source):
            continue

        # Check file extension and move
        if file_name.split(".")[-1].lower() in extensions:
            destination = os.path.join(category_folder, file_name)
            try:
                shutil.move(source, destination)
                print(f"Moved: {file_name} -> {category}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

print("File organization completed!")
