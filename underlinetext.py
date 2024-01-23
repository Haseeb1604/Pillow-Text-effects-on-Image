from PIL import Image, ImageDraw, ImageFont, ImageFilter

img = Image.open("./picture.jpg")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

W, H  = img.size

text = "Your underlineable text \n New Line Text"

_, _, text_width, text_height = draw.textbbox((0, 0), text=text, font=font)
horizontal_margin = (W - text_width) // 2
vertical_margin = (H - text_height) // 2

lines = text.splitlines()
max_width = max(draw.textbbox(text=line, xy=(0, 0), font=font)[2] for line in lines)

underline_y = vertical_margin + 2
for line in lines:
    line_width = draw.textbbox(text=line, xy=(0, 0), font=font)[2]
    x_start = horizontal_margin + (max_width - line_width) // 2
    draw.line((x_start, underline_y, x_start + line_width, underline_y), fill="white", width=2)
    underline_y += draw.textbbox(text=line, xy=(0, 0), font=font)[3]  # Add the height of the line

draw.text((horizontal_margin, vertical_margin), text, fill="white", font=font)

img.save("text.png")