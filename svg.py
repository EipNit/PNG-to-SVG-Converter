import os
from PIL import Image

def png_to_pgm(png_path, pgm_path):
    # 打开PNG图像并转换为灰度
    image = Image.open(png_path).convert('L')
    # 保存为PGM格式
    image.save(pgm_path)

def pgm_to_svg(pgm_path, svg_path):
    # 使用potrace命令行工具将PGM转换为SVG
    os.system(f'potrace "{pgm_path}" -s -o "{svg_path}"')

def png_to_svg(png_path):
    # 获取文件名和目录
    directory, filename = os.path.split(png_path)
    name, _ = os.path.splitext(filename)
    pgm_path = os.path.join(directory, name + '.pgm')
    svg_path = os.path.join(directory, name + '.svg')
    
    # 转换PNG到PGM
    png_to_pgm(png_path, pgm_path)
    # 转换PGM到SVG
    pgm_to_svg(pgm_path, svg_path)
    # 删除中间的PGM文件
    os.remove(pgm_path)

# 列出需要处理的PNG文件路径
png_files = [
    "your.png"
]

# 批量处理PNG文件
for png_file in png_files:
    png_to_svg(png_file)
