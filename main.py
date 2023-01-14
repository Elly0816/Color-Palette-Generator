from resizeimage import resizeimage
from resizeimage.imageexceptions import ImageSizeError
from PIL import Image
import os
import webcolors
from colorthief import ColorThief

class Palette:
    """summary:
        image: image file name
        max_width: new with for the resized image
        folder: folder that contains the image
        count: number of colors to get from the image
        quality: quality settings, 1 is the highest quality, the bigger
                        the number, the faster a color will be returned but
                        the greater the likelihood that it will not be the
                        visually most dominant color
    """
    def __init__(self, image: str, max_width: int, folder: str=None, count: int=10, quality: int=1) -> None:
        self.image = image
        self.count = count
        self.folder = folder
        self.max_width = max_width
        self.new_file_name = None
        self.quality = quality
        self.image_colors: list[int] = []
        
    def get_image(self):
        """summary:
            This gets the image from the path defined in the class instance
        Returns:
            type: None
        """
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
                
    def get_colors(self):
        """summary:
            Gets the specified amount of colors from the image in located
            at the path given in the image parameter
        Returns:
            type: None
        """
        color_thief = ColorThief(os.path.join(self.folder, self.new_file_name))
        color_palette = color_thief.get_palette(color_count=self.count, quality=self.quality)
        for color in color_palette:
            self.image_colors.append(webcolors.rgb_to_hex(color));
        return self.image_colors
            
    def save_to_static(self, current_folder, new_folder, new_width, filename):
        with open(os.path.join(current_folder, filename), 'r+b') as f:
                with Image.open(f) as image:
                    #Resize the image
                    try:
                        smaller_image = resizeimage.resize_width(image, new_width)
                    except ImageSizeError:
                        #self.max_width = image.size[0]
                        smaller_image = image
                        smaller_image.save(os.path.join(new_folder, filename), image.format)
                    else:
                        smaller_image.save(os.path.join(new_folder, filename), image.format)

                        ##print("This is the new filename")
                        ##print(self.new_file_name)

    def delete_from_images(self):
        for filename in os.listdir(self.folder):
            if self.image in filename:
                os.remove(os.path.join(self.folder, filename))


# palette = Palette('nature.jpg', 1800, 'images', quality=1)
# palette.getImage()
# print(palette.getColors())