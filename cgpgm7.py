import cv2

def split_image(image_path):
 image = cv2.imread(image_path) # Get the dimensions of the image
 height, width, _ = image.shape # Split the image into four quadrants
 left = image[0:height, 0:width//2]
 right = image[0:height, width//2:width]
 up = image[0:height//2, 0:width]
 down = image[height//2:height, 0:width]
 return left, right, up, down
    
def display_quadrants(left, right, up, down):
 cv2.imshow('Left Quadrant', left)
 cv2.imshow('Right Quadrant', right)
 cv2.imshow('Upper Quadrant', up)
 cv2.imshow('Lower Quadrant', down)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def main():
 image_path = "img.jpg" 
 left, right, up, down = split_image(image_path)
 display_quadrants(left, right, up, down)
    
if __name__ == "__main__":
 main()