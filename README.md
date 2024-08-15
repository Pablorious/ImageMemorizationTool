# Image Memorization Tool

The Image Memorization Tool is a unique utility designed to help improve your memory by interactively masking parts of an image and creating variations to test your recall. Built using Python and Pygame, this tool allows you to cover specific areas of an image and then generate multiple versions of the image with different masked sections. It's perfect for visual learners looking to reinforce their memory through active recall.

It is supposed to be used in conjunction with [ANKI](https://apps.ankiweb.net/).

## What's Special?

- **Memory Enhancement**: Mask parts of an image, such as important details or sections you want to memorize, and then recreate the image from memory using different variations.
- **Interactive Learning**: Draw rectangles on the image to cover areas you want to test your memory on, and generate different versions with these areas hidden.
- **Customizable Practice**: Generate multiple versions of the image, each with different masked sections, allowing for varied and repeated practice.

## How to Use

1. **Run the Tool**:
   Start the program by running the Python script. You'll be prompted to enter the path to the image file you want to use for memorization practice.

   ```bash
   python ul_memorizing_img_generator.py
   ```

2. **Masking Areas**:
   - Click and drag your mouse on the image to draw rectangles over areas you want to memorize. These rectangles will define the sections that will be hidden in the generated images.
   - Press `X` to undo the last rectangle drawn if you make a mistake.

3. **Creating Variations**:
   - Press `O` to generate and save variations of the image. Each version will have different rectangles masked, helping you practice recalling the hidden parts.
   - The generated images will be saved in a new directory named after your image file.

4. **Exit the Tool**:
   - Close the window or press the quit button to exit the tool when you're finished.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install the required dependencies:
   ```bash
   pip install pygame
   ```
2. Run the script:
   ```bash
   python ul_memorizing_img_generator.py
   ```

## Future Improvements

- Adding more interactive tools for enhanced memorization techniques.
- Implementing support for different shapes, like triangles, for more complex masking.
- Enhancing the UI for a more intuitive user experience.
