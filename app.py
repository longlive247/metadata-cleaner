import os
import argparse
from PIL import Image

def clean_image_metadata(input_path, output_path):
    """
    Opens an image, strips all metadata, and saves it.
    """
    try:
        if not os.path.exists(input_path):
            print(f"[ERROR] The file '{input_path}' does not exist.")
            return

        with Image.open(input_path) as img:
            # We recreate the image data to ensure no metadata blocks are copied
            data = list(img.getdata())
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(data)
            
            clean_img.save(output_path)
            print(f"[SUCCESS] Metadata removed. Saved to: {output_path}")
            
    except Exception as e:
        print(f"[ERROR] Could not process image: {e}")

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="A simple CLI tool to strip metadata from images.")
    
    # Add arguments: input file (required) and output file (optional)
    parser.add_argument("input", help="Path to the original image file")
    parser.add_argument("-o", "--output", help="Path for the cleaned image (default: 'cleaned_image.jpg')")

    args = parser.parse_args()

    # Set default output name if none is provided
    output_name = args.output if args.output else "cleaned_" + os.path.basename(args.input)

    clean_image_metadata(args.input, output_name)

if __name__ == "__main__":
    main()