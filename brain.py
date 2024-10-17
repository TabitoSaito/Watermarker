from PIL import Image
import numpy as np


class ProcessImage:

    def __init__(self, image_path: str, watermark_path: str = "Pictures/Watermark_domi.png"):
        self.image_path: str = image_path
        self.image = Image.open(self.image_path)
        self.watermark_path: str = watermark_path
        self.watermark = Image.open("Pictures/Watermark_domi.png")

    def calculate_position(self) -> tuple[int, int]:
        position: tuple[int, int] = (self.image.size[0] - self.watermark.size[0],
                                     self.image.size[1] - self.watermark.size[1])
        return position

    def watermark_image(self) -> None:
        watermark_array = np.array(self.watermark.resize(self.image.size).convert("RGB"))
        image_array = np.array(self.image.convert("RGB"))

        image_array[watermark_array != 0] = image_array[watermark_array != 0] * 0.6

        watermarked_img = Image.fromarray(image_array)
        watermarked_img.show()
        save_path_list: list = self.image_path.split("/")
        save_path: str = "/".join(save_path_list[:-1])
        watermarked_img.save(f"{save_path}/watermarked_{save_path_list[-1]}")
