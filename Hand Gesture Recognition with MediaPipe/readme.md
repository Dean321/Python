# Hand Gesture Recognition with MediaPipe

#### Prequisites:

Install MediaPipe<br>
**pip install mediapipe**

### MediaPipe

MediaPipe has very powerful methods which can easily detect various human body poses, hand gestures and faces with very little code.<br>
MediaPipe provides ready to use Machine Learning Solutions (that are predefined machine learning algorithms)for live and streaming media.<br>
MediaPipe ML Solutions include:
- Face Detection
-  Face Mesh
-  Iris
-  Hands
-  Pose
-  Holistic
-  Hair Segmentation
-  Object Detection
-  Box Tracking
-  Instant Motion Tracking
-  Objectron
-  KNIFT

We used the MediaPipe Library Hands Solution to detect a hand.
The MediaPipe Hands Solution tracks 21 points/landmarks on our hand. Each point has a unique ID starting from 0. With this ID we can get the x and y position
of this landmark/point on our hand.

![image](https://user-images.githubusercontent.com/17800800/202407801-29174a17-9435-4f3a-a3a7-67aa639bba0a.png)



