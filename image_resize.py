from PIL import Image
import os

def resize_image(input_path, output_path, target_size=(1280, 720)):
    """
    Resize image to target size while maintaining aspect ratio
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to save resized image
        target_size (tuple): Target size (width, height)
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert image to RGB if it's not
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate new size maintaining aspect ratio
            width, height = img.size
            target_width, target_height = target_size
            
            # Calculate scaling factor
            scale = min(target_width/width, target_height/height)
            new_size = (int(width * scale), int(height * scale))
            
            # Resize image
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Create new image with target size and black background
            new_img = Image.new('RGB', target_size, (0, 0, 0))
            
            # Calculate position to paste resized image (centered)
            paste_x = (target_width - new_size[0]) // 2
            paste_y = (target_height - new_size[1]) // 2
            
            # Paste resized image onto new image
            new_img.paste(resized_img, (paste_x, paste_y))
            
            # Save the processed image
            new_img.save(output_path)
            print(f"Resized: {input_path} -> {output_path}")
            
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

def batch_resize_images(input_dir, output_dir, target_size=(1280, 720)):
    """
    Resize all images in the input directory to target size
    
    Args:
        input_dir (str): Directory containing input images
        output_dir (str): Directory to save resized images
        target_size (tuple): Target size (width, height)
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each image in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"resized_{filename}")
            resize_image(input_path, output_path, target_size)

if __name__ == "__main__":
    # Example usage
    input_directory = "input_images"
    output_directory = "output_images"
    
    # Resize all images to 1280x720
    batch_resize_images(input_directory, output_directory)
