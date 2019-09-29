# car-sim-steering
This is an algorithm to predict the steering angle of a car from a Unity simulation. This simulation is based on a project called DonkeyCar in which teams create a RC car to autonomously drive. This is a virtual solution to this problem using Computer Vision. Dataset for training images can be found here: https://www.kaggle.com/niallmandal/car-data-from-a-unity-simulation

## Unity
The github to the simulator used can be found here: https://github.com/tawnkramer/sdsandbox.

~10K images were captured on frame data, with the steering angle and throttle recorded in the actual name of each image.

Each image is unaltered, and is just pure pixel data.

## Breakdown of each file:
1) **`my_cv.py`**: holds most of the OpenCV2 files that manipulate the image and ultimately creates the lines
2) **`lines.py`**: runs the functions set up in `my_cv.py` defined as one overall function
3) **`formula.py`**: creates a dataset from the lines of each simulation image, with the columns as `left_line_y_int`,`left_line_slope`,`left_line_angle`,`right_line_y_int`,`right_line_slope`,`right_line_angle`,`steering`, and `throttle`
3) **`formula_rho_theta.py`**: creates a dataset from the lines of each simulation image, with the columns as `left_line_rho`,`left_line_theta`,`right_line_rho`,`right_line_theta`,`steering`, and `throttle`

The ρ function is a numpy version of this function:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/be2ab4a9d9d77f1623a2723891f652028a7a328d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -3.171ex; width:71.253ex; height:7.009ex;" alt="\operatorname {distance}(P_{1},P_{2},(x_{0},y_{0}))={\frac  {|(y_{2}-y_{1})x_{0}-(x_{2}-x_{1})y_{0}+x_{2}y_{1}-y_{2}x_{1}|}{{\sqrt  {(y_{2}-y_{1})^{2}+(x_{2}-x_{1})^{2}}}}}.">

The θ is calculated as so:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/72263d5113a7cc985f29fc9fc4b3f5e85dd5bbe5" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -2.171ex; width:14.23ex; height:5.509ex;" alt="m=\frac{y_2-y_1}{x_2-x_1}.">
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9e53a5ce7db600961ae411d4d1fbef636a62ddb9" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.838ex; width:11.398ex; height:2.843ex;" alt="m = \tan (\theta)">

**Note:** raw_log is the name of the folder used where all of the images are proccessed. The folder "example images" is used purely to show what each image may look like.
