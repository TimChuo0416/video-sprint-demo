# step_b.py
import os
import glob
import cv2

# 從容器內的共享資料夾讀取與輸出
image_dir = '/app/data/images'
output_video_path = '/app/data/demo.mp4'
frame_rate = 1.0

print("Step B: Creating video from images...")
img_array = []
files = sorted(glob.glob(os.path.join(image_dir, '*.png')))

if not files:
    print("Step B Error: No images found!")
    exit(1)

first_img = cv2.imread(files[0])
height, width, layers = first_img.shape
size = (width, height)

for filename in files:
    img = cv2.imread(filename)
    img_array.append(img)

out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print(f"Step B: Video successfully created at {output_video_path}")