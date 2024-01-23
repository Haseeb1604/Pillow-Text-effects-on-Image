from typing import Tuple, List
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_y_and_heights(
    text_wrapped: List[str],
    dimensions: Tuple[int, int],
    margin: int,
    font: ImageFont.FreeTypeFont,
) -> Tuple[int, List[int]]:
    """
    Calculate the vertical coordinate to draw the first line of text and the height
    of each line.

    Args:
        text_wrapped (List[str]): A list of wrapped text lines.
        dimensions (Tuple[int, int]): Dimensions of the image (width, height).
        margin (int): Margin between lines.
        font (ImageFont.FreeTypeFont): Font used for drawing text.

    Returns:
        Tuple[int, List[int]]: The Y coordinate for the first line of text and
        a list of line heights.
    """
    # Get the descent value of the font to consider the space below the baseline
    _, descent = font.getmetrics()

    # Empty list to store the height of each line
    line_heights = []

    for text_line in text_wrapped:
        # mask of current line of text
        text_mask = font.getmask(text_line)

        # If the mask exists, calculate the height including descent and margin
        if text_mask:
            line_heights.append(text_mask.getbbox()[3] + descent + margin)
        else:
            # If the line is empty, consider only the descent and margin
            line_heights.append(descent + margin)

    # Adjust the height of the last line by subtracting the margin
    line_heights[-1] -= margin

    # Calculate the total height of the text
    height_text = sum(line_heights)

    # Calculate the starting vertical coordinate to center the text
    y = (dimensions[1] - height_text) // 2

    return y, line_heights

def draw_underlined_text(draw, pos, text, font, **options):
    _, _, width, height = draw.textbbox((0,0), text, font=font)
    lx, ly = pos[0], pos[1] + height
    draw.text(pos, text, font=font, **options)
    draw.line((lx, ly, lx + width, ly), **options)

img = Image.open("./picture.jpg")

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

W, H = img.size

message = "Hello There!\nText on Image"

# Split the message into lines if it contains newline characters
if '\n' in message:
    text_lines = message.split('\n')
else:
    text_lines = [message]

# Vertical margin between lines
v_margin = 8

# Get the starting vertical coordinate and line heights
y, line_heights = get_y_and_heights(text_lines, (W, H), v_margin, font)

# Draw each line of text with a strikethrough effect
for i, line in enumerate(text_lines):
    draw_underlined_text(draw, pos=(10, y), text=line, font=font, fill="white")
    y += line_heights[i]

img.save("output_image.png")
