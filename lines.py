import numpy as np
import cv2
import my_cv

#height and width to resize image to
img_rows , img_cols = 80, 80

def process_image(obs):
        #pre-process pure image to be used to detect lines from
        obs = cv2.cvtColor(obs, cv2.COLOR_BGR2GRAY)
        obs = cv2.resize(obs, (img_rows, img_cols))
        edges = my_cv.detect_edges(obs, low_threshold=50, high_threshold=150)

        #parameters for the HoughLinesP function in opencv2
        rho = 0.8
        theta = np.pi/180
        threshold = 25
        min_line_len = 5
        max_line_gap = 10

        #Get actual lines
        hough_lines = my_cv.hough_lines(edges, rho, theta, threshold, min_line_len, max_line_gap)

        #Separate lines based on slope of line
        left_lines, right_lines = my_cv.separate_lines(hough_lines)

        #Filter each line from right to left
        #In the end, only return 1 line (if any lines found) for right and left
        filtered_right, filtered_left = [],[]
        if len(left_lines):
            filtered_left = my_cv.reject_outliers(left_lines, cutoff=(-30.0, -0.1), lane='left')
        if len(right_lines):
            filtered_right = my_cv.reject_outliers(right_lines,  cutoff=(0.1, 30.0), lane='right')

        return (filtered_left,filtered_right)
