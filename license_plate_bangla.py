# test file if you want to quickly try tesseract on a license plate image
import pytesseract
import cv2
import os
import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

plate = "./detections/crop/130/license_plate_1.png"

# point to license plate image (works well with custom crop function)
gray = cv2.imread(plate, 0)
gray = cv2.resize( gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(gray, (5,5), 0)
gray = cv2.medianBlur(gray, 3)
# perform otsu thresh (using binary inverse since opencv contours work better with white text)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
# xx = cv2.resize(thresh, (800,400))
cv2.imwrite("detections/cleared.jpg", thresh)
cv2.imshow("Licese Plate 1", thresh)
cv2.waitKey(0)



image = cv2.imread('detections/cleared.jpg')

data = pytesseract.image_to_string(image, lang='ben', config='--psm 6 --oem 3')
print("\nCleared:\n")
print(data)

text_file = open("bangla_license.txt", "w", encoding='utf-8')
n = text_file.write(data+'\n')
# text_file.close()



###########################################################################################
###########################################################################################

in_image = cv2.imread(plate)
s_file6 = 'temp/verifying.jpg'

gray = cv2.cvtColor(in_image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(gray, (0,0), sigmaX=33, sigmaY=33)
divide = cv2.divide(gray, blur, scale=255)
thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imwrite(s_file6, morph)
cv2.imshow("Licese Plate 2", morph)
cv2.waitKey(0)


image = cv2.imread('temp/verifying.jpg')

data = pytesseract.image_to_string(image, lang='ben', config='--psm 6 --oem 3')
print("\nVerified:\n")
print(data)

n = text_file.write('\n' + data)

text_file.close()

cv2.destroyAllWindows()
