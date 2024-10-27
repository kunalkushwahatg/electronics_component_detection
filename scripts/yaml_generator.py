import os

def generate_yaml_file(output_path, num_classes, class_names):
    # Convert class_names list to a properly formatted YAML string
    class_names_str = ", ".join([f"'{name}'" for name in class_names])

    # Create the YAML content
    yaml_content = f"""
train: {output_path}/train/images
val: {output_path}/val/images

nc: {num_classes}
names: [{class_names_str}]
    """

    # Path to save the YAML file
    yaml_path = os.path.join(output_path, 'dataset.yaml')
    
    # Write the YAML content to the file
    with open(yaml_path, 'w') as yaml_file:
        yaml_file.write(yaml_content)



