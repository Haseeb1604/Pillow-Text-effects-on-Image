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

# blurred = Image.new('RGBA', img.size)
# draw = ImageDraw.Draw(blurred)
# xdrop = 0
# ydrop = -10
# blurRatio = 10
# draw.text(xy=(W/2 - xdrop, H/2 - ydrop), text=message, fill='white', font=font, anchor='mm')
# blurred = blurred.filter(ImageFilter.BoxBlur(blurRatio))

# img.paste(blurred, blurred)

# draw = ImageDraw.Draw(img)
# draw.text(xy=(W/2, H/2), text=message, fill='black', font=font, anchor='mm')

# ------------------------------------------------------------------------------------

# text = "Your underlineable text \n New Line Text"

# _, _, text_width, text_height = draw.textbbox((0, 0), text=text, font=font)
# horizontal_margin = (W - text_width) // 2
# vertical_margin = (H - text_height) // 2

# lines = text.splitlines()
# max_width = max(draw.textbbox(text=line, xy=(0, 0), font=font)[2] for line in lines)

# underline_y = vertical_margin + 2
# for line in lines:
#     line_width = draw.textbbox(text=line, xy=(0, 0), font=font)[2]
#     x_start = horizontal_margin + (max_width - line_width) // 2
#     draw.line((x_start, underline_y, x_start + line_width, underline_y), fill="white", width=2)
#     underline_y += draw.textbbox(text=line, xy=(0, 0), font=font)[3]  # Add the height of the line

# draw.text((horizontal_margin, vertical_margin), text, fill="white", font=font)

# img.save("text.png")