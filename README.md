# File Organizer Script

## Description

A Python script that automatically organizes files in a directory into folders based on their file type. The script uses `os.scandir()` to efficiently scan directories and `shutil` to move the files to designated folders (e.g., "Text Files", "Images", "PDF Files"). This project is ideal for intermediate Python learners interested in file management automation.

## How It Works

The script performs the following steps:
1. **Scan Directory Files**: It scans the specified directory using `os.scandir()` to identify all files.
2. **Create Folders Based on File Type**: It checks the file extension (e.g., `.txt`, `.jpg`) and creates a corresponding folder if it doesn’t exist.
3. **Move Files to the Appropriate Folder**: It moves the files to their respective folders using `shutil.move()`.

### Supported File Types

By default, the script supports organizing the following file types:

- `.txt` files go to the "Text Files" folder.
- `.jpg` and `.png` files go to the "Images" folder.
- `.pdf` files go to the "PDF Files" folder.
- `.docx` files go to the "Documents" folder.

You can easily add support for additional file types by modifying the `file_types` dictionary in the script.

### Error Handling

- If a folder already exists, the script will not attempt to create it again.
- If a file cannot be moved (due to permissions or other issues), an error message will be printed to the console.

### Future Improvements

- Add support for more file types dynamically.
- Implement logging to track file movements.
- Create a user interface for selecting directories and file types.
- Handle duplicate file names during the move process.
