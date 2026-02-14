Face and Name Recognition in Real-Time
Real-time face recognition using OpenCV.

How the Project Works
This project consists of 3 scripts:

Script 1: Performs face scanning, captures individual photos of users, and stores them in the dataset folder.

Script 2: Trains the data set using the collected photos.

Script 3: Executes the final face recognition process.

Code Overview
1. Script: Dataset Generation
Source: Images are captured via webcam. The resolution is defined as 640 (width) by 480 (height) pixels (lines 6 and 7).

Classifier: The face classifier is initialized on line 8.

Data Simulation: ID, first name, last name, and ID number (TC) are saved to a .txt file to simulate database entry and retrieval.

Process: A while loop captures faces from the webcam and saves them to the dataset folder.

Accuracy: The higher the count value (number of photos taken), the better the training accuracy and the precision of the recognition process.

2. Script: Training
Mechanism: This script trains the data set and generates a trainer.yml file containing the training results.

3. Script: Recognition
Loading Data: The trained dataset is loaded into the recognizer object via the trainer.yml file.

Detection: Face detection in the live camera feed is handled using the haarcascade_frontalface_default.xml filter (stored in the faceCascade variable).

Mapping: User names are pulled from the .txt file and mapped to the recognized face IDs.

Prediction: The recognizer.predict() method returns the id and confidence level. The id identifies the person, while confidence represents the estimated accuracy of the detection.

Original Project Repository
