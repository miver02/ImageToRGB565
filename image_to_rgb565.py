import os
from PIL import Image
import numpy as np

def image_to_rgb565(image_path, output_name):
    # 打开图片
    img = Image.open(image_path)
    
    # 获取图片尺寸
    width, height = img.size
    
    # 确保图片是RGB模式
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # 创建输出文件
    with open(f"{output_name}.h", "w") as f:
        # 写入头部信息
        f.write(f"// 图片宽度和高度\n")
        f.write(f"const uint16_t {output_name}Width = {width};\n")
        f.write(f"const uint16_t {output_name}Height = {height};\n\n")
        
        # 开始写入数组
        f.write(f"const unsigned short {output_name}[{width * height}] PROGMEM = {{\n")
        
        # 转换每个像素
        pixels = []
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                
                # 转换为RGB565格式
                # RGB565: 5位红色，6位绿色，5位蓝色
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                pixels.append(f"0x{rgb565:04X}")
            
        # 每行写入16个像素
        for i in range(0, len(pixels), 16):
            line = pixels[i:i+16]
            f.write("    " + ", ".join(line) + ",\n")
        
        # 结束数组
        f.write("};\n")

if __name__ == "__main__":

    # for imagename in os.listdir("images"):
    #     # print(imagename)
    #     # 使用示例
    #     output_name = imagename.replace('.jpg', '')  # 输出的数组名称
    #     image_to_rgb565('images\\'+imagename, output_name)
    image_to_rgb565(r'images\333.jpg', 'ddd')
