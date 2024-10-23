import os

def setup_yolo_folder_structure(base_path):
    paths = [
        os.path.join(base_path, 'train/images'),
        os.path.join(base_path, 'train/labels'),
        os.path.join(base_path, 'val/images'),
        os.path.join(base_path, 'val/labels')
    ]
    
    for path in paths:
        os.makedirs(path, exist_ok=True)

# base_path = './datasets'
# setup_yolo_folder_structure(base_path)
