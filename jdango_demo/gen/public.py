import random
import uuid
from PIL import Image, ImageDraw, ImageFont
import os

def randomColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def mergepic(backfile, msg, fontSize, x, y):
    imageFile = Image.open(backfile)
    dw = ImageDraw.Draw(imageFile)
    font = ImageFont.truetype("gen/static/font/xiaowei.ttf", fontSize)
    dw.text((x, y), msg, font=font, fill=randomColor2())
    file = "gen/static/images/gen/{}".format(str(uuid.uuid1()) + ".jpg")
    imageFile.save(file)
    return os.path.basename(file)

def save_backfile(f):
    target = "gen/static/images/gen/{}".format(str(uuid.uuid1()) + ".jpg")
    with open(target, "wb") as fileObj:
        for chunk in f.chunks():
            fileObj.write(chunk)
    return os.path.basename(target)