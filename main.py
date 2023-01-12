from resizeimage import resizeimage
from resizeimage.imageexceptions import ImageSizeError
from PIL import Image
import os
import webcolors
from colorthief import ColorThief

class Palette:
    def __init__(self, image: str, max_width: int, folder: str=None, count: int=10) -> None:
        self.image = image
        self.count = count
        self.folder = folder
        self.max_width = max_width
        self.new_file_name = None
        self.image_colors: list[int] = []
        
    def getImage(self):
        try:
            f = open(os.path.join(self.folder, self.image), 'r')
        except FileNotFoundError: ##Expected error goes here
            if not os.path.exists(self.folder):
                os.mkdir(self.folder)
            
            if not os.path.exists(os.path.join(self.folder, self.image)):
                print('the file was not found')   
        else:
            with open(os.path.join(self.folder, self.image), 'r+b') as f:
                with Image.open(f) as image:
                    #Resize the image
                    try:
                        smaller_image = resizeimage.resize_width(image, self.max_width)
                    except ImageSizeError:
                        self.max_width = image.size[0]
                        smaller_image = image
                        self.new_file_name = self.image
                    else:
                        self.new_file_name = f"{self.max_width}+{self.image}"
                        smaller_image.save(os.path.join(self.folder, self.new_file_name), image.format)
                    finally:
                        ##print("This is the new filename")
                        ##print(self.new_file_name)
                        pass
                
    def getColors(self):
        color_thief = ColorThief(os.path.join(self.folder, self.new_file_name))
        color_palette = color_thief.get_palette(color_count=self.count, quality=10)
        for color in color_palette:
            self.image_colors.append(webcolors.rgb_to_hex(color));
        return self.image_colors
            


palette = Palette('nature.jpg', 1800, 'images')
palette.getImage()
print(palette.getColors())