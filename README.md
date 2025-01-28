Human Pose Estimation with OpenCV and Mediapipe
This project performs human pose estimation in real-time using OpenCV and Mediapipe. The goal is to detect key body parts and their connections to track a person's posture, providing insights into the body's movements.

Table of Contents
Introduction
Prerequisites
Installation
Usage
How it Works
Example
License
Introduction
Human pose estimation is a computer vision task that focuses on detecting human figures in images or videos and understanding their body posture. By identifying key body parts (e.g., nose, shoulders, elbows, wrists, hips, etc.), we can track movements, create interactive applications, or build fitness tracking tools.

This project uses OpenCV for image processing and Mediapipe, a Google library that provides real-time pose tracking capabilities.

Prerequisites
Before running the project, make sure you have the following installed:

Python 3.x
OpenCV
Mediapipe
Streamlit (for interactive web-based interface)
To install these dependencies, run the following commands:

bash
Copy
Edit
pip install opencv-python
pip install mediapipe
pip install streamlit
Additionally, you will need a trained model for pose estimation. You can download it from the following link or use your own trained model.

Installation
Clone the repository or download the files to your local machine.
Install the required dependencies using the commands mentioned above.
Make sure you have a graph_opt.pb file (the pre-trained pose detection model) in your project directory.
bash
Copy
Edit
git clone https://github.com/your-username/pose-estimation.git
cd pose-estimation
Usage
Upload an image:
You can upload a clear image of a person via the provided interface, and the pose estimation model will detect and display the key points of the body.

Use Webcam:
For live webcam feed, you can use the video capture functionality provided by OpenCV. This will allow you to track the pose of the person in real-time.

To run the Streamlit interface:

bash
Copy
Edit
streamlit run app.py
How it Works
The system works in the following steps:

Image/Video Input:
The input can either be an image uploaded by the user or a live video stream from a webcam.

Preprocessing:
The input is processed using OpenCV and converted to RGB format for compatibility with the Mediapipe model.

Pose Estimation:
The image is passed through the Mediapipe Pose model to detect key body landmarks. The body landmarks include parts such as the nose, neck, shoulders, elbows, wrists, hips, knees, etc.

Post-Processing:
The detected body parts are drawn on the image as circles. The system also draws lines connecting the body parts to show the human pose.

Output:
The final image or video frame is displayed with the body landmarks, allowing you to see the detected pose.

Example
Upload an Image

Click on the "Upload an image" button and select an image from your device.
The pose detection model will process the image and display the key points and pose connections.
Webcam Capture

Select the "Webcam" option to start the real-time pose estimation.
The webcam feed will display live human pose estimation, with detected body landmarks.
License
This project is licensed under the MIT License - see the LICENSE file for details.
