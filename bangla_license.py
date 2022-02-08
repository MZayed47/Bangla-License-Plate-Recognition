import cv2
import pytesseract

image = cv2.imread('cleared.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Blur and perform text extraction(you can use raw image)
# thresh = cv2.GaussianBlur(thresh, (3,3), 0)
data = pytesseract.image_to_string(image, lang='ben', config='--psm 6')
print(data)

text_file = open("bangla_license.txt", "w", encoding='utf-8')
n = text_file.write(data)
text_file.close()
