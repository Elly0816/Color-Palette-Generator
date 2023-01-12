from resizeimage import resizeimage
from PIL import Image
import os

class Palette:
    def __init__(self, image, folder=None):
        self.image = image
        self.folder = folder
        
    def getImage(self):
        try:
            f = open(os.path.join(self.folder, self.image), 'r')
        except FileNotFoundError: ##Expected error goes here
            if not os.path.exists(self.folder):
                os.mkdir(self.folder)
            
            if not os.path.exists(os.path.join(self.folder, self.image)):
                print('the file was not found')   
        else:
            print('success')
            


palette = Palette('bed.jpg', 'images')
palette.getImage()