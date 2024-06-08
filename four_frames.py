import sys
import os
import cv2
import random

def extract_random_frames(video_file, num_frames=4):
    # Capture the video
    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_file}")
        sys.exit(1)

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames < num_frames:
        print(f"Error: Video file {video_file} has less than {num_frames} frames")
        sys.exit(1)

    # Generate random frame numbers
    frame_numbers = sorted(random.sample(range(total_frames), num_frames))

    # Extract and save frames
    base_filename = os.path.splitext(os.path.basename(video_file))[0]
    frame_count = 0

    for frame_number in frame_numbers:
        # Set the video to the specific frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        
        # Read the frame
        ret, frame = cap.read()
        if not ret:
            print(f"Error: Cannot read frame {frame_number} from video file {video_file}")
            continue
        
        # Save the frame as a JPEG file
        frame_filename = f"{base_filename}_{frame_number:06d}.jpeg"
        cv2.imwrite(frame_filename, frame)
        print(f"Saved frame {frame_number} as {frame_filename}")
        
        frame_count += 1

    # Release the video capture object
    cap.release()

    if frame_count == 0:
        print(f"No frames were extracted from the video file {video_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python four_frames.py <video-file>")
        sys.exit(1)

    video_file = sys.argv[1]

    if not os.path.isfile(video_file):
        print(f"File not found: {video_file}")
        sys.exit(1)

    extract_random_frames(video_file)

if __name__ == "__main__":
    main()
