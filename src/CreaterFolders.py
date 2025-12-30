from pathlib import Path

def CreaterFolders():
    # Используем полный путь
    folders = [
        Path("C:/Data"),
        Path("C:/Data/Media"),
        Path("C:/Data/Downloads"),
        Path("C:/Data/Docs"),
        Path("C:/Dev"),
        Path("C:/Dev/Projects"),
        Path("C:/Dev/Archiv"),
        Path("C:/Dev/Experimetns")
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
