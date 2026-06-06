import shutil
from pathlib import Path
from config import EXTENSION_MAP

def organize_directory(target_path: Path):
    """Scans and organizes files in the given target directory path."""
    if not target_path.exists() or not target_path.is_dir():
        print(f"[-] Error: '{target_path}' is not a valid directory.")
        return

    print(f"[+] Organizing directory: {target_path}")
    print("=" * 50)

    for item in target_path.iterdir():
        if item.is_dir():
            continue

        file_extension = item.suffix.lower()

        if file_extension in EXTENSION_MAP:
            folder_name = EXTENSION_MAP[file_extension]
            destination_folder = target_path / folder_name
            destination_folder.mkdir(exist_ok=True)

            destination_path = destination_folder / item.name
            print(f"[MOVING] {item.name} -> {folder_name}/")
            shutil.move(str(item), str(destination_path))
        else:
            print(f"[SKIPPED] {item.name} (No rule matched)")