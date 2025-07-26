from PIL import ImageFile,Image,ImageDraw

def AvatarCircler(image:ImageFile.ImageFile)->ImageFile.ImageFile:
        
    # 以图片的最小边为圆形裁剪的边长
    size = min(image.size)
    image = image.resize((size, size))  # 缩放图片为正方形
 
    # 创建一个圆形蒙版
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)  # 绘制白色的圆形

    image_with_circle = Image.new("RGB", (size, size), (229,229,229))
    image_with_circle.paste(image, (0, 0), mask) # 使用圆形蒙版将图片粘贴到背景上

    return image_with_circle