from os import listdir
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 读取图片，调整为统一的大小和格式
image_files = [fn for fn in listdir() if fn.startswith('img') and fn.endswith('.png')]
images = [Image.open(fn).resize((1280, 720)).convert('RGBA') for fn in image_files]

# 不显示坐标轴、刻度、网格线等
plt.axis('off')

# 程序运行时显示第一个图片
if images:
    image = plt.imshow(np.array(images[0]))
else:
    print("没有找到符合条件的图片文件")
    plt.close()
    exit()

# 透明度参数取值范围
alphas = np.linspace(0, 1, 50)

# 暂停5秒
plt.pause(5)

for im1, im2 in zip(images[:-1], images[1:]):
    # 暂停1秒后切换图片
    plt.pause(1)
    for alpha in alphas:
        # 渐变，过渡到下一张图片
        # 合成图像，计算过程为: im1 * (1 - alpha) + im2 * alpha
        image.set_data(np.array(Image.blend(im1, im2, alpha)))
        plt.pause(0.1)

plt.show()