import os
from PIL import Image, ImageFilter
from pathlib import Path
def w(p1, p2):
    p1 = Path( )
    p2 = Path( )
    p2.mkdir()
    for i in img:
        im = Image.open(i)
        im.show()
        f = im.filter(ImageFilter.SHARPEN)
        f.save(f'')