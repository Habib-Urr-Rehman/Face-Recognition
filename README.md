
# Face Recognition App

This Face Recognition App uses OpenCV and face_recognition libraries to detect and recognize faces in real-time using your webcam. The application offers three primary functionalities: Face Detection, Face Recognition using sample images, and Face Recognition using the Labeled Faces in the Wild (LFW) dataset.

## Features

1. **Face Detection**: Detects faces in real-time using the Haar Cascade classifier.
2. **Face Recognition**: Recognizes faces in real-time using a pre-trained model with sample images.
3. **Face Recognition via LFW**: Recognizes faces using the Labeled Faces in the Wild (LFW) dataset.

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- tkinter

## Usage

1. **Run the Application**:
   - `python face.py`

2. **Main Window**:
   The main window provides options to start face detection, face recognition, or face recognition via LFW.
    
   - **Face Detection**: Click on "Face Detection" to start detecting faces in real-time.
   - **Face Recognition**: Click on "Face Recognition" to start recognizing faces based on sample images.
   - **Face Recognition via LFW**: Click on "Face Recognition via LFW" to recognize faces using the LFW dataset.

3. **Training the Model**:
   - To train the model with more images, add your images to the `sample_img` folder.
   - Update the image paths in the `train_model` method in `app.py` with the paths to your new images.
   - The model will automatically train on these images when you start the application.

## Sample Images

The application comes with some sample images for face recognition. These images are located in the `sample_img` folder. You can add more images to this folder to train the model on additional faces.

### Adding More Images

1. Add your images to the `sample_img` folder.
2. Update the `train_model` method in `app.py` with the paths to your new images:
   - `training_image_paths = ["path_to_your_image1.jpg", "path_to_your_image2.jpg", ...]`

## Labeled Faces in the Wild (LFW)

The LFW dataset is a public benchmark for face verification, provided by the University of Massachusetts Amherst. You can download images from the LFW website [here](https://vis-www.cs.umass.edu/lfw/).

### Using LFW Images

1. Download the desired images from the LFW website.
2. Add the images to the `sample_img` folder.
3. Update the image paths in the `train_model` method in `app.py` with the paths to these LFW images:
   - `lfw_image_paths = ["path_to_lfw_image1.jpg", "path_to_lfw_image2.jpg", ...]`

## How It Works

### Face Detection

- Uses Haar Cascade classifier to detect faces in the webcam feed.
- Displays rectangles around detected faces.

### Face Recognition

- Loads pre-trained face encodings from sample images.
- Compares detected face encodings with known encodings.
- Displays the name of the recognized person or "Unknown" if the face is not recognized.

### Face Recognition via LFW

- Loads pre-trained face encodings from LFW images.
- Compares detected face encodings with known encodings from the LFW dataset.
- Displays the name of the recognized person or "Unknown" if the face is not recognized.

## Graphical User Interface

The application uses `tkinter` to provide a user-friendly interface. The main window has the following buttons:

- **Face Detection**: Starts the face detection process.
- **Face Recognition**: Starts the face recognition process using sample images.
- **Face Recognition via LFW**: Starts the face recognition process using the LFW dataset.
- **Quit**: Exits the application.

## Running the Application

1. **Face Detection**:
   - Click the "Face Detection" button.
   - The application will start the webcam and detect faces in real-time.
   - Press the "a" key to stop the webcam feed and exit the face detection mode.

2. **Face Recognition**:
   - Click the "Face Recognition" button.
   - The application will start the webcam and recognize faces based on the sample images.
   - Press the "a" key to stop the webcam feed and exit the face recognition mode.

3. **Face Recognition via LFW**:
   - Click the "Face Recognition via LFW" button.
   - The application will start the webcam and recognize faces based on the LFW dataset.
   - Press the "a" key to stop the webcam feed and exit the face recognition mode.

4. **Quit**:
   - Click the "Quit" button to close the application.

## Quitting the Application

- Press the "a" key during any mode to stop the webcam feed and exit.
- Click on the "Quit" button to close the application.

