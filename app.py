import os
import argparse
from PIL import Image

def clean_image_metadata(input_path, output_directory):
    """
    Opens an image, strips all metadata, and saves it into the specified folder.
    """
    try:
        if not os.path.exists(input_path):
            print(f"[ERROR] The file '{input_path}' does not exist.")
            return

        # Create the output directory if it doesn't exist yet
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
            print(f"[INFO] Created directory: {output_directory}")

        # Construct the final output path
        file_name = os.path.basename(input_path)
        output_path = os.path.join(output_directory, f"cleaned_{file_name}")

        with Image.open(input_path) as img:
            # Recreate the image data to drop all metadata blocks
            data = list(img.getdata())
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(data)
            
            clean_img.save(output_path)
            print(f"[SUCCESS] Metadata removed. Saved to: {output_path}")
            
    except Exception as e:
        print(f"[ERROR] Could not process image: {e}")

def main():
    parser = argparse.ArgumentParser(description="A CLI tool to strip metadata and save images to a specific folder.")
    
    # Argument for the input file
    parser.add_argument("input", help="Path to the original image file")
    
    # Argument for the target folder (default is 'cleaned_photos')
    parser.add_argument("-d", "--dir", default="cleaned_photos", help="Target directory for cleaned images")

    args = parser.parse_args()

    clean_image_metadata(args.input, args.dir)

if __name__ == "__main__":
    main()