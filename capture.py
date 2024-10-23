import cv2
import os

def capture_images_from_stream(ip_url, folder_path, interval_ms):
    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Start video capture from IP camera
    cap = cv2.VideoCapture(ip_url)

    if not cap.isOpened():
        print("Failed to connect to the camera.")
        return

    print("Connected to camera. Press 'q' to stop.")
    image_count = 0

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Display the current frame in a window
            cv2.imshow("Live Camera Feed", frame)

            # Save the frame at specified intervals
            if image_count % (30 // (1000 // interval_ms)) == 0:  # Save every 'interval_ms'
                image_name = f"{folder_path}/image_{image_count}.jpg"
                cv2.imwrite(image_name, frame)
                print(f"Saved: {image_name}")

            image_count += 1

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting on user request.")
                break

    except KeyboardInterrupt:
        print("Image capture stopped by user.")

    finally:
        # Release the capture object and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace with the correct IP Webcam stream URL (append `/video`)
    ip_url = "http://192.168.0.105:8080/video"
    # Specify the folder path to save images
    folder_path = "./background"
    # Interval in milliseconds between frame captures
    interval_ms = 1000  # 1 second

    capture_images_from_stream(ip_url, folder_path, interval_ms)
