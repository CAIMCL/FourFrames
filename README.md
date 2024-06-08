# FourFrames

FourFrames is a Python script that extracts four random frames from a video file and saves them as JPEGs with the format `title_framenumber.jpeg`, padding the frame number to 6 places. This script is useful for quickly sampling frames from a video.

## Features

- Extracts four random frames from a video file.
- Saves the frames as JPEGs with filenames in the format `title_framenumber.jpeg`.
- Pads the frame number to 6 places (e.g., `000045` for frame 45).

## Requirements

- Python 3.x
- `opencv-python` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/CAIMCL/FourFrames.git
    cd FourFrames
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with the video file as an argument:

```bash
python four_frames.py <video-file>
