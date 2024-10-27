from augmentation_generator import AugmentationGenerator
from setup_directories import setup_yolo_folder_structure
from yaml_generator import generate_yaml_file
from val_dataset import move_files_to_val
from pathlib import Path
import os
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Create a custom YOLO dataset")
parser.add_argument('--components-folder', type=str, required=True, help="Path to the components folder")
parser.add_argument('--num-images', type=int, default=1000, help="Number of images to generate")
parser.add_argument('--image-size', type=int, default=224, help="Size of the generated images")


# Define the paths
components_folder = parser.parse_args().components_folder
num_images = parser.parse_args().num_images
image_size = parser.parse_args().image_size

bg_folder = './background'
output_path = './datasets/train'
yaml_path = './'
base_path = './datasets'



# #setup the yolo folder structure
setup_yolo_folder_structure(base_path)


# Get the list of component image paths
component_paths = list(Path(components_folder).glob('**/*.jpg'))

# Get the list of class names and create a mapping
class_names = os.listdir(components_folder)
class_names = {class_name: i for i, class_name in enumerate(class_names)}

# Create background image paths
bg_paths = AugmentationGenerator.get_background_image_paths(bg_folder)

# Create an instance of the AugmentationGenerator class
generator = AugmentationGenerator(component_paths, bg_paths, output_path, class_names, (image_size, image_size))

# Generate the augmented images and annotations
generator.create_augmented_images_with_annotations(num_images=num_images)


#move the images and labels to the val folder
move_files_to_val(base_path, val_split=0.2)

#generate yaml file
generate_yaml_file(yaml_path, len(class_names), class_names)




#python create_dataset.py --components-folder ./components --num-images 1000 --image-size 224