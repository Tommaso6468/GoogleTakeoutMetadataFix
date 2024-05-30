# Google Photos Takeout Metadata Fix

![Python](https://img.shields.io/badge/Python-3)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Unix-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

This Python script helps you clean up your Google Photos export by updating the creation time of your JPG files based on the `photoTakenTime` metadata from the corresponding JSON files. Additionally, it removes the JSON files after processing. This script is especially useful for organizing your photos after exporting them from Google Photos.

## Prerequisites

- Python 3 or higher
- `pywin32` library for Windows file time modification (Windows only)

## Installation

### Step 1: Clone the repository

```sh
git clone https://github.com/Tommaso6468/GooglePhotosTakeoutMetadataFix.git
cd GooglePhotosTakeoutMetadataFix
```
### Step 2: Install dependencies
Windows only:
```sh
pip install pywin32
```

## Usage

### Command line arguments
The script accepts multiple directories as arguments. Each directory should contain the JPG files and their corresponding JSON metadata files.

### Example command
```sh
python windows.py /path/to/your/photos1 /path/to/your/photos2
```

### Script execution
1. Open a terminal or command prompt
2. Navigate to the directory where you cloned the repository
3. Run the script with the desired directories

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
