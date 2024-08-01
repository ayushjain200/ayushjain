import cv2

def display_image(title, image):
 cv2.imshow(title, image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def contour_image(image):
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
 contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 contour_image = image.copy()
 cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
 return contour_image
    
def main():
 # Read the image
 image_path = "img.jpg" # Replace with the path to your image
 image = cv2.imread(image_path)
 contoured_image = contour_image(image)
 display_image('Original Image', image)
 display_image('Contoured Image', contoured_image)
    
if __name__ == "__main__":
 main()