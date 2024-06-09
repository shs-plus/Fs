from tkinter import messagebox, Tk, Button

from processer import Processor
from file_manager import FileManager
from settings import Settings

import os


class Application:
    """Main application class."""

    def __init__(self):
        self.root = Tk()
        self.setup_gui()
        self.settings = Settings()
        self.proc = Processor(self.settings)
        self.io = FileManager(self.settings)

    def process_images(self):
        """Process selected images."""
        input_files = self.io.select_files_ui()
        if not input_files:
            return
        output_directory = self.io.select_output_directory_ui()
        if not output_directory:
            return
        for input_file in input_files:
            output_file = os.path.join(output_directory, os.path.basename(input_file))
            processed_img = self.proc.apply_otsu_threshold(input_file)
            processed_img.save(output_file)
        messagebox.showinfo("Success", "Files processed successfully.")

    def setup_gui(self):
        """Set up the GUI."""
        self.root.title("Fs T0")
        self.root.geometry("210x100")
        self.root.resizable(False, False)
        Button(self.root, text="Select Images", command=self.process_images).pack(pady=20)

    def run(self):
        """Run the application."""
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
