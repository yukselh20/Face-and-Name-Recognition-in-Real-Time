# Face-and-Name-Recognition-in-Real-Time

Face recognition with OpenCV.

## How the Project Works
This project consists of 3 main scripts:
1. **Script 1:** Scans faces, takes individual photos of people, and stores them in the "dataset" folder.
2. **Script 2:** Trains the data model using the photos collected in the dataset.
3. **Script 3:** Performs real-time face recognition.

## Code Content
### Script 1:
• Images are obtained via webcam. The resolution is defined as 640 pixels wide and 480 pixels high (Lines 6 and 7).<br/>
• The face classifier is located on line 8.<br/>
• Data received from ID, name, surname, and ID number (tcno) fields are saved to a .txt file to simulate database entry and retrieval.<br/>
• Inside the "While" loop, the webcam captures photos of the detected person and saves them to the "dataset" folder.<br/>
• The number of captured photos is determined by the *count* value; as this value increases, the training quality and the accuracy of the recognition process also increase.<br/>

### Script 2:
• This script trains the dataset and saves the output to a file named *trainer.yml*.<br/>

### Script 3:
• We load the trained dataset into our recognition object, *recognizer*, via the *trainer.yml* file.<br/>
• Live camera faces are detected using the *haarcascade_frontalface_default.xml* filter (assigned to the variable *faceCascade*).<br/>
• Name data is retrieved from the .txt file (matching names with the captured photos).<br/>
• The *recognizer.predict()* method returns *id* and *confidence* values. The ID represents the person's number, while confidence represents the estimated accuracy rate of the detection.<br/>

### [Original Project Repository](https://github.com/Mjrovai/OpenCV-Face-Recognition)
