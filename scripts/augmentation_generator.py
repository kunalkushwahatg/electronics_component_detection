import os
import random
from PIL import Image, ImageEnhance
from pathlib import Path
from tqdm import tqdm
from matplotlib import pyplot as plt

class AugmentationGenerator:
    def __init__(self, component_paths, bg_paths, output_path, class_names, img_size=(640, 640)):
        self.component_paths = component_paths
        self.bg_paths = bg_paths
        self.output_path = output_path
        self.class_names = class_names
        self.img_size = img_size

    def random_resize_and_position(self, component, bg_w, bg_h):
        # Set the size range for components
        min_size, max_size = 48, 128

        # Get the current size of the component
        comp_w, comp_h = component.size

        # Maintain the aspect ratio
        aspect_ratio = comp_w / comp_h

        # Randomly select a new width and height within the desired size range
        new_size = random.randint(min_size, max_size)

        # Adjust width and height based on aspect ratio
        if comp_w > comp_h:
            comp_w = new_size
            comp_h = int(comp_w / aspect_ratio)
        else:
            comp_h = new_size
            comp_w = int(comp_h * aspect_ratio)

        # Resize the component
        component = component.resize((comp_w, comp_h))

        # Randomly rotate the image (between 0 and 360 degrees)
        angle = random.randint(0, 360)
        component = component.rotate(angle, expand=True)

        # Apply random brightness and contrast
        enhancer_brightness = ImageEnhance.Brightness(component)
        component = enhancer_brightness.enhance(random.uniform(0.7, 1.3))

        enhancer_contrast = ImageEnhance.Contrast(component)
        component = enhancer_contrast.enhance(random.uniform(0.8, 1.5))

        # Random position for placing the component on the background
        x_min = random.randint(0, bg_w - component.width)
        y_min = random.randint(0, bg_h - component.height)

        comp_w, comp_h = component.width, component.height

        return component, x_min, y_min, comp_w, comp_h

    def create_augmented_images_with_annotations(self, num_images=100):
        for i in tqdm(range(num_images)):
            # Randomly select a background image
            bg_img_path = random.choice(self.bg_paths)
            bg_img = Image.open(bg_img_path)
            bg_img = bg_img.resize(self.img_size)
            bg_w, bg_h = bg_img.size

            bg_img_copy = bg_img.copy()
            num_components = random.randint(1, 4)  # Place 1-4 components on the image
            annotations = []

            for _ in range(num_components):
                # Select a random component image
                component_img_path = random.choice(self.component_paths)
                compo_class = str(component_img_path).split('/')[-2]
                component_img = Image.open(component_img_path).convert('RGBA')

                # Resize and place component on background
                component_img, x_min, y_min, comp_w, comp_h = self.random_resize_and_position(component_img, bg_w, bg_h)

                # Split the alpha channel for transparency
                r, g, b, alpha = component_img.split()
                bg_img_copy.paste(component_img, (x_min, y_min), mask=alpha)

                # Calculate YOLO format bbox (normalize)
                x_center = (x_min + comp_w / 2) / bg_w
                y_center = (y_min + comp_h / 2) / bg_h
                width = comp_w / bg_w
                height = comp_h / bg_h

                class_id = self.class_names[compo_class]  # Get the class ID

                # Append annotation in YOLO format
                annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")

            # Save the generated image
            img_output_path = os.path.join(self.output_path, 'images', f'augmented_{i}.jpg')
            bg_img_copy.save(img_output_path)

            # print(f"Saved image: {img_output_path}")

            # #load the saved image and display it
            # img = Image.open(img_output_path)   
            # plt.imshow(img)
            # plt.show()


            # Save the corresponding label file
            label_output_path = os.path.join(self.output_path, 'labels', f'augmented_{i}.txt')
            with open(label_output_path, 'w') as label_file:
                label_file.write('\n'.join(annotations))

    @staticmethod
    def get_background_image_paths(bg_folder):
        extensions = ['*.jpg', '*.jpeg', '*.png']
        bg_paths = []
        for ext in extensions:
            bg_paths.extend(list(Path(bg_folder).rglob(ext)))  # Use rglob to search recursively
        return bg_paths


'''
from pathlib import Path
import os

# Define the paths
components_folder = './archive/images/'
bg_folder = 'bg'
output_path = './datasets/train'

# Get the list of component image paths
component_paths = list(Path(components_folder).glob('**/*.jpg'))

# Get the list of class names and create a mapping
class_names = os.listdir(components_folder)
class_names = {class_name: i for i, class_name in enumerate(class_names)}

# Create background image paths
bg_paths = AugmentationGenerator.get_background_image_paths(bg_folder)

# Create an instance of the AugmentationGenerator class
generator = AugmentationGenerator(component_paths, bg_paths, output_path, class_names)

# Generate the augmented images and annotations
generator.create_augmented_images_with_annotations(num_images=1000)

'''