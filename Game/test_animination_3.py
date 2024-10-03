from PySide6.QtCore import QRect

# 创建一个矩形
original_rect = QRect(10, 20, 100, 50)

# 打印原始矩形的信息
print("Original Rect:")
print("Top Left:", original_rect.topLeft())
print("Bottom Right:", original_rect.bottomRight())
print("Width:", original_rect.width())
print("Height:", original_rect.height())

# 使用 adjusted 方法调整矩形
# 向左移动 5，向上移动 10，向右扩展 15，向下扩展 20
adjusted_rect = original_rect.adjusted(-5, -10, 15, 20)

# 打印调整后的矩形的信息
print("\nAdjusted Rect:")
print("Top Left:", adjusted_rect.topLeft())
print("Bottom Right:", adjusted_rect.bottomRight())
print("Width:", adjusted_rect.width())
print("Height:", adjusted_rect.height())