import os
import argparse
from ultralytics import YOLO
import matplotlib.pyplot as plt

def perform_inference(model_path, image_path, output_path='./output', show_plot=False):
    # Load the YOLOv8 model
    model = YOLO(model_path)

    # Create a directory to save the output image
    os.makedirs(output_path, exist_ok=True)

    # Perform inference on the image
    results = model.predict(source=image_path, save=False, conf=0.25)  # Adjust confidence threshold if needed

    print(results)

    # Plot the results (this will add bounding boxes and labels)
    results_img = results[0].plot()

    # Show plot if requested
    if show_plot:
        plt.imshow(results_img)
        plt.axis('off')  # Hide axes for better visualization
        plt.show()

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Save the image with bounding boxes and labels using plt.savefig
    output_image_path = os.path.join(output_path, os.path.basename(image_path))
    plt.imsave(output_image_path, results_img)  # Save the plotted image

    print(f"Output image saved to {output_image_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="YOLOv8 Inference Script")

    parser.add_argument('--model-path', type=str, required=True, help="Path to the YOLOv8 model")
    parser.add_argument('--image-path', type=str, required=True, help="Path to the input image")
    parser.add_argument('--output-path', type=str, default='./output', help="Directory to save the output image")
    parser.add_argument('--show-plot', action='store_true', help="Flag to display the image with bounding boxes")

    # Parse the arguments
    args = parser.parse_args()

    # Call the perform_inference function with parsed arguments
    perform_inference(args.model_path, args.image_path, args.output_path, args.show_plot)

if __name__ == "__main__":
    main()


#python inference.py --model-path ./runs/train/exp/weights/best.pt --image-path ./datasets/val/images/0.jpg --output-path ./output --show-plot
