import os
import random
import cv2
import matplotlib.pyplot as plt
import argparse

def create_bbox_image(image_path, label_path, class_names):
    # Load the image
    image = cv2.imread(str(image_path))
    h, w, _ = image.shape

    # Open the corresponding label file
    with open(label_path, 'r') as label_file:
        lines = label_file.readlines()

    # Draw bounding boxes and class labels on the image
    for line in lines:
        class_id, x_center, y_center, width, height = map(float, line.strip().split())

        # Convert YOLO format to pixel coordinates
        x_min = int((x_center - width / 2) * w)
        y_min = int((y_center - height / 2) * h)
        x_max = int((x_center + width / 2) * w)
        y_max = int((y_center + height / 2) * h)

        # Get the class name
        class_name = class_names[int(class_id)]
        color = (0, 255, 0)  # Green color for bounding box
        thickness = 2

        # Draw the rectangle (bounding box)
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)
        # Put the class name near the bounding box
        cv2.putText(image, class_name, (x_min, y_min - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

    return image

def randomly_select_and_display_image(base_path, class_names):
    # Define the train/val directories
    train_images_path = os.path.join(base_path, 'train/images')
    val_images_path = os.path.join(base_path, 'val/images')
    
    # Choose whether to select from train or val
    dataset_choice = random.choice(['train', 'val'])
    images_path = train_images_path if dataset_choice == 'train' else val_images_path
    
    # Get a list of all image files
    image_files = [f for f in os.listdir(images_path) if f.endswith('.jpg')]

    # Randomly select an image
    selected_image = random.choice(image_files)
    image_path = os.path.join(images_path, selected_image)

    # Get the corresponding label file
    label_path = image_path.replace('images', 'labels').replace('.jpg', '.txt')

    # Create the bounding box image
    bbox_image = create_bbox_image(image_path, label_path, class_names)

    # Display the image with bounding boxes using matplotlib
    plt.imshow(cv2.cvtColor(bbox_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Hide the axes for a cleaner display
    plt.show()

    print(f"Displayed image: {image_path} from the {dataset_choice} dataset")

# Example usage
  # Path to component images

#setup argument parser
parser = argparse.ArgumentParser(description="Randomly select and display an image")
parser.add_argument('--components-folder', type=str, required=True, help="Path to the components folder")

components_folder = parser.parse_args().components_folder
base_path = './datasets'  # Base path to the dataset (train/val folders)

# Extract folder names as class names
class_names = os.listdir(components_folder)
class_names = {i: class_name for i, class_name in enumerate(class_names)}

# Call the function to randomly select and display an image
randomly_select_and_display_image(base_path, class_names)


