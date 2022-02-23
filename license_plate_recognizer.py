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


# # apply dilation
# rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# dilation = cv2.dilate(thresh, rect_kern, iterations = 1)
# #cv2.imshow("dilation", dilation)
# #cv2.waitKey(0)
# # find contours
# try:
#     contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# except:
#     ret_img, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

# # create copy of image
# im2 = gray.copy()

# plate_num = ""
# # loop through contours and find letters in license plate
# for cnt in sorted_contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     height, width = im2.shape
    
#     # if height of box is not a quarter of total height then skip
#     if height / float(h) > 6: continue
#     ratio = h / float(w)
#     # if height to width ratio is less than 1.5 skip
#     if ratio < 1.5: continue
#     area = h * w
#     # if width is not more than 25 pixels skip
#     if width / float(w) > 15: continue
#     # if area is less than 100 pixels skip
#     if area < 100: continue
#     # draw the rectangle
#     rect = cv2.rectangle(im2, (x,y), (x+w, y+h), (0,255,0),2)
#     roi = thresh[y-5:y+h+5, x-5:x+w+5]
#     roi = cv2.bitwise_not(roi)
#     roi = cv2.medianBlur(roi, 5)
#     #cv2.imshow("ROI", roi)
#     #cv2.waitKey(0)
#     text = pytesseract.image_to_string(roi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
#     # text = pytesseract.image_to_string(roi, config='-c -l ben --psm 6 --oem 3')
#     #print(text)
#     plate_num += text

# print(plate_num)
# cv2.imshow("Character's Segmented", im2)
# cv2.waitKey(0)


image = cv2.imread('detections/cleared.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Blur and perform text extraction(you can use raw image)
# thresh = cv2.GaussianBlur(thresh, (3,3), 0)
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
# in_image = cv2.resize(morph, (300, 300))
cv2.imwrite(s_file6, morph)
cv2.imshow("Licese Plate 2", morph)
cv2.waitKey(0)


image = cv2.imread('temp/verifying.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Blur and perform text extraction(you can use raw image)
# thresh = cv2.GaussianBlur(thresh, (3,3), 0)
data = pytesseract.image_to_string(image, lang='ben', config='--psm 6 --oem 3')
print("\nVerified:\n")
print(data)

# text_file = open("bangla_license2.txt", "w", encoding='utf-8')
n = text_file.write('\n' + data)

text_file.close()

cv2.destroyAllWindows()
