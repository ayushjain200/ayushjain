import cv2

def display_image(title, image):
 cv2.imshow(title, image)
 cv2.waitKey(0)
 cv2.destroyAllWindows()
    
def detect_faces(image_path):
 
 face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
 image = cv2.imread(image_path)
 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
 for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
 return image
    
def main():
 image_path = "img.jpg" # Replace with the path to your image
 image_with_faces = detect_faces(image_path)
 display_image('Image with Faces Detected', image_with_faces)
    
if __name__ == "__main__":
 main()