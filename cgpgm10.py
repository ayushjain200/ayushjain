import cv2
def display_image(title, image):
 cv2.imshow(title, image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def blur_image(image):
 # Apply Gaussian blur
 blurred = cv2.GaussianBlur(image, (5, 5), 0)
 return blurred
    
def main():
 # Read the image
 image_path = "img.jpg" # Replace with the path to your image
 image = cv2.imread(image_path)
    
 # Blur the image
 blurred_image = blur_image(image)
    
 # Display the original and blurred images
 display_image('Original Image', image)
 display_image('Blurred Image', blurred_image)
    
if __name__ == "__main__":
 main()