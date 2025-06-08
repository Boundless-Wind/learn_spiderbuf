# 图形滑块验证码，太难了，不会

# from PIL import Image
# import numpy as np
#
#
# def detect_white_block_left(image_path, threshold=240, min_white_ratio=0.5):
#     """
#     检测图片中白块距离左边的宽度
#     参数：
#     image_path: 图片路径
#     threshold: 白色判定阈值(0-255)，默认240（接近纯白）
#     min_white_ratio: 最小白色像素比例阈值(0-1)，默认0.5
#     """
#     # 1. 打开图片并转换为灰度图
#     img = Image.open(image_path).convert('L')
#     img_array = np.array(img)
#
#     # 2. 二值化处理
#     binary = img_array > threshold
#
#     # 3. 逐列扫描检测
#     height, width = binary.shape
#     for x in range(width):
#         # 提取当前列
#         column = binary[:, x]
#
#         # 计算白色像素比例
#         white_ratio = np.sum(column) / height
#
#         # 4. 判断是否满足白块条件
#         if white_ratio > min_white_ratio:
#             # 5. 验证连续性（可选）
#             if x < width - 1 and np.any(binary[:, x + 1]):  # 确保右侧有连续白色
#                 return x  # 返回左侧边缘坐标
#     return None  # 未找到符合条件的白块
#
#
# # 使用示例
# result = detect_white_block_left("c05_bg.png")
# if result is not None:
#     print(f"白块左侧边缘距离左边宽度：{result} 像素")
# else:
#     print("未检测到符合条件的白块")