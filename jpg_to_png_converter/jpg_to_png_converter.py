import os
from PIL import Image

def convert_image(input_path, output_path):
    with Image.open(input_path) as im:
        im.save(output_path, 'png', optimize=True, quality=100)


def main():
    print("Welcome to JPG to PNG Converter!")
    jpg_folder = input("Enter the path to the folder containing JPG images: ")
    png_folder = input("Enter the path to the folder where PNG images will be saved: ")
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            output_path = os.path.join(png_folder, os.path.splitext(filename)[0] + '.png')
            convert_image(input_path, output_path)
    print("All images converted successfully!")


if __name__ == "__main__":
    main()

# softy_plug