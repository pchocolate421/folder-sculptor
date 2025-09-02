# Folder Sculptor 🗂️

**Folder Sculptor** is a Python utility that organizes messy directories by sorting files into folders based on their extensions and grouping all subfolders into a single `folder/` directory.

## Features
- Automatically creates folders named after file extensions
- Moves all subfolders into a `folder/` directory
- Handles files with no extension
- Simple command-line interface

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/folder-sculptor.git
cd folder-sculptor
pip install -r requirements.txt
```

## Usage

```bash
python organize.py /path/to/your/messy/folder
```

### Example

```bash
python organize.py "C:/Users/Daniel/Downloads"
```

This will:
- Move `.pdf` files to `pdf/`
- Move `.mp4` files to `mp4/`
- Move folders to `folder/`
- Move files with no extension to `no_extension/`

## License
MIT License
