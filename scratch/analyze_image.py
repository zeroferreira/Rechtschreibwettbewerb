from PIL import Image
import os

img_path = "English/img/trofeo.png"
if os.path.exists(img_path):
    img = Image.open(img_path)
    bbox = img.getbbox()
    print("Bounding box of active content (left, upper, right, lower):", bbox)
    if bbox:
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        print(f"Active dimensions: {w}x{h}")
        print(f"Canvas size: {img.size[0]}x{img.size[1]}")
        print(f"Active ratio in width: {w / img.size[0]:.2%}")
        print(f"Active ratio in height: {h / img.size[1]:.2%}")
else:
    print(f"File not found: {img_path}")
