import numpy as np
import cv2 as cv
import math

def get_img_fact(img_path):
  im = cv.imread(img_path)
  imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
  ret, thresh = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY)
  contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  edge = contours[1]
  approx = cv.approxPolyDP(edge, 0.01*cv.arcLength(edge,True),True)

  count = len(approx)
  result_point = []

  for i, a in enumerate(approx):
    point = a[0]
    result_point.append([point[0], point[1]])

  result_length = []
  result_la = []
  for i, a in enumerate(approx):
    p1 = approx[i][0]
    p2 = approx[(i+1) % count][0]
    delta_x = p1[0]-p2[0]
    delta_y = p1[1]-p2[1]
    r = math.sqrt(delta_x**2 + delta_y**2)
    result_length.append(int(round(r,0)))

  result_angle = []
  for i, a in enumerate(approx):
    p0 = approx[(i-1) % count][0]
    p1 = approx[i][0]
    p2 = approx[(i+1) % count][0]
    a = math.sqrt((p0[0]-p2[0])**2 + (p0[1]-p2[1])**2)
    b = math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)
    c = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    angle = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
    result_angle.append(int(round(angle, 0)))

  for i in range (count):
    result_la.append([result_angle[i], result_length[i]])

  cv.drawContours(im, contours, -1, (0,255,0), 3)
  cv.imwrite('./shape/result.jpg', im)
  print(im)

  print(img_path)
  print('point', result_point)
  print('angle, length', result_la)

  return result_point, result_la