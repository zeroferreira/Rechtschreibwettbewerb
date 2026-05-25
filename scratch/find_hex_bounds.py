from PIL import Image
import numpy as np

img = Image.open("English/img/trofeo.png")
rgba = np.array(img)
r, g, b, alpha = rgba[:,:,0], rgba[:,:,1], rgba[:,:,2], rgba[:,:,3]

# Let's find bounding box for different alpha thresholds
for threshold in [10, 50, 100, 150, 200, 250]:
    ys, xs = np.where(alpha >= threshold)
    if len(xs) > 0 and len(ys) > 0:
        x_min, x_max = xs.min(), xs.max()
        y_min, y_max = ys.min(), ys.max()
        print(f"Threshold alpha >= {threshold}: bbox = ({x_min}, {y_min}, {x_max}, {y_max}), size = {x_max-x_min}x{y_max-y_min}")
