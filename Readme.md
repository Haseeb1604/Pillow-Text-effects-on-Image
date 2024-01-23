# Image Processing Scripts with Pillow

This repository contains a collection of Python scripts utilizing the Pillow library for image processing and text manipulation. Each script is designed for specific purposes, from basic text drawing to advanced effects.

## Table of Contents

1. [Prerequisites](#5-prerequisites)
2. [Getting Started](#6-getting-started)
3. [Basic Text Drawing](#1-basic-text-drawing)
4. [Text with Shadow Effect](#2-text-with-shadow-effect)
5. [Text with Strikethrough Effect](#3-text-with-strikethrough-effect)
6. [Text with Underline Effect](#4-text-with-underline-effect)
7. [Customization](#7-customization)

## 1. Prerequisites

- **Python 3.x**
- **Pillow Library:** A modern version of PIL.
  ```bash
  pip install Pillow
  ```

## 2. Getting Started

1. Clone the repository or download the individual scripts.
2. Place your image file (e.g., `picture.jpg`) in the same directory as the scripts.
3. Adjust script parameters as needed for your specific use case.
4. Run the desired script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of the script.

5. The output image will be saved in the same directory.

## 3. Basic Text Drawing

- **Description:** This script opens an image file, draws formatted text, and showcases basic geometric shapes.
- **Usage:** Ideal for adding simple text and shapes to images for annotation or watermarking.
- **Script:** [texttoimage.py](texttoimage.py)

## 4. Text with Shadow Effect

- **Description:** Introduces a shadow effect to the text on an image using a transparent layer and blurring techniques.
- **Usage:** Create visually appealing text with a subtle shadow for improved readability.
- **Script:** [blurText.py](blurText.py)

## 5. Text with Strikethrough Effect

- **Description:** Defines functions to calculate vertical coordinates and draw text with a strikethrough effect.
- **Usage:** Ideal for emphasizing or marking through certain parts of the text.
- **Script:** [strikethrough.py](strikethrough.py)

## 6. Text with Underline Effect

- **Description:** Defines functions to calculate vertical coordinates and draw text with an underline effect.
- **Usage:** Useful for highlighting or underlining specific sections of the text.
- **Script:** [underlinetext.py](underlinetext.py)

## 6. Customization

Feel free to customize the scripts by adjusting parameters such as font type, font size, image file name, or other drawing options. Explore the scripts' functions and modify them according to your needs.

## 7. Fonts

The `Calibri` folder contains three different variations of the Calibri font:
- Normal
- Italic
- Bold
