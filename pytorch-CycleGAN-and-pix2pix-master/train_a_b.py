import os

def rename_files(folder, suffix_to_remove):
    """
    Rename files in a given folder by removing a specified suffix (excluding the file extension).
    """
    files = os.listdir(folder)
    for file in files:
        # 检查文件名是否包含指定的后缀
        if suffix_to_remove in file:
            # 生成新的文件名
            base_name, ext = os.path.splitext(file)
            if ext == '.jpg':
                new_name = base_name.replace(suffix_to_remove, '') + ext
                # 构造完整的旧路径和新路径
                old_path = os.path.join(folder, file)
                new_path = os.path.join(folder, new_name)
                # 重命名文件
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')

# 设置文件夹路径
folder_A = r"D:\Download\pytorch-CycleGAN-and-pix2pix-master\pytorch-CycleGAN-and-pix2pix-master\datasets\vangogh2photo\train\A"
folder_B = r"D:\Download\pytorch-CycleGAN-and-pix2pix-master\pytorch-CycleGAN-and-pix2pix-master\datasets\vangogh2photo\train\B"

# 调用重命名函数
rename_files(folder_A, '_input')
rename_files(folder_B, '_target')

