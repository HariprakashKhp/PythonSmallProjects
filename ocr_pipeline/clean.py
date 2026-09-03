import cv2
import os

input = "images"
ouptut = "processed_images"

def image_cleaning(input, output):
    valide_extensions = (".jpg", ".jpeg",".png")
    converted_count = 0
    for filename in os.listdir(input):
        if filename.lower().endswith(valide_extensions):
            input_path = os.path.join(input, filename)
            output_path = os.path.join(output, filename)
            try:
                color_img = cv2.imread(input_path)
                grey_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
                blur_img = cv2.GaussianBlur(grey_img, (5, 5), 0)
                ret, binary_image = cv2.threshold(blur_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                cv2.imwrite(output_path, binary_image)
            except Exception as e:
                print(f"Failed to convert {filename} due to {e}")

if __name__ == "__main__":
    image_cleaning(input, ouptut)
