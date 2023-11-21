import os
import sys
import re
import shutil

def replace_special_characters_with_underline(str):
    return re.sub(r'[^\w.]', '_', str)

def remove_multiple_underline(s):
    # 将连续的下划线替换为单个下划线
    return re.sub(r'_+', '_', s)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 读取文件路径
        filepaths = sys.argv[1:]
        for filepath in filepaths:
            # 文件夹和文件名称
            dir_path, filename = os.path.split(filepath)

            if dir_path != '':
                # 将工作目录切换到文件目录下
                os.chdir(dir_path)
            
            filename = filename.strip() # 去除字符串两端的空格
            filename = replace_special_characters_with_underline(filename)
            filename = remove_multiple_underline(filename)

            dest_filepath = os.path.join(dir_path, filename)
            print("dest filepath:", dest_filepath)
            if os.path.exists(dest_filepath):
                print("文件名被占用!")
            else:
                shutil.copy(filepath, dest_filepath)
    else:
        filename = input("Please enter your filename: ")
        filename = filename.strip().replace(" ", "_")
        print(filename)
        input("请按「回车键」退出...")

