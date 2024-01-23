from PIL import Image, ImageDraw, ImageFont, ImageFilter

img = Image.open("./picture.jpg")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

W, H  = img.size

message = "Hello There!\nText on Image"