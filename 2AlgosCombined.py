import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Load the uploaded image
image_path = '/content/tech1.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale for the second algorithm
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresholded = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Display the thresholded image
cv2_imshow(thresholded)

# Apply Gaussian blur with larger kernel size to reduce noise more aggressively
blurred = cv2.GaussianBlur(thresholded, (5, 5), 0)  # Increased kernel size

# Perform edge detection using Canny with adjusted thresholds
edges = cv2.Canny(blurred, 100, 200)  # Adjusted thresholds

# Apply morphological closing to close small gaps in edges
kernel = np.ones((5, 5), np.uint8)
closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Find contours in the closed edge image
contours, _ = cv2.findContours(closed_edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Filter out contours representing closed areas
closed_areas = []
for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if area > 500 and perimeter > 50:  # Adjust threshold as needed
        closed_areas.append(contour)

# Draw contours of closed areas on the original image
cv2.drawContours(image, closed_areas, -1, (0, 0, 255), 1)

# Display the original image with detected closed areas
cv2_imshow(image)
