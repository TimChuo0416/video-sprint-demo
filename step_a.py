# step_a.py
import os
import numpy as np
import cv2

# 輸出路徑設定在容器內的共享資料夾
output_dir = '/app/data/images'
os.makedirs(output_dir, exist_ok=True)
num_images = 3 # 產生 3 張圖片

print("Step A: Generating images...")
for i in range(num_images):
    file_path = os.path.join(output_dir, f'image_{i:04d}.png')
    # 產生 256x256 的隨機彩色雜訊影像
    image = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
    cv2.imwrite(file_path, image)

print(f"Step A: Successfully generated {num_images} images.")