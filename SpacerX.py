import os
import sys
import re
import shutil

def replace_special_characters_with_space(s):
    return re.sub(r'[^\w\.]', ' ', s).replace('_', ' ')

def remove_multiple_space(s):
    # 将连续的空格替换为单个空格
    return re.sub(r'\s+', ' ', s)

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
            filename = replace_special_characters_with_space(filename)
            filename = remove_multiple_space(filename)

            dest_filepath = os.path.join(dir_path, filename)
            print("dest filepath:", dest_filepath)
            if os.path.exists(dest_filepath):
                print("错误: 文件名被占用!")
                input("请按「回车键」继续...")
            else:
                shutil.copy(filepath, dest_filepath)
    else:
        filename = input("Please enter your filename: ")
        filename = filename.strip().replace("_", " ")
        filename = remove_multiple_space(filename)
        print(filename)
        input("请按「回车键」退出...")

