# Final Scan

Final Scan is a Python application that allows users to process images using Otsu's thresholding method and save the processed images to a selected directory.

## Features

- Select multiple images for processing
- Apply Otsu's thresholding method to images
- Save processed images to a selected directory

## How to Use

1. Run the application.
2. Click on the "Select Images" button to select the images you want to process.
3. Select the directory where you want to save the processed images.
4. The application will process the images and save them to the selected directory.

## Dependencies

- Python
- Tkinter
- PIL (Pillow)
- skimage
- numpy

## Files

- `main.py`: The main application file. It contains the `Application` class which is responsible for the GUI and the image processing workflow.
- `processer.py`: Contains the `Processor` class which handles image processing tasks.
- `file_manager.py`: Contains the `FileManager` class which manages file and directory selection dialogs.

## Author

colinwang1703