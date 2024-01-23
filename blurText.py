from PIL import Image, ImageDraw, ImageFont, ImageFilter

img = Image.open("./picture.jpg")

font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

W, H  = img.size

message = "Hello There!\nText on Image"

# New transparent image to create blur effect 
blurred = Image.new('RGBA', img.size)
draw = ImageDraw.Draw(blurred)

# Shadow Direction
xdrop = 0
ydrop = -10

# Blur Effect Ratio
blurRatio = 10

draw.text(xy=(W/2 - xdrop, H/2 - ydrop), text=message, fill='white', font=font, anchor='mm')
blurred = blurred.filter(ImageFilter.BoxBlur(blurRatio))

img.paste(blurred, blurred)

draw = ImageDraw.Draw(img)
draw.text(xy=(W/2, H/2), text=message, fill='black', font=font, anchor='mm')