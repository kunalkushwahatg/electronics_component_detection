import cv2
import os
from tqdm import tqdm

def video_to_images(video_path, output_path, fps=1):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not video_capture.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Get the video's FPS (frames per second)
    video_fps = video_capture.get(cv2.CAP_PROP_FPS)
    
    # Calculate how many frames to skip to get the desired FPS
    frame_skip = int(video_fps // fps)
    
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Initialize frame counter and image counter
    frame_count = 0
    image_count = 0

    # Get the total number of frames for progress bar
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Loop through the video frames
    with tqdm(total=total_frames // frame_skip, desc="Extracting frames") as pbar:
        while True:
            ret, frame = video_capture.read()

            # Break the loop if there are no frames left to read
            if not ret:
                break

            # Save the frame as an image if it matches the desired FPS
            if frame_count % frame_skip == 0:
                image_filename = os.path.join(output_path, f"frame_{image_count:05d}.jpg")
                cv2.imwrite(image_filename, frame)
                image_count += 1

            frame_count += 1
            pbar.update(1)

    # Release the video capture object
    video_capture.release()
    print(f"Finished extracting {image_count} images to {output_path}")

# Example usage:
# video_to_images('path/to/video.mp4', 'path/to/output_images', fps=2)
