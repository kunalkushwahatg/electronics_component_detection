
# YOLO Electronics Detection
This project implements a custom YOLO model for detecting and classifying various electronic components. Using a unique, custom dataset and complete training and inference pipelines, the model accurately identifies multiple electronic parts in complex visual settings.

## Usage/Examples

### Clone the Repository
Clone this repository to get started:
you  can  create background images for dataset from camera recorded video just store the videos to a folder 

```
git clone https://github.com/kunalkushwahatg/electronics_component_detection.git
cd electronics_component_detection 
```

### Install Requirements
Navigate to the project directory and install the required packages:

```
pip install -r requirements.txt
```

### Create Background Images from Video
You can create background images for dataset augmentation from recorded videos. Simply store the videos in a specified folder and use the following command to generate background images:
```
!python /path/to/electronics_component_detection/scripts/create_bg_dataset.py --video-path /path/to/data/videos --output-path /path/to/output/backgrounds --fps 5
```
### Download and Prepare the Electronic Components Dataset
To create the dataset, download the electronic components dataset from [https://www.kaggle.com/datasets/aryaminus/electronic-components](Kaggle). Once downloaded, specify the path to the components folder to preprocess the data:
```
!python /path/to/electronics_component_detection/scripts/create_dataset.py --components-folder /path/to/electronic-components/images/
```
### Train the Model
Use the following command to train the YOLO model with custom parameters:
```
!python /path/to/train.py --data /path/to/dataset.yaml --epochs 100 --batch-size 16 --img-size 640 --weights yolov8n.pt
```

### Run Inference
After training, you can use the following command to perform inference on an image. This will save the output to the specified folder and optionally display the result: 

```
!python /path/to/inference.py --model-path /path/to/runs/train/exp/weights/best.pt --image-path /path/to/dataset/val/images/sample_image.jpg --output-path /path/to/output --show-plot
```
