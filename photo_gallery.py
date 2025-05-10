from PIL import Image
import os
import matplotlib.pyplot as plt


def create_collage(image_folder, collage_filename, collage_width, collage_height, cell_width, cell_height):
    # Get the list of images in the image folder
    image_files = [file for file in os.listdir(image_folder) if file.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    num_images = len(image_files)
    
    # Calculate the number of cells horizontally and vertically in the collage
    cells_x = collage_width // cell_width
    cells_y = collage_height // cell_height
    
    # Create a new blank image for the collage
    collage = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))
    
    # Loop through the images and paste them into the collage
    for i, img_file in enumerate(image_files):
        img_path = os.path.join(image_folder, img_file)
        img = Image.open(img_path)
        img.thumbnail((cell_width, cell_height))
        
        # Calculate the position to paste the image in the collage
        x_offset = (i % cells_x) * cell_width
        y_offset = (i // cells_x) * cell_height
        
        # Paste the image into the collage
        collage.paste(img, (x_offset, y_offset))
        
        # Print progress
        print(f"Processing image {i + 1}/{num_images}")
    
    # Save the collage to the specified filename
    collage.save(collage_filename)
    print("Collage generated successfully!")
     # Display the collage using matplotlib
    plt.imshow(collage)
    plt.axis('off')
    plt.show() 

if __name__ == "__main__":
    # Example usage: replace the folder path and collage dimensions accordingly
    image_folder = "D:\Photo_Gallery\image stock"
    collage_filename = "output_collage.jpg"
    collage_width = 600
    collage_height = 600
    cell_width = 200
    cell_height = 150
    
    create_collage(image_folder, collage_filename, collage_width, collage_height, cell_width, cell_height)
