import argparse
import os
from ultralytics import YOLO

def parse_arguments():
    # Argument parsing to allow flexibility
    parser = argparse.ArgumentParser(description="Train YOLOv8 on custom dataset")
    parser.add_argument('--data', type=str, required=True, help="Path to dataset YAML file")
    parser.add_argument('--epochs', type=int, default=100, help="Number of training epochs")
    parser.add_argument('--batch-size', type=int, default=16, help="Batch size for training")
    parser.add_argument('--img-size', type=int, default=224, help="Image size for training")
    parser.add_argument('--weights', type=str, default='yolov8n.pt', help="Path to pre-trained weights (default: yolov8n.pt)")
    parser.add_argument('--project', type=str, default='./runs/train', help="Project directory for saving training results")
    parser.add_argument('--name', type=str, default='exp', help="Name of the training experiment")
    return parser.parse_args()

def train_model(data, epochs, batch_size, img_size, weights, project, name):
    # Load the model and begin training
    model = YOLO(weights)  # Load the pre-trained weights (e.g., yolov8n.pt)
    
    # Train the model
    model.train(
        data=data,         # Path to the dataset YAML file
        epochs=epochs,     # Number of epochs
        batch=batch_size,  # Batch size
        imgsz=img_size,    # Image size
        project=project,   # Directory to save results
        name=name          # Name of the experiment
    )

if __name__ == "__main__":
    args = parse_arguments()

    # Ensure the dataset YAML exists
    if not os.path.exists(args.data):
        raise FileNotFoundError(f"Dataset YAML file '{args.data}' not found")

    # Start training
    train_model(
        data=args.data,
        epochs=args.epochs,
        batch_size=args.batch_size,
        img_size=args.img_size,
        weights=args.weights,
        project=args.project,
        name=args.name
    )


#python train.py --data ./datasets/dataset.yaml --epochs 100 --batch-size 16 --img-size 640 --weights yolov8n.pt
