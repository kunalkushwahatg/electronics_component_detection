from video_to_image import video_to_images
import os
import tqdm

video_path = 'data/'
output_path = 'background/'
for video in tqdm.tqdm(os.listdir(video_path)):
    video_to_images(os.path.join(video_path, video), output_path, fps=5)