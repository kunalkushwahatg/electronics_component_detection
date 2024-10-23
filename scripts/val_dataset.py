#move the images and labels to the val folder
import shutil
from pathlib import Path
import os
import random
import matplotlib.pyplot as plt
from PIL import Image


def move_files_to_val(base_path, val_split=0.2):
    image_paths = list(Path(os.path.join(base_path, 'train/images')).glob('*.jpg'))
    label_paths = list(Path(os.path.join(base_path, 'train/labels')).glob('*.txt'))
    
    num_val_images = int(val_split * len(image_paths))
    
    val_image_paths = random.sample(image_paths, num_val_images)
    val_label_paths = [Path(os.path.join(base_path, 'train/labels', f'{image.stem}.txt')) for image in val_image_paths]

    print(f"Moving {num_val_images} images and labels to val folder")
    
    for image_path, label_path in zip(val_image_paths, val_label_paths):
        shutil.move(image_path, os.path.join(base_path, 'val/images'))
        shutil.move(label_path, os.path.join(base_path, 'val/labels'))

# base_path = './datasets'