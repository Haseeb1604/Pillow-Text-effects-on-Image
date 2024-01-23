from PIL import Image, ImageDraw, ImageFont

# Open the image and create a drawing object
img = Image.open("./picture.jpg")
draw = ImageDraw.Draw(img)

# Load the font and get image dimensions
font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)
W, H = img.size

# Get text bounding box and calculate margin for centering
text = "Your underlineable text \n text on new line"
_, _, text_width, text_height = draw.textbbox((0, 0), text=text, font=font)
horizontal_margin = (W - text_width) // 2
vertical_margin = (H - text_height) // 2

# Draw the text with centered position
draw.multiline_text((horizontal_margin, vertical_margin), text, fill="black", font=font)

# Calculate y-coordinate for underline and draw underline line
underline_y = text_height + vertical_margin + 2
draw.line((horizontal_margin, underline_y, horizontal_margin + text_width, underline_y), fill="black", width=2)

# Save the image
img.save("text.png")