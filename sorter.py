import os
import shutil
from pathlib import Path

# 1. Define the exact path where the script should look.
# Path(__file__).parent dynamically targets the directory where THIS script sits.
BASE_DIR = Path(__file__).parent
TARGET_DIR = BASE_DIR / "test_files"

# 2. Define the structural map (Dictionary)
# Key = file extension to look for, Value = folder name it belongs in
EXTENSION_MAP = {
    ".pdf": "PDFs",
    ".txt": "Texts",
    ".mp4": "Videos",
    ".mkv": "Videos",
}

def organize_files():
    # Safety Check: Ensure the folder actually exists before scanning
    if not TARGET_DIR.exists():
        print(f"Error: Target directory '{TARGET_DIR}' does not exist.")
        return

    print(f"Scanning target directory: {TARGET_DIR}\n" + "="*40)

    # 3. Read the contents of the folder line-by-line
    for item in TARGET_DIR.iterdir():
        
        # Rule: If it's a directory (like our future 'PDFs' folder), skip it!
        if item.is_dir():
            continue

        # 4. Extract the file extension (e.g., '.pdf') and make it lowercase
        file_extension = item.suffix.lower()

        # 5. Check if the file's extension exists in our map
        if file_extension in EXTENSION_MAP:
            target_folder_name = EXTENSION_MAP[file_extension]
            destination_folder = TARGET_DIR / target_folder_name

            # 6. Create the subfolder if it isn't already there
            # 'exist_ok=True' prevents Python from crashing if the folder already exists
            destination_folder.mkdir(exist_ok=True)

            # 7. Define the new destination path, keeping the original filename
            destination_path = destination_folder / item.name

            # 8. Use shutil (Shell Utilities) to move the file
            print(f"[MOVING] {item.name} ---> {target_folder_name}/")
            shutil.move(str(item), str(destination_path))
        else:
            # If the extension isn't in our dictionary, leave it alone entirely
            print(f"[SKIPPED] {item.name} (No category rule defined)")

    print("="*40 + "\nOrganization workflow complete.")

if __name__ == "__main__":
    organize_files()