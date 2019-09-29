import os
import lines
import cv2
import numpy as np
import pandas as pd

files = []
data = []

columns=['l_y_int','l_slope','l_angle','r_y_int','r_slope','r_angle','st','th']
df = pd.DataFrame(columns=columns)

def derive_info(line):
    if len(line):
        x1,y1,x2,y2,slope = line
        y_int = y1 - (slope*x1)
        angle = np.arctan((y1 - y2)/(x1 - x2))
        return [y_int,slope,angle]
    else:
        print("Hello")
        return [0,0,0]

for file in os.listdir('./raw_log/'):
    if file.endswith(".jpg"):
        files.append(file)
for file in files:
    img = cv2.imread('./raw_log/{}'.format(file))
    st = file[:-4].split('_')[3]
    th = file[:-4].split('_')[5]
    left, right = lines.process_image(img)
    left_info = derive_info(left)
    right_info = derive_info(right)
    line_info = left_info + right_info + [st] + [th]
    df = df.append(pd.Series(line_info,index=columns),ignore_index=True)


df.to_csv('CarData.csv')
