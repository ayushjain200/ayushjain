import cv2
import numpy as np
def display_image(title, image):
 cv2.imshow(title, image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def canny_edge_detection(image):
    
 # Convert the image to grayscale
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
 # Apply Gaussian blur to reduce noise
 blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
 # Perform Canny edge detection
 edges = cv2.Canny(blurred, 50, 150)
 return edges
def texture_filtering(image):
    
 # Convert the image to grayscale
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
 # Apply Laplacian filter for edge detection
 laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    
 # Convert the Laplacian result to uint8
 laplacian_uint8 = np.uint8(np.absolute(laplacian))
 return laplacian_uint8
    
def main():
 # Read the image
 image_path = "img.jpg" # Replace with the path to your image
 image = cv2.imread(image_path)
    
 # Apply Canny edge detection
 edges = canny_edge_detection(image)
 display_image('Canny Edge Detection', edges)
    
 # Apply texture filtering
 textures = texture_filtering(image)
 display_image('Texture Filtering (Laplacian)', textures)
    
if __name__ == "__main__":
 main()