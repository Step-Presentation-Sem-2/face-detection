# Face Detection
Face detection using MTCNN for Step Presentation Project

## MTCNN (Multi-Task Cascaded Convolutional Networks)
MTCNN is a deep learning based face detection method. It uses a cascading series of convolutional neural networks (CNNs) to detect and localize faces in digital images or videos.

## Resources
- [Official GitHub repository of MTCNN](https://github.com/ipazc/mtcnn)
- [Medium article providing an overview of MTCNN and its real-world applications](https://medium.com/the-modern-scientist/multi-task-cascaded-convolutional-neural-network-mtcnn-a31d88f501c8)
- [Medium article explaining the architecture and working principles of MTCNN](https://medium.com/@iselagradilla94/multi-task-cascaded-convolutional-networks-mtcnn-for-face-detection-and-facial-landmark-alignment-7c21e8007923)

## Usage
This repository contains code for detecting faces in images using MTCNN.

### Prerequisites
- Python 3
- mtcnn library
- PIL library

### Instructions
1. Clone the repository:
   ```
   git clone https://github.com/your-username/face-detection.git
   ```
2. Navigate to the repository directory:
   ```
   cd face-detection
   ```
3. Run the script with the desired options:
   ```
   python face_detection.py -i path/to/your/image.jpg -c confidence_score -d -s -p -u
   ```

### Options
- `-i`, `--image_path`: Path to the image file.
- `-c`, `--conf_score`: Confidence score threshold for face detection (default: 0.9).
- `-d`, `--draw_faces`: Activate drawing bounding boxes and keypoints on the detected faces.
- `-s`, `--show_image`: Display the image with drawn faces.
- `-p`, `--save_cropped`: Save the cropped faces.
- `-u`, `--save_uncropped`: Save the image with drawn faces.
- `-o`, `--save_image_path`: Path to save the image with drawn faces.


## Example
```
python face_detection.py -i path/to/your/image.jpg -c 0.8 -d -s -p -u
```

Replace `path/to/your/image.jpg` with the image file.

For more information on how to use MTCNN for face detection, please refer to the [official GitHub repository of MTCNN](https://github.com/ipazc/mtcnn) and the provided resources.