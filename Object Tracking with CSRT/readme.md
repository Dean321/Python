# Object Tracking with CSRT

#### Prequisites:
- Install 
  
  pip install opencv-contrib-python==3.4.13.47
  
### Object Tracking
 
 Object Tracking is a process of finding and keeping 
   a track of the position of an object that is 
    continuously moving in a video.
    

https://user-images.githubusercontent.com/17800800/201634569-a275c506-6cf5-4ea0-a345-f4832c5f10e9.mp4


  - To track an object in any video, the object has to
    be detected first and then we need to keep track 
    of the position of the object.
  - The process of object detection involves only 
    detecting an object in a still image(or one 
    frame at a time in a video). Wherein the process
    object tracking involves keeping track of the 
    object's position in a video.
    
Let’s understand the overall steps to detect and track an object 
in video using OpenCV
1. Load the video
2. Start the tracker(the inbuilt algorithm in OpenCV)
3. Object Selection by creating a bounding box around
the object using the mouse
4. Get the center point of the bounding box
5. Plot the trajectory using center points


#### Algorithm:
1. Load the video
2. Algorithm that will track the object
3. Object Selection creating a bounding box around 
   the object using the mouse
4. Initialize the tracker(the inbuilt algorithm in OpenCV)

<b><ins>To load CSRT tracker</ins></b><br>
**tracker = cv2.TrackerCSRT_create()**<br>
Once the tracker is loaded, we need to load the first frame of our video. This is because when our code starts it should show an image from our video, then we can select any object by creating a bounding box on that image and our tracker will track the object present in the bounding box.

<b><ins>To select the bounding box</ins></b><br>
**bbox = cv2.selectROI("Tracking", img, False)**<br>
To track the position of a moving object, we will create a bounding box around the object, and use the bounding box  to track the position of the object. The bounding box determines the Region Of Interest(ROI) or the portion of the image that needs to be tracked. 
![image](https://user-images.githubusercontent.com/17800800/201636347-38965b70-0267-4215-b7ee-53b5df4324de.png)

To find out the ROI we have the OpenCV method **cv2.selectROI()** that helps us to select the region of the image during runtime(that means while the Python script is running).<br>
This method takes three parameters: 
- Name of this ROI(Region Of Interest), 
- Image on which we create this ROI and l 
- Boolean value(True/False) to set the origin of the bounding box, to rectangle to start from the center of the ROI selected then this will be True else it will be False.<br>
The values returned by the **cv2.selectROI()** method is bounding box data tuple **(x, y, w, h)** where x and y are the coordinates of the starting point of the bounding box and w and h are width and height of the bounding box respectively.
We can store the result returned by the **cv2.selectROI()** method using a variable called bbox.

<b><ins>To initialize Tracker</ins></b><br>
**tracker.init(img, bbox)**<br>
Next step is to load the tracker algorithm.
These are pre-built Machine Learning(ML) algorithms
in the OpenCV library that can be used in our 
application. In upcoming classes we will build our 
own ML algorithms from scratch!
There are different trackers available in the OpenCV
library such as:<br>
- BOOSTING 
- MIL 
- KCF 
- TLD 
- MEDIANFLOW 
- GOTURN
- MOSSE

Each tracker has some pros and cons such as MOSSE is very 
fast in tracking objects, but it lacks accuracy for our use,
so we are going to use CSRT, because it is fast as
well as accurate.
The last step of the process is to initialize the tracker.
This is done using tracker.init(img, bbox). This function
will initialize our tracker on the first frame of video 
using the bounding box created by us.

<b><ins>For ccreating two points for calculating distance</ins></b><br>
The point will not exactly be a point, because OpenCV
        does not have a method to create a point. But we are 
        going to draw a circle which will have a very small 
        radius, and it will look like a point.
- To create a circle at the center of the bounding box 
        which is tracking the basketball, we will get the x, 
        y, w, h coordinates of the bounding box store in the 
        variable bbox. 
- The center point of the basketball is
        located in the middle of the bounding box rectangle.
- Middle point of any rectangle is always located at 
        half of width and height from the starting point.
        ![image](https://user-images.githubusercontent.com/17800800/201634431-c3226072-2bc4-49e7-ac5f-2f232accc30c.png)

- In the image below, x and y is the starting point 
        located at top left on the bounding box. The middle
        point is represented using c1 and c2.
        
<b><ins>To draw a circle</ins></b><br>
**cv2.circle(img, (c1, c2), 2, (0, 0, 255), 5)**<br>
Parameters: <br>
- **image**: The image to draw the circle on. 
- **center points**: x and y coordinates of the center 
          of the circle, which is represented by c1 and c2 
          in this case.
- **radius**: Radius of the circle. 
- **color**: Color of the circle, red (0, 0, 255) in this
          case.
- **thickness**: Thickness of the circle

### Screenshots:

![image](https://user-images.githubusercontent.com/17800800/201636655-91f2e748-6e43-4f60-962e-edb5308b3ec2.png)
