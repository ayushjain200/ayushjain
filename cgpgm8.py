import cv2
import numpy as np

def rotate_image(image, angle):
 height, width = image.shape[:2]
 rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
 rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
 return rotated_image
    
def scale_image(image, scale_factor):
 scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, 
interpolation=cv2.INTER_LINEAR)
 return scaled_image
    
def translate_image(image, tx, ty):
 translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
 translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
 return translated_image
    
def main():
 # Read the image
 image_path = "img.jpg" # Replace with the path to your image
 original_image = cv2.imread(image_path)
    
 # Rotate the image
 rotated_image = rotate_image(original_image, 45)
    
 # Scale the image
 scaled_image = scale_image(original_image, 1.5)
    
 # Translate the image
 translated_image = translate_image(original_image, 50, 50)
 # Display the images
 cv2.imshow('Original Image', original_image)
 cv2.imshow('Rotated Image', rotated_image)
 cv2.imshow('Scaled Image', scaled_image)
 cv2.imshow('Translated Image', translated_image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
if __name__ == "__main__":
 main()