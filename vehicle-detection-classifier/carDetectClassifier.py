import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Load image from local source
#image = cv2.imread("traffic2.jpeg")
image = cv2.imread("traffic.png")

# Call cvlib func that can detect different type of objects with 0.4 confidence (0.4 looks good for full screen road images) 
bbox, label, conf = cv.detect_common_objects(image, 0.4)

# Draw bounding boxes on output image
output_image = draw_bbox(image, bbox, label, conf, None, True)

print("Number of cars in the image: " + str(label.count("car")))
print("Number of trucks in the image: " + str(label.count("truck")))
print("Number of motorcycles in the image: " + str(label.count("motorcycle")))

# Draw output image on screen
plt.imshow(output_image)
plt.show()

my_dict = {}

# Exit the window with q
if cv2.waitKey(1) & 0xFF == ord("q"):
    cv2.destroyAllWindows()  