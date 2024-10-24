from video_to_image import video_to_images
import os
import tqdm
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Extract frames from videos")

parser.add_argument('--video-path', type=str, help="Path to the directory containing videos" , default='./videos')
parser.add_argument('--output-path', type=str, help="Path to the output directory" , default='./background')
parser.add_argument('--fps', type=int, help="Frames per second to extract" , default=5)

video_path = parser.parse_args().video_path
output_path = parser.parse_args().output_path




for video in tqdm.tqdm(os.listdir(video_path)):
    video_to_images(os.path.join(video_path, video), output_path, fps=5)

total_images = len(os.listdir(output_path))
print(f"Extracted {total_images} images from {len(os.listdir(video_path))} videos to {output_path}")

#python create_bg_dataset.py                    
