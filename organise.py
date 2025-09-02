import os
import shutil
import argparse
from pathlib import Path

def organize_by_extension_and_folder(folder_path):
    folder = Path(folder_path).resolve()

    for item in folder.iterdir():
        # Handle folders
        if item.is_dir():
            if item.name == "folder":
                continue  # Skip if already organized
            dest = folder / "folder"
            dest.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(dest / item.name))
            except Exception as e:
                print(f"⚠️ Could not move folder {item.name}: {e}")
            continue

        # Handle files
        ext = item.suffix.lower().lstrip(".") or "no_extension"
        dest = folder / ext
        dest.mkdir(exist_ok=True)
        try:
            shutil.move(str(item), str(dest / item.name))
        except Exception as e:
            print(f"⚠️ Could not move file {item.name}: {e}")

    print(f"✅ Organized contents of '{folder_path}' by extension and folder type")

def main():
    parser = argparse.ArgumentParser(
        description="Organize files by extension and move folders into a 'folder/' subdirectory."
    )
    parser.add_argument(
        "folder",
        help="Path to the folder you want to organize"
    )

    args = parser.parse_args()
    organize_by_extension_and_folder(args.folder)

if __name__ == "__main__":
    main()
