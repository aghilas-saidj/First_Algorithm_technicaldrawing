import cv2
from google.colab.patches import cv2_imshow

# Load the image
image_path = '/content/tech7.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
11
# Apply thresholding
_, thresholded = cv2.threshold(gray, 150, 200, cv2.THRESH_BINARY)

# Display the thresholded image
cv2_imshow(thresholded)
