import os
import lines
import cv2
import numpy as np
import pandas as pd

files = []
data = []

columns=['l_rho','l_theta','r_rho','r_theta','st','th']
df = pd.DataFrame(columns=columns)

def derive_info(line):
    if len(line):
        x1,y1,x2,y2,slope = line
        difference_y = y2-y1
        difference_x = x2-x1

        #formula for finding the "rho" of a line
        rho = abs(x2*y1 - y2*x1)/np.sqrt(difference_y**2 + difference_x**2)

        #formula for finding the "theta" of a line
        theta = np.arctan2((y2-y1),(x2 - x1))
        return [rho,theta]
    else:
        #return zero for both rho and theta if there is no line present
        return [0,0]

#raw_log is the file path for the set of simulator images
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

#save the data as a csv file
df.to_csv('CarDataRT.csv')
