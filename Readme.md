# Image Processing Scripts

This repository contains a set of Python scripts leveraging the Pillow library for image processing and text drawing. Each script serves a specific purpose related to manipulating and enhancing images.

## Prerequisites

- **Python 3.x**
- **Pillow Library:** A modern version of PIL.
  ```bash
  pip install Pillow
  ```

## Getting Started

1. Clone the repository or download the individual scripts.
2. Place your image file (e.g., `picture.jpg`) in the same directory as the scripts.
3. Adjust script parameters as needed for your specific use case.
4. Run the desired script:
   ```bash
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of the script.

5. The output image will be saved in the same directory.

## Files

### [File 1: Basic Text Drawing](texttoimage.py)

- **Description:** This script opens an image file, draws formatted text on it, and showcases basic geometric shapes.
- **Usage:** Demonstration of basic text and shape drawing capabilities.

### [File 2: Text with Shadow Effect](blurText.py)

- **Description:** Introduces a shadow effect to the text on an image using a transparent layer and blurring techniques.
- **Usage:** Create visually appealing text with a subtle shadow for improved readability.

### [File 3: Text with Strikethrough Effect](strikethrough.py)

- **Description:** Defines functions to calculate vertical coordinates and draw text with a strikethrough effect.
- **Usage:** Ideal for emphasizing or marking through certain parts of the text.

### [File 4: Text with Underline Effect](underlinetext.py)

- **Description:** Defines functions to calculate vertical coordinates and draw text with an underline effect.
- **Usage:** Useful for highlighting or underlining specific sections of the text.