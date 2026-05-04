import os
from rembg import remove
from PIL import Image

def convert_to_transparent_png(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Failed to process {input_path}: {e}")

images_dir = "c:/Users/2024/OneDrive/Documents/antigravity/proj2 animated website/images"

convert_to_transparent_png(os.path.join(images_dir, "user_1.jpg"), os.path.join(images_dir, "user_1_transparent.png"))
convert_to_transparent_png(os.path.join(images_dir, "chick_pulao.jpg"), os.path.join(images_dir, "chick_pulao_transparent.png"))
convert_to_transparent_png(os.path.join(images_dir, "user_4.jpg"), os.path.join(images_dir, "user_4_transparent.png"))
