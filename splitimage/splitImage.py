#pip install image_slicer
import image_slicer
from PIL import ImageDraw, ImageFont
import os, errno


tiles = image_slicer.slice('false_full_tile1.jpg', 4, save=False)

if not os.path.exists('slices/'):
    os.makedirs('slices/')

image_slicer.save_tiles(tiles, directory='slices/', prefix='slice')