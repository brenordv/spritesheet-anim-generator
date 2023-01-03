# -*- coding: utf-8 -*-
import os
import math
from pathlib import Path

from PIL import Image

from utils import create_anim_configs


def split_image(image, parts, output_dir):
    """Split an image into frames of the specified width and height.

    Parameters
    ----------
    image : str
        Path to the image file.
    frame_width : int
        Width of each frame.
    frame_height : int
        Height of each frame.
    output_dir : str
        Directory to save the frames to.

    Returns
    -------
    List[str]
        List of file paths to the frames.
    """
    # Open the image
    im = Image.open(image)

    # Get the image width and height
    width, height = im.size

    cols, rows = parts

    frame_width = math.ceil(width / cols)
    frame_height = math.ceil(height / rows)

    # Calculate the number of rows and columns in the image
    rows = math.ceil(height / frame_height)
    cols = math.ceil(width / frame_width)

    # Create a list to store the file paths to the frames
    frame_file_paths = []

    # Iterate over the rows and columns of the image
    for row in range(rows):
        for col in range(cols):
            # Calculate the starting and ending x and y coordinates for this frame
            start_x = col * frame_width
            end_x = start_x + frame_width
            start_y = row * frame_height
            end_y = start_y + frame_height

            # Crop the image to the desired frame
            frame_im = im.crop((start_x, start_y, end_x, end_y))

            # Generate a file name for the frame
            file_name = f"frame_{row}_{col}.png"

            # Create the file path for the frame
            file_path = os.path.join(output_dir, file_name)

            # Save the frame image
            frame_im.save(file_path)

            # Add the file path to the list
            frame_file_paths.append(file_path)

    return frame_file_paths


def create_spritesheet(images, output_file):
    """Create a spritesheet from a list of images.

    Parameters
    ----------
    images : List[str]
        List of file paths to the images.
    output_file : str
        File path to save the spritesheet to.
    """
    # Get the width and height of each image
    im_width, im_height = Image.open(images[0]).size

    # Calculate the number of rows and columns in the spritesheet
    cols = len(images)
    rows = math.ceil(len(images) / cols)

    # Calculate the width and height of the spritesheet
    sheet_width = im_width * cols
    sheet_height = im_height * rows

    # Create a blank image with the desired spritesheet dimensions
    spritesheet = Image.new("RGBA", (sheet_width, sheet_height))

    # Iterate over the rows and columns of the spritesheet
    for row in range(rows):
        for col in range(cols):
            # Calculate the position to paste the image
            x = col * im_width
            y = row * im_height

            # Get the index of the image to paste
            index = row * cols + col

            # If there are no more images to paste, break out of the loop
            if index >= len(images):
                break

            # Open the image
            im = Image.open(images[index])

            # Paste the image onto the spritesheet
            spritesheet.paste(im, (x, y))

    # Save the spritesheet
    spritesheet.save(output_file)


if __name__ == '__main__':
    # Path to the image file
    image_file = "test_img/Catty_Weapon.png"  # CHANGE HERE: Replace here with the path to the original spritesheet.
    img_name = Path(image_file).stem

    # Number of parts to split the image into
    parts = (23, 4)

    # Directory to save the split image parts to
    output_dir = "test_output"  # CHANGE HERE: With the folder where the final sprites/spritesheets will be saved.

    # Split the image into frames
    frame_file_paths = split_image(image_file, parts, output_dir)

    # Create the configurations for the animations that will be created.
    animation_configs = create_anim_configs()

    # Iterates over all the animations that will be created.
    for ac in animation_configs:
        name, indexes = ac.values()

        # Get frames that will be used in that animation
        anim_imgs = [frame_file_paths[i] for i in indexes]

        # File path to save the spritesheet to
        output_file = str(Path(output_dir).joinpath(f"{img_name}__{name}.png").absolute())

        # Create the spritesheet
        create_spritesheet(anim_imgs, output_file)
