# Image Processing Scripts with Pillow

This repository contains a collection of Python scripts utilizing the Pillow library for image processing and text manipulation. Each script is designed for specific purposes, from basic text drawing to advanced effects.

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Setting Up a Virtual Environment](#2-setting-up-a-virtual-environment)
3. [Installing Dependencies](#3-installing-dependencies)
4. [Getting Started](#4-getting-started)
5. [Basic Text Drawing](#5-basic-text-drawing)
6. [Text with Shadow Effect](#6-text-with-shadow-effect)
7. [Text with Strikethrough Effect](#7-text-with-strikethrough-effect)
8. [Text with Underline Effect](#8-text-with-underline-effect)
9. [Customization](#9-customization)

## 1. Prerequisites

- **Python 3.x**

## 2. Setting Up a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies for your projects. Follow these steps to create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (on Windows)
venv\Scripts\activate

# Activate the virtual environment (on Unix or MacOS)
source venv/bin/activate
```

## 3. Installing Dependencies

After activating the virtual environment, install the required dependencies using the following command:

```bash
pip install Pillow
```

## 4. Getting Started

1. Clone the repository or download the individual scripts.
2. Place your image file (e.g., `picture.jpg`) in the same directory as the scripts.
3. Adjust script parameters as needed for your specific use case.
4. Run the desired script:

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the script.

5. The output image will be saved in the same directory.

## 5. Basic Text Drawing

- **Description:** This script opens an image file, draws formatted text, and showcases basic geometric shapes.
- **Usage:** Ideal for adding simple text and shapes to images for annotation or watermarking.
- **Script:** [texttoimage.py](texttoimage.py)

## 6. Text with Shadow Effect

- **Description:** Introduces a shadow effect to the text on an image using a transparent layer and blurring techniques.
- **Usage:** Create visually appealing text with a subtle shadow for improved readability.
- **Script:** [blurText.py](blurText.py)

## 7. Text with Strikethrough Effect

- **Description:** Defines functions to calculate vertical coordinates and draw text with a strikethrough effect.
- **Usage:** Ideal for emphasizing or marking through certain parts of the text.
- **Script:** [strikethrough.py](strikethrough.py)

## 8. Text with Underline Effect

- **Description:** Defines functions to calculate vertical coordinates and draw text with an underline effect.
- **Usage:** Useful for highlighting or underlining specific sections of the text.
- **Script:** [underlinetext.py](underlinetext.py)

## 9. Customization

Feel free to customize the scripts by adjusting parameters such as font type, font size, image file name, or other drawing options. Explore the scripts' functions and modify them according to your needs.

## 10. Fonts

The `Calibri` folder contains three different variations of the Calibri font:
- Normal
- Italic
- Bold