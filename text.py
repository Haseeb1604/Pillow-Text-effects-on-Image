import logging
import os
import sys
from pathlib import Path, PosixPath
from typing import Tuple, List, Dict
from urllib.request import urlopen

# from moviepy.editor import (
#     CompositeVideoClip,
#     ImageClip,
#     TextClip,
#     VideoFileClip,
# )
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def get_y_and_heights(
    text_wrapped: List[str],
    dimensions: Tuple[int, int],
    margin: int,
    font: ImageFont.FreeTypeFont,
) -> Tuple[int, List[int]]:
    """
    Get the vertical coordinate to draw the first line of text and the height
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
    _, descent = font.getmetrics()

    line_heights = []
    for text_line in text_wrapped:
        text_mask = font.getmask(text_line)
        if text_mask:
            line_heights.append(text_mask.getbbox()[3] + descent + margin)
        else:
            line_heights.append(descent + margin)  # Add margin for empty lines

    line_heights[-1] -= margin
    height_text = sum(line_heights)
    y = (dimensions[1] - height_text) // 2

    return y, line_heights


def draw_underlined_text(draw, pos, text, font, align, **options):
    _, _, width, height = draw.textbbox((0,0), text, font=font)
    lx, ly = pos[0], pos[1] + height
    draw.text(pos, text, font=font, align=align, **options)
    draw.line((lx, ly, lx + width, ly), **options)


def draw_shadow_effect(bg, pos, text: str, font, fill, align):
    # Create piece of canvas to draw text on and blur
    blurred = Image.new("RGBA", bg.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=pos, text=text, fill=fill, font=font, align=align)
    blurred = blurred.filter(ImageFilter.BoxBlur(15))

    # Paste soft text onto background
    bg.paste(blurred, blurred)

    # Draw on sharp text
    draw = ImageDraw.Draw(bg)
    draw.text(xy=pos, text=text, fill=fill, font=font, align=align)


def draw_strikethrough_text(draw, pos, text, font, align, **options):
    # width, text_height = draw.textsize(text, font=font) # Depreciated | Removed from latest version
    _, _, width, text_height = draw.textbbox((0,0), text, font=font) 

    # Calculate the baseline and height of the text
    ascent, descent = font.getmetrics()
    baseline = pos[1] + text_height - descent

    # Calculate the position for the strikethrough line
    line_thickness = 2  # Adjust the thickness of the strikethrough line as needed
    ly = baseline + (line_thickness // 2)

    draw.text(pos, text, font=font, align=align, **options)
    draw.line((pos[0], ly, pos[0] + width, ly), **options)

def overlay_text():
    """
    Overlay static text on the video clip.

    Args:
        layer (dict): Layer information containing text properties.
        duration (float): Duration of the video clip.

    Returns:
        VideoFileClip: Video clip with overlaid text.
    """

    img = Image.open("./picture.jpg")

    # font = ImageFont.truetype("./Calibri/calibrib.ttf", 100)

    width, height  = 466, 1056
    
    v_margin = 10

    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw_interface = ImageDraw.Draw(img)

    font_size = 50

    while True:
        font = ImageFont.truetype("./Calibri/calibrib.ttf", font_size)
        text_lines = ["1fadk", "2dflkjda", "3lkajdlskf", "4dfkjdk", "5dfdkjlds", "6dfsjdl",
                      "7fadk", "8dflkjda", "9dflkajdlskf", "10dfkjdk", "11dfdkjlds", "12dfsjdl",
                      "13fadk", "14dflkjda", "15dflkajdlskf", "16dfkjdk", "17dfdkjlds", "18dfsjdl",
                      ]

        # Get the first vertical coordinate at which to draw text and the height of each line of text
        y, line_heights = get_y_and_heights(text_lines, (width, height), v_margin, font)

        # print("v_margin : ", v_margin)
        # print("font_size : ", font_size)
        # Check if the text fits within the specified dimensions
        if sum(line_heights) < height:
            break
        
        if v_margin != 0:
            v_margin -= 2
        else:
            font_size -=5
    # y, line_heights = get_y_and_heights(text_lines, (width, height), v_margin, font)

    underline = True
    strikethrough = False
    shadow_effect = True
    text_color  = "white"
    align = "right"

    margin = 50
    # Draw each line of text
    for i, line in enumerate(text_lines):
        line_mask = font.getmask(line)
        if line_mask:
            line_width = line_mask.getbbox()[2]

            if align == "left":
                x = margin  # Set your left margin value here
            elif align == "right":
                x = (width - line_width) - margin  # Adjust for any additional margin you want
            else:
                x = (width - line_width) // 2  # Center alignment

            if underline:
                draw_underlined_text(
                    draw_interface, pos=(x, y), text=line, font=font, fill=text_color, align=align
                )
            elif strikethrough:
                draw_strikethrough_text(
                    draw_interface, pos=(x, y), text=line, font=font, fill=text_color, align=align
                )
            elif shadow_effect:
                draw_shadow_effect(
                    bg=img,
                    pos=(x, y),
                    text=line,
                    font=font,
                    fill=text_color,
                    align=align
                )
            else:
                draw_interface.text((x, y), line, font=font, fill=text_color, align=align)
            y += line_heights[i]

    # Save the resulting image
    img.save("text.png")

overlay_text()