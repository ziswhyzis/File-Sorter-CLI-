from pathlib import Path

EXTENSION_MAP = {
    # Documents & Texts
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".md": "Documents",
    ".rtf": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    # Images & Graphics
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",
    ".ico": "Images",

    # Videos & Movies
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".flv": "Videos",
    ".wmv": "Videos",

    # Audio & Music
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".m4a": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",

    # Compressed Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar.gz": "Archives",
    ".tgz": "Archives",
    ".gz": "Archives",

    # Installers & System Binaries
    ".exe": "Installers",
    ".msi": "Installers",
    ".deb": "Installers",  # Linux installations
    ".dmg": "Installers",  # macOS installations
    ".iso": "Installers",  # Disc images

    # Programming Code Files
    ".py": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".h": "Code",
    ".java": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".json": "Code"
}