from PIL import Image, ImageDraw, ImageFont, ImageFilter

def draw_strikethrough_text(draw, pos, text, font, **options):
    _, _, width, text_height = draw.textbbox((0,0), text, font=font) 

    # Calculate the baseline and height of the text
    ascent, descent = font.getmetrics()
    baseline = pos[1] + text_height - descent

    # Calculate the position for the strikethrough line
    line_thickness = 2  # Adjust the thickness of the strikethrough line as needed
    ly = baseline + (line_thickness // 2)

    draw.text(pos, text, font=font, **options)
    draw.line((pos[0], ly, pos[0] + width, ly), **options)


img = Image.open("./picture.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

W, H = img.size

message = "Hello There!\nText on Image"

if '\n' in message:
    text_lines = message.split('\n')
else:
    text_lines = [message]

y = 10  # Set your starting y-coordinate

for line in text_lines:
    # Draw each line of text with a strikethrough effect
    draw_strikethrough_text(draw, pos=(10, y), text=line, font=font, fill="black")
    _, _, _, line_height = draw.textbbox((10, y), line, font=font)
    y += line_height 


# Save the resulting image
img.save("output_image.png")
