import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, UnidentifiedImageError
from brain import ProcessImage


class Interface(tk.Tk):

    def __init__(self):
        super().__init__()
        self.file_path = None
        self.title("Watermarker")
        self.title_img = ImageTk.PhotoImage(Image.open("Pictures/Watermark.jpg"))

        import_button = tk.Button(self, text="Import File", command=self.import_file)

        process_button = tk.Button(self, text="Process Image", command=self.process)

        canvas = tk.Canvas(self, width=300, height=300)
        canvas.create_image(20, 20, image=self.title_img)

        label_file_path = tk.Label(self, text="FilePath:")

        self.input_file_path = tk.Entry(self)

        import_button.grid(row=1, column=2, pady=20)
        process_button.grid(row=2, column=0, padx=20, pady=20, columnspan=3)
        canvas.grid(row=0, column=0, padx=20, pady=20, columnspan=3)
        label_file_path.grid(row=1, column=0, pady=20)
        self.input_file_path.grid(row=1, column=1, pady=20, ipadx=30)

    def import_file(self) -> None:
        self.file_path: str = filedialog.askopenfilename(title="Select a file",
                                                         filetypes=[("Images", ".jpg .png"), ("All files", "*.*")])
        if self.file_path:
            self.input_file_path.delete(0, tk.END)
            self.input_file_path.insert(0, self.file_path)

    def process(self):
        file_path: str = self.input_file_path.get()
        try:
            processor = ProcessImage(file_path)
            processor.watermark_image()
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File not found.")
        except UnidentifiedImageError:
            messagebox.showinfo(title="Error", message="Not an accepted file format.")


