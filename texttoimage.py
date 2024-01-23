from PIL import Image, ImageDraw, ImageFont, ImageFilter

img = Image.open("./picture.jpg")

# def drawCross(img, color, width):
#     draw = ImageDraw.Draw(img)
#     draw.line((0, 0) + img.size, fill=color, width=width)
#     draw.line((0, img.size[0], img.size[1], 0), fill=color, width=width)
#     return img

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

W, H  = img.size

message = "Hello There!\nText on Image"

w, h = draw.textbbox((0, 0), message, font=font)

print(W, H)
print(w, h)

topleft = (100, 100)
bottomright = (250, 250)
draw.arc((W/2-350, H/2-350, W/2 + 350, H/2 + 350), 90, 270, fill="red", width=20)
draw.rectangle(topleft, bottomright, outline="red", width=2)
draw.text(
    (W/2, H/2), 
    message, font=font, fill="White", align='right', anchor="mm"
    )
