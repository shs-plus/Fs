from tkinter import filedialog


class FileManager:
    """Manages file and directory selection dialogs."""

    def __init__(self, settings):
        self.settings = settings

    @staticmethod
    def select_files_ui():
        """UI for selecting input files."""
        return filedialog.askopenfilenames(title="Select input files",
                                           filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"),
                                                      ("All files", "*.*")])

    @staticmethod
    def select_output_directory_ui():
        """UI for selecting output directory."""
        return filedialog.askdirectory(title="Select output directory")
