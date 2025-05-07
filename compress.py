import os
from PIL import Image

def compress_images(input_folder="images", output_folder="compressed", quality=50):
    """
    Compress all images in the input folder and save them to the output folder.
    
    Args:
        input_folder (str): Folder containing original images.
        output_folder (str): Folder to save compressed images.
        quality (int): JPEG quality (1-100), lower means more compression.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
            continue
        
        try:
            with Image.open(input_path) as img:
                output_path = os.path.join(output_folder, filename)
                
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                img.save(output_path, optimize=True, quality=quality)
                print(f"Compressed: {filename}")
        
        except Exception as e:
            print(f"Error compressing {filename}: {e}")

if __name__ == "__main__":
    compress_images(quality=50)