import numpy as np
import mtcnn
from PIL import Image, ImageDraw
import argparse


def detect_faces(image_path):
    """
    Function to detect faces in an image using MTCNN.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    image: An Image object.
    faces: A list of dictionaries containing details of the detected faces.
    """
    # lets create a MTCNN class so we can detect faces
    face_detector = mtcnn.MTCNN()
    image = Image.open(image_path)
    # convert image to RGB
    image = image.convert("RGB")
    # detect faces
    faces = face_detector.detect_faces(np.array(image))
    return image, faces


def draw_faces(image, faces):
    """
    Function to draw bounding boxes and keypoints on the detected faces.

    Parameters:
    image: An Image object.
    faces: A list of dictionaries containing details of the detected faces.
    """
    # we can use opencv or PIL to draw the face bounding boxes
    draw = ImageDraw.Draw(image)

    for face in faces:
        box = face["box"]
        conf_text = str(round(face["confidence"], 2))
        keypoints = face["keypoints"]
        # box output are x, y, height and width
        draw.rectangle(
            [(box[0], box[1]), (box[0] + box[2], box[1] + box[3])], outline="green"
        )
        draw.text((box[0], box[1] - 10), "Confidence Score: " + conf_text, fill="red")
        # we need to draw for each keypoint
        for keypoint in keypoints.values():
            draw.ellipse(
                (keypoint[0] - 2, keypoint[1] - 2, keypoint[0] + 2, keypoint[1] + 2),
                fill="red",
            )

    # Display the image using PIL
    image.show()
    # image.save(fp='drawn.png')


def main(image_path, draw_faces_flag):
    """
    Main function to detect and draw faces on an image.

    Parameters:
    image_path (str): Path to the image file.
    draw_faces_flag (bool): Flag to control the activation of the draw_faces function.
    """
    image, faces = detect_faces(image_path)
    if draw_faces_flag:
        draw_faces(image, faces)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect and draw faces on an image.")
    parser.add_argument("--image_path", type=str, help="Path to the image file.")
    parser.add_argument(
        "--draw_faces",
        action="store_true",
        help="Flag to control the activation of the draw_faces function.",
    )
    args = parser.parse_args()
    main(args.image_path, args.draw_faces)
